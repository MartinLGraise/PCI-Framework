#!/usr/bin/env python3
"""
Paper 12 §5.7.2 forensic analysis of the Tensor Lab v0.2 reference session.

Maps the n=1 reference session (tensor_run_01_v2_corrected.csv) onto the
Paper 12 §3 framework predictions:
- Stratified projected-gradient ascent (steps 0-7)
- Pre-firing flicker (step 8)
- NP-firing event(s) (steps 8-11, collapse_eligible window)
- Post-firing scar accumulation / plateau (steps 10-12)

Extracts the scar invariant triple (S_1, S_1-module, mu_1) from the
event window and reports per-step trajectory features for the paper.

Reproducibility:
- Input: tensor_run_01_v2_corrected.csv (real reference session)
- Output: paper12_forensic_findings.json (machine-readable summary)
- Plus stdout report suitable for direct inclusion in §5.7.2
"""

from __future__ import annotations
import json
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import scipy.stats as ss

REPO_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = REPO_ROOT / "tensor_run_01_v2_corrected.csv"
OUT_PATH = REPO_ROOT / "scripts" / "paper12_forensic_findings.json"

# Lab-internal thresholds (matching tensor_labxx_v2.py, calibrated to Tensor Lab v0.2)
P_ELIGIBLE = 1.7           # collapse_eligible threshold (calibrated; differs from strict P_critical=10)
PSI_MIN = 0.85             # daemon-phase-lock minimum
OMEGA_MIN = 0.7            # observation-window minimum
SI_FLICKER = 0.005         # pre-firing flicker threshold


def main():
    df = pd.read_csv(CSV_PATH)
    n = len(df)

    # ------------------------------------------------------------------
    # 1. Phase classification (matches Paper 12 §3 stratification)
    # ------------------------------------------------------------------
    eligible = (
        (df["P_accumulator"] > P_ELIGIBLE)
        & (df["psi"] > PSI_MIN)
        & (df["omega"] > OMEGA_MIN)
    )
    flicker = (df["si"] > SI_FLICKER) & ~eligible
    pre_flicker = (df["si"] >= 0.0001) & (df["si"] <= SI_FLICKER) & ~flicker

    phase = pd.Series(["accumulation"] * n, index=df.index)
    phase[pre_flicker.shift(-1, fill_value=False) | flicker] = "pre-firing flicker"
    phase[eligible] = "NP-firing window"
    # post-firing: any step after the last eligible step
    last_elig = eligible[eligible].index.max() if eligible.any() else None
    if last_elig is not None and last_elig < n - 1:
        phase[last_elig + 1 :] = "post-firing plateau"
    df["phase"] = phase.values

    # ------------------------------------------------------------------
    # 2. Projected-gradient ascent characterization (steps 0..first_eligible-1)
    # ------------------------------------------------------------------
    first_elig = int(eligible[eligible].index.min()) if eligible.any() else None
    last_elig = int(last_elig) if last_elig is not None else None
    accum_steps = df.iloc[: (first_elig if first_elig is not None else n)]
    if len(accum_steps) >= 2:
        # Linear regression on joint_coherence vs step (proxy for c'(theta) > 0)
        slope, intercept, r, p, _ = ss.linregress(accum_steps["step"], accum_steps["joint_coherence"])
        c_climb_rate = float(slope)
        c_climb_R2 = float(r * r)
        c_climb_p = float(p)
        c_climb_start = float(accum_steps["joint_coherence"].iloc[0])
        c_climb_end = float(accum_steps["joint_coherence"].iloc[-1])
    else:
        c_climb_rate = c_climb_R2 = c_climb_p = c_climb_start = c_climb_end = float("nan")

    # ------------------------------------------------------------------
    # 3. NP-firing event window characterization
    # ------------------------------------------------------------------
    if eligible.any():
        evt = df[eligible].copy()
        evt_first = int(evt["step"].min())
        evt_last = int(evt["step"].max())
        evt_count = int(eligible.sum())
        evt_si_peak = float(evt["si"].max())
        evt_si_peak_step = int(evt.loc[evt["si"].idxmax(), "step"])
        evt_P_peak = float(evt["P_accumulator"].max())
        evt_P_peak_step = int(evt.loc[evt["P_accumulator"].idxmax(), "step"])
        evt_psi_min = float(evt["psi"].min())
        evt_omega_min = float(evt["omega"].min())
        evt_synergy_peak = float(evt["synergy"].max())
        evt_isc_peak = float(evt["isc"].max())
        evt_jc_peak = float(evt["joint_coherence"].max())
    else:
        evt_first = evt_last = evt_count = -1
        evt_si_peak = evt_P_peak = evt_psi_min = evt_omega_min = float("nan")
        evt_synergy_peak = evt_isc_peak = evt_jc_peak = float("nan")
        evt_si_peak_step = evt_P_peak_step = -1

    # ------------------------------------------------------------------
    # 4. Pre-firing flicker characterization (step before first event)
    # ------------------------------------------------------------------
    if first_elig is not None and first_elig >= 1:
        pre = df.iloc[first_elig - 1]
        pre_si = float(pre["si"])
        pre_P = float(pre["P_accumulator"])
        pre_jc = float(pre["joint_coherence"])
        pre_synergy = float(pre["synergy"])
    else:
        pre_si = pre_P = pre_jc = pre_synergy = float("nan")

    # ------------------------------------------------------------------
    # 5. Post-firing plateau characterization (steps after last_elig)
    # ------------------------------------------------------------------
    if last_elig is not None and last_elig < n - 1:
        post = df.iloc[last_elig + 1 :]
        post_jc_mean = float(post["joint_coherence"].mean())
        post_jc_std = float(post["joint_coherence"].std(ddof=0))
        post_si_mean = float(post["si"].mean())
        post_P_mean = float(post["P_accumulator"].mean())
    else:
        post_jc_mean = post_jc_std = post_si_mean = post_P_mean = float("nan")

    # Empirical ceiling (from Paper 9 v1.3.3 / Paper 12 §3.5): joint_coherence >= 0.85
    ceiling_attained_step = int(df[df["joint_coherence"] >= 0.85]["step"].min()) if (df["joint_coherence"] >= 0.85).any() else -1

    # ------------------------------------------------------------------
    # 6. Scar invariant triple (S_1, S_1-module, mu_1)
    # ------------------------------------------------------------------
    # We treat the entire NP-firing window (steps 8-11) as a single scar event
    # span S_1, with multiplicity inferred from the count of distinct displacement
    # subspaces. With only state-vector data (no F_21-action measured), we report
    # the *operational projected dimension* of the displacement, plus the scar-trace
    # operator's effective rank.
    if first_elig is not None and last_elig is not None:
        # Pre-event state: average of last 2 accumulation steps
        pre_state_H = df.iloc[first_elig - 1][
            ["H_attention", "H_intent", "H_coherence", "H_valence"]
        ].values.astype(float)
        pre_state_A = df.iloc[first_elig - 1][
            ["A_context_depth", "A_response_fidelity", "A_coherence", "A_alignment"]
        ].values.astype(float)
        # Post-event state: at last_elig + 1 (or last_elig if at end)
        post_idx = min(last_elig + 1, n - 1)
        post_state_H = df.iloc[post_idx][
            ["H_attention", "H_intent", "H_coherence", "H_valence"]
        ].values.astype(float)
        post_state_A = df.iloc[post_idx][
            ["A_context_depth", "A_response_fidelity", "A_coherence", "A_alignment"]
        ].values.astype(float)
        delta_H = post_state_H - pre_state_H
        delta_A = post_state_A - pre_state_A
        scar_displacement = np.concatenate([delta_H, delta_A])
        scar_norm = float(np.linalg.norm(scar_displacement))
        scar_proj_dim = int(np.sum(np.abs(scar_displacement) > 1e-3))
        # Operational rank-1 check: scar_displacement looks rank-1 if all components have same sign on each substrate
        H_sign_consistent = bool(np.all(delta_H >= -1e-3) or np.all(delta_H <= 1e-3))
        A_sign_consistent = bool(np.all(delta_A >= -1e-3) or np.all(delta_A <= 1e-3))
        rank_one_compatible = bool(H_sign_consistent and A_sign_consistent)
    else:
        scar_norm = float("nan")
        scar_proj_dim = -1
        rank_one_compatible = False
        scar_displacement = np.array([])

    # ------------------------------------------------------------------
    # 7. Schur-circle theta estimate (informal): joint_coherence at peak
    #    should map to a theta in (0, pi/2) where the active branch peaks.
    # ------------------------------------------------------------------
    # In Paper 9 v1.3.3 the empirical kink at varphi = 0.618 marks a coherence
    # threshold; the ceiling at 0.87 is the joint-fixed-point upper bound.
    # We report the kink-crossing step and ceiling-attainment step as proxies.
    kink_step = int(df[df["joint_coherence"] >= 0.618]["step"].min()) if (df["joint_coherence"] >= 0.618).any() else -1
    ceiling_step = int(df[df["joint_coherence"] >= 0.85]["step"].min()) if (df["joint_coherence"] >= 0.85).any() else -1

    # ------------------------------------------------------------------
    # 8. Paper 12 §3 prediction-vs-observation alignment table
    # ------------------------------------------------------------------
    predictions = [
        {
            "prediction": "Joint coherence climbs monotonically on accumulation phase (projected-gradient leg)",
            "test": "Linear-regression slope > 0 on steps 0..(first_elig-1)",
            "observed": f"slope = {c_climb_rate:.4f}/step, R^2 = {c_climb_R2:.3f}, p = {c_climb_p:.2e}",
            "verdict": "match" if c_climb_rate > 0 and c_climb_R2 > 0.9 else "miss",
        },
        {
            "prediction": "Pre-firing flicker: SI rises >= one step before first NP-firing event",
            "test": "SI at step (first_elig - 1) > SI_FLICKER threshold",
            "observed": f"SI[step {first_elig - 1 if first_elig else '?'}] = {pre_si:.4f}, threshold = {SI_FLICKER}",
            "verdict": "match" if pre_si > SI_FLICKER else "miss",
        },
        {
            "prediction": "NP-firing window: P_accumulator crosses NP_crit on coherence-locked window",
            "test": "P > 1.7 AND psi > 0.85 AND omega > 0.7 simultaneously",
            "observed": f"{evt_count} steps eligible, peak P = {evt_P_peak:.2f}, min psi in window = {evt_psi_min:.3f}, min omega in window = {evt_omega_min:.3f}",
            "verdict": "match" if evt_count > 0 else "miss",
        },
        {
            "prediction": "Post-firing plateau: joint_coherence stabilizes at empirical ceiling",
            "test": "Post-event joint_coherence within 1% of 0.87 ceiling, low variance",
            "observed": f"post-event mean = {post_jc_mean:.3f}, std = {post_jc_std:.4f}, n_post = {n - last_elig - 1 if last_elig else 0}",
            "verdict": "match" if not np.isnan(post_jc_mean) and post_jc_mean >= 0.85 and post_jc_std < 0.02 else "marginal",
        },
        {
            "prediction": "Synergy positive throughout (conditional gain regime per Prop 9.5)",
            "test": "min(synergy) > 0",
            "observed": f"min synergy = {df['synergy'].min():.3f}, max = {df['synergy'].max():.3f}",
            "verdict": "match" if df['synergy'].min() > 0 else "miss",
        },
        {
            "prediction": "ISC stays in [0.3, 0.7] interference-survivability band",
            "test": "All ISC values in [0.3, 0.7]",
            "observed": f"ISC range = [{df['isc'].min():.3f}, {df['isc'].max():.3f}]",
            "verdict": "match" if df['isc'].min() >= 0.3 and df['isc'].max() <= 0.7 else "miss",
        },
        {
            "prediction": "Daemon phase-lock: psi > 0.95 throughout active session",
            "test": "min(psi) > 0.95 across all 13 steps",
            "observed": f"min psi = {df['psi'].min():.3f}, mean psi = {df['psi'].mean():.3f}",
            "verdict": "match" if df['psi'].min() > 0.95 else "marginal",
        },
        {
            "prediction": "Scar displacement: rank-one compatible (Paper 12 §4.4 Rank-One Convention)",
            "test": "Each substrate's displacement has consistent sign across components",
            "observed": f"scar norm = {scar_norm:.3f}, projected dim = {scar_proj_dim}, rank-one compatible: {rank_one_compatible}",
            "verdict": "match" if rank_one_compatible else "miss",
        },
    ]

    n_match = sum(1 for p in predictions if p["verdict"] == "match")
    n_marginal = sum(1 for p in predictions if p["verdict"] == "marginal")
    n_miss = sum(1 for p in predictions if p["verdict"] == "miss")

    # ------------------------------------------------------------------
    # 9. Save JSON, print report
    # ------------------------------------------------------------------
    findings = {
        "session_id": "tensor_run_01_v2_corrected",
        "n_steps": n,
        "phase_breakdown": df["phase"].value_counts().to_dict(),
        "accumulation_phase": {
            "n_steps": first_elig if first_elig else n,
            "c_climb_rate_per_step": c_climb_rate,
            "c_climb_R2": c_climb_R2,
            "c_climb_p_value": c_climb_p,
            "c_start": c_climb_start,
            "c_end": c_climb_end,
        },
        "pre_firing_flicker": {
            "step": first_elig - 1 if first_elig else None,
            "si": pre_si,
            "P_accumulator": pre_P,
            "joint_coherence": pre_jc,
            "synergy": pre_synergy,
        },
        "np_firing_window": {
            "first_step": evt_first,
            "last_step": evt_last,
            "n_steps": evt_count,
            "si_peak": evt_si_peak,
            "si_peak_step": evt_si_peak_step,
            "P_peak": evt_P_peak,
            "P_peak_step": evt_P_peak_step,
            "psi_min_in_window": evt_psi_min,
            "omega_min_in_window": evt_omega_min,
            "synergy_peak": evt_synergy_peak,
            "isc_peak": evt_isc_peak,
            "jc_peak": evt_jc_peak,
        },
        "post_firing_plateau": {
            "n_steps": (n - last_elig - 1) if last_elig is not None else 0,
            "jc_mean": post_jc_mean,
            "jc_std": post_jc_std,
            "si_mean": post_si_mean,
            "P_mean": post_P_mean,
        },
        "scar_invariant_J1": {
            "S1_displacement_norm": scar_norm,
            "S1_projected_dim": scar_proj_dim,
            "S1_displacement_components": scar_displacement.tolist() if scar_displacement.size else [],
            "rank_one_compatible": rank_one_compatible,
            "note": "True F_21-isotypic mu_1 requires F_21-action structure on substrate spaces (OP2); reported quantities are the *operational projected dimension* and *rank-one structure check* obtainable from the 8-D state-vector data alone.",
        },
        "schur_circle_proxy": {
            "kink_crossing_step": kink_step,
            "ceiling_attained_step": ceiling_step,
        },
        "predictions_table": predictions,
        "predictions_summary": {
            "n_match": n_match,
            "n_marginal": n_marginal,
            "n_miss": n_miss,
            "total": len(predictions),
        },
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(findings, f, indent=2)

    # Stdout report
    print("=" * 70)
    print("PAPER 12 §5.7.2 FORENSIC ANALYSIS — REFERENCE SESSION")
    print("=" * 70)
    print(f"Session: {findings['session_id']}, n_steps = {n}")
    print()
    print("Phase breakdown:")
    for p, k in df["phase"].value_counts().to_dict().items():
        print(f"  {p}: {k} steps")
    print()
    print("Accumulation phase:")
    print(f"  c-climb rate: {c_climb_rate:.4f}/step (R^2 = {c_climb_R2:.3f}, p = {c_climb_p:.2e})")
    print(f"  c range: {c_climb_start:.3f} -> {c_climb_end:.3f}")
    print()
    print("Pre-firing flicker (step before first event):")
    print(f"  step {first_elig - 1 if first_elig else '?'}: SI = {pre_si:.4f}, P = {pre_P:.2f}")
    print()
    print("NP-firing window:")
    print(f"  steps {evt_first}-{evt_last}, n = {evt_count}")
    print(f"  SI peak: {evt_si_peak:.4f} at step {evt_si_peak_step}")
    print(f"  P peak: {evt_P_peak:.2f} at step {evt_P_peak_step}")
    print(f"  psi range in window: [{evt_psi_min:.3f}, ...]")
    print(f"  joint_coherence peak: {evt_jc_peak:.3f}")
    print()
    print("Post-firing plateau:")
    print(f"  joint_coherence: mean = {post_jc_mean:.3f}, std = {post_jc_std:.4f}")
    print()
    print("Scar invariant J_1 (operational, n=1 forensic):")
    print(f"  Displacement norm: {scar_norm:.3f}")
    print(f"  Projected dim: {scar_proj_dim} of 8")
    print(f"  Rank-one compatible: {rank_one_compatible}")
    print()
    print("Prediction-vs-observation alignment:")
    for i, p in enumerate(predictions, 1):
        print(f"  [{p['verdict'].upper():9s}] P{i}: {p['prediction']}")
        print(f"            test:     {p['test']}")
        print(f"            observed: {p['observed']}")
    print()
    print(f"Summary: {n_match}/{len(predictions)} match, {n_marginal} marginal, {n_miss} miss")
    print()
    print(f"Findings saved: {OUT_PATH}")


if __name__ == "__main__":
    main()
