---
from: C-7RO
to: Φ
priority: 1
project: paper7
deadline: 2026-04-26 eod (Sunday)
expected_output: /outbox/paper7/work2/{B1_landauer_numbers,B2_mode_counting,priesemann_reanalysis,JHEP_doi_verified,status}.md + analysis CSV/plots for the Priesemann reanalysis
verification:
  - B1 Landauer derivation reproduces ~16 zJ at 310 K with published ATP comparison
  - B2 derivation identifies the factor of 7 explicitly from V₇ mode structure
  - Priesemann reanalysis reports subsampling-corrected mean σ and distributional skewness
  - JHEP DOI verified
---

# Paper 7 Work Item 2 (WI2b): Finalize predictions and execute the lead empirical test

Φ — your Work Item 1, 2, 3 landed clean. The three routed questions plus the 10⁹ flag all have resolutions now. All four are committed on the `paper7-foundation` branch. Summary:

**Martin's decision on the 10⁹ flag:** APPROVED the hybrid B1 + B2 split (see `/inbox/for_human/10e9_flag_recommendation.md` for the recommendation text). Prediction (b) is now two sub-predictions. Details in `/outbox/paper7/PAPER7_revisions_v2.md`.

**C-7RO's responses to your three questions:** All in `/outbox/paper7/responses/`. Short versions:
- FDT reference: Option B (PSD ratio), bound form ε ≥ 1/7, reference state = deep anesthesia as empirical equilibrium proxy. Derived from Banach contraction L = 6/7 directly (Paper 6).
- 8-coset Hamiltonian: V₇ fundamental rep, clock = H_singlet in the V₁ direction of 3 ⊕ 3̄ ⊕ 1 branching, S_reference = log₂(6) k_B. Coset entropy differences discrete, indexed by Cayley distance d ∈ {0,1,2,3}.
- Branching ratio: 49 = 1+14+27+7 (primary interpretation); sign c < 0 (sub-critical) from dissipative Laplacian flow; σ_pred = 1 − 1/49 ≈ 0.9796.

Read the full responses before starting.

---

## Work Item 2b — Five deliverables

All outputs go to `/outbox/paper7/work2/`. Create that directory.

### Task 1 — B1 Biological Landauer derivation

Save to `/outbox/paper7/work2/B1_landauer_numbers.md`.

Compute the explicit Landauer lower bound for the G₂ Checkpoint at biological temperature, and compare to published ATP measurements.

- Derive ΔE_min = log₂(42) × k_B T ln 2 explicitly. Show the arithmetic.
- At T = 310 K: ΔE_min = ? (expected ~16 zJ). Recompute exactly; do not round until the end.
- Also compute bounds for the 10-bit and 20-bit scenarios you flagged earlier as the biological range.
- Compare to published ATP data for G₂/M transition. Cite the Imamura et al. (2009) PNAS paper and any follow-ups you can find. What is the measured ATP cost per checkpoint event, in zJ?
- Report the orders-of-magnitude gap: predicted minimum ~16 zJ vs. measured ~10⁵ zJ. The prediction is a bound (≥), not an equality, so this is the expected direction for an irreversible biological switch.
- Flag any caveats: substrate-specific variation, cell-type dependence, measurement protocol assumptions.

### Task 2 — B2 Quantum mode-counting derivation

Save to `/outbox/paper7/work2/B2_mode_counting.md`.

Derive the factor of 7 from the V₇ fundamental representation explicitly.

- Set up a Lindblad clock model where the ticking mechanism is a quantum process constrained to G₂ symmetry.
- Show that the entropy per tick contains a mode-counting factor equal to dim(V₇) = 7.
- Identify the remaining factor in the Wadhia 10⁹ as the temperature ratio (T_readout / T_clock) × ln(N_pointer) where N_pointer is the pointer-state distinguishability. For Wadhia's experiment: millikelvin quantum dot (T_clock ~ 10⁻² K) vs room-temperature classical readout (T_readout ~ 300 K), so T_readout/T_clock ~ 3 × 10⁴; pointer distinguishability adds another ~10⁴; total ~10⁸ from hardware, times G₂'s 7 = ~7 × 10⁸ ≈ 10⁹. Honesty check: is the factorization exactly like this, or is some of the hardware contribution subsumed into the mode count?
- **Honest note:** This is an order-of-magnitude structural argument, not a precision derivation. State as `[Conjecture + Order-of-Magnitude]`.
- Flag: the precise Lindblad derivation of the factor-of-7 is an open computation for Paper 8 or a companion note.

### Task 3 — Priesemann reanalysis on Hengen-Shew data (LEAD EMPIRICAL TEST)

Save to `/outbox/paper7/work2/priesemann_reanalysis.md` plus a CSV of per-dataset σ values (`per_dataset_sigma.csv`) and a plot (`sigma_distribution.png` or `.svg`).

**This is the lead empirical confirmation for Paper 7.** Download the Hengen-Shew data from Zenodo record 15420312 (open access, https://zenodo.org/record/15420312).

1. **Extract σ for each of the 140 datasets** using the Wilting-Priesemann subsampling-corrected estimator. Critical: uncorrected σ estimates have finite-size bias that can mimic sub-critical displacement. The correction is described in Wilting & Priesemann (2018) Nat Commun; reference implementation exists in the mrestimator Python package.
2. **Compute the distributional statistics:**
   - Mean σ
   - Median σ
   - Mode σ (if distribution is unimodal)
   - Standard deviation
   - Skewness (negative skew = tail toward sub-critical, positive skew = tail toward super-critical)
3. **Subset analysis:**
   - Awake stationary-state datasets (cluster prediction: ~0.98)
   - Transition-state datasets (spread prediction: wider distribution centered closer to 1.00)
   - Anesthesia datasets (cluster prediction: closer to 1.00, since anesthesia may push above the attractor)
4. **Report the predicted number:** G₂ predicts σ_pred = 1 − 1/49 ≈ 0.9796. Is this consistent with the subsampling-corrected awake-state subset?
5. **Report the G₂ falsification:** If subsampling-corrected mean σ > 1.0 in awake stationary data, the prediction is falsified.
6. **Produce a plot:** histogram of per-dataset σ values, with the G₂ prediction σ = 0.9796 marked as a vertical line, and the Hengen-Shew pooled σ = 1.0 marked as a second vertical line. Color by dataset subset if possible.

This task has the highest priority — a positive result here is Paper 7's empirical headline.

If any dataset is gated, inaccessible, or improperly formatted, flag it — don't silently drop it.

### Task 4 — Verify the JHEP DOI

Save to `/outbox/paper7/work2/JHEP_doi_verified.md`.

- Expected DOI format: 10.1007/JHEP07(2025)146
- Verify by manual URL check: https://link.springer.com/article/10.1007/JHEP07(2025)146
- Confirm authors: De Vuyst J, Eccles S, Höhn PA, Kirklin J
- Confirm title — record the exact published title.
- If the DOI doesn't resolve, search INSPIRE-HEP for authors + 2025 to locate the paper.

### Task 5 — Status and flags

Save to `/outbox/paper7/work2/status.md`.

One-paragraph status. Include:
- What completed.
- Any surprises (always flag surprises).
- Any derivation that broke under scrutiny.
- Estimated time-to-complete if anything runs long.

---

## Flags and questions

As before: any derivation that breaks, any dataset contradiction, any prior-art discovery that scoops Paper 7 → flag immediately to `/inbox/for_human/`.

Technical questions for C-7RO that block forward progress → `/inbox/for_c7ro/`.

Don't guess when uncertain. Flag.

---

## Context files to read before starting

1. `/outbox/paper7/PAPER7_revisions_v2.md` — full revisions approved today
2. `/outbox/paper7/responses/FDT_reference_response.md` — Option B, bound form, operationalization
3. `/outbox/paper7/responses/8coset_Hamiltonian_response.md` — V₇, singlet clock, coset structure
4. `/outbox/paper7/responses/branching_ratio_sign_response.md` — 49 disambiguation, c < 0, Laplacian dissipation
5. `/inbox/for_human/10e9_flag_recommendation.md` — the B1+B2 rationale
6. `/outbox/paper7/anchor_papers_verified.md` — your own WI1 output (citations)

Target completion: Sunday April 26 EOD PDT. Paper 7 body drafting by C-7RO begins Monday against your output.

— C-7RO
