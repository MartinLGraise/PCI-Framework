# G₂ Daemon Hamiltonian — Computation Results
## Computed March 20, 2026 (Claude Chat)

---

## 1. Construction Verification

**14 G₂ generators confirmed.** Extracted as the null space of the octonion structure constant (ψ) preservation constraint on so(7). The constraint matrix C has shape (35 × 21); null_space(C) = 14-dimensional. ✓

**Normalization**: tr(TₐTᵦ) = −2δₐᵦ. Off-diagonal maximum < 10⁻¹⁵ (machine epsilon).

---

## 2. Quadratic Casimir

**C₂(G₂) = −4 × I₇** (scalar multiple of identity)

This was expected and is a structural fact: the 7-dim rep is irreducible, so Schur's lemma forces the Casimir to be scalar. 

**Consequence**: The pure G₂ Casimir (α·C₂(G₂) alone) produces **zero spectral splitting**. It shifts all 7 modes uniformly. The interesting structure comes from the SU(3) subalgebra and Cartan terms.

---

## 3. SU(3) Decomposition: 7 → 1 ⊕ 3 ⊕ 3̄

| Mode | Rep | SU(3) Casimir C₂(SU3) | Degeneracy | Interpretation |
|---|---|---|---|---|
| e₀ (Ω_void) | **1** (singlet) | 0 | 1-fold | The blind-spot mode; fixed by all SU(3) generators |
| v₁, v₂, v₃ | **3** (triplet) | −8/3 | 3-fold | Active daemons |
| v̄₁, v̄₂, v̄₃ | **3̄** (anti-triplet) | −8/3 | 3-fold | Conjugate daemons |

**Key structural fact**: In the real representation, the triplet and anti-triplet have **equal** Casimir values (−8/3). They cannot be separated by the Casimir alone — only by the Cartan generators.

**Stabilizer verification**: The null space of {Tₐ · e₀} is exactly 8-dimensional ✓, confirming the SU(3) subalgebra.

**Coset G₂/SU(3)**: 6 generators, uniform SVD singular values (0.8165 each), consistent with G₂/SU(3) ≅ S⁶ (the 6-sphere).

---

## 4. Complex Structure & Cartan Generators

The complex structure J_{ij} = ψ₀ᵢⱼ satisfies J² = −I on ℝ⁶ ✓.

Its real Schur form reveals **3 invariant 2-planes**. Rotating each plane independently gives Cartan generators H₁, H₂, H₃ (all mutually commuting).

SU(3) Cartan basis (rank 2):
- H_c1 = H₁ − H₂  (simple root α₁)
- H_c2 = H₂ − H₃  (simple root α₂)

**Weight structure under a₁·H_c1 + a₂·H_c2**:

| Weight (w₁, w₂) | Triplet shift | Anti-triplet shift |
|---|---|---|
| (+1, 0) / (−1, 0) | +a₁ | −a₁ |
| (−1, +1) / (+1, −1) | −a₁ + a₂ | +a₁ − a₂ |
| (0, −1) / (0, +1) | −a₂ | +a₂ |

---

## 5. Full Hamiltonian Spectrum

**H_daemon = α·C₂(G₂) + β·C₂(SU3) + γ·P_void + a₁·H_c1 + a₂·H_c2**

### Spectral Regimes

| Parameters | # Distinct Levels | Structure |
|---|---|---|
| β = γ = a₁ = a₂ = 0 | 1 | 7-fold degenerate |
| β ≠ 0, rest = 0 | 2 | singlet ⊕ [6-fold] |
| β ≠ 0, γ ≠ 0 | 2 | shifted singlet ⊕ [6-fold] |
| β ≠ 0, a₁ = a₂ ≠ 0 | **4** | singlet ⊕ 3×[2-fold] — **triplet-of-triplet** |
| β ≠ 0, a₁ ≠ a₂ ≠ 0 | **7** | fully resolved (all 7 distinct) |

### Canonical Example: α = 1, β = 1, γ = 0.5, a₁ = a₂ = 1

| Level | Eigenvalue | Degeneracy | Gap from Ω_void |
|---|---|---|---|
| Ω_void (singlet) | −3.500 | ×1 | — |
| Doublet 3 | −5.667 | ×2 | 2.167 |
| Doublet 2 | −6.667 | ×2 | 3.167 |
| Doublet 1 | −7.667 | ×2 | 4.167 |

**Gaps are uniformly spaced** at Δ = 1.000 (exactly equal to a₁ = a₂ = 1).

**Ratios**: 1.000 : 1.462 : 1.923 (gap₁ : gap₂ : gap₃, normalized to gap₁)

---

## 6. Interpretation for the Paper

### What the computation confirms:

1. **G₂ structure is real.** The 14 generators, the SU(3) decomposition 7 → 1 ⊕ 3 ⊕ 3̄, the S⁶ coset — all check out numerically to machine precision. This is not hand-waving.

2. **The singlet (Ω_void) is structurally distinct.** It has zero SU(3) Casimir eigenvalue while the daemons have −8/3. The void mode is mathematically singled out by the algebra itself.

3. **The triplet-of-triplet pattern is natural.** With Cartan terms switched on, you get exactly 3 pairs of degenerate levels (triplet + anti-triplet paired) plus the singlet. This is the "3+3̄+1" pattern — 3 doubly-degenerate daemon pairs plus the void.

4. **The eigenvalue ratios are tunable, not fixed.** The ratios depend on the Cartan parameters (a₁, a₂). This means the G₂ structure does not predict a single set of frequency ratios — it predicts a *family* of possible ratios parameterized by the coupling strengths. The experimental comparison to Bandyopadhyay becomes: "Is there a point in the (a₁, a₂) parameter space that matches the observed triplet-of-triplet frequencies?"

### What this means for the Bandyopadhyay comparison (FP-1):

*Corrected after adversarial review by ChatGPT and Claude (March 20, 2026). Original C-7RO framing overclaimed "4 levels or G₂ is ruled out" — the computation itself shows 7 distinct levels are perfectly allowed when a₁ ≠ a₂.*

**What G₂ fixes (topology — cannot be tuned)**:
1. The spectrum decomposes into a **singlet sector** and a **3⊕3̄ sector** — never 2⊕5, never 4⊕3, never any other split. The singlet void mode is structurally forced by the null-space construction, not hand-labeled.
2. The singlet has SU(3) Casimir eigenvalue **0** while all other modes have **−8/3**. This is algebraic, not parametric.
3. The non-singlet modes come in **conjugate pairs** (3 and 3̄ related by complex conjugation). This is structural.
4. The gap ratios are determined by **at most two independent Cartan parameters** (a₁, a₂) — not three, not seven — because SU(3) has rank 2.

**What G₂ does NOT fix (metric — parameter-dependent)**:
- The raw level count: allowed patterns are 1, 2, 4, or 7 depending on (β, γ, a₁, a₂).
- The specific eigenvalue ratios: these are continuous functions of a₁/a₂.

**The corrected falsifiable prediction (FP-1)**:
Does the resonance data fit a two-parameter family with a structurally forced singlet and a conjugate-paired 3⊕3̄ sector?

G₂ is ruled out if:
- The data requires more than two independent splitting parameters
- The conjugate pairing (3 ↔ 3̄) is absent
- The singlet/non-singlet Casimir ratio deviates from 0 vs −8/3
- The branching topology doesn't match 1⊕3⊕3̄ (e.g., a 1⊕6 or 2⊕5 pattern)

**The line to protect**: G₂ does not fix the metric uniquely, but it does fix the topology of the spectral family.

### What to write in Section 3:

The section should present:
1. The construction (generators, Casimir, decomposition)
2. The spectrum table across all regimes (1, 2, 4, and 7 levels)
3. The structural prediction: 1⊕3⊕3̄ branching topology and conjugate pairing
4. The rank-2 Cartan constraint (only two free parameters for all gap ratios)
5. The revised FP-1: resonance data must fit the constrained spectral family
6. What is explicitly ruled out (1⊕6, 2⊕5, unconstrained 7-mode fits)

---

## 7. Raw Numerical Data

### β scan (γ = 0, no Cartan): singlet vs 3⊕3̄ splitting

| β/α | Singlet | 3⊕3̄ | Gap |
|---|---|---|---|
| 0.0 | −4.000 | −4.000 | 0.000 |
| 0.5 | −4.000 | −5.333 | 1.333 |
| 1.0 | −4.000 | −6.667 | 2.667 |
| 1.5 | −4.000 | −8.000 | 4.000 |
| 2.0 | −4.000 | −9.333 | 5.333 |

### a₁ = a₂ = a sweep (β = 1, γ = 0.5)

| a | # Levels | Eigenvalues |
|---|---|---|
| 0.0 | 2 | {−6.667 ×6, −3.500 ×1} |
| 0.5 | 4 | {−7.167 ×2, −6.667 ×2, −6.167 ×2, −3.500 ×1} |
| 1.0 | 4 | {−7.667 ×2, −6.667 ×2, −5.667 ×2, −3.500 ×1} |
| 1.5 | 4 | {−8.167 ×2, −6.667 ×2, −5.167 ×2, −3.500 ×1} |
| 2.0 | 4 | {−8.667 ×2, −6.667 ×2, −4.667 ×2, −3.500 ×1} |

---

*Results documented by C-7RO — March 20, 2026*
*Source computation: Claude Chat (regular), interactive React visualization artifact*
