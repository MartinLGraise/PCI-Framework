# Paper 10 Task 3 — SIC Triple Products vs G₂ Associative 3-Form
## C-7RO Computation Report

**Date:** 2026-04-30  
**Framework:** PCI/PME  
**Precision:** 50 decimal places (mpmath)  
**Definition:** T_{ijk} = ⟨ψ_i|ψ_j⟩⟨ψ_j|ψ_k⟩⟨ψ_k|ψ_i⟩ where ψ_i = D(i,0)|Ψ_W⟩  
**Fiducial:** ABGHM 2022 exact d=7 SIC, Fano-compatible convention (W = diag(−1,1,1,1,1,1,1))

---

## Executive Summary

**Conjecture 3 as stated (T_{ijk} ∝ φ_{ijk}) FAILS** at all three tolerance levels, with residual ε ≈ 0.0259 >> 10⁻³.

**However, a stronger structural result holds exactly:** The SIC triple product decomposes as

> **T_{ijk} = a + ib·φ_{ijk}**

for all Fano-line triples, where a = (√2−1)/16 and b = (√2−1)√(2+4√2)/32 are exact algebraic constants. The imaginary part tracks the G₂ associative 3-form **exactly** (ε_Im = 0, verified to 50-digit precision), while the real part is a uniform symmetric background independent of orientation.

All four phases completed successfully. The WH covariance is exact (variance < 10⁻⁵²). An unexpected structural fact emerged from Phase 4: triples with all ordered differences in the quadratic-residue set {1,2,4} mod 7 give T = α³ regardless of Fano-line membership.

---

## Setup

### Fiducial vector
```
|Ψ_W⟩ = W|Ψ⟩,  W = diag(−1,1,1,1,1,1,1)
|Ψ⟩ = N⁻¹(−2−2√2, z₀, z₀, z₁, z₀, z₁, z₁)ᵀ
z₀ = −(2+√2)/2 + (i/2)√(2+4√2)
z₁ = −(2+√2)/2 − (i/2)√(2+4√2)
N = √(24+20√2)
```

Dominant component: |Ψ_W[0]| = 0.667759617... ≈ 0.668 ✓

### SIC states for Fano points
```
ψ_i = D(i,0)|Ψ_W⟩ = X^i|Ψ_W⟩,  i = 0,...,6
```

SIC property verified: |⟨ψ_i|ψ_j⟩|² = 1/8 for all i≠j ✓

### Fano lines (0-indexed, Baez 2002)
```
L1=(0,1,3), L2=(1,2,4), L3=(2,3,5), L4=(3,4,6),
L5=(4,5,0), L6=(5,6,1), L7=(6,0,2)
```

---

## Phase 1 — Fano Lines Through j=0 (L1, L5, L7)

**Status: PASS**

| Line | Triple (cyclic) | Re(T) | Im(T) | φ |
|------|-----------------|-------|-------|---|
| L1 | (0,1,3) | 0.025888347648318 | +0.035817851080708 | +1 |
| L1 | (0,3,1) anti | 0.025888347648318 | −0.035817851080708 | −1 |
| L5 | (4,5,0) | 0.025888347648318 | +0.035817851080708 | +1 |
| L5 | (4,0,5) anti | 0.025888347648318 | −0.035817851080708 | −1 |
| L7 | (6,0,2) | 0.025888347648318 | +0.035817851080708 | +1 |
| L7 | (6,2,0) anti | 0.025888347648318 | −0.035817851080708 | −1 |

**Pass criteria satisfied:**
- Im(T) has opposite signs for cyclic vs anti-cyclic: ✓
- Im(T) magnitude equal across all 3 lines: max deviation = 0 exactly
- Re(T) equal across all 3 lines: max deviation = 4.18 × 10⁻⁵³

**Note:** All three lines through j=0 give **identical** T values to 50-digit precision, confirming WH covariance. No j=0 preference signal.

---

## Phase 2 — All 7 Fano Lines

**Status: PASS**

| Line | Triple | Re(T) | Im(T) | |T| |
|------|--------|-------|-------|-----|
| L1 | (0,1,3) cyc | 0.02588834764832 | +0.03581785108071 | 0.04419417382 |
| L2 | (1,2,4) cyc | 0.02588834764832 | +0.03581785108071 | 0.04419417382 |
| L3 | (2,3,5) cyc | 0.02588834764832 | +0.03581785108071 | 0.04419417382 |
| L4 | (3,4,6) cyc | 0.02588834764832 | +0.03581785108071 | 0.04419417382 |
| L5 | (4,5,0) cyc | 0.02588834764832 | +0.03581785108071 | 0.04419417382 |
| L6 | (5,6,1) cyc | 0.02588834764832 | +0.03581785108071 | 0.04419417382 |
| L7 | (6,0,2) cyc | 0.02588834764832 | +0.03581785108071 | 0.04419417382 |

(Anti-cyclic entries: same Re, opposite Im sign)

**Pass criteria satisfied:**
- All 14 triples confirm Phase 1 pattern: ✓
- WH covariance: lines through j=0 and lines NOT through j=0 give **identical** signal: ✓
- Max Re deviation across all 7 lines: 1.25 × 10⁻⁵²
- Max |Im| deviation across all 7 lines: 0 (exactly)

**j=0 axis preference: NONE.** All 7 Fano lines give the same T value, as expected from WH covariance. The Fano-line differences {1,2,4} are all quadratic residues mod 7, and the ABGHM autocorrelation satisfies f(QR) = constant for all QR shifts.

---

## Phase 3 — Conjecture 3 Residual Test

**Status: STRUCTURAL FAILURE with STRONGER PARTIAL RESULT**

### Conjecture as stated: T_{ijk} = C·φ_{ijk}

Best-fit C (least squares over 42 Fano-line entries):

> **C_best = 0 + 0.035817851080708...i** (purely imaginary)

Residual:

> **ε = ‖π_Fano[T] − C·φ‖_F / ‖φ‖_F = 0.02588834765**

| Tolerance | Result |
|-----------|--------|
| ε < 10⁻¹⁰ | ✗ FAIL |
| ε < 10⁻⁶ | ✗ FAIL |
| ε < 10⁻³ | ✗ FAIL |

**Conjecture 3 as stated is cleanly falsified.**

### Why it fails — structural decomposition

The computation reveals:

$$\boxed{T_{ijk} = a + ib\cdot\varphi_{ijk}}$$

for **all** Fano-line triples, where:

| Quantity | Exact formula | Numerical value |
|----------|---------------|-----------------|
| a = Re(T) | **(√2−1)/16** | 0.025888347648318... |
| b = Im(T) | **(√2−1)√(2+4√2)/32** | 0.035817851080708... |
| \|T\| | **√2/32 = 1/(16√2)** | 0.044194173824159... |

Verification: (√2−1)²·(6+4√2) = 2 → a²+b² = 1/512 = |T|² ✓

### Modified Conjecture 3': Im(T_{ijk}) = b·φ_{ijk}

> **ε_Im = 0 exactly** (verified to 50-digit precision)

The imaginary part of the SIC triple overlap tracks the G₂ associative 3-form **perfectly**:

$$\mathrm{Im}(T_{ijk}) = \frac{(\sqrt{2}-1)\sqrt{2+4\sqrt{2}}}{32} \cdot \varphi_{ijk}$$

The real part a = (√2−1)/16 is a symmetric background: it is identical for both cyclic (φ=+1) and anti-cyclic (φ=−1) Fano triples, so it carries no orientation information.

### Why Conjecture 3 fails

The cyclic autocorrelation function satisfies:

$$f(k) = \langle\Psi_W|X^k|\Psi_W\rangle = \begin{cases} \alpha = -\frac{(2-\sqrt{2}) + i\sqrt{2+4\sqrt{2}}}{8} & k \in \{1,2,4\} \text{ (QR mod 7)} \\ \bar{\alpha} & k \in \{3,5,6\} \text{ (NQR mod 7)} \end{cases}$$

For a Fano-line cyclic triple (ordered differences all in {1,2,4}):

$$T_\text{cyc} = f(r_1)f(r_2)f(r_3) = \alpha^3 = \frac{(\sqrt{2}-1)}{16} + i\frac{(\sqrt{2}-1)\sqrt{2+4\sqrt{2}}}{32}$$

For anti-cyclic (ordered differences all in {3,5,6}):

$$T_\text{anti} = \bar{\alpha}^3 = \frac{(\sqrt{2}-1)}{16} - i\frac{(\sqrt{2}-1)\sqrt{2+4\sqrt{2}}}{32} = T_\text{cyc}^*$$

For T ∝ φ we would need T_anti = −T_cyc (i.e., α³ purely imaginary), which requires Re(α³) = 0. But Re(α³) = (√2−1)/16 ≠ 0. The Conjecture fails by exactly this symmetric term.

---

## Phase 4 — Non-Fano Negative Controls

**Status: COMPLETE — Unexpected structural finding**

| Triple | Re(T) | Im(T) | φ | Notes |
|--------|-------|-------|---|-------|
| (0,1,2) | −0.00915291 | −0.04323597 | 0 | diffs {1,1,5}: mixed QR/NQR |
| (0,2,4) | −0.00915291 | −0.04323597 | 0 | same diff pattern |
| (1,3,5) | −0.00915291 | −0.04323597 | 0 | same diff pattern |
| (0,3,5) | −0.00915291 | −0.04323597 | 0 | diffs {3,2,2}: mixed |
| **(0,4,6)** | **+0.02588835** | **+0.03581785** | 0 | **SAME AS FANO-CYCLIC** |
| (2,4,6) | −0.00915291 | −0.04323597 | 0 | diffs {2,2,3}: mixed |

**Notable finding:** Triple (0,4,6) gives T = T_Fano-cyclic exactly. The set {0,4,6} is NOT a Fano line, yet:

- Ordered differences (0→4→6→0): 4, 2, 1 — all in {1,2,4} (QR mod 7)
- Therefore T_{046} = f(4)·f(2)·f(1) = α·α·α = α³ = T_Fano-cyc

**Structural interpretation:** T_{ijk} depends only on the QR-classification of the ordered differences (j−i, k−j, i−k) mod 7, not on Fano-line membership per se. The Fano lines are the canonical representatives of the all-QR difference pattern, but non-Fano triples with all-QR differences (like {0,4,6}) also give T = α³.

The 42 all-QR ordered triples (7 starting points × 6 permutations of {1,2,4}) split as:
- 21 Fano-line cyclic triples (differences = cyclic permutations of (1,2,4))
- 21 non-Fano triples (differences = anti-cyclic permutations like (1,4,2),(4,2,1),(2,1,4))

Both subsets give T = α³ by commutativity of multiplication.

---

## Summary of Exact Results

### The autocorrelation function of the ABGHM d=7 fiducial

$$f(k) \equiv \langle\Psi_W|X^k|\Psi_W\rangle = \begin{cases} \alpha & k \bmod 7 \in \{1,2,4\} \\ \bar{\alpha} & k \bmod 7 \in \{3,5,6\} \\ 1 & k = 0 \end{cases}$$

**Exact value:** α = −[(2−√2) + i√(2+4√2)]/8

The fact that f is constant on QR and NQR classes is a consequence of the F₂₁ symmetry of the ABGHM fiducial under the Galois automorphism σ: √2 ↦ −√2 and the C₃ symmetry that cyclically permutes the QRs {1,2,4} among themselves.

### The triple overlap on Fano-line triples

$$T_{ijk} = \alpha^3 \quad \text{(cyclic Fano)}, \qquad T_{ijk} = \bar{\alpha}^3 \quad \text{(anti-cyclic Fano)}$$

$$T_{ijk} = \frac{\sqrt{2}-1}{16} + i\cdot\frac{(\sqrt{2}-1)\sqrt{2+4\sqrt{2}}}{32}\cdot\varphi_{ijk}$$

$$= a + ib\cdot\varphi_{ijk}$$

### For Paper 10 §7

**Conjecture 3 as stated (T ∝ φ) is FALSE.** The correct statement is:

> **Modified Theorem 3 (to be confirmed):** For the ABGHM d=7 SIC with Fano-compatible fiducial |Ψ_W⟩, the imaginary part of the Gram triple product
> $$\mathrm{Im}\bigl(\langle\psi_i|\psi_j\rangle\langle\psi_j|\psi_k\rangle\langle\psi_k|\psi_i\rangle\bigr) = \frac{(\sqrt{2}-1)\sqrt{2+4\sqrt{2}}}{32}\cdot\varphi_{ijk}$$
> for all ordered Fano-line triples (i,j,k), where φ is the G₂ associative 3-form.

This holds exactly (ε_Im = 0 to 50-digit precision, verified over all 42 Fano-line triples).

The real part a = (√2−1)/16 is the orientation-independent SIC overlap background: it is a structural constant of the SIC frame, not carrying G₂ information.

---

## Verification of Prior Tasks

- Task 1 (G₂ embedding): f(QR) = constant confirms the WH covariance structure and the rank-14 embedding
- Task 2 (Fano axis): No j=0 preference found — WH covariance is exact across all 7 Fano lines. The Fano axis at j=0 remains unique by Task 2 arguments (W uniqueness), but the triple products are democratic.

---

*Computation by Φ (Claude Sonnet 4.6) for C-7RO, 2026-04-30. All results at 50-digit mpmath precision.*
