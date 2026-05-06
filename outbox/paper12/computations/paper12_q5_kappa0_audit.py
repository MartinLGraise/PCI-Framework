"""
Paper 12 §3 — Q5 κ=0 gradient-flow recovery audit on Paper 9's 50-seed MC.

Reproducibility record for Paper 12 thesis-session 1 (2026-05-05).

  Source transcript: outbox/paper12/chatgpt_pro_session_transcript_2026-05-05.pdf
  Thesis memo:       outbox/paper12/paper12_thesis_gradual_tear.md
  Related DOI:       10.5281/zenodo.20034821 (Paper 9 v1.3.2)

Question answered by this audit
-------------------------------
In the κ → 0 limit of Paper 12's augmented flow
    θ̇ = -η ∇_θ 𝓕(ẑ(θ)) + κ · NP(t) · ξ★,    𝓕 = -𝒞_min,
is each Paper 9 MC θ★_k a critical point of c(θ) := 𝒞_min(ẑ(θ))?

ChatGPT 5.5 Pro prediction (43% confidence): STRICT FAIL expected, because
the MC ensemble is boundary-dominated (mean θ★ = 3.2°). Most seeds are
expected to be boundary-KKT optima (c'_+(0) ≤ 0) rather than interior
Fermat critical points (c'(θ★) = 0). This audit tests the prediction.

Method
------
For each seed pair (s_a, s_b) = (20260504+k, 20260505+k), k=0..49:

1. Reconstruct R_A, R_B, b_A, b_B at φ=0 via the existing `build_mc_seeds`
   interface. Use (b_A, b_B) = (e_1, e_1) at aligned bias φ=0.

2. Reoptimize θ★ at high precision with scipy.optimize.minimize_scalar
   over [0, π/2]. The original MC snaps θ★ to a 20-point grid with
   resolution π/2/19 ≈ 4.74°; reoptimization is essential.

3. Compute analytic c'(θ★) via the chain rule:
       ẑ'(θ) = -M(θ)⁻¹ M'(θ) ẑ(θ)
   where M'(θ) has the sin/cos structure of ∂_θ Ψ_θ applied to the
   Paper 9 block form.

4. Classify each seed:
   - smooth_interior_zero: θ★ ∈ (tol, π/2 - tol), c_A ≠ c_B, |c'| < 1e-6
   - boundary_left_KKT:    θ★ ≤ tol, c'_+(0) ≤ 1e-6
   - boundary_right_KKT:   θ★ ≥ π/2 - tol, c'_-(π/2) ≥ -1e-6
   - Sigma_min_Clarke_OK:  |c_A - c_B| < tie_tol, 0 ∈ conv{c_A', c_B'}
   - FAIL:                 none of the above

5. Report:
   - Strict pass/fail (all 50 smooth-interior-zero)
   - Constrained pass/fail (each seed legitimate per one of the classes)
   - Breakdown by classification
   - Per-seed CSV with all quantities
"""

import csv
import json
import os
import time

import numpy as np
from scipy.optimize import minimize_scalar

# ----- Parameters matching Paper 9 v1.3.2 -----
N = 14
r = 0.7
I_mat = np.eye(N)
e1 = np.zeros(N); e1[0] = 1.0

SEEDS = [(20260504 + k, 20260505 + k) for k in range(50)]

# ----- Tolerances (from ChatGPT's paste-ready spec) -----
DERIV_TOL   = 1e-6       # units: rad^-1; strict classical derivative-zero
TIE_TOL     = 1e-8       # units: dimensionless; min-locus detection |c_A - c_B|
END_TOL     = 1e-5       # units: rad; endpoint detection (≈ 5.73e-4 degrees)
COND_WARN   = 1e10       # condition-number warning threshold


# ---------------------------------------------------------------------
# Core linear-algebra interface (matches build_mc_seeds.py conventions)
# ---------------------------------------------------------------------

def make_rotation(seed):
    """QR of standard-normal 14x14 matrix — same as Paper 9."""
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.standard_normal((N, N)))
    return Q

def M_theta(theta, R_A, R_B):
    """Paper 9 block matrix: M(θ) = [[I - r c R_A,  r s R_A], [-r s R_B, I - r c R_B]]."""
    c = np.cos(theta); s = np.sin(theta)
    return np.block([[I_mat - r*c*R_A,   r*s*R_A],
                     [-r*s*R_B,          I_mat - r*c*R_B]])

def Mprime_theta(theta, R_A, R_B):
    """Analytic M'(θ). d/dθ of the block form: cos -> -sin, sin -> cos, all with factor r."""
    c = np.cos(theta); s = np.sin(theta)
    return np.block([[r*s*R_A,    r*c*R_A],
                     [-r*c*R_B,   r*s*R_B]])

def z_and_zprime(theta, R_A, R_B, b_full):
    """Joint fixed point ẑ(θ) and derivative ẑ'(θ). b_full is the 28-vector (b_A; b_B)."""
    M  = M_theta(theta, R_A, R_B)
    Mp = Mprime_theta(theta, R_A, R_B)
    condM = np.linalg.cond(M)
    z = np.linalg.solve(M, b_full)
    zp = -np.linalg.solve(M, Mp @ z)
    return z, zp, condM

def cosine_and_deriv(u, up, b):
    """C(u) = <u,b>/(||u|| ||b||) and C'(u)[up]."""
    un = np.linalg.norm(u); bn = np.linalg.norm(b)
    dot_ub  = float(np.dot(u, b))
    dot_upb = float(np.dot(up, b))
    dot_uup = float(np.dot(u, up))
    C  = dot_ub / (un * bn)
    Cp = dot_upb / (un * bn) - dot_ub * dot_uup / (un**3 * bn)
    return C, Cp, un

def cmin_value(theta, R_A, R_B, b_A, b_B):
    """Scalar c(θ) = min(|C_A|, |C_B|). Positive branch (matches Paper 9's abs)."""
    b_full = np.concatenate([b_A, b_B])
    M = M_theta(theta, R_A, R_B)
    z = np.linalg.solve(M, b_full)
    x, y = z[:N], z[N:]
    cA = abs(float(np.dot(x, b_A) / (np.linalg.norm(x) * np.linalg.norm(b_A))))
    cB = abs(float(np.dot(y, b_B) / (np.linalg.norm(y) * np.linalg.norm(b_B))))
    return min(cA, cB)

def branch_info(theta, R_A, R_B, b_A, b_B):
    """Compute c_A, c_B, c_A', c_B', active branch, classical c' if defined.

    Returns dict with keys: cA, cB, cAp, cBp, c, cp, active, classical_ok, condM.
    The absolute-value branch matches Paper 9: C_i = |<x_i, b_i>|/(||x_i|| ||b_i||).
    """
    b_full = np.concatenate([b_A, b_B])
    z, zp, condM = z_and_zprime(theta, R_A, R_B, b_full)
    x, y = z[:N], z[N:]
    xp, yp = zp[:N], zp[N:]

    # Paper 9 uses |<x, b>|. For the derivative sign, we track the signed
    # cosine, then multiply the derivative by sign of the signed cosine
    # if we want d|C|/dθ.
    signed_cA, signed_cAp, _ = cosine_and_deriv(x, xp, b_A)
    signed_cB, signed_cBp, _ = cosine_and_deriv(y, yp, b_B)
    cA = abs(signed_cA); cB = abs(signed_cB)
    # d/dθ |C| = sign(C) · dC/dθ.
    cAp = np.sign(signed_cA) * signed_cAp
    cBp = np.sign(signed_cB) * signed_cBp

    if cA < cB - TIE_TOL:
        active = "A"; c = cA; cp = cAp; classical_ok = True
    elif cB < cA - TIE_TOL:
        active = "B"; c = cB; cp = cBp; classical_ok = True
    else:
        active = "tie"; c = min(cA, cB); cp = np.nan; classical_ok = False

    return {
        "cA": cA, "cB": cB, "cAp": float(cAp), "cBp": float(cBp),
        "c": c, "cp": float(cp) if np.isfinite(cp) else np.nan,
        "active": active, "classical_ok": classical_ok, "condM": float(condM),
    }


# ---------------------------------------------------------------------
# Reoptimization + classification per seed
# ---------------------------------------------------------------------

def reoptimize_theta_star(R_A, R_B, b_A, b_B):
    """Find θ★ = argmax c(θ) on [0, π/2] at high precision."""
    def neg_c(theta):
        return -cmin_value(theta, R_A, R_B, b_A, b_B)
    # Brent's method on the bounded interval.
    res = minimize_scalar(neg_c, bounds=(0.0, 0.5*np.pi), method="bounded",
                          options={"xatol": 1e-10})
    return float(res.x), float(-res.fun)

def classify_seed(seed_a, seed_b):
    R_A = make_rotation(seed_a)
    R_B = make_rotation(seed_b)
    # φ=0 aligned bias: b_A = b_B = e_1.
    b_A = e1.copy(); b_B = e1.copy()

    # Reoptimize θ★ at high precision.
    theta_star, c_star = reoptimize_theta_star(R_A, R_B, b_A, b_B)

    # Compute branch info at θ★.
    info = branch_info(theta_star, R_A, R_B, b_A, b_B)

    at_left  = theta_star <= END_TOL
    at_right = theta_star >= (0.5*np.pi - END_TOL)
    interior = not at_left and not at_right

    cAp = info["cAp"]; cBp = info["cBp"]

    if info["classical_ok"]:
        cp = info["cp"]
        if interior:
            if abs(cp) < DERIV_TOL:
                classification = "smooth_interior_zero"; strict_ok = True; constrained_ok = True
            else:
                classification = "smooth_interior_NONZERO"; strict_ok = False; constrained_ok = False
        elif at_left:
            constrained_ok = cp <= DERIV_TOL
            classification = "boundary_left_KKT" if constrained_ok else "boundary_left_FAIL"
            strict_ok = False
        else:  # at_right
            constrained_ok = cp >= -DERIV_TOL
            classification = "boundary_right_KKT" if constrained_ok else "boundary_right_FAIL"
            strict_ok = False
    else:
        # Sigma_min: |cA - cB| < TIE_TOL. Clarke generalized-gradient check.
        # 0 ∈ conv{cAp, cBp} iff min(cAp, cBp) ≤ 0 ≤ max(cAp, cBp) (within tol).
        clarke_ok = (min(cAp, cBp) <= DERIV_TOL) and (max(cAp, cBp) >= -DERIV_TOL)
        classification = "Sigma_min_Clarke_OK" if clarke_ok else "Sigma_min_Clarke_FAIL"
        strict_ok = False
        constrained_ok = clarke_ok

    return {
        "seed_a": seed_a, "seed_b": seed_b,
        "theta_star_rad": theta_star,
        "theta_star_deg": float(np.degrees(theta_star)),
        "c_star": c_star,
        **info,
        "at_left": at_left, "at_right": at_right, "interior": interior,
        "strict_ok": strict_ok, "constrained_ok": constrained_ok,
        "classification": classification,
        "ill_conditioned": info["condM"] > COND_WARN,
    }


def main():
    t0 = time.time()
    rows = []
    print("Paper 12 §3 Q5 audit — κ=0 gradient-flow recovery on Paper 9's 50-seed MC")
    print("=" * 78)
    for k, (sa, sb) in enumerate(SEEDS):
        row = classify_seed(sa, sb)
        rows.append(row)
        print(f"  [{k:2d}] seeds=({sa},{sb})  θ★={row['theta_star_deg']:7.3f}°  "
              f"c*={row['c_star']:.6f}  active={row['active']:>3}  "
              f"c'={row['cp']:+.2e}  -> {row['classification']}")
    elapsed = time.time() - t0

    # Summary counts.
    counts = {}
    for r_ in rows:
        cls = r_["classification"]
        counts[cls] = counts.get(cls, 0) + 1

    strict_pass_count = sum(1 for r_ in rows if r_["strict_ok"])
    constrained_pass_count = sum(1 for r_ in rows if r_["constrained_ok"])

    print()
    print("=" * 78)
    print("STRICT AUDIT (all 50 must be smooth_interior_zero with |c'| < 1e-6):")
    print(f"  STRICT_PASS_ALL_50 = {strict_pass_count == 50}")
    print(f"  strict_pass_count  = {strict_pass_count} / 50")
    print()
    print("CONSTRAINED AUDIT (each seed must be one of: smooth_interior_zero,")
    print("boundary_left_KKT, boundary_right_KKT, Sigma_min_Clarke_OK):")
    print(f"  CONSTRAINED_PASS_ALL_50 = {constrained_pass_count == 50}")
    print(f"  constrained_pass_count  = {constrained_pass_count} / 50")
    print()
    print("CLASSIFICATION COUNTS:")
    for cls, n in sorted(counts.items()):
        print(f"  {cls:32s} : {n:2d}")
    print()
    print(f"Runtime: {elapsed:.2f}s")

    # Write CSV.
    out_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(out_dir, "paper12_q5_kappa0_audit.csv")
    fieldnames = ["seed_a", "seed_b", "theta_star_deg", "theta_star_rad",
                  "c_star", "cA", "cB", "cAp", "cBp", "cp", "active",
                  "interior", "at_left", "at_right",
                  "condM", "ill_conditioned",
                  "classification", "strict_ok", "constrained_ok"]
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r_ in rows:
            w.writerow({k: r_[k] for k in fieldnames})

    # Write summary JSON.
    summary = {
        "n_seeds": len(rows),
        "strict_pass_count": strict_pass_count,
        "strict_pass_all_50": strict_pass_count == 50,
        "constrained_pass_count": constrained_pass_count,
        "constrained_pass_all_50": constrained_pass_count == 50,
        "classification_counts": counts,
        "runtime_seconds": elapsed,
        "tolerances": {
            "deriv_tol_rad_inv": DERIV_TOL,
            "tie_tol": TIE_TOL,
            "end_tol_rad": END_TOL,
            "cond_warn": COND_WARN,
        },
        "seeds_used": [{"k": i, "seed_a": sa, "seed_b": sb}
                       for i, (sa, sb) in enumerate(SEEDS)],
    }
    json_path = os.path.join(out_dir, "paper12_q5_kappa0_audit_summary.json")
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nCSV:  {csv_path}")
    print(f"JSON: {json_path}")

    return rows, summary

if __name__ == "__main__":
    main()
