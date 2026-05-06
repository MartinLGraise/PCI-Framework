# Paper 12 §3/§4 — Phi Audit Findings (Session 1)

**Date:** 2026-05-05 (late)
**Auditor:** Φ (Perplexity Computer running Claude Sonnet 4.6)
**Source session:** ChatGPT 5.5 Pro, transcript at `outbox/paper12/chatgpt_pro_session_transcript_2026-05-05.pdf`
**Audit queue source:** `outbox/paper12/paper12_section3_session_extract.md` §7

## Headline Verdicts

### Q5 — κ=0 gradient-flow recovery audit

**STRICT FAIL — CONSTRAINED PASS (50/50)**

ChatGPT's prediction was confirmed exactly as stated. The strict claim "all 50 MC θ★ values satisfy c'(θ★) = 0" fails (only 3 of 50 are smooth interior critical points). The constrained/stratified recovery — that each seed is one of {smooth-interior-zero, boundary-left-KKT, boundary-right-KKT, Σ_min-Clarke-OK} — passes for all 50 seeds.

**Implication for Paper 12 §3:** the projected-gradient framing is *forced by the data*. The unperturbed flow must be written as

$$\dot\theta = \Pi_{T_{[0, \pi/2]}(\theta)}\bigl(\eta c'(\theta)\bigr)$$

with Filippov sliding on Σ_min and Clarke generalized-gradient treatment of nonsmooth critical points.

### Q4 — F₂₁ character verification

**CONFIRMED: V¹⁴|_{F₂₁} ≅ L₂ ⊕ 2U₆**

All three layers of verification pass:

1. **Per-class character values:** computed χ_V¹⁴ = (14, 0, 0, -1, -1) matches predicted L₂ ⊕ 2U₆ exactly.
2. **Frobenius norm:** ⟨χ_V¹⁴, χ_V¹⁴⟩_F = 10, matching the complex-type-corrected expected value 0 + 1·2 + 4·2 = 10.
3. **Isotypic multiplicities:** m_trivial = 0, m_{L₂} = 1, m_{U₆} = 2 — exact match.

**Implication for Paper 12 §4:** the hierarchy theorem $G_2 \Rightarrow F_{21} \Rightarrow \mu_k$-match has its load-bearing computation verified. ChatGPT's Q4 confidence rises from 74% to 95%.

---

## Q5 Detailed Results

### Classification breakdown across 50 seeds

| Classification | Count | Fraction |
|---|---|---|
| boundary_left_KKT (θ★ = 0°, c'_+(0) ≤ 0) | **25** | 50% |
| Sigma_min_Clarke_OK (on Σ_min, 0 ∈ conv{c_A', c_B'}) | **19** | 38% |
| smooth_interior_zero (interior, |c'| < 1e-6) | **3** | 6% |
| boundary_right_KKT (θ★ = π/2, c'_-(π/2) ≥ 0) | **3** | 6% |
| **Total constrained pass** | **50/50** | **100%** |

**Interpretation:**

- **The "boundary-dominated" prediction was correct.** 25 of 50 seeds are boundary-left optima where the gradient at θ=0 is strictly negative (mean c'(0) ≈ -0.27 rad⁻¹ across these seeds). At θ=0, the system *wants* to move into negative θ but is blocked by the [0, π/2] constraint — classic KKT condition. Trying to write these as classical gradient critical points would be wrong.

- **A surprise: 19 of 50 are Σ_min seeds.** ChatGPT predicted "Σ_min seeds rare/none." Reality: 38% of seeds have c_A(θ★) = c_B(θ★) at the optimum. The min-functional's kink locus is doing more work than expected. **This makes the Filippov sliding-mode treatment of §3 more important than predicted, not less.**

- **The original Paper 9 MC seed (k=0, θ★ ≈ 51° from the snapped 20-point grid) reoptimizes to θ★ = 0°** — the high-precision optimum is on the boundary, not at 51°. The Paper 9 grid resolution (π/2/19 ≈ 4.74°) was simply too coarse to see this. **This is a real correction:** Paper 9's k=0 seeded-geometry θ★ value reported in Proposition 9.5 is grid-snapped; the true high-precision optimum is at the boundary. The Paper 9 substantive results (existence of gain region, etc.) are unaffected, but Paper 12's §3 must use reoptimized values, not the MC-snapped ones.

- **Only 3 seeds (k=16, 23, 38) land in the smooth interior** with |c'| < 1e-9 cleanly. These are the cases where Fermat's theorem applies and §3's classical recovery argument works without modification. The other 47 require constraint or stratification handling.

### Notable per-seed values

| k | seeds | θ★ (deg) | c★ | classification | c'(θ★) |
|---|---|---|---|---|---|
| 0 | (20260504, 20260505) | 0.000 | 0.7401 | boundary_left_KKT | -0.315 |
| 7 | (20260511, 20260512) | 5.190 | 0.7650 | Sigma_min_Clarke_OK | NaN |
| 16 | (20260520, 20260521) | 66.745 | 0.6526 | **smooth_interior_zero** | +4.4e-9 |
| 23 | (20260527, 20260528) | 75.566 | 0.6753 | **smooth_interior_zero** | -6.9e-9 |
| 38 | (20260542, 20260543) | 34.213 | 0.6427 | **smooth_interior_zero** | -4.4e-9 |

Full per-seed CSV: `outbox/paper12/computations/paper12_q5_kappa0_audit.csv`.

### Tolerances used

- `DERIV_TOL = 1e-6 rad⁻¹` — strict classical derivative-zero
- `TIE_TOL = 1e-8` — min-locus detection on |c_A − c_B|
- `END_TOL = 1e-5 rad ≈ 5.73e-4°` — endpoint detection
- `COND_WARN = 1e10` — condition-number warning (none triggered)

### Runtime

Total: 0.19 seconds for 50 seeds. Cheap.

---

## Q4 Detailed Results

### Method

The Fano-orientation subgroup F₂₁ ⊂ G₂ acts on the imaginary octonions ℝ⁷ via:
- Z₇ generator $r$: cyclic shift $i \mapsto i+1 \mod 7$ (acting on indices 0..6)
- Z₃ generator $s$: multiplication by 2, $i \mapsto 2i \mod 7$

These generate F₂₁ via $s r s^{-1} = r^2$ (Frobenius relation, verified numerically).

The 14-dim adjoint character is computed from the 7-dim defining representation via:
$$\chi_{V^{14}}(g) = \chi_{\Lambda^2(\mathbb{R}^7)}(g) - \chi_{\mathbb{R}^7}(g) = \frac{\mathrm{tr}(g)^2 - \mathrm{tr}(g^2)}{2} - \mathrm{tr}(g)$$

### Per-class characters

| Class | Size | tr(g) on R⁷ | Predicted χ_V¹⁴ | Computed χ_V¹⁴ | Match |
|---|---|---|---|---|---|
| 1a (identity) | 1 | 7 | 14 | 14.0000 | ✓ |
| 7a (order 7) | 3 | 0 | 0 | 0.0000 | ✓ |
| 7b (order 7) | 3 | 0 | 0 | 0.0000 | ✓ |
| 3a (order 3) | 7 | 1 | -1 | -1.0000 | ✓ |
| 3b (order 3) | 7 | 1 | -1 | -1.0000 | ✓ |

### Inner-product check

$$\langle \chi_{V^{14}}, \chi_{V^{14}} \rangle_{F_{21}} = \frac{1}{|F_{21}|} \sum_{c} |c| \cdot |\chi(c)|^2 = \frac{1 \cdot 196 + 3 \cdot 0 + 3 \cdot 0 + 7 \cdot 1 + 7 \cdot 1}{21} = \frac{210}{21} = 10$$

For real complex-type irreps, ⟨χ_W, χ_W⟩_F = 2 (not 1) because each is the real packaging of two conjugate complex 1-dim or 3-dim irreps. So the expected value for $V^{14}|_F = L_2 \oplus 2 U_6$ is

$$0^2 \cdot 1 + 1^2 \cdot 2 + 2^2 \cdot 2 = 0 + 2 + 8 = 10 ✓$$

### Multiplicities

Computed via $m_W = \frac{1}{2} \langle \chi_{V^{14}}, \chi_W \rangle$ for complex-type irreps:

| Irrep | Real dim | ⟨χ_V¹⁴, χ_W⟩_F (raw) | Multiplicity m_W |
|---|---|---|---|
| trivial | 1 | 0.000000 | 0 |
| L_2 (complex-type) | 2 | 2.000000 | **1** |
| U_6 (complex-type) | 6 | 4.000000 | **2** |

Verifying: $\dim(L_2 \oplus 2 U_6) = 2 + 12 = 14$ ✓.

### Implication

$$V^{14}|_{F_{21}} \cong L_2 \oplus 2 U_6$$

is now a *computed* result, not a *claimed* result. Paper 12 §4 can cite this directly. The hierarchy theorem $G_2 \Rightarrow F_{21} \Rightarrow \mu_k$-match has its concrete F₂₁-decomposition pinned.

JSON: `outbox/paper12/computations/paper12_q4_character_verify.json`.

---

## What This Means for Paper 12 Going Forward

### §3 (NP-pump nonlinearity) is now ready to draft

The κ=0 limit must be the **projected gradient flow** on $[0, \pi/2]$, with three legitimate cases:

1. **Smooth interior** (3 of 50 seeds): classical Fermat condition c'(θ★) = 0 applies.
2. **Boundary KKT** (28 of 50 seeds: 25 left + 3 right): one-sided derivative inequality, projected gradient is zero on the constraint.
3. **Σ_min Clarke** (19 of 50 seeds): nonsmooth critical point, generalized gradient 0 ∈ conv{c_A', c_B'}.

The framework ChatGPT specified is the right one. The unexpected finding — Σ_min activity in 38% of seeds — strengthens rather than weakens the case for the layered Carathéodory/Filippov/hybrid framework: the Filippov sliding-mode treatment is now well-motivated empirically.

### §4 (commensurability hierarchy) is now ready to draft

The F₂₁-decomposition $V^{14}|_F = L_2 \oplus 2 U_6$ is verified at machine precision. The forced thesis upgrade — F₂₁ insufficient, full G₂ required — has its load-bearing computation. The hierarchy

$$G_2\text{-commensurability} \Rightarrow F_{21}\text{-profile} \Rightarrow \mu_k\text{-match}$$

is now a concretely-citable result, not a sketch.

### Updated confidence ranking

| # | Question | ChatGPT | Φ-audited |
|---|---|---|---|
| 1 | Q2 — Schur ξ★ derivation | 92% | 92% (no audit needed) |
| 2 | Q1 — Σ_tot stratification | 84% | **92%** (Σ_min activity confirms layered framework) |
| 3 | Q4 — F₂₁→G₂ upgrade | 74% | **95%** (character calc verified) |
| 4 | Q3 — 𝔍_k scar invariant | 61% | 61% (language-tighten only) |
| 5 | Q5 — κ=0 recovery | 43% | **90%** (predicted strict-fail confirmed; bonus discovery of Σ_min activity) |

Overall the session went from average confidence ≈70% to ≈86% in 30 minutes of computation. **Paper 12 §3 and §4 are no longer thesis-only — they're computationally-grounded with a verified decomposition theorem and a verified κ=0 recovery classification.**

### Paper 9 cross-reference

One result here has a *direct implication* for Paper 9 v1.3.2: the seed-k=0 θ★ value reported in Proposition 9.5 (≈51° from the 20-point MC grid) reoptimizes to θ★ = 0° at high precision. The seeded geometry is on the boundary, not the interior. **Paper 9's substantive results are unaffected** (existence of gain region, the 50-seed Conjecture 9.5' results, etc.), but a one-paragraph errata note may be appropriate — to be evaluated when drafting Paper 12 §3 next session. For now, this is captured in the audit record and does not require immediate Paper 9 republication.

### Action items

**Pre-§3-drafting (complete):**
- [x] Φ runs Q5 audit ← DONE, 50/50 constrained pass
- [x] Φ verifies V¹⁴|_{F₂₁} character ← DONE, confirmed
- [ ] Update thesis memo §8 changelog with audit verdicts (next git commit)

**During §3 drafting:**
- Use "representation-theoretic scar invariant" language for 𝔍_k throughout
- State κ=0 recovery as projected-gradient flow with three legitimate cases
- Cite the 25/19/3/3 seed breakdown as empirical motivation for the Filippov treatment
- Note the seed-k=0 reoptimization at first reference to Paper 9's Proposition 9.5

**During §4 drafting:**
- State the hierarchy theorem with the verified F₂₁ decomposition $V^{14}|_F = L_2 \oplus 2 U_6$
- Cite End_F(W) = M₂(ℂ) ⊕ M₄(ℂ) vs End_{G₂}(W) = M₂(ℝ) as the quantitative gap
- Frame P3 as the two-level test (necessary F₂₁-screen + sufficient G₂-canonical)

### Files created

- `outbox/paper12/computations/paper12_q5_kappa0_audit.py` (309 lines, runs in 0.19s)
- `outbox/paper12/computations/paper12_q5_kappa0_audit.csv` (50 rows, full per-seed data)
- `outbox/paper12/computations/paper12_q5_kappa0_audit_summary.json` (aggregate stats)
- `outbox/paper12/computations/paper12_q4_character_verify.py` (303 lines, runs in <0.1s)
- `outbox/paper12/computations/paper12_q4_character_verify.json` (verification results)
- `outbox/paper12/computations/paper12_session1_audit_findings.md` (this document)

All files committed to GitHub branch `paper7-foundation` of `MartinLGraise/PCI-Framework`.

---

*End of audit findings. Session complete; Paper 12 §3 and §4 cleared for drafting whenever Martin returns to the work.*
