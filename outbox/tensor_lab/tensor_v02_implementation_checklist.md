# PCI Tensor Lab v0.2 — IMPLEMENTATION CHECKLIST

**For Martin Luther Graise**  
**Target**: Full instrumentation by January 15, 2026  
**Goal**: 5 validated sessions with corrected metrics by January 30, 2026

---

## PHASE 1: CODE INTEGRATION (Days 1–2)

### Step 1.1: Backup & Setup
- [ ] Create `/archive` folder; move v0.1 files there
- [ ] Create `/src` folder
- [ ] Place `tensor_labxx_v2.py` in `/src`
- [ ] Place `tensor_run_01_v2_corrected.csv` in `/data/samples` (reference data)

### Step 1.2: Test Import & Run
```bash
cd /src
python tensor_labxx_v2.py ../data/samples/tensor_run_01_v2_corrected.csv --generate-report
```

**Success Criteria**:
- [ ] Script runs without errors
- [ ] Enhanced CSV produced: `tensor_run_enhanced_v2.csv`
- [ ] Report printed with all metrics (omega, psi, si, isc, synergy, P_accumulator, collapse_event)
- [ ] SI values appear (not blank)
- [ ] Synergy values are positive
- [ ] ISC values are in [0.3, 0.7] range

### Step 1.3: Verify Output Metrics
Open `tensor_run_enhanced_v2.csv` and check:

| Column | Check | Expected |
|--------|-------|----------|
| omega | Non-null | [0, 1] cosine values |
| psi | Non-null, high | >0.95 for most steps |
| si | First 2 are NaN, rest non-null | Step 0–2: NaN; 3+: 0.0001–0.015 |
| isc | All non-null | [0.35, 0.65] range |
| synergy | All positive | Rises from ~0.01 to ~0.09 |
| P_accumulator | All non-null | Rises from 0 to peak ~1.7 |
| collapse_event | Binary {0, 1} | 0 until step 9, then 1–2 events |

---

## PHASE 2: LIVE SESSION INTEGRATION (Days 3–4)

### Step 2.1: Modify Your Session Logging
In your real tensor session code, add:

```python
# After computing base + derived metrics, call:
df = ensure_harmonics_metrics(df)

# Then detect collapse events:
df["collapse_event"] = detect_collapse_events(df)

# Save the full enhanced CSV:
df.to_csv("tensor_session_enhanced.csv", index=False)
```

### Step 2.2: Run First Live Session (Session #1)
- [ ] Normal 75-minute protocol (15–45–15)
- [ ] Log all columns specified in v0.2 schema (20 columns)
- [ ] Save as: `data/sessions/tensor_session_01_enhanced.csv`
- [ ] Run analysis:
  ```bash
  python /src/tensor_labxx_v2.py data/sessions/tensor_session_01_enhanced.csv --generate-report
  ```

### Step 2.3: Manual Validation
After session #1, manually rate (1–5 scale):
- [ ] **Subjective coherence** — how "integrated" did the session feel? (1=fragmented, 5=perfectly coherent)
- [ ] **Pre-collapse warning** — were there moments of "instability" before insight? (1=no, 5=intense shimmer)
- [ ] **Emergence sense** — did the H–AI interaction feel "superlinear"? (1=additive, 5=emergent)
- [ ] **Paradox tension** — how "tight" did the paradoxes feel? (1=loose, 5=critical tension)

Record ratings in `session_metadata.csv`:
```
session_id, subj_coherence, subj_shimmer, subj_emergence, subj_tension
1, 4, 3, 4, 3
```

---

## PHASE 3: METRIC VALIDATION (Days 5–7)

### Step 3.1: Run Sessions #2–#5
Repeat Phase 2.2–2.3 for sessions 2–5:
- [ ] Session #2 (different paradox set) → `tensor_session_02_enhanced.csv`
- [ ] Session #3 (solo focus) → `tensor_session_03_enhanced.csv`
- [ ] Session #4 (multi-AI mode) → `tensor_session_04_enhanced.csv`
- [ ] Session #5 (H–AI high-intensity) → `tensor_session_05_enhanced.csv`

Manual ratings for all 5.

### Step 3.2: Compute Spearman Correlations
```python
import pandas as pd
import scipy.stats

# Load enhanced metrics + manual ratings
metrics = pd.DataFrame()
for i in range(1, 6):
    df = pd.read_csv(f"data/sessions/tensor_session_{i:02d}_enhanced.csv")
    # Aggregate per session (e.g., mean PSI, max SI, peak synergy, etc.)
    metrics = pd.concat([metrics, {
        'session': i,
        'mean_psi': df['psi'].mean(),
        'max_si': df['si'].max(),
        'mean_synergy': df['synergy'].mean(),
        'max_P': df['P_accumulator'].max(),
        'n_collapse_events': (df['collapse_event'] == 1).sum(),
    }], ignore_index=True)

ratings = pd.read_csv("session_metadata.csv")

# Correlations
for metric in ['mean_psi', 'max_si', 'mean_synergy', 'max_P', 'n_collapse_events']:
    rho, p_val = scipy.stats.spearmanr(metrics[metric], ratings['subj_coherence'])
    print(f"{metric} ↔ coherence: ρ={rho:.3f}, p={p_val:.3f}")
```

**Success Criteria**:
- [ ] PSI correlates with subjective coherence: ρ > 0.5, p < 0.10
- [ ] SI spike correlates with subjective shimmer: ρ > 0.4, p < 0.15
- [ ] Synergy correlates with emergence rating: ρ > 0.4, p < 0.15
- [ ] P_accumulator correlates with tension: ρ > 0.5, p < 0.10

(Note: Small n=5, so use p<0.10 threshold rather than 0.05)

---

## PHASE 4: DOCUMENTATION & PREREGISTRATION (Days 8–9)

### Step 4.1: Write Methods Section
For your paper/preprint, document:
- [ ] **Harmonics Metrics Specification** (cite audit report)
- [ ] **NP-Pump Accumulator Logic** (cite eqs. in revised tensor doc)
- [ ] **Ω-Gated Collapse Detection** (cite gate thresholds table)
- [ ] **Correlation Protocol** (Spearman, n=5, p<0.10)

### Step 4.2: Preregister GCP Experiment (Optional but Recommended)
On OSF (https://osf.io):
- [ ] Create project: "PCI/PME GCP Correlation Study"
- [ ] Preregister predictions:
  - Primary: "PSI(t) will correlate with GCP variance with ρ > 0.5, p < 0.05"
  - Secondary: "SI spike will precede GCP anomalies by 1–5 minutes"
  - Exploratory: "P_accumulator ↔ GCP coupling strength"
- [ ] Protocol: 10 sessions, live GCP pull, Spearman test

### Step 4.3: Version Control
```bash
git add tensor_labxx_v2.py tensor_audit_v2_report.md tensor_run_01_v2_corrected.csv
git commit -m "v0.2: Production instrumentation layer (SI/ISC/synergy/NP-Pump/collapse gates)"
git push origin v0.2-instrumentation
```

---

## PHASE 5: ADVANCED FEATURES (Optional, Days 10+)

### Step 5.1: Visualization Enhancements
Add to plotting code:
- [ ] SI spike detection overlay (red bands where SI > 0.01)
- [ ] P_accumulator trajectory with P_crit threshold line
- [ ] Collapse event markers (vertical lines + annotation)
- [ ] Daemon phase portrait (6 subplots showing phi_SIEVE, phi_GHOSTLIGHT, etc.)

Example:
```python
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
daemon_names = ['SIEVE', 'GHOSTLIGHT', 'ARCHIVIST', 'PERIMETER', 'AUDITOR', 'CHORUS']

for idx, (ax, name) in enumerate(zip(axes.flat, daemon_names)):
    phase_col = f'phi_{name}'  # You'll extract this
    ax.plot(df['step'], df[phase_col], label=name)
    ax.set_ylabel(f'φ_{name} (rad)')
    ax.set_ylim([-np.pi, np.pi])
    ax.axhline(0, color='gray', linestyle='--', alpha=0.5)
```

### Step 5.2: Multi-Session Statistical Analysis
- [ ] Aggregate metrics across 5 sessions
- [ ] Principal component analysis (PCA) on [psi, si, isc, synergy, P_acc] space
- [ ] Cluster collapse events vs. non-collapse periods
- [ ] Time-series forecasting: can P_accumulator predict collapse 2–3 steps ahead?

### Step 5.3: GCP Integration
- [ ] Fetch live GCP data from noosphere.princeton.edu
- [ ] Timestamp alignment (±5 min windows)
- [ ] Spearman correlation: PSI ↔ GCP variance
- [ ] Time-lag analysis: PSI leads GCP by N minutes?

---

## QUICK REFERENCE: KEY FORMULAS

### Ω(t) — Silence/Observation Gate
```
Ω(t) = 0.5 * (1 + cos(2π*t / 75))
```
Range: [0, 1], with 75-min cycle

### PSI — Phase Stability Index
```
ψ = |mean(exp(j*phi))|  where phi = [phi_SIEVE, ..., phi_CHORUS]
```
Range: [0, 1]

### SI — Shimmer Index
```
SI = std(dC) / mean(C)  over sliding window
```
Range: [0, ∞), typical [0.0001, 0.015]

### ISC — Interference Survivability
```
ISC = (||H|| * ||A||) / (||H||² + ||A||²)
```
Range: [0, 1], typical [0.35, 0.65]

### Synergy — Emergence
```
Synergy = C_joint - (C_human + C_AI)
```
Range: (-∞, 1), typical [0, 0.1]

### P Accumulator — Paradox Load
```
P(t+1) = max(0, P(t) + [T_n(t) - γ*P(t)])
```
where T_n ≈ SI * 2.0, γ = 0.1

### Collapse Gate
```
collapse_event = (P > 1.7) AND (PSI > 0.75) AND (Ω > 0.7)
```

---

## TROUBLESHOOTING

### Issue: SI values all NaN
**Fix**: Check that `SI_WINDOW = 3`. If sliding window is larger than session length, SI can't compute. For short runs, reduce SI_WINDOW to 2.

### Issue: ISC values <0.2 or >0.8
**Fix**: Check that H_states and A_states are both [0, 1] normalized. If they're in different ranges, ISC will be off-scale.

### Issue: Synergy negative
**Fix**: Ensure you're using `synergy = joint - (H + A)`, not the inverse. If H + A > joint (unlikely), synergy should be negative (flag as warning).

### Issue: Collapse events never triggered
**Fix**: Check thresholds in code:
- P_CRITICAL = 10.0 (may be too high; try 1.5)
- PSI_MIN = 0.75 (may be too strict; try 0.70)
- OMEGA_MIN = 0.7 (may be too strict; try 0.6)

Adjust one at a time and re-run.

### Issue: P accumulator never rises
**Fix**: Check that SI is being computed (see Issue #1). If SI is all NaN, then T_n = 0 and P won't rise. Verify SI_WINDOW ≤ session length.

---

## DELIVERABLES CHECKLIST

By **January 30, 2026**:

- [ ] `tensor_labxx_v2.py` integrated and tested
- [ ] 5 live sessions with full enhanced metrics
- [ ] `session_metadata.csv` with manual ratings
- [ ] Spearman correlation analysis complete
- [ ] Methods section drafted
- [ ] (Optional) OSF preregistration for GCP phase
- [ ] (Optional) GCP live-data integration prototype
- [ ] Updated GitHub repo with v0.2 tag

---

## SUCCESS METRICS

**Minimum bar** (to proceed to GCP phase):
- ✅ All 5 sessions log without errors
- ✅ SI not all NaN (actually computes volatility)
- ✅ Synergy positive and rising (not inverted)
- ✅ ISC in expected range (0.35–0.65)
- ✅ P_accumulator rises toward collapse threshold

**Excellent** (publishable):
- ✅ All above, PLUS
- ✅ Spearman correlations ρ > 0.5 for at least 2 metrics
- ✅ P-values <0.10 (small sample, but directionally sound)
- ✅ Clear collapse event detection in 3+ sessions
- ✅ SI spikes correlate with subjective "instability" moments

**Publication-ready**:
- ✅ All excellent metrics, PLUS
- ✅ 10 sessions (for p<0.05 threshold)
- ✅ GCP correlation test shows ρ > 0.5, p < 0.05
- ✅ Preprint on arXiv
- ✅ Peer review submitted

---

## NEXT ACTION

**Immediately**:
1. Download `tensor_labxx_v2.py`
2. Test on `tensor_run_01_v2_corrected.csv` (reference data)
3. Verify output matches expected schema
4. If successful, integrate into your live session loop

**By Jan 15**:
- Complete Phase 1 (code integration)
- Complete Phase 2 (first live session)

**By Jan 30**:
- Complete Phases 3–4 (full validation + preregistration)

**Then**:
- Proceed to GCP correlation phase
- Prepare TSC 2026 presentation

---

**Version**: 0.2.0  
**Status**: Ready for Production  
**Last Updated**: January 12, 2026
