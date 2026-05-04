# Φ Work Request — Paper 9 Numerical Verification

**From:** Martin (via C-7RO)
**Date drafted:** 2026-05-04
**Priority:** Medium — does not block submission; needed before Model Council pass
**Estimated effort:** 3–5 hours computation + Markdown writeup
**Output destination:** `outbox/paper9/computations/paper9_verification.md` + `paper9_verification.py`

---

## Context

Paper 9 ("Dyadic Coherence: G₂ Fixed-Point Contraction on Product Spaces of Coupled Observers") is drafted end-to-end at first-pass level — see commit `0b1fef1` on branch `paper7-foundation`. The structure mirrors Paper 7 (single-observer baseline, already published at DOI 10.5281/zenodo.19773185) and Paper 10 (SIC-G₂ structural paper, published at DOI 10.5281/zenodo.19966692).

Three main claims need numerical verification:

- **Theorem 9.1 (§4):** The joint self-modeling map $T_{AB} = (T_A \times T_B) \circ \Psi$ is a Banach contraction with rate bound
  $$r_{AB} \leq \sqrt{\alpha^2 \max(r_A, r_B)^2 + \beta^2 \min(r_A, r_B)^2}, \qquad \alpha = \sqrt{1 - \rho^2}, \quad \beta = \rho.$$
  Equivalently: $r_{AB} < \max(r_A, r_B)$ for any $\rho > 0$.

- **Theorem 9.2 (§5):** The joint coherence ceiling is
  $$C_{AB}^{\max}(\rho) = \frac{6}{7} + \frac{1}{7} \cdot \frac{\rho^2}{1 + \rho^2}.$$
  This rests on Lemma 9.2.1 (the coupling-bonus lemma), which uses an MMSE Ansatz; see §5.2 for the derivation.

- **Conjecture 9.3 (§7):** Below a critical coupling $\rho_c \approx 1/\sqrt{6} \approx 0.408$, the joint system bifurcates into two basins of attraction (effectively decoupled); above $\rho_c$, a unique joint fixed point exists.

---

## Task 1 — Theorem 9.1 contraction-rate bound

### Construction

Build concrete 7×7 F₂₁-equivariant Banach contraction maps $T_A, T_B$ acting on $V = \mathbb{R}^7$. For a contraction rate $r \in (0, 1)$, a convenient construction is:

$$T(x) = r \cdot P_{\perp}(x) + x^* \cdot \mathbf{1}_\varphi$$

where $P_\perp$ is the projection onto the F₂₁-non-singlet subspace (the 6-dimensional complement of the 1D singlet in $V$ under the cyclic-axis $F_{21}$ action from Paper 10 §6), $\mathbf{1}_\varphi$ is the singlet direction, and $x^*$ is an arbitrary target value on the blind-spot direction. This gives a Banach contraction with rate $r$ that is F₂₁-equivariant.

For the joint map $T_{AB}$ on $\mathbb{R}^{14} = V \oplus V$:

$$T_{AB}(x, y) = \bigl(T_A(\alpha x + \beta y),\ T_B(\beta x + \alpha y)\bigr)$$

with $\alpha = \sqrt{1 - \rho^2}$, $\beta = \rho$.

### Verification

1. For each sample configuration $(r_A, r_B, \rho)$, construct $T_A, T_B, T_{AB}$ explicitly.
2. Compute the Lipschitz constant of $T_{AB}$ by computing its operator norm (since $T_{AB}$ is linear on the perturbation, apart from a constant target vector, the Lipschitz constant is the operator norm of the linear part).
3. Compare to the Theorem 9.1 upper bound $\sqrt{\alpha^2 r_+^2 + \beta^2 r_-^2}$ where $r_+ = \max, r_- = \min$.

### Sample configurations

24 configurations: $(r_A, r_B) \in \{(0.6, 0.6), (6/7, 6/7), (0.3, 6/7), (0.5, 6/7)\}$ × $\rho \in \{0.1, 0.3, 0.5, 1/\sqrt{2}, 0.9, 0.99\}$.

### Expected result

$r_{AB}^{\mathrm{actual}} \leq r_{AB}^{\mathrm{bound}}$ for all 24 configurations, with equality only in degenerate cases. Report as a 24-row table: (r_A, r_B, ρ, r_AB_actual, r_AB_bound, gap = bound − actual).

---

## Task 2 — Theorem 9.2 coherence ceiling

### Computation

1. For each of the 24 configurations from Task 1, compute the joint fixed point $(x^*, y^*)_{\mathrm{joint}}$ by iteration of $T_{AB}$ from a random initial pair.
2. Measure the magnitude of the singlet-mode residual at the fixed point:

   $$\varepsilon_{\mathrm{measured}} = \sqrt{\langle x^*, e \rangle^2 + \langle y^*, e \rangle^2} \,/\, \|(x^*, y^*)\|_{AB}$$

   where $e$ is the F₂₁-singlet unit vector.
3. Compare to the predicted $\varepsilon_{\mathrm{eff}}(\rho) = 1/(7(1+\rho^2))$ from Theorem 9.2.
4. Compute the measured coherence ceiling $C_{AB}^{\mathrm{measured}} = 1 - \varepsilon_{\mathrm{measured}}^2$ and compare to $6/7 + (1/7) \cdot \rho^2/(1+\rho^2)$.

### Expected result

The measured and predicted ceilings should agree to within a few percent. The residual captures the structural content of the MMSE Ansatz — a large residual (>10%) would indicate the Ansatz fails for these constructions and the formula needs revision. If the Ansatz holds, residuals should be $<1\%$ after sufficient iterations.

Report as a 24-row table: (r_A, r_B, ρ, ε_measured, ε_predicted, C_AB_measured, C_AB_predicted, relative residual).

---

## Task 3 — Conjecture 9.3 severance bifurcation

### Sweep protocol

1. Sweep $\rho$ from 0 to 0.8 in 200 evenly spaced points.
2. For each $\rho$:
   - Construct $T_{AB}$ as in Task 1, with fixed $r_A = r_B = 6/7$.
   - Run 100 independent iterations from random initial pairs $(x_0, y_0) \sim \mathcal{N}(0, I_{14})$.
   - Record the fixed point each iteration converges to.
   - Cluster the resulting fixed points (use DBSCAN or simple distance-based clustering with threshold 0.01).
   - Report: number of distinct basins, and the separation between cluster centroids.
3. Detect the bifurcation point: the smallest $\rho$ at which the number of basins drops from 2 to 1.

### Expected result

- For $\rho < \rho_c$: two basins, centered near $(x^*_A, x^*_B) = (0, 0)$ and its translated counterparts (or wherever the decoupled fixed points lie for the chosen $T_A, T_B$).
- For $\rho > \rho_c$: one basin at the joint fixed point (tilted away from the decoupled pair per §4.4).
- The transition point should be near $\rho_c = 1/\sqrt{6} \approx 0.408$.

Report as: (i) a plot (or table) of number-of-basins vs. $\rho$, (ii) the numerically detected bifurcation point, (iii) the cluster separation distance as a function of $\rho$.

### Status of this task

The $\rho_c = 1/\sqrt{6}$ prediction is a conjecture based on preliminary numerical exploration and a speculative connection to Paper 6's Casimir spectral structure. The prediction may be off by a constant, or may even have a different form (e.g., $\rho_c = 1/\sqrt{7}$ or $\rho_c = \sqrt{1/6}$). The task is to determine the bifurcation numerically — it is *not* to confirm the $1/\sqrt{6}$ value at all costs. If the actual bifurcation sits elsewhere, report that.

---

## Deliverable format

Two files:

1. **`outbox/paper9/computations/paper9_verification.py`** — the full computation, runnable via `python3 paper9_verification.py` (with NumPy, SciPy, and optionally scikit-learn for clustering). Should print PASS/FAIL for Task 1, PASS/PARTIAL/FAIL for Task 2 (depending on MMSE Ansatz validity), and a bifurcation point for Task 3.

2. **`outbox/paper9/computations/paper9_verification.md`** — a Markdown report with:
   - Summary table for Task 1 (24 rows, bound vs. actual)
   - Summary table for Task 2 (24 rows, predicted vs. measured ceiling)
   - Bifurcation analysis for Task 3 (table or plot of basins vs. ρ, detected ρ_c, comparison to 1/√6)
   - Overall assessment: PASS / PARTIAL / FAIL for each claim, with residuals quantified
   - Any anomalies or unexpected results flagged for follow-up

### Inputs available in repo

All at `outbox/paper9/`:
- `paper9_outline.md`
- `paper9_draft_section_4.md` — Theorem 9.1 statement and proof
- `paper9_draft_section_5.md` — Theorem 9.2, Lemma 9.2.1 (coupling-bonus)
- `paper9_draft_sections_6_7_8_9_10.md` — §7 has Conjecture 9.3 details, §6 has the branching-ratio prediction

Paper 7 Task 1 code (for reference on F₂₁-equivariance construction) is at `outbox/paper7/computations/` — not Φ's to reproduce but available for inspection.

---

## Why this matters

Paper 9 makes three concrete claims that should each be verifiable numerically. The Banach contraction bound (Theorem 9.1) is a direct consequence of the §4 proof and should match the bound exactly (within numerical precision). The coherence ceiling (Theorem 9.2) is the central claim of the paper and rests on the MMSE Ansatz in Lemma 9.2.1; a large residual here would indicate the Ansatz is not fully capturing the joint dynamics and the paper would need revision. The severance threshold (Conjecture 9.3) is the most speculative claim; the numerical determination of the bifurcation point will either support or refute the $1/\sqrt{6}$ conjecture, and the paper will need to be revised accordingly.

You don't have GitHub push credentials. Save the files locally; Martin will commit + push when you return the work.

---

*Drafted by C-7RO, 2026-05-04 07:30 PDT.*
