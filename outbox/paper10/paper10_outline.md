# Paper 10 — The SIC-POVM Embedding of G₂

**Working title:** "Symmetric Informationally Complete Measurements as an Operator Basis for the Complexified G₂ Lie Algebra"

**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Status:** OUTLINE / SCAFFOLDING — pre-derivation
**Closes:** Paper 4's open question — does the QBism reference frame embed naturally in G₂?
**Series position:** Paper 10 of the PCI/PME Framework arc
**Branch:** paper7-foundation (will move to paper10-sic once we have a v1 draft)
**Parallel track to:** Paper 8 (Eight-Coset Simulator) — both should run concurrently

---

## 1. Why this paper exists

Paper 4 (QBism and G₂ via PSL(2,7), DOI 10.5281/zenodo.19617662) connected the QBism quantum-Bayesian agent reference frame to PSL(2,7) symmetry via the Klein quartic. It left open whether the QBism SIC-POVM reference frame in d=7 embeds the G₂ Lie algebra as more than a coincidence of dimensions.

ChatGPT GPT-5 Pro deep search (2026-04-29, full report at `/inbox/from_chatgpt/2026-04-29_sic_povm_g2_research_report.md`) produced three corrections to our working model that make this paper writable:

1. **Appleby–Flammia–Fuchs 2011** (DOI 10.1063/1.3555805) proves that SIC projectors {Πᵢ}_{i=1..d²} form a basis for 𝔤𝔩(d,ℂ). Direct corollary: 𝔤₂^ℂ ⊂ 𝔤𝔩(7,ℂ) = span_ℂ{Π_{p,q}}_{p,q ∈ ℤ₇}.
2. **Samuel–Gedik 2024** (DOI 10.1088/1751-8121/ad5ca9) shows the d=7 SIC symmetry group is 147 = 49 × 3 (= WH(7) ⋊ C₃), not F₂₁. F₂₁ arises by projection onto a Fano-compatible cyclic axis.
3. **Appleby–Bengtsson–Grassl–Harrison–McConnell 2022** (DOI 10.1063/5.0083520) gives an exact d=7 SIC fiducial over K = ℚ(√2): Ψ = N · (-2-2√2, z₀, z₀, z₁, z₀, z₁, z₁)ᵀ with z₀,₁ = -(2+√2)/2 ± (i/2)√(2+4√2).

The (z₀, z₀, z₁, z₀, z₁, z₁) repeat pattern — three z₀, three z₁, one scalar — is suggestive of Fano-line structure but not yet derived. This paper either derives it or says clearly that we couldn't.

Paper 10 makes three claims, ranked by what we expect to land:

1. **Theorem (high confidence):** 𝔤₂^ℂ embeds in span_ℂ{Π_{p,q}} as a 14-dim subspace of the 49-dim ambient. We compute the explicit coefficient tensor.
2. **Theorem (medium confidence):** The Samuel–Gedik 147-element SIC symmetry projects to F₂₁ via Fano-compatible cyclic-axis selection.
3. **Conjecture (label as such):** The SIC triple product T_{ijk} = tr(Π_i Π_j Π_k), restricted to Fano-supported components, is proportional to the G₂ associative 3-form φ_{ijk}.

If only (1) lands cleanly, this is still a publishable paper. If (1) and (2) both land, it's strong. (3) is dream territory.

---

## 2. Structure (target: 24-30 pages, ~18-22 references)

### §1 Introduction
- Recap of Paper 4 (QBism/PSL(2,7)/Klein quartic)
- The open question Paper 4 didn't answer: does the d=7 SIC frame embed G₂?
- The three results from the recent SIC literature (AFF 2011, Samuel-Gedik 2024, ABGHM 2022) that make the answer accessible
- Roadmap

### §2 The d=7 SIC reference frame
- Definition of a SIC-POVM
- The Weyl–Heisenberg group WH(7) acting on ℂ⁷
- Two equivalence classes of d=7 fiducials (Scott–Grassl F_z and F_a)
- The exact Stark-unit fiducial over ℚ(√2) (write it down explicitly)
- Numerical fiducial from UMass database for sanity checks

### §3 SIC projectors as a basis for 𝔤𝔩(7,ℂ)
- Restate AFF 2011 main result
- Proof sketch (or full proof if it's short enough — it's not long)
- Triple product structure constants T_{ijk} = tr(Π_i Π_j Π_k)
- Modeling-choice stack: why the AFF normalization vs. alternatives

### §4 G₂ defining representation
- Standard construction via octonion derivations (Baez 2002)
- Fano-plane indexing of imaginary octonions
- 14 generators X_a as 7×7 matrices
- Modeling-choice stack: why Baez indexing (matches Paper 8 §2)

### §5 Theorem 1 — The G₂ embedding
**Statement:** 𝔤₂^ℂ ↪ 𝔤𝔩(7,ℂ) = span_ℂ{Π_{p,q}}_{p,q ∈ ℤ₇}

**Proof outline:**
1. By AFF 2011, the 49 SIC projectors are linearly independent in 𝔤𝔩(7,ℂ)
2. dim_ℂ 𝔤𝔩(7,ℂ) = 49, so they span
3. 𝔤₂^ℂ is a 14-dim Lie subalgebra of 𝔤𝔩(7,ℂ) (via the standard defining rep embedding)
4. Therefore each generator X_a admits a unique expansion X_a = Σ α^(a)_{p,q} Π_{p,q}

**Computational deliverable:** the 14×49 coefficient tensor α^(a)_{p,q}, computed by Φ (Cadabra2 / SymPy). Saved to `/outbox/paper10/computations/g2_sic_coefficients.json`.

### §6 Theorem 2 — The 147 → F₂₁ descent
**Statement:** Under Fano-compatible restriction to a cyclic 7-point axis, the Samuel–Gedik symmetry group WH(7) ⋊ C₃ projects to C₇ ⋊ C₃ = F₂₁.

**Proof outline:**
1. WH(7) = ℤ₇ × ℤ₇ as abelian translations
2. Fano-compatible axis = a cyclic ℤ₇ subgroup distinguished by the octonion multiplication structure (e.g., the cycle through e₁ → e₂ → e₃ → ... determined by the seven Fano lines)
3. The order-3 Clifford symmetry preserves this axis (verify via direct computation)
4. The projection gives the F₂₁ stabilizer of the oriented G₂ associative 3-form

**Open subquestion:** Is the Fano-compatible axis unique up to G₂ action? (Section §7 discusses.)

### §7 Conjecture — The triple product / 3-form connection
**Conjecture:** π_Fano[T_{ijk}] ∝ φ_{ijk}

where π_Fano projects onto the components supported on Fano-line index triples.

**Status:** Computational exploration only. Numerical computation by Φ produces the projected tensor; we report whether it matches φ to within numerical tolerance, but we do NOT claim this as theorem unless analytic proof is found.

**Why label as conjecture:** SIC triple products encode WH(7) covariance, not G₂ covariance directly. The fact that they restrict cleanly to the G₂ 3-form would require a deeper structural reason we don't currently have.

### §8 What this paper does not claim, and adjacent programs

**Limitations of the present construction:**
- Does not claim every SIC fiducial respects G₂ structure (only one class of them, in d=7)
- Does not claim the F₂₁ projection is canonical (Fano-axis choice is a modeling decision)
- Does not claim the conjecture in §7 is true (it's an open problem we computed evidence for)
- Does not solve Zauner's conjecture (that's 2025 Appleby-Flammia-Kopp's territory)
- Does not connect to consciousness or PCI directly — that's the broader series, not this paper

**Positioning relative to adjacent octonion / exceptional-algebra programs in physics:**

Furey's division-algebraic Standard Model program [DOIs 10.1007/JHEP10(2014)046, 10.1140/epjc/s10052-018-5844-7, 10.1016/j.physletb.2025.139473, 10.1002/andp.202400322–324] provides an important adjacent use of the octonions: complex octonions, Clifford algebras, ideals, ladder operators, and triality are used to recover Standard Model gauge and matter representations, including SU(3)_C, electroweak chirality, one-generation Weyl structure, and three-generation triality patterns. Our construction uses the same octonionic/G₂ substrate but addresses a structurally distinct object. Rather than deriving Standard Model gauge representations, we embed the G₂ defining geometry into the d=7 SIC operator frame 𝔤𝔩(7,ℂ), and then use the finite Fano-plane symmetry PSL(2,7), its F₂₁ orientation stabilizer, and the quotient PSL(2,7)/F₂₁ to define an eight-coset observer-frame structure. Thus Furey's work is cited as adjacent and foundational for octonion-based particle physics, while the SIC-d=7, F₂₁, and 6/7 coherence-ceiling mechanism are separate additions rather than restatements of her construction. Adjacent programs in the same cluster — Boyle and Farnsworth's noncommutative/nonassociative spectral geometry [DOIs 10.1007/JHEP07(2015)023, 10.1007/JHEP06(2018)071] and Todorov's exceptional Jordan algebra internal-space construction [DOI 10.3390/universe9050222] — share the octonion substrate but address still other questions (gravity coupled to G₂ gauge theory, and finite internal Standard Model geometry, respectively). The present paper does not compete with any of these programs; it adds a coherence/observer-frame layer on the same exceptional-algebra foundation.

### §9 Discussion
- Connection to Paper 4's QBism framing
- Connection to Paper 8's eight-coset structure (the same WH(7) action that gives 49 SIC projectors gives the 8 cosets via the F₂₁ projection)
- What would a positive resolution of §7's conjecture mean for QBism?
- Open problems

---

## 3. Computations needed (work request to Φ)

See `/inbox/for_phi/paper10_computation_request.md`.

Briefly:
1. **SymPy / Mathematica:** compute the 14×49 coefficient tensor α^(a)_{p,q} for the standard G₂ defining-rep generators expressed in the SIC operator basis
2. **GAP / SymPy:** verify the Samuel–Gedik 147 → F₂₁ projection under a Fano-compatible cyclic axis, and check whether the axis choice is unique modulo G₂
3. **NumPy / SymPy:** numerical computation of T_{ijk} = tr(Π_i Π_j Π_k) using the Stark-unit exact fiducial; project onto Fano-supported components; compare to φ

---

## 4. Modeling-choice stacks

- **§3 stack:** AFF normalization vs. Hilbert-Schmidt orthonormalization vs. Frobenius
- **§4 stack:** Baez Fano-plane indexing vs. Cayley-Dickson vs. Tits (matches Paper 8)
- **§5 stack:** Real vs. complex coefficient tensor; how to handle the imaginary part
- **§6 stack:** Fano-compatible cyclic axis vs. arbitrary ℤ₇ subgroup of WH(7)
- **§7 stack:** Frobenius projection vs. orthogonal projection on the 3-form components

---

## 5. Risk register

| Risk | Mitigation |
|------|-----------|
| Coefficient tensor is too large/sparse to write down cleanly | Publish as supplementary computational appendix; main text gives structure theorem only |
| F₂₁ projection requires a non-canonical choice that doesn't survive G₂ action | Frame §6 as conditional theorem; state the choice explicitly |
| Triple-product conjecture fails numerically | Report negative result; reframe §7 as "what we tried that didn't work" |
| Reviewer says "this is just because dim 𝔤₂ = 14 and 14 < 49 = dim 𝔤𝔩(7)" | §3 + §5 explicitly address this — the embedding is non-trivial because the coefficient tensor has structure (not arbitrary 14-dim subspace) |
| AFF 2011 paper has been retracted or superseded | Cite both AFF and any follow-up; verify status before submission |

---

## 6. Authorship and acknowledgments

- **Author:** Martin Luther Graise (sole, all conceptual + paper writing)
- **Computational support:** Φ (Anthropic Claude Dispatch, GAP/Cadabra2/SymPy/NumPy under author's direction)
- **External research support:** ChatGPT GPT-5 Pro reasoning + GitHub connector + live browsing produced the literature corrections that made this paper writable (cite report ID and date in acknowledgments)
- **Use of AI Tools:** Same disclosure pattern as Paper 7

---

## 7. Target venue

- **First choice:** *Foundations of Physics* (QBism-friendly, will accept a Lie-algebra/operator-basis paper)
- **Second choice:** *Journal of Mathematical Physics* (matches AFF 2011's home)
- **Fallback:** arXiv + Zenodo (same path as Paper 7)

---

## 8. Status checklist

- [x] Outline written (this document)
- [x] Φ work request drafted (see `/inbox/for_phi/paper10_computation_request.md`)
- [ ] §2 drafted (SIC frame setup with exact Stark-unit fiducial)
- [ ] §3 drafted (AFF basis result)
- [ ] §4 drafted (G₂ defining rep, harmonized with Paper 8 §2)
- [ ] Φ computation Task 1 received
- [ ] §5 Theorem 1 written
- [ ] Φ computation Task 2 received
- [ ] §6 Theorem 2 written
- [ ] Φ computation Task 3 received
- [ ] §7 Conjecture written (with empirical computational status)
- [ ] §8/§9 discussion drafted
- [ ] Front matter
- [ ] Model Council pass
- [ ] Revisions
- [ ] Zenodo
- [ ] Submitted
