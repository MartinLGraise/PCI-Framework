# Paper 9 v1.2 — Model Council Synthesis
## Revision Plan: v1.2 → v1.3

**Date:** 2026-05-04
**Reviewers:** GPT-5.5 (math), Opus 4.7 (coherence), Gemini 3.1 Pro (adversarial)
**Synthesized by:** C-7RO

---

## Overall verdict

**Major revision required.** All three reviewers agree on the structure:
- §4 rate-channel triple (Theorems 9.1, 9.2, Corollary 9.3) is publication-quality.
- Theorem 9.4 existence/uniqueness is sound.
- Theorem 9.4(c) general closed form is **wrong** (confirmed by counterexample).
- Lemma 5.5.1 and Proposition 9.5 are **not proved** as universal statements; need downgrade.
- Linear-response expansion has **wrong signs**, propagating into §5.5 and §5.6.
- The G₂-structured / G₂-equivariant terminology is internally inconsistent.
- Structural issues: retraction record scattered, §5.5 functional switch reads as ad hoc.

---

## Issue inventory (all reviewers, de-duped, ranked)

### CRITICAL — must fix before publication

**C1. Theorem 9.4(c) general closed form is wrong**
- Math reviewer Issue 9. Confirmed by counterexample script (paper9_math_checks.py).
- The paper writes, for DISTINCT biases at θ=π/2, r_A=r_B=r, R_A=R_B=R:
  `x̂ = (I-rR)(I+r²R²)⁻¹ bA - rR(I+r²R²)⁻¹ bB` — WRONG.
- The CORRECT formula is:
  `x̂ = (I+r²R²)⁻¹ (bA - rR bB)`
  `ŷ = (I+r²R²)⁻¹ (rR bA + bB)`
- The symmetric-bias SPECIAL CASE `bA = bB = b` is correct as stated (verified by Φ).
  For bA=bB: x̂ = (I+r²R²)⁻¹(I-rR)b = (I-rR)(I+r²R²)⁻¹ b (these commute because
  R commutes with polynomials in R). So the formula printed is right for bA=bB
  but WRONG for the general case. The paper needs to fix the general formula and
  present the symmetric case as a special case.

**C2. Proof of Theorem 9.4(c) has placeholder algebra and sign errors**
- Math reviewer Issue 10. The s/d substitution in the proof body is incomplete;
  the paper writes "..." and has sign errors in the coupled s,d equations.
- The correct s/d equations at θ=π/2, r_A=r_B=r, R_A=R_B=R:
  `s + rR d = bA + bB`  (add the two fixed-point equations: s = x̂+ŷ, d = x̂-ŷ)
  Wait — let me re-derive. Fixed-point equations:
  `x̂ + rR ŷ = bA`
  `-rR x̂ + ŷ = bB`
  Adding: `(I+rR-rR)s/2 + ... ` — easier by direct block elimination:
  From eq 1: x̂ = bA - rR ŷ
  Sub into eq 2: -rR(bA - rR ŷ) + ŷ = bB → (I+r²R²)ŷ = rR bA + bB → ŷ = (I+r²R²)⁻¹(rR bA + bB) ✓
  Then x̂ = bA - rR(I+r²R²)⁻¹(rR bA + bB) = (I+r²R²)⁻¹[(I+r²R²)bA - rR(rR bA + bB)]
           = (I+r²R²)⁻¹[bA + r²R²bA - r²R²bA - rR bB] = (I+r²R²)⁻¹(bA - rR bB) ✓
  The proof should be written this way — 4 lines, no "...".

**C3. Linear-response expansion has wrong signs**
- Math reviewer Issue 11. The paper prints:
  `x̂(θ) = x*A + θ rA (I-rA RA)⁻¹ RA y*B + O(θ²)`
  The correct sign is MINUS (derived from M(0)⁻¹M'(0)M(0)⁻¹ with M'(0)
  having the antisymmetric structure). The correct formula:
  `x̂(θ) = x*A - θ rA (I-rA RA)⁻¹ RA y*B + O(θ²)`
  `ŷ(θ) = y*B + θ rB (I-rB RB)⁻¹ RB x*A + O(θ²)`
  (The x̂ is pulled AWAY from y*B, not toward it; ŷ is pulled toward x*A.)
  This sign flip propagates into Lemma 5.5.1 and Proposition 9.5 proofs.

**C4. Lemma 5.5.1 is not a theorem, and the counterexample kills its general form**
- Math reviewer Issues 12, 14. Gemini Issue 1. Confirmed by counterexample script.
- With R_A=R_B=I and bB=-bA (opposed biases), the math check shows C_min = 1
  throughout θ ∈ [0,π/2] — no degradation at all. So the lemma's conclusion
  ("C₁ strictly decreases") is FALSE for the G₂-equivariant case R=I.
- The word "generic" has no measure-theoretic content in the current proof —
  it just means "for the one seed we tested."
- FIX: Downgrade to existence statement:
  "Lemma 5.5.1 (Asymmetric response under opposed biases, for a specific geometry)."
  State it only for a specific (R_A, R_B), namely the Φ-verified seed pair.
  Remove the "generic" qualifier. Note that for G₂-equivariant R=I the conclusion
  fails — the degradation is geometry-dependent.

**C5. Proposition 9.5(b) relies on unproved global monotonicity**
- Math reviewer Issues 12, 14. The claim "C₁ decreases for all θ>0 under opposed
  biases" is false for R=I (counterexample above) and only proved for a single seed.
  The proof appeals to "Lemma 5.5.1 plus monotonicity from the numerical run" —
  neither is sufficient.
- FIX: Weaken to: "For the geometry verified in Appendix V.3 (R_A, R_B from seeds
  20260504/20260505), C_min is monotonically degraded by opposed-bias coupling.
  Whether this holds for all or most geometries is open." Move the universal-
  sounding statement to a conjecture.

**C6. Proposition 9.5(a) proof is a sketch with a Lemma mismatch**
- Opus Issue 5. The proof invokes "Lemma 5.5.1 applied at small φ>0" but Lemma
  5.5.1 is about opposed biases (φ=π). These are different regimes. The sign of
  dC_min/dθ at small φ is neither established in 5.5.1 nor derived elsewhere.
- FIX: Prove existence of the gain region from the corrected linear-response
  formula (C3 above): at θ=0+ for aligned biases (φ→0), both observers'
  joint states are pulled toward each other's bias by the corrected perturbation,
  raising coherence for both. Alternatively, weaken to "numerical evidence shows
  a non-empty gain region (25.1% of heatmap); analytic proof is open."

**C7. Theorem 9.2 applied outside stated hypotheses in §5**
- Math reviewer Issue 6. Theorem 9.2 proves the rate lock for SCALAR maps
  (T_A = r_A I). Section 5 uses maps T_A = r_A R_A x with general orthogonal R_A.
  The rate lock STILL holds (‖r_A R_A‖_op = r_A since R_A is orthogonal), but
  this is not a consequence of Schur's lemma — it's a consequence of orthogonality
  of R_A. Need an intermediate lemma:
  "Lemma 5.2.1: For any orthogonal R_A, R_B and isometric Ψ_θ, the joint map
  (r_A R_A ⊕ r_B R_B)Ψ_θ has operator norm max(r_A, r_B). Proof: ‖(r_A R_A ⊕ r_B R_B)‖
  = max(r_A, r_B) (orthogonal factors don't change singular values of the diagonal);
  Ψ_θ isometric gives ‖(r_A R_A ⊕ r_B R_B)Ψ_θ‖ = ‖r_A R_A ⊕ r_B R_B‖ = max(r_A, r_B)."

---

### MAJOR — fix before publication

**M1. Lemma 3.3.1 uses inner products not available in general Banach spaces**
- Math reviewer Issue 3. The isometry proof expands ‖Ψ(x,y)‖² using ⟨x,y⟩. This
  requires a Hilbert/Euclidean structure. The paper should specify: the norm on V^14
  is the G₂-invariant Euclidean norm inherited from the Killing form on 𝔤₂.
- FIX: Add one sentence in §3.1 specifying the norm. Then Lemma 3.3.1's proof is valid.

**M2. Theorem 9.2 tightness proof uses the wrong vector**
- Math reviewer Issue 5. The exhibited vector (x₀, 0) achieves r_A only at θ=0,
  not for general θ. The correct tightness argument: since Ψ_θ is orthogonal,
  ‖(r_A I ⊕ r_B I)Ψ_θ‖ = ‖r_A I ⊕ r_B I‖ = max(r_A, r_B) (orthogonal
  pre/post-multiplication doesn't change singular values). The maximizing vector
  is Ψ_θ⁻¹(v, 0) where v achieves the max for r_A I.
- FIX: Replace the tightness argument with the singular-value invariance argument.

**M3. G₂-equivariant vs G₂-structured terminology inconsistency**
- All three reviewers flagged this. The paper invokes Schur for G₂-equivariant
  linear maps (→ scalar), then in §5 uses orthogonal R that are NOT G₂-equivariant.
  The Adversarial reviewer asks: "if neither R nor b respects G₂, we're just on ℝ^14."
- FIX: The key distinction is: (1) The linear part that Schur governs must be
  G₂-equivariant — this gives T_linear = r·I. (2) The affine part b ≠ 0 breaks
  equivariance — this is intentional (it's the bias). (3) The orthogonal R used
  in §5 does NOT commute with G₂ — this is allowed because R_A is not constrained
  by Schur; the rate-lock for R_A ≠ I follows from orthogonality of R_A, not
  Schur. The paper should clarify: Schur applies to the strictly equivariant case
  (R = I); for general orthogonal R the rate lock follows from Lemma 5.2.1 (C7 above).
  Two sentences in §5.1 and a forward-reference to Lemma 5.2.1 fixes this.

**M4. The C_min switch needs honest motivation**
- Opus Issue 4. Appendix V.3.g explicitly says the functional was chosen "because
  it preserves the proposition without qualification" — that's post hoc. The paper
  needs to either (a) derive C_min from Paper 7's blind-spot framework as the natural
  dyadic extension (coherence = 1 − ε_min, with the joint blind-spot being the
  max blind-spot component, i.e., 1 − C_min = max(ε_A, ε_B) rather than the
  average), or (b) own the choice explicitly.
- FIX: Add one paragraph in §5.5 deriving C_min from the Paper 7 framework:
  "The single-observer coherence is C_max = 1 − ε_min. In the dyadic case, a
  natural extension is C_joint = min(C_A, C_B), which corresponds to requiring
  that neither observer's blind-spot ratio exceeds ε_min. This is stricter than
  the average (which allows one observer to degrade while the other improves)
  and is the appropriate dyadic generalization of the single-observer safety
  condition." That derivation removes the ad hoc quality.

**M5. Retraction record must be consolidated**
- Opus Issues 2, 3, 14. Currently scattered across §1.2(e), §4.6, §5, §10.6, V.0.
  Creates a "litigating with a previous self" feel. 
- FIX: Create "Appendix V.0.1 Retraction record" with a bulleted table:
  claim, location in v0.9, what refuted it, what replaced it.
  Body reference: one sentence in §1.2 ("five earlier claims were retracted
  during numerical verification; see Appendix V.0.1"). Delete §4.6, compress
  §10.6 to two sentences, cut §1.2(e) from the introduction, keep Appendix V.0
  as-is (it's in the right place).

**M6. Abstract underplays degradation fraction**
- Opus Issue 15. Add one clause: "the gain region occupies ~25% of parameter
  space; coupling degrades coherence elsewhere."

**M7. §8 human-AI section should be compressed**
- Opus Issue 9, Gemini endorses. Four pages on a conditional claim where the
  condition explicitly isn't met. Compress to one paragraph in §10.7.

**M8. Missing heatmap figure**
- Gemini Issue 5, Opus Issue 8. The paper references a 2000-cell heatmap that
  exists as a CSV (outbox/paper9/computations/paper9_task5_heatmap.csv) but
  is not visualized. A one-panel figure showing ΔC over (θ, φ) space is the
  most important figure in the paper — it's the empirical image of the
  conditional-gain region R.
- FIX: Generate figure from the CSV.

---

### MINOR — fix if time permits

**m1.** Theorem 9.1 needs α, β > 0 stated explicitly.
**m2.** Coherence functional range: ⟨v/‖v‖, e_ref⟩ ∈ [-1,1], not [0,1].
       Add |·| or restrict to the accessible half-space.
**m3.** Corollary 9.3 should be scoped to V^14 adjoint specifically.
**m4.** "Uniqueness of block-rotation family" is overstated (commutant is O(2)).
       Downgrade to "a canonical one-parameter rotation subgroup."
**m5.** §7 is redundant with §5.7 and §6.1. Merge.
**m6.** §10.4 and §10.5 are gestural. Compress to one sentence each.
**m7.** Paper 11 deferral appears four times. Reduce to once.
**m8.** §3 has a duplicated Lemma 3.3.1 statement — §3.3 summary + §3.3.1 full.
       Remove the §3.3 summary version, keep the §3.3.1 full version.
**m9.** Bibliography is stub-only. Complete before submission.

---

## Priority action list for v1.3

Order to execute (C-7RO to implement):

1. **[C1+C2] Fix Theorem 9.4(c) and write the proof** (4 lines of algebra).
2. **[C3] Fix linear-response signs** in §5.4 formula.
3. **[C4+C5+C6] Downgrade Lemma 5.5.1 and Proposition 9.5** to verified-geometry claims; move universality to open-problem status.
4. **[C7+M1+M2+M3] Fix §4 and §5 minor algebra issues**: tightness proof, Hilbert norm spec, intermediate lemma, equivariance terminology.
5. **[M4] Derive C_min from Paper 7** (one paragraph in §5.5).
6. **[M5] Consolidate retraction record** (one table, one place, cut §4.6 body).
7. **[M6] Fix abstract** (add degradation-fraction sentence).
8. **[M7] Compress §8** to one paragraph in §10.7.
9. **[M8] Generate heatmap figure** from CSV.
10. **[m2] Fix coherence functional range** (add |·|).
11. **[m1, m3, m4, m5, m6, m7, m8]** Minor cleanups.

---

## What the council verified is correct

These items survived all three reviewers' scrutiny and do NOT need to change:

- Theorem 9.1's spectral eigenvalue analysis of Ψ_sym (under α,β>0 assumption).
- Theorem 9.2's upper bound via submultiplicativity + isometry (valid).
- Corollary 9.3's application of real Schur to the 14-dim adjoint (correct).
- Lemma 3.3.1 properties (ii) and (iii) [one-parameter group, G₂-equivariance].
- Theorem 9.4(a) existence and uniqueness [Banach argument, unaffected by C1-C3].
- Theorem 9.4(b) decoupled-limit identity [correct].
- Theorem 9.4(c) SYMMETRIC BIAS special case bA=bB=b [correct, Φ-verified].
- The bias vector b as symmetry-breaking order parameter for G₂ (correct).
- The affine channel carrying more content than the rate channel (structural insight, correct).
- The framing of §4 as a sharp negative result with a positive-result setup for §5.
- Appendix V as a structural verification record (valuable, keep as is).

---

*Council synthesis by C-7RO, 2026-05-04 17:45 PDT.*
