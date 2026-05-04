# Paper 9 — Task 5 Verification Report (v3)

## Affine Channel Fixed-Point Analysis

**PCI/PME Framework · MartinLGraise/PCI-Framework · paper7-foundation**
**Date:** 2026-05-04 · **Seed:** 20260504 · **n = 14 (G₂ adjoint)**

---

## Executive Summary

| Sub-task | Status | Core result |
|---|---|---|
| 5.1 Fixed-point existence & θ-variation | PASS | All 50 fixed points exist; Δ\|x̂−ŷ\| = 0.406 (nontrivial) |
| 5.2 Closed-form verification | PASS | Three analytic predictions match to <1e-15 |
| 5.3 Coherence tables (28 rows) | PASS | C3 (cross-alignment) most θ-sensitive; Config C shows Δ=0.52 |
| 5.4 Conditional-improvement heatmap | PASS | 25.1% of cells have ΔC > 0; improvement region spans φ ∈ [0°, 180°] |
| 5.5 Asymmetric-rate robustness | PASS | θ-variation persists for all three rate pairs; max var = 0.113 |
| 5.6 Destructive geometry null check | FINDING | ΔC > 0 at θ ∈ [0°, ~14.7°] even with b_A = −b_B |

The pivot to affine channels is vindicated: the coupling angle θ acts nontrivially on the joint fixed point in all configurations tested. The one honesty result (5.6) is a genuine structural finding that sharpens rather than defeats Proposition 9.5.

---

## Comparison with the Linear Case (Tasks 1–4)

In the linear case T_A = r_A·U (U orthogonal), the fixed point of the coupled system is always **zero**, and the coupling angle θ is entirely inert. Theorem 9.2 (rate lock) and Corollary 9.3 (Schur's lemma) established this cleanly.

In the affine case T_A(x) = r_A·R_A·x + b_A, the bias b_A breaks G₂-equivariance. The fixed point is now a non-zero vector that depends on both bias vectors and the full coupling geometry (θ, R_A, R_B). Every task in this report confirms that the coupling angle is no longer inert — the affine formulation is where the paper's positive content lives.

---

## Task 5.1 — Fixed-Point Existence and θ-Dependence

**Setup:** r_A = r_B = 0.7, b_A = make_bias(14, 20260504), b_B = make_bias(14, 20260504+50), θ ∈ [0, π/2] at 50 evenly spaced points.

**Results:**

| Quantity | Min | Max | Variation |
|---|---|---|---|
| \|x̂(θ)\| | 0.9634 | 2.0414 | **1.0780** |
| \|ŷ(θ)\| | 0.8727 | 1.3032 | **0.4305** |
| \|x̂(θ)−ŷ(θ)\| | 1.6064 | 2.0119 | **0.4056** |

All 50 fixed points were computed successfully (solve() returned a unique solution for every θ). The variations are far above the 1e-6 nontriviality threshold.

The maximum of \|x̂−ŷ\| occurs at θ = 0° (fully decoupled — the two agents' fixed points are maximally separated). The minimum occurs at θ = 51.4°, not at θ = 45° or θ = 90°, indicating that the optimal coupling angle for coherence depends on the specific rotation geometry (R_A, R_B) rather than any universal value.

**Conclusion:** Fixed points exist for all θ in [0, π/2]; coupling IS doing something nontrivial in the affine case, unlike the linear case.

---

## Task 5.2 — Closed-Form Verification

**Setup:** Three analytic predictions are verified against the numerical solver. The original expectation x̂(π/4) = ŷ(π/4) when b_A=b_B was incorrect — this equality does NOT hold at θ=π/4 because the coupling rotation Ψ_{π/4}: (x,y) → ((x−y)/√2, (x+y)/√2) is not symmetric under x↔y. The correct analytic predictions are as follows.

**Check A — θ=0 (decoupled), independent biases:** At θ=0, cos θ=1, sin θ=0, so the block system decouples exactly: x̂ = (I − r·R_A)⁻¹ b_A, ŷ = (I − r·R_B)⁻¹ b_B (b_B has no influence on x̂).

| Error | Value |
|---|---|
| \|x̂_numerical − (I−r·R_A)⁻¹ b_A\| | 0.00e+00 |
| \|ŷ_numerical − (I−r·R_B)⁻¹ b_B\| | 1.11e-16 |

**Check B — θ=0, R_A=R_B=R, b_A=b_B=b:** When the system is symmetric at θ=0, x̂=ŷ.

| Error | Value |
|---|---|
| \|x̂ − ŷ\| | 3.18e-16 |

**Check C — θ=π/2, R_A=R_B=R, b_A=b_B=b:** Via the s=x+y, d=x−y reduction: d = −r·R·s, s = 2(I+r²R²)⁻¹ b, giving: x̂ = (I−rR)(I+r²R²)⁻¹ b, ŷ = (I+rR)(I+r²R²)⁻¹ b. Note: x̂ ≠ ŷ at θ=π/2 even with b_A=b_B; their difference is −2r·R·(I+r²R²)⁻¹ b, with magnitude 1.4616.

| Error | Value |
|---|---|
| \|x̂ − (I−rR)(I+r²R²)⁻¹ b\| | 4.65e-16 |
| \|ŷ − (I+rR)(I+r²R²)⁻¹ b\| | 4.32e-16 |
| \|x̂+ŷ − 2(I+r²R²)⁻¹ b\| | 6.72e-16 |

**Conclusion:** All three checks match analytic predictions to numerical precision (<1e-15). Task 5.2 PASSES.

**Correction noted for §5 proof body:** The closed form in the v1.1 §5 skeleton assumed scalar R_A = R_B = I, giving a rational expression in sin θ, cos θ. The general case (R_A, R_B arbitrary 14-dim orthogonal) requires matrix-valued expressions. The θ=π/2 symmetric-case closed form x̂ = (I−rR)(I+r²R²)⁻¹ b is the correct generalization.

---

## Task 5.3 — Coherence Functionals × Four Bias Configurations

**Setup:** r_A = r_B = 0.7, R_A and R_B (seed 20260504, 20260505), θ ∈ {0, π/12, π/6, π/4, π/3, 5π/12, π/2}, four bias configurations.

**Full table (28 rows):**

| Config | θ | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|
| A (identical) | 0 | 0.7655 | 0.8309 | 0.7655 | 0.5745 |
| A (identical) | π/12 | 0.8062 | 0.6560 | 0.8062 | 0.5498 |
| A (identical) | π/6 | 0.8686 | 0.5771 | 0.8686 | 0.4806 |
| A (identical) | π/4 | 0.9334 | 0.6159 | 0.9334 | 0.3967 |
| A (identical) | π/3 | 0.9242 | 0.6875 | 0.9242 | 0.3617 |
| A (identical) | 5π/12 | 0.8262 | 0.7294 | 0.8262 | 0.3732 |
| A (identical) | π/2 | 0.7574 | 0.7507 | 0.7574 | 0.3691 |
| B (orthogonal) | 0 | 0.7655 | 0.7236 | −0.0637 | 0.7277 |
| B (orthogonal) | π/12 | 0.7658 | 0.6964 | −0.0063 | 0.7165 |
| B (orthogonal) | π/6 | 0.7568 | 0.6894 | 0.0723 | 0.7068 |
| B (orthogonal) | π/4 | 0.7299 | 0.7043 | 0.1505 | 0.7132 |
| B (orthogonal) | π/3 | 0.6979 | 0.7311 | 0.2056 | 0.7435 |
| B (orthogonal) | 5π/12 | 0.6823 | 0.7496 | 0.2361 | 0.7813 |
| B (orthogonal) | π/2 | 0.6880 | 0.7507 | 0.2757 | 0.7905 |
| C (parallel 2x) | 0 | 0.7655 | 0.8309 | 0.7655 | 0.4279 |
| C (parallel 2x) | π/12 | 0.8479 | 0.7724 | 0.8479 | 0.3814 |
| C (parallel 2x) | π/6 | 0.9470 | 0.7742 | 0.9470 | 0.3876 |
| C (parallel 2x) | π/4 | 0.7929 | 0.8090 | 0.7929 | 0.4893 |
| C (parallel 2x) | π/3 | 0.5039 | 0.8335 | 0.5039 | 0.5524 |
| C (parallel 2x) | 5π/12 | 0.4283 | 0.8419 | 0.4283 | 0.5520 |
| C (parallel 2x) | π/2 | 0.4606 | 0.8466 | 0.4606 | 0.5208 |
| D (opposed) | 0 | 0.7655 | 0.8309 | −0.7655 | 0.9286 |
| D (opposed) | π/12 | 0.7420 | 0.8664 | −0.7420 | 0.9181 |
| D (opposed) | π/6 | 0.7245 | 0.8152 | −0.7245 | 0.8865 |
| D (opposed) | π/4 | 0.7004 | 0.7948 | −0.7004 | 0.8640 |
| D (opposed) | π/3 | 0.6635 | 0.8050 | −0.6635 | 0.8593 |
| D (opposed) | 5π/12 | 0.6200 | 0.8211 | −0.6200 | 0.8694 |
| D (opposed) | π/2 | 0.5955 | 0.8208 | −0.5955 | 0.8847 |

**Sensitivity (max−min across θ):**

| Config | ΔC1 | ΔC2 | ΔC3 | ΔC4 |
|---|---|---|---|---|
| A (identical) | 0.176 | 0.254 | 0.176 | 0.213 |
| B (orthogonal) | 0.084 | 0.061 | **0.339** | 0.084 |
| C (parallel 2x) | **0.519** | 0.074 | **0.519** | 0.171 |
| D (opposed) | 0.170 | 0.072 | 0.170 | 0.069 |

**Observations:** C3 (cross-alignment: cosine similarity of x̂ to b_B) is the most θ-sensitive measure in configs B and C, with variation up to 0.519. This makes structural sense: C3 measures how much coupling "bleeds" agent A's state toward agent B's target, which is directly driven by θ.

Config C (parallel, 2x scale) shows the strongest C1 variation (0.519), peaking at θ=π/6 where C1=0.9470 — an extraordinary self-alignment. This is the regime where Proposition 9.5's conditional gain is most pronounced.

---

## Task 5.4 — Conditional-Improvement Heatmap

**Setup:** b_A = e₁ (unit basis vector), b_B = cos(φ)·e₁ + sin(φ)·e₂ (normalised), φ ∈ [0°, 180°] at 100 points, θ ∈ [0°, 90°] at 20 points. ΔC = C_joint(θ, φ) − C_decoupled(φ).

**Key results:**

- Total grid cells: 2000
- Cells with ΔC > 0 (coupling improves over decoupled baseline): **502 (25.1%)**
- ΔC range: [−0.0710, +0.0186]
- Improvement region spans φ ∈ [1.8°, 180°]

**Pattern:** The improvement region (ΔC > 0) is not confined to small φ (aligned biases). The conditional gain spans a wide range of bias angles, indicating that the interaction between θ and the rotation geometry (R_A, R_B) allows coupling to improve coherence even when biases are not closely aligned. The maximum gain ΔC_max = 0.0186 is modest but reproducible.

The degradation region (ΔC < 0) is larger by cell count (74.9%), concentrated at large φ (near 180°) and large θ. This is the expected regime: coupling two agents whose targets are nearly opposed, at large coupling angles, disrupts both.

**Implication for Proposition 9.5:** The conditional-gain framing is structurally correct — improvement exists and is geometry-dependent — but the condition "aligned biases → improvement" is insufficient as stated. The heatmap suggests the true condition involves an interaction between φ, θ, and the rotation geometry. A stronger statement might be: for given (R_A, R_B), there exists an optimal coupling angle θ*(φ, R) that produces positive conditional gain for a range of φ wider than the naive alignment condition predicts.

---

## Task 5.5 — Asymmetric-Rate Robustness

**Setup:** Config B biases (b_A ⊥ b_B), θ ∈ [0°, 90°] at 20 points, three rate pairs.

| Rate pair | C_min | C_max | Max variation | θ at min | θ at max |
|---|---|---|---|---|---|
| (r_A=0.3, r_B=0.7) | 0.8385 | 0.8795 | 0.0411 | 4.7° | 75.8° |
| (r_A=0.5, r_B=0.857) | 0.6929 | 0.7650 | 0.0721 | 9.5° | 80.5° |
| (r_A=0.3, r_B=0.857) | 0.7352 | 0.8481 | **0.1128** | 4.7° | 75.8° |

**Observations:** θ-dependence of the joint fixed point survives asymmetric rates in all three cases. The maximum variation is largest for the most asymmetric rate pair (0.3, 0.857), reaching 0.113 — a substantial effect. The optimal coupling angle (θ at C_max) clusters near 75–80°, close to but not at 90°, again indicating geometry-dependent optima rather than a universal value.

The structure θ_min ≈ 5° and θ_max ≈ 75–80° is consistent across rate pairs with the slower agent (r=0.3) paired with the faster one: the slow agent's fixed point has a large "self-projection" under small coupling that degrades with strong rotation.

**Conclusion:** The affine channel θ-dependence is robust to rate asymmetry. Proposition 9.5's conditional gain claim does not require rate symmetry.

---

## Task 5.6 — Destructive Geometry Null Check (b_A = −b_B)

**This is the honesty test.** Proposition 9.5 predicts that coupling should degrade coherence when biases are opposed.

**Setup:** r_A = r_B = 0.7, b_A = make_bias(14, 20260504), b_B = −b_A, θ ∈ [0°, 90°] at 50 points.

**Decoupled baseline:** C_joint_dec = 0.7982

| θ range | ΔC sign | ΔC magnitude |
|---|---|---|
| 0° | 0.0000 | (boundary) |
| ~1.8° to ~14.7° | **ΔC > 0** | Peak +0.0144 at θ ≈ 7° |
| ~18° to 90° | ΔC < 0 | Trough −0.0901 at θ = 90° |

**Points with ΔC > 0: 9 out of 50.**

### Mechanism (diagnosed)

The improvement at small θ is driven by an asymmetry between C1 and C2 under small coupling. Tracing C1 and C2 separately:

- C1 (alignment of x̂ to b_A): decreases monotonically from 0.7655 to 0.5955 as θ increases. Coupling "pulls" A's state away from its own target.
- C2 (alignment of ŷ to b_B = −b_A): INCREASES from 0.8309 to a peak of 0.8749 at θ ≈ 7°, then gradually decreases.

The initial rise of C2 occurs because agent B's rotation R_B, when given a small coupling push from agent A's state, accidentally improves ŷ's alignment with b_B = −b_A. This is a fortuitous geometry: R_B's action on the coupled input (s·x̂_dec) has a component that projects onto b_B. The C2 gain (+0.044) outpaces the C1 loss (−0.005) at small θ, producing a net positive ΔC.

This is NOT a measurement artifact or code error. It is a structural property of the specific rotation geometry (R_A seed=20260504, R_B seed=20260505) combined with the bias choice.

### Implication for Proposition 9.5

The original prediction "opposed biases → no improvement" is falsified in the small-coupling regime. The null prediction holds for large θ (coupling is always destructive at θ > 20°), but fails at small θ where the random geometry of R_B can produce incidental alignment improvement.

**This is the third reformulation signal.** The proposition needs to either:

1. **Restrict to θ above a geometry-dependent threshold:** "For θ > θ*(R_A, R_B, b_A, b_B), coupling under opposed biases degrades coherence." The threshold here is ≈ 18°.
2. **Replace average coherence with a different functional:** A C_joint defined as the minimum of C1, C2 (rather than average) would be monotonically degraded by coupling in the opposed-bias case, since C1 always falls.
3. **Restrict the proposition to the aligned-bias regime entirely:** The claim of conditional gain can be made cleanly for φ ∈ [0°, ~170°) (see Task 5.4). The opposed-bias regime (φ = 180°) can be moved to a remark noting the small-θ exception.

Option 2 (min-coherence functional) is most conservative and would rescue the proposition without qualification. Option 3 preserves the averaging functional but narrows the domain. Option 1 is mathematically precise but requires computing θ* for each geometry.

---

## Diagnostic Cross-Check

All six tasks used the same base rotations (seed 20260504, 20260504+1) and biases (seed 20260504, 20260504+50). The Task 5.6 finding is specific to the opposed-bias configuration and does not affect any other sub-task. Tasks 5.1–5.5 are independent of the 5.6 finding.

The CSVs `paper9_task5_coherence_tables.csv` (28 rows) and `paper9_task5_heatmap.csv` (2000 rows) are saved and ready for plotting.

---

## Appendix: Environment

- numpy float64 throughout; no mpmath
- seed = 20260504 for all random constructions
- n = 14 (G₂ adjoint representation dimension)
- Rotations: QR decomposition of a standard-normal matrix
- solve() from numpy.linalg; no singular matrices encountered in any task

*Φ (Anthropic Claude Dispatch), 2026-05-04. Reported to C-7RO.*
