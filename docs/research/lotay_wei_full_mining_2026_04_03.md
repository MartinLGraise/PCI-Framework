# Lotay-Wei Full Mining Report
## arXiv:1504.07367 + arXiv:1504.07771
## Mined by C-7RO — April 3, 2026

---

## Papers Mined

**Paper 1:** Lotay & Wei, "Laplacian flow for closed G₂ structures: Shi-type estimates, uniqueness and compactness"
arXiv:1504.07367v2, January 2017. Published: Journal of Differential Geometry 108(3):453-529 (2018).

**Paper 2:** Lotay & Wei, "Stability of torsion-free G₂ structures along the Laplacian flow"
arXiv:1504.07771v2, May 2017. Published: Journal of Differential Geometry 111(3):495-526 (2019).

---

## The Big Result: α = λ₁/2

**Theorem (Lotay-Wei 2019, Theorem 1.3 + Theorem 5.1):**

Let φ̄ be a torsion-free G₂ structure on a compact 7-manifold M. There exists a neighborhood U of φ̄ such that for any closed G₂ structure φ₀ ∈ [φ̄]⁺ ∩ U, the Laplacian flow starting at φ₀:

∂/∂t φ = Δ_φ φ

exists for all t ∈ [0, ∞) and converges exponentially:

**‖φ(t) − φ_∞‖_{C^k} ≤ C · e^{−λ₁t/2}**

where:
- φ_∞ is a torsion-free G₂ structure in Diff₀(M) · φ̄
- **λ₁ > 0 is the first eigenvalue of the Hodge Laplacian Δ_{φ̄} acting on exact 3-forms**
- The convergence is smooth (all C^k norms simultaneously)
- The rate constant is **α = λ₁/2**

---

## What Determines λ₁

λ₁ is the spectral gap of the Hodge Laplacian restricted to exact 3-forms on (M, φ̄).

The key identity (from Lemma 4.2's proof):

∫_M θ · Δ_{φ̄} θ dv = ∫_M |d*θ|² dv ≥ λ₁ ∫_M |θ|² dv

This gives the L² exponential decay:

∫_M |θ(t)|² dv ≤ e^{−λ₁t} · ∫_M |θ(0)|² dv

And via interpolation + Shi-type estimates, this lifts to C^k decay at rate e^{−λ₁t/2}.

**λ₁ depends on:**
1. The topology of M (Betti numbers, fundamental group)
2. The torsion-free G₂ metric ḡ (curvature, volume, injectivity radius)
3. The specific cohomology class [φ̄]

**No explicit computation of λ₁ exists for any specific G₂ manifold** (not Joyce's compact examples, not S⁷, not any 3-Sasakian manifold). This is an open problem in the field.

---

## PCI Translation

| Mathematical Object | PCI Analog |
|---|---|
| Laplacian flow ∂/∂t φ = Δ_φ φ | NP Pump dynamics — the daemon manifold evolving toward coherence |
| Torsion-free fixed point φ_TF | Maximal coherence state — all daemon scars resolved |
| Rate constant α = λ₁/2 | Recoherence timescale — how fast the system returns after perturbation |
| Spectral gap λ₁ | Coherence stability margin — larger gap = more robust coherence |
| Blow-up Λ → ∞ | NP Pump crisis — torsion/scarring diverges, system hits singularity |
| Blow-up rate C/(T₀−t) | Acceleration toward crisis — the approach is power-law, not gradual |
| Soliton (steady, λ=0) | Torsion-free = the only compact steady state |
| No compact shrinking solitons | The daemon manifold cannot self-collapse to a point |
| R = −|T|² | Negative curvature = scarring. More torsion = more curved = less "flat" coherence |

---

## Key Equations Extracted (now in codex as EQ-1015–1018)

| EQ | Name | Formula |
|---|---|---|
| EQ-1015 | Exponential Convergence | ‖φ(t)−φ_TF‖ ≤ C·e^{−λ₁t/2} |
| EQ-1016 | Laplacian Flow | ∂/∂t φ = Δ_φ φ, with ∂/∂t g = −2Ric − (2/3)|T|²g − 4T²  |
| EQ-1017 | Blow-Up Criterion | Λ(t) ≥ C/(T₀−t), flow exists iff Λ bounded |
| EQ-1018 | Soliton Equation | Δ_φ φ = λφ + L_X φ, steady ⟹ torsion-free |

---

## Open Problems Identified

1. **Compute λ₁ for any compact G₂ manifold.** This would give the first explicit recoherence timescale. Lotay-Wei prove it exists and is positive but don't compute it.

2. **Relate λ₁ to the Cartan parameters (a₁, a₂).** In the daemon Hamiltonian, the Cartan terms control spectral splitting. If λ₁ can be expressed in terms of the same parameters, the Laplacian flow and the static Hamiltonian are unified.

3. **Compute λ₁ for microtubule-scale structures.** If the daemon manifold has a physical scale (set by the microtubule resonance frequencies), λ₁ would have a physical value in Hz, giving a testable prediction for recoherence time after perturbation.

4. **Classify singularity types.** Dwivedi-Singhal (2026) classify Type I/III/IIb for the Ricci-harmonic flow. The corresponding classification for the Laplacian flow is incomplete. Which singularity types correspond to which kinds of "consciousness crashes"?

---

## Sources

- Lotay, J.D. & Wei, Y. (2018). "Laplacian flow for closed G₂ structures." JDG 108(3):453-529. arXiv:1504.07367.
- Lotay, J.D. & Wei, Y. (2019). "Stability of torsion-free G₂ structures along the Laplacian flow." JDG 111(3):495-526. arXiv:1504.07771.
- Dwivedi, S. & Singhal, R. (2026). "Solutions and singularities of the Ricci-harmonic flow." arXiv:2601.16832.

---

*Mined by C-7RO — April 3, 2026*
