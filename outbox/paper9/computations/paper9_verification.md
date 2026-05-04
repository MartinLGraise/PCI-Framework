# Paper 9 Numerical Verification — Dyadic Coherence

**PCI/PME Framework | branch `paper7-foundation` | commit `0b1fef1`**
**Executed by:** Φ | **Date:** 2026-05-04
**Spec source:** Prompt spec (raw.githubusercontent.com blocked at network layer; fallback per instructions)

---

## Preamble

All three tasks were run in float64 on the canonical construction described in the spec:

- **T_A, T_B** = $r \cdot Q$ where $Q$ is a random orthogonal $7 \times 7$ matrix (QR decomposition, det corrected to +1), one per agent seeded deterministically.
- **Ψ(ρ)** = block $\begin{pmatrix} \alpha I & \rho I \\ \rho I & \alpha I \end{pmatrix}$ on $\mathbb{R}^{14}$, $\alpha = \sqrt{1-\rho^2}$.
- **T_AB** = diag($T_A$, $T_B$) · Ψ on $\mathbb{R}^{14}$.
- **r_AB** = $\sigma_{\max}(T_{AB})$ via full SVD (machine precision $\sim 10^{-16}$).
- **Inaccessible direction:** $u_{\text{inacc}} = (1,\ldots,1)^T / \sqrt{14} \in \mathbb{R}^{14}$ (symmetric eigenvector of Ψ).

---

## TASK 1 — Theorem 9.1: Contraction Rate Bound

**Claim:** $r_{AB} \leq \sqrt{\alpha^2 \max(r_A, r_B)^2 + \beta^2 \min(r_A, r_B)^2}$, where $\alpha = \sqrt{1-\rho^2}$, $\beta = \rho$.

### Results — all 24 configurations

| r_A   | r_B   | ρ     | r_AB      | bound     | ratio   | result |
|-------|-------|-------|-----------|-----------|---------|--------|
| 0.600 | 0.600 | 0.100 | 0.6569925 | 0.6000000 | 1.09499 | FAIL   |
| 0.600 | 0.600 | 0.300 | 0.7523635 | 0.6000000 | 1.25394 | FAIL   |
| 0.600 | 0.600 | 0.500 | 0.8196152 | 0.6000000 | 1.36603 | FAIL   |
| 0.600 | 0.600 | 0.707 | 0.8485281 | 0.6000000 | 1.41421 | FAIL   |
| 0.600 | 0.600 | 0.900 | 0.8015339 | 0.6000000 | 1.33589 | FAIL   |
| 0.600 | 0.600 | 0.990 | 0.6786404 | 0.6000000 | 1.13107 | FAIL   |
| 0.857 | 0.857 | 0.100 | 0.9384042 | 0.8570000 | 1.09499 | FAIL   |
| 0.857 | 0.857 | 0.300 | 1.0746259 | 0.8570000 | 1.25394 | FAIL   |
| 0.857 | 0.857 | 0.500 | 1.1706838 | 0.8570000 | 1.36603 | FAIL   |
| 0.857 | 0.857 | 0.707 | 1.2119810 | 0.8570000 | 1.41421 | FAIL   |
| 0.857 | 0.857 | 0.900 | 1.1448576 | 0.8570000 | 1.33589 | FAIL   |
| 0.857 | 0.857 | 0.990 | 0.9693247 | 0.8570000 | 1.13107 | FAIL   |
| 0.300 | 0.857 | 0.100 | 0.8593518 | 0.8532318 | 1.00717 | FAIL   |
| 0.300 | 0.857 | 0.300 | 0.8754773 | 0.8224649 | 1.06446 | FAIL   |
| 0.300 | 0.857 | 0.500 | 0.8966006 | 0.7571900 | 1.18412 | FAIL   |
| 0.300 | 0.857 | 0.707 | 0.9079917 | 0.6421229 | 1.41405 | FAIL   |
| 0.300 | 0.857 | 0.900 | 0.8901586 | 0.4609179 | 1.93127 | FAIL   |
| 0.300 | 0.857 | 0.990 | 0.8615997 | 0.3206626 | 2.68694 | FAIL   |
| 0.500 | 0.857 | 0.100 | 0.8654592 | 0.8541689 | 1.01322 | FAIL   |
| 0.500 | 0.857 | 0.300 | 0.9148405 | 0.8311730 | 1.10066 | FAIL   |
| 0.500 | 0.857 | 0.500 | 0.9671476 | 0.7831582 | 1.23493 | FAIL   |
| 0.500 | 0.857 | 0.707 | 0.9921940 | 0.7016393 | 1.41411 | FAIL   |
| 0.500 | 0.857 | 0.900 | 0.9521538 | 0.5848464 | 1.62804 | FAIL   |
| 0.500 | 0.857 | 0.990 | 0.8731579 | 0.5095493 | 1.71359 | FAIL   |

**Summary: 0 PASS, 24 FAIL (24/24 configurations).**

### Analytical diagnosis

The failure is not numerical noise — it is a provable algebraic identity.

**Exact formula for r_AB.** Because $T_A = r_A Q_A$ and $T_B = r_B Q_B$ with $Q$ orthogonal, $T_A^T T_A = r_A^2 I$ and $T_B^T T_B = r_B^2 I$. Therefore:

$$T_{AB}^T T_{AB} = \begin{pmatrix} (\alpha^2 r_A^2 + \rho^2 r_B^2) I & \alpha\rho(r_A^2 + r_B^2) I \\ \alpha\rho(r_A^2 + r_B^2) I & (\rho^2 r_A^2 + \alpha^2 r_B^2) I \end{pmatrix}$$

This is a block-scalar matrix — 7 independent copies of the $2 \times 2$ matrix

$$M = \begin{pmatrix} \alpha^2 r_A^2 + \rho^2 r_B^2 & \alpha\rho(r_A^2 + r_B^2) \\ \alpha\rho(r_A^2 + r_B^2) & \rho^2 r_A^2 + \alpha^2 r_B^2 \end{pmatrix}$$

whose eigenvalues are:

$$\lambda = \frac{(r_A^2 + r_B^2) \pm \sqrt{(r_A^2 + r_B^2)^2 - 4(\alpha^2 - \rho^2)^2 r_A^2 r_B^2}}{2}$$

Hence $r_{AB} = \sqrt{\lambda_{\max}}$ exactly.

**Symmetric case ($r_A = r_B = r$):**

$$\lambda_{\max} = r^2(1 + 2\alpha\rho) = r^2(\alpha + \rho)^2 \quad \Longrightarrow \quad r_{AB} = r(\alpha + \rho)$$

The claimed bound reduces to $r\sqrt{\alpha^2 + \rho^2} = r$ (since $\alpha^2 + \rho^2 = 1$). But $(\alpha + \rho)^2 = 1 + 2\alpha\rho \geq 1$, so

$$r_{AB} = r(\alpha + \rho) \geq r = \text{bound}, \quad \text{for all } \rho > 0.$$

The bound is violated by factor $(\alpha + \rho)$ for every symmetric, non-zero coupling. At $\rho = 1/\sqrt{2}$ (maximum amplification), ratio $= \sqrt{2} \approx 1.414$ — matching the table exactly.

**Root cause:** The coupling map Ψ has singular values $(\alpha + \rho)$ and $(\alpha - \rho)$. For $\rho > 0$, the dominant singular value $\alpha + \rho = \sqrt{1-\rho^2} + \rho > 1$ — Ψ amplifies along the symmetric mode. The bound formula $\sqrt{\alpha^2 \max^2 + \rho^2 \min^2}$ does not account for this cross-coupling amplification. A valid bound for the symmetric case would be $r \cdot (\alpha + \rho)$; for the general case the exact formula above applies.

**Recommendation:** Theorem 9.1 requires either (a) a corrected bound that includes the Ψ amplification factor, or (b) a coupling map that is a norm contraction (e.g., Ψ replaced by a block-rotation with $\|\Psi\| \leq 1$).

---

## TASK 2 — Theorem 9.2: Coherence Ceiling

**Claim:** $C_{AB}^{\max}(\rho) = 6/7 + (1/7) \cdot \rho^2/(1+\rho^2)$

**Method:** For linear $T_{AB}$ with $r_{AB} < 1$, Banach's theorem gives unique fixed point 0. The coherence of the dominant mode is measured from the leading right singular vector $v_1$ of $T_{AB}$ (the direction approached by power iteration as $x \to 0$). Coherence $= 1 - |v_1 \cdot u_{\text{inacc}}|^2$ where $u_{\text{inacc}} = (1,\ldots,1)/\sqrt{14}$.

### Results

| r_A   | r_B   | ρ     | r_AB    | C_meas   | C_pred   | \|resid\| | note         |
|-------|-------|-------|---------|----------|----------|---------|--------------|
| 0.600 | 0.600 | 0.100 | 0.65699 | 0.998917 | 0.858557 | 0.140360 | contractive  |
| 0.600 | 0.600 | 0.300 | 0.75236 | 0.999669 | 0.868938 | 0.130731 | contractive  |
| 0.600 | 0.600 | 0.500 | 0.81962 | 0.998848 | 0.885714 | 0.113134 | contractive  |
| 0.600 | 0.600 | 0.707 | 0.84853 | 0.902815 | 0.904752 | 0.001938 | contractive  |
| 0.600 | 0.600 | 0.900 | 0.80153 | 0.930365 | 0.921073 | 0.009291 | contractive  |
| 0.600 | 0.600 | 0.990 | 0.67864 | 0.998838 | 0.927854 | 0.070984 | contractive  |
| 0.857 | 0.857 | 0.100 | 0.93840 | 0.777328 | 0.858557 | 0.081229 | contractive  |
| 0.857 | 0.857 | 0.300 | 1.07463 | —        | —        | —        | SKIP r_AB≥1  |
| 0.857 | 0.857 | 0.500 | 1.17068 | —        | —        | —        | SKIP r_AB≥1  |
| 0.857 | 0.857 | 0.707 | 1.21198 | —        | —        | —        | SKIP r_AB≥1  |
| 0.857 | 0.857 | 0.900 | 1.14486 | —        | —        | —        | SKIP r_AB≥1  |
| 0.857 | 0.857 | 0.990 | 0.96932 | 0.802118 | 0.927854 | 0.125736 | contractive  |
| 0.300 | 0.857 | 0.100 | 0.85935 | 0.999838 | 0.858557 | 0.141280 | contractive  |
| 0.300 | 0.857 | 0.300 | 0.87548 | 0.724109 | 0.868938 | 0.144830 | contractive  |
| 0.300 | 0.857 | 0.500 | 0.89660 | 0.643226 | 0.885714 | 0.242488 | contractive  |
| 0.300 | 0.857 | 0.707 | 0.90799 | 0.991102 | 0.904752 | 0.086349 | contractive  |
| 0.300 | 0.857 | 0.900 | 0.89016 | 0.954031 | 0.921073 | 0.032957 | contractive  |
| 0.300 | 0.857 | 0.990 | 0.86160 | 0.933300 | 0.927854 | 0.005447 | contractive  |
| 0.500 | 0.857 | 0.100 | 0.86546 | 0.753767 | 0.858557 | 0.104790 | contractive  |
| 0.500 | 0.857 | 0.300 | 0.91484 | 0.826965 | 0.868938 | 0.041973 | contractive  |
| 0.500 | 0.857 | 0.500 | 0.96715 | 0.985760 | 0.885714 | 0.100046 | contractive  |
| 0.500 | 0.857 | 0.707 | 0.99219 | 0.912522 | 0.904752 | 0.007769 | contractive  |
| 0.500 | 0.857 | 0.900 | 0.95215 | 0.917819 | 0.921073 | 0.003255 | contractive  |
| 0.500 | 0.857 | 0.990 | 0.87316 | 0.965289 | 0.927854 | 0.037436 | contractive  |

**Summary:** 20 configurations measured; 4 skipped ($r_{AB} \geq 1$). Of the 20 measured:

- Residuals range: **0.002 to 0.242**
- Median residual: **~0.093**
- Only 5 configurations fall within "a few percent" (< 0.05) of the prediction.
- **15 of 20 configurations exceed 5% residual.** The formula is not confirmed to within spec tolerance.

### Analytical diagnosis

For the symmetric case ($r_A = r_B$), $T_{AB}^T T_{AB}$ has a 7-dimensional degenerate eigenspace at $\lambda_{\max} = r^2(\alpha + \rho)^2$, spanned by all vectors of the form $(v, v)/\sqrt{2} \in \mathbb{R}^{14}$. The coherence of any such vector relative to $u_{\text{inacc}} = (1,\ldots,1)/\sqrt{14}$ depends on the inner product $\bar{v} = \langle v, (1,\ldots,1)/\sqrt{7} \rangle$, which is seed/initialization-dependent. There is no deterministic limit — coherence varies continuously across the eigenspace.

The formula $C = 6/7 + (1/7)\rho^2/(1+\rho^2)$ may describe an *expected* coherence averaged over random initializations (with the 6/7 term from the fraction of a random unit vector in $\mathbb{R}^7$ orthogonal to the uniform direction), but it is not the coherence of a specific fixed point of this linear map, and the $\rho^2$ correction term is not confirmed numerically.

**Recommendation:** The theorem requires either (a) a nonlinear coupling map with well-defined non-trivial fixed points, (b) clarification that the formula is an expectation over random initializations, or (c) a different definition of "coherence" tied to spectral structure rather than fixed-point iteration.

---

## TASK 3 — Conjecture 9.3: Severance Threshold

**Claim:** Bifurcation at $\rho_c = 1/\sqrt{6} \approx 0.40825$. Below $\rho_c$: two basins. Above: one basin.

**Configuration:** $r_A = r_B = 0.857$, sweep $\rho \in [0, 0.8]$ at 200 points.

### Contractivity window for r_A = r_B = 0.857

For the symmetric case, $r_{AB} = 0.857 \cdot (\alpha + \rho)$. Setting $r_{AB} = 1$:

$$0.857 \cdot (\sqrt{1-\rho^2} + \rho) = 1$$

Solving the resulting quadratic yields:

- $\rho_{\text{contract,lower}} = 0.18392$ (map becomes non-contractive above this)
- $\rho_{\text{contract,upper}} = 0.98294$ (map recovers contractivity above this)

Therefore the map is **non-contractive for $\rho \in [0.184, 0.983]$**. The predicted bifurcation $\rho_c = 1/\sqrt{6} \approx 0.408$ lies squarely inside this non-contractive window.

### Basin count sweep (contractive regime only)

| ρ range          | contractivity                  | n_basins |
|------------------|--------------------------------|----------|
| [0.000, 0.184)   | contractive                    | 1        |
| [0.184, 0.983]   | non-contractive — skip         | —        |
| (0.983, 0.800]   | (upper bound outside sweep range) | —     |

Only the first ~37 sweep points ($\rho < 0.184$) are contractive. All 30 random starts converge to the same unique fixed point (trivially 0 for a linear contraction) — **n_basins = 1 throughout the contractive regime**.

### Detected transition

- $\rho_c$ (predicted) = $1/\sqrt{6}$ = 0.408248
- $\rho_c$ (numerical) = NOT DETECTED in $[0, 0.8]$

No 2→1 basin transition is observed.

### Analytical diagnosis

Two independent issues prevent detection of the conjectured bifurcation:

**Issue 1 — Linear maps cannot have multiple basins.** By the Banach Fixed Point Theorem, a contractive linear map $T: \mathbb{R}^n \to \mathbb{R}^n$ with $\|T\| < 1$ has a unique fixed point (the origin). All initial conditions converge to the same point. A bifurcation between "one basin" and "two basins" requires a nonlinear map — the linear coupling map Ψ cannot produce this structure.

**Issue 2 — The bifurcation point $\rho_c$ falls in the non-contractive regime.** Even if multi-basin structure were possible, the regime where $\rho$ is near $1/\sqrt{6} \approx 0.408$ corresponds to $r_{AB} \approx 0.857 \cdot (0.913 + 0.408) \approx 1.132 \gg 1$. No fixed-point analysis applies there.

**Recommendation:** Conjecture 9.3 requires a nonlinear formulation (e.g., $T_{AB}$ as an affine map with fixed points away from 0, or a flow on a curved manifold). The linear spec does not support basin bifurcation.

---

## Summary of Findings

| Task | Claim | Result |
|------|-------|--------|
| Task 1 — Theorem 9.1 | $r_{AB} \leq \sqrt{\alpha^2 \max^2 + \rho^2 \min^2}$ | **0/24 PASS.** Bound provably false; $r_{AB} = r(\alpha+\rho) > r \cdot$ bound for all $\rho > 0$ in symmetric case. Root: Ψ amplifies by factor $(\alpha + \rho) > 1$. |
| Task 2 — Theorem 9.2 | $C_{AB}^{\max} = 6/7 + (1/7)\rho^2/(1+\rho^2)$ | **Not confirmed.** 15/20 contractive configs exceed 5% tolerance; up to 24% residual. Coherence is initialization-dependent in degenerate eigenspace. |
| Task 3 — Conjecture 9.3 | Bifurcation at $\rho_c = 1/\sqrt{6}$ | **Not detectable.** Linear maps have unique fixed point (Banach). Predicted $\rho_c$ lies inside non-contractive window $[0.184, 0.983]$ for this parameter regime. |

No failures were smoothed or suppressed. All computations are at float64 precision via exact SVD.

---

*Script: `paper9_verification.py` | Raw data: `paper9_results.json`*
