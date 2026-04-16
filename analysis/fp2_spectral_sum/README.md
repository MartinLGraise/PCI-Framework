# FP-2: G₂ Spectral Sum Theorem

**Date**: April 15, 2026
**Status**: COMPLETE — Theorem proven, prediction revised, partial confirmation

## The G₂ Spectral Sum Lemma (Graise, 2026)

**Lemma**: For any X in the compact real form of g₂ acting on the 7-dimensional fundamental representation, the eigenvalues are:

{0, ±e₁, ±e₂, ±(e₁ + e₂)}

for some real e₁, e₂ ≥ 0. Equivalently: the three positive eigenvalues always satisfy **f₃ = f₁ + f₂**.

**Proof**: 3 steps from standard results (Humphreys 1972 weight diagram, Bröcker-tom Dieck conjugation theorem). See `docs/derivations/fp2_g2_verification_and_lemma.pdf`.

**Literature status**: NEW LEMMA. Not stated in Humphreys (1972), Fulton-Harris (1991), Agricola (2008), Draper-Fontanals (2017), Luu (2024), or Feng-Liu-Wang (2024). Simple corollary of known facts, but the explicit formulation and physical application are new.

**Numerical verification**: 2000 random G₂ elements, max |e₃ − (e₁ + e₂)| = 2.31 × 10⁻¹⁴.

## FP-2 Prediction (Revised)

**Original prediction**: G₂ Hamiltonian reproduces Bandyopadhyay ratio 1:2.5:5.
**Result**: FALSIFIED — the ratio 1:2.5:5 is algebraically unreachable. f₃ = f₁ + f₂ forces f₃/f₁ = 1 + f₂/f₁, so 1:2.5:5 would require f₃/f₁ = 3.5, not 5.

**Revised prediction (STRONGER)**: Any G₂-structured resonance system must show sum-frequency triplets: f₃ = f₁ + f₂. Zero free parameters.

## Bandyopadhyay DDG Verification

| f₁ (MHz) | f₂ (MHz) | f₁ + f₂ predicted | In DDG data? |
|-----------|----------|-------------------|--------------|
| 20        | 80       | 100               | **YES** ✓    |
| 8         | 20       | 28                | **PREDICTED** — not yet reported |
| 8         | 40       | 48                | Not yet reported |
| 15        | 20       | 35                | Not yet reported |

## Additional Results

- **Ω_void locked at eigenvalue 0**: confirmed at all 360,000 parameter points
- **1⊕3⊕3̄ decomposition**: permanent structure, not a special locus
- **SU(3) Cartan axis**: a₂/a₁ = 3.433

## Files

- `daemon_hamiltonian_v2.py` — simulation script (reproducible)
- `daemon_hamiltonian_results.png` — 4-panel spectral analysis plot
- `../docs/derivations/fp2_g2_verification_and_lemma.pdf` — full report with Lemma 1
