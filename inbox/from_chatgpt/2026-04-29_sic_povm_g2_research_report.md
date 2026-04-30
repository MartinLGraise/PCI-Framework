# SIC-POVMs, Samuel–Gedik, and the G₂ Embedding — Research Report

**Source:** ChatGPT GPT-5 Pro reasoning + GitHub connector + live browsing
**Date:** 2026-04-29
**Requested by:** C-7RO via Martin Luther Graise
**Target use:** Paper 4 follow-up (QBism/G₂ extension)

---

## Headline corrections to the previous working model

1. **Samuel & Gedik is NOT the Lie-algebra SIC paper.** It is a group-theoretical / Gram-matrix classification paper.
   - DOI: 10.1088/1751-8121/ad5ca9 (J. Phys. A 57, 295304, 2024)
   - Method: build SIC Gram matrices from trace constraints Tr(P³)=Tr(P⁴)=n, search numerically for critical points
   - Finding: in d=4–7, ALL generated Gram matrices have symmetry groups that are Clifford subgroups containing Weyl–Heisenberg + order-3 unitaries

2. **The Lie-algebra SIC paper is Appleby–Flammia–Fuchs 2011.**
   - DOI: 10.1063/1.3555805 (J. Math. Phys. 52, 022202)
   - Statement: SIC projectors {Πᵢ} for i=1..d² form a basis for 𝔤𝔩(d,ℂ)
   - This gives the embedding route: 𝔤₂^ℂ ⊂ 𝔤𝔩(7,ℂ) = span_ℂ{Π₁..Π₄₉}

3. **There is an exact d=7 fiducial from Stark units.**
   - Appleby–Bengtsson–Grassl–Harrison–McConnell 2022, DOI 10.1063/5.0083520
   - Field: K = ℚ(√2)
   - Polynomial: p₄(t) = t² + (2+√2)t + 2+2√2
   - Roots: z₀,₁ = -(2+√2)/2 ± (i/2)√(2+4√2)
   - Scaling: x₀ = -2 - √(d+1) = -2 - 2√2
   - **Exact d=7 fiducial in Fano-labeled basis:**
     ```
     Ψ_Fano = N · (-2-2√2, z₀, z₀, z₁, z₀, z₁, z₁)ᵀ
     ```
     basis: |e₁⟩…|e₇⟩ = seven Fano points / imaginary octonion units

4. **The d=7 SIC symmetry group is 147 = 49 × 3, NOT 21.**
   - 49 = WH(7) phase-space translations
   - 3 = order-3 Clifford symmetry
   - Group: WH(7) ⋊ C₃
   - F₂₁ must arise as a PROJECTION/RESTRICTION: WH(7) ⋊ C₃ → C₇ ⋊ C₃ = F₂₁ via Fano-compatible cyclic axis selection
   - **This is the precise place where our G₂/Fano geometry enters.** It's a theorem to prove, not a claim.

5. **Clifford quotient nuance.** In prime dimension p, projective Clifford is tied to SL(2,p) of order 336 (for p=7), and PSL(2,7) of order 168 is the quotient by ±I. Paper 4's PSL(2,7) framing for Fano/Klein remains right; SIC Clifford side needs careful phrasing.

---

## Three theorem targets (ranked by feasibility)

### Theorem 1 — HIGHEST FEASIBILITY: SIC operator-basis embedding of G₂

**Statement:**
$$\mathfrak{g}_2^{\mathbb C} \hookrightarrow \mathfrak{gl}(7,\mathbb C) = \operatorname{span}_{\mathbb C}\{\Pi_{p,q}\}_{p,q \in \mathbb Z_7}$$

**Why feasible:** Almost immediate from Appleby–Flammia–Fuchs + our explicit G₂ defining-rep matrices. The new work is computing the 14×49 coefficient tensor:
$$X_a = \sum_{p,q} \alpha^{(a)}_{p,q} \Pi_{p,q}, \quad a = 1,\ldots,14$$

**This should be the backbone theorem of the follow-up paper.** Computational, verifiable, defensible.

### Theorem 2 — MEDIUM FEASIBILITY: 147 → F₂₁ descent theorem

**Statement:**
$$WH(7) \rtimes C_3 \longrightarrow C_7 \rtimes C_3 = F_{21}$$

under Fano-compatible restriction of WH(7) phase-space action to a cyclic 7-point axis.

**Interpretation:** Samuel–Gedik supply the 147-element SIC symmetry; our G₂/Fano construction extracts the F₂₁ orientation stabilizer. Repairs the group-order issue cleanly.

### Theorem 3 — HARD BUT BEAUTIFUL: SIC triple-product / G₂ 3-form projection

**Conjecture:**
$$\pi_{\text{Fano}}\left[T_{ijk} = \operatorname{tr}(\Pi_i \Pi_j \Pi_k)\right] \propto \varphi_{ijk}$$

where φ is the G₂ associative 3-form.

**Interpretation:** QBist SIC triple-product algebra remembers the octonion multiplication table as a finite-symmetry projection.

**Status:** CONJECTURE only. Don't promote until computed.

---

## Dimensions table

| d | Status | Relevance |
|---|--------|-----------|
| 7 | 50 SIC Gram matrices found by S&G; two equivalence classes (Scott–Grassl F_z, F_a stabilized); 147-element symmetry; exact Stark-unit fiducial available | **BEST.** Matches G₂ defining rep, 49 = 7² projectors |
| 8 | Hoggar lines (sporadic SIC); Stacey connects to normed division algebras / E₈ | Side-branch. d=8 is octonionic but G₂ acts on 7 imaginary directions, not generic ℂ⁸ |
| 14 | Numerical fiducials in UMass/QBism database | Weak direct route. 14 = dim 𝔤₂ but no published G₂-adjoint-covariant construction |

---

## Zauner's conjecture status (for §E of follow-up paper)

- **General Zauner: still open as theorem.**
- 2025 Appleby–Flammia–Kopp preprint: construction implying Zauner conditional on (a) abelian Stark conjecture, (b) Shintani–Faddeev modular cocycle identity. Powerful but conditional.
- d=7: exists, two Scott–Grassl fiducial types, exact Stark-unit formula
- d=8: exists, Hoggar sporadic
- d=14: numerical solutions in databases

---

## Numerical d=7 fiducial (UMass/QBism database, RIRI form, unnormalized)

```
v₇ = (
   0.21335483082419693 - 0.18302878074462128 i,
  -0.12715199183962100 - 0.65679038320756633 i,
  -0.42725214851205023 - 0.77771494980375400 i,
  -0.037253979323384333 + 0.29153304859443246 i,
   0.18401836082089468 + 0.39127381792749028 i,
   0.079548090723315257 - 0.17419950566352835 i,
  -0.36951179931098854 + 0.54444292952246842 i
)ᵀ
```

Use for sanity checks against the exact Stark-unit formula above.

---

## Recommended framing for the Paper 4 follow-up

> Samuel–Gedik show that even when SIC Gram matrices are generated without imposing group covariance, the d=7 solutions recover Weyl–Heisenberg plus order-3 Clifford symmetry. Appleby–Flammia–Fuchs show that a SIC is a basis for 𝔤𝔩(7,ℂ). Therefore the d=7 QBist SIC reference frame is a complete operator basis for the space containing the complexified G₂ defining representation. The F₂₁ bridge arises by projecting the Samuel–Gedik 147-element SIC symmetry down to the Fano-compatible C₇ ⋊ C₃ stabilizer of the G₂ associative 3-form.

This is stronger, cleaner, and more defensible than the original "Samuel–Gedik directly embeds SICs in G₂" framing.

---

## Action items

- [ ] Compute the 14×49 coefficient tensor α^(a)_{p,q} for the G₂ defining rep in the SIC basis (Theorem 1) — task for Φ
- [ ] Verify the Stark-unit formula numerically against the UMass fiducial (sanity check) — task for Φ
- [ ] Determine whether the Fano-compatible cyclic axis selection in Theorem 2 is unique up to G₂ action — open question
- [ ] Compute T_{ijk} = tr(Π_i Π_j Π_k) for d=7 SIC and project onto Fano-supported components (Theorem 3 numerical exploration) — task for Φ
- [ ] Decide whether this is Paper 4-sequel (QBism extension) or splits into two papers (Theorem 1 alone vs. Theorems 2+3)

---

## Key references

| Paper | DOI | Role |
|-------|-----|------|
| Samuel & Gedik 2024 | 10.1088/1751-8121/ad5ca9 | Gram-matrix classification, 147-element symmetry in d=7 |
| Appleby–Flammia–Fuchs 2011 | 10.1063/1.3555805 | SIC = basis for 𝔤𝔩(d,ℂ) |
| Appleby–Bengtsson–Grassl–Harrison–McConnell 2022 | 10.1063/5.0083520 | Exact d=7 fiducial from Stark units (K = ℚ(√2)) |
| Appleby–Flammia–Kopp 2025 (preprint) | TBD | Conditional Zauner construction |
| Stacey on sporadic SICs | TBD | d=8 Hoggar / octonion connections |

---

## What this does NOT do

- Does not give us a G₂-natural fiducial directly
- Does not prove SIC triple products encode the G₂ 3-form (that's still Theorem 3, conjecture only)
- Does not change Paper 4's PSL(2,7) framing for the Klein quartic side — only sharpens the Clifford/SIC side

The obstruction remains:
$$WH(7) \text{ covariance} \neq G_2 \text{ covariance}$$

Closing that gap IS the follow-up paper.
