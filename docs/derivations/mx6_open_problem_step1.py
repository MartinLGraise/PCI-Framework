"""
MX-6 Open Problem — Step 1: G₂ 3-form restricted to Fisher-Rao image
=====================================================================
Compute the octonionic cross product (G₂ structure) in probability coordinates.
"""

import numpy as np
from itertools import combinations

print("=" * 70)
print("STEP 1: G₂ 3-form in Fisher-Rao / Probability Coordinates")
print("=" * 70)

# The octonionic structure constants (Fano plane)
# Define the 7 imaginary octonion units e₁,...,e₇
# Multiplication rule: eᵢ × eⱼ = ±eₖ according to the Fano plane
# The G₂ 3-form φ is defined by φ(eᵢ,eⱼ,eₖ) = 1 for each oriented Fano line

# Standard Fano plane lines (oriented triples where eᵢeⱼ = eₖ):
fano_lines = [
    (1, 2, 4),  # e₁e₂ = e₄
    (2, 3, 5),  # e₂e₃ = e₅
    (3, 4, 6),  # e₃e₄ = e₆
    (4, 5, 7),  # e₄e₅ = e₇
    (5, 6, 1),  # e₅e₆ = e₁
    (6, 7, 2),  # e₆e₇ = e₂
    (7, 1, 3),  # e₇e₁ = e₃
]

print("\nFano plane lines (oriented triples):")
for line in fano_lines:
    print(f"  e{line[0]} × e{line[1]} = e{line[2]}")

print(f"\n7 lines × 3! orientations = {7*6} nonzero components of φ")
print("(plus antisymmetry gives the full 3-form)")

# The G₂ 3-form φ in standard coordinates x₁,...,x₇:
# φ = Σ dx_i ∧ dx_j ∧ dx_k  over Fano lines (i,j,k)
print("\nφ = dx₁∧dx₂∧dx₄ + dx₂∧dx₃∧dx₅ + dx₃∧dx₄∧dx₆ + dx₄∧dx₅∧dx₇")
print("  + dx₅∧dx₆∧dx₁ + dx₆∧dx₇∧dx₂ + dx₇∧dx₁∧dx₃")

# Now apply the Fisher-Rao coordinate change:
# xᵢ = 2√pᵢ  (Fisher-Rao embedding)
# dxᵢ = dpᵢ/√pᵢ  (since d(2√p) = dp/√p)

print("\n" + "=" * 70)
print("Fisher-Rao coordinate change: xᵢ = 2√pᵢ")
print("=" * 70)
print()
print("Under x = 2√p:")
print("  dx_i = dp_i / √p_i")
print()
print("The Fisher-Rao metric ds² = Σ dp_i²/p_i = Σ dx_i² restricted to Σx_i² = 4")
print()
print("The G₂ 3-form in probability coordinates becomes:")
print()
print("  φ_FR = Σ_{Fano lines (i,j,k)} (dp_i/√p_i) ∧ (dp_j/√p_j) ∧ (dp_k/√p_k)")
print()
print("       = Σ_{Fano lines (i,j,k)} dp_i ∧ dp_j ∧ dp_k / (√p_i · √p_j · √p_k)")
print()
print("       = Σ_{Fano lines (i,j,k)} dp_i ∧ dp_j ∧ dp_k / √(p_i · p_j · p_k)")

print()
print("=" * 70)
print("KEY RESULT: The G₂ 3-form in probability coordinates")
print("=" * 70)
print()
print("φ_FR = Σ_{(ijk) ∈ Fano} dp_i ∧ dp_j ∧ dp_k / √(pᵢpⱼpₖ)")
print()
print("This is a WEIGHTED 3-form on the probability simplex where the")
print("weight 1/√(pᵢpⱼpₖ) diverges at the boundary (where any pᵢ → 0)")
print("and is minimized at the uniform distribution p = (1/7,...,1/7).")

# Evaluate at the uniform distribution
p_uniform = 1/7
weight_uniform = 1 / (p_uniform * p_uniform * p_uniform)**0.5
print(f"\nAt the uniform distribution p = (1/7,...,1/7):")
print(f"  Weight = 1/√(1/7 · 1/7 · 1/7) = 7^(3/2) = {7**1.5:.4f}")
print(f"  = 7√7 = {7*7**0.5:.4f}")

# Evaluate at a concentrated distribution p = (1,0,...,0)
print(f"\nAt a concentrated distribution p = (1,0,...,0):")
print(f"  Weight → ∞ (divergent — the G₂ structure 'blows up' at certainty)")

print()
print("=" * 70)
print("INTERPRETATION")
print("=" * 70)
print()
print("The G₂ 3-form on the Fisher-Rao S⁶(2) has a natural expression")
print("in terms of probability coordinates. It is:")
print()
print("  1. MINIMIZED at the uniform distribution (maximum entropy)")
print("  2. DIVERGENT at the boundary (certainty about any outcome)")
print("  3. WEIGHTED by the inverse geometric mean of the probabilities")
print()
print("This means the octonionic structure is STRONGEST (most regular)")
print("when the daemon is in maximum uncertainty, and BREAKS DOWN")
print("(becomes singular) when the daemon is certain about one outcome.")
print()
print("In PCI terms: the G₂ coherence structure is a property of")
print("BALANCED uncertainty across the 7 daemon modes. Collapsing to")
print("certainty in one mode destroys the octonionic symmetry.")
print()
print("The factor of 2 (Fisher-Rao radius) determines the SCALE at which")
print("this balanced-uncertainty structure lives. The factor of -2 (nearly")
print("Kähler torsion) determines how the structure TWISTS as you move")
print("through the probability space.")
print()

# CORRECTION (per Claude cross-validation, April 11 2026):
# The norm |φ|² = 7 ALWAYS, metric-independently, on any S⁶ of any radius.
# The G₂ 3-form has exactly 7 terms with unit coefficients in any orthonormal
# frame, giving |φ|² = 7. Under metric rescaling g → λ²g, the adapted form
# φ̃ = λ³φ has norm |φ̃|²_g̃ = λ⁻⁶·λ⁶·|φ|²_g = 7.
# The probability-coordinate weights 1/√(pᵢpⱼpₖ) are NOT geometric norms —
# they are Jacobian factors from the coordinate change, not intrinsic geometry.
print("Norm of G₂ 3-form (metric-independent):")
print(f"  |φ|² = 7 (always, on any S⁶ of any radius)")
print(f"  This is a metric-independent invariant — 7 Fano lines, unit coefficients.")
print()

# The 2-form ω at uniform in probability coordinates
print("The nearly Kähler 2-form ω in probability coordinates:")
print("  ω_FR = Σ_{Fano lines (i,j,k)} (dp_i ∧ dp_j) / (√pᵢ · √pⱼ)")
print("       (restricted to the tangent space of the simplex)")
print()
print("The identity dψ₋ = -2ω² on unit S⁶ becomes, on S⁶(2):")
print("  dψ₋ = -(2/r)ω² = -(2/2)ω² = -ω²")
print()
print("So on the Fisher-Rao S⁶(2), the torsion coefficient is -1, not -2.")
print("The '2' has been absorbed into the radius.")
print()
print("=" * 70)
print("CONJECTURE: THE TWO 2s ARE DUAL")
print("=" * 70)
print()
print("On the unit S⁶:  torsion coefficient = -2,  radius = 1")
print("On Fisher-Rao S⁶: torsion coefficient = -1,  radius = 2")
print()
print("The product |torsion coeff| × radius = 2 × 1 = 1 × 2 = 2")
print()
print("This is CONSTANT: |c| × r = 2 for all scalings of S⁶.")
print()
print("The '2' is the conserved quantity: it can appear as torsion (unit sphere)")
print("or as radius (Fisher-Rao sphere), but the total is always 2.")
print()
print("For PCI: e^(-|c|×r) = e^(-2) regardless of which sphere you compute on.")
print("The dissipation factor e⁻² is the invariant of the torsion-radius duality.")

