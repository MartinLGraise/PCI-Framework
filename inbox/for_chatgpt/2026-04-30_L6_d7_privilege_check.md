# L6 — Is d=7 Privileged? Stark Units, SICs, and Exceptional Structure in Prime Dimensions

**Tool combo:** Live web search + reasoning (NO deep research; GitHub connector OPTIONAL — Paper 10 outline is helpful context but not strictly required)
**Lane:** L6
**Target use:** Determines whether the (d-1)/d = 6/7 saturation in Paper 7 is a special property of d=7 specifically, or a general feature of prime dimensions. Materially affects Paper 10 §5.5 ("unification of four 7s") framing — if d=7 is genuinely privileged, that subsection is earned; if it's just one of many prime cases, the unification claim weakens.
**Model:** GPT-5 Pro reasoning mode
**Estimated runtime:** 15-20 minutes

---

## Why this matters

Paper 10 §5.5 frames the prime number 7 as appearing in four places across the PCI series:
1. PSL(2,7)/F₂₁ blind-spot ratio ε_min = 1/7 (Paper 4)
2. 6/7 contraction ratio (Paper 6)
3. Thermodynamic coherence ceiling 1 - σ_pred = 1/49 = (1/7)² (Paper 7)
4. SIC Gram inversion factor (8/7) = (d+1)/d (Paper 10)

Item 4 is dimension-generic: any d-dim SIC has the (d+1)/d factor. So the question is whether the *coincidence* of d=7 with G₂'s natural action and PSL(2,7)'s symmetry is structurally privileged, or whether analogous "(d-1)/d ceilings" exist for other primes (d=11, d=13, etc.) and we're just one of many cases.

**Stakes:** if d=7 is genuinely privileged, Paper 10 §5.5 is publishable. If d=7 is just convenient, the unification framing needs rewriting.

---

## Prompt to send

```
You are doing a structural privilege check for the dimension
d=7 in the context of SIC-POVMs and exceptional Lie group
geometry. The question I am trying to answer is whether d=7
is genuinely privileged among prime dimensions, or whether
analogous structure exists in d=11, d=13, and other primes.

Background context (you do not need GitHub access; the
relevant papers are cited below):

- Appleby–Bengtsson–Grassl–Harrison–McConnell 2022, "SIC-POVMs
  from Stark units: Prime dimensions n²+3," J. Math. Phys.
  63, 112205 (DOI 10.1063/5.0083520) — gives an exact SIC
  fiducial in dimensions d = n²+3, so the d=7 case is n=2.
  But d=11 ≠ k²+3 for any integer k (closest: 12 = 3²+3),
  and d=13 ≠ k²+3 either.

- Appleby–Flammia–Fuchs 2011, "The Lie algebraic significance
  of symmetric informationally complete measurements,"
  J. Math. Phys. 52, 022202 (DOI 10.1063/1.3555805) — proves
  SIC projectors form a basis for gl(d,C) in any dimension.

- Samuel & Gedik 2024, "Group theoretical classification of
  SIC-POVMs," J. Phys. A 57, 295304 (DOI 10.1088/1751-8121/ad5ca9)
  — Gram-matrix classification.

I am asking five distinct sub-questions. Answer each in its
own subsection, citing primary literature with DOIs.

1. SIC existence in d=11 and d=13:
   For each of d=11 and d=13, what is the current literature
   status? Is an exact algebraic SIC fiducial known? If yes,
   what is the construction (Stark units? Heisenberg–Weyl
   covariance? Sporadic?). Quote or paraphrase the most recent
   exact fiducials if they exist. If only numerical fiducials
   exist, note that.

2. Stark-unit constructions outside d = n²+3:
   The ABGHM 2022 paper covers d = n²+3 (so d = 7, 12, 19,
   28, 39, ...). Are there other Stark-unit-type constructions
   that cover other dimensions? Specifically:
   - Bengtsson 2017 "The Number Behind the Simplest SIC"
     (DOI 10.3390/e19100485 or similar)
   - Appleby–Flammia–McConnell–Yard 2017 "SICs and algebraic
     number theory"
   - Kopp 2021 "SIC-POVMs and the Stark conjectures"
   - Any 2023–2026 followups
   For each, note which prime dimensions are covered and
   whether d=11 and d=13 are accessible.

3. The (d-1)/d "ceiling" pattern:
   In d=7, the ratio 6/7 = (d-1)/d arises from the SIC Gram
   inversion (the (d+1)/d factor) and from the PSL(2,7)/F_21
   blind-spot calculation. Does an analogous (d-1)/d ratio
   appear naturally in d=11 (10/11) or d=13 (12/13) anywhere
   in the SIC literature, the projective representation
   theory of SL(2,p), or the Galois-orbit structure of SIC
   fiducials?

4. Exceptional Lie groups acting in prime dimensions:
   List the prime dimensions in which an exceptional Lie group
   (G_2, F_4, E_6, E_7, E_8) has a natural irreducible
   representation. Specifically:
   - G_2 acts on R^7 (defining), R^14 (adjoint)
   - F_4 acts on R^26
   - E_6 has irreps in 27, 78
   - E_7 has irreps in 56, 133
   - E_8 has irreps in 248
   Of these dimensions, which are prime? In particular:
   - Is there an exceptional Lie group with a natural
     irreducible representation in d=11?
   - In d=13?
   - In d=17, 19, 23, ...?
   If the answer is "G_2 in d=7 is the unique smallest case,
   and no exceptional acts naturally in d=11 or d=13,"
   confirm this with citations.

5. Verdict on privilege:
   Synthesize sub-questions 1–4 into a single verdict:
   (a) Is d=7 PRIVILEGED — meaning, the conjunction of
       "exact Stark-unit SIC + exceptional Lie group natural
       action + (d-1)/d ceiling pattern" holds in d=7 but
       NOT in d=11, d=13, or other small primes?
   (b) Is d=7 GENERIC — meaning, this conjunction holds in
       multiple prime dimensions and our 6/7 result is one
       of many possible (d-1)/d analogues?
   (c) UNDERSPECIFIED — cannot determine from current literature.

Be conservative. Cite primary literature. If d=7 is
genuinely the smallest prime where all three structural
features (Stark-unit SIC, exceptional Lie action, (d-1)/d
ceiling) coexist, that is the answer I expect — but I want
you to verify it rather than confirm my prior.

Deliverable format:

Section 1 — SIC existence in d=11, d=13 (current status,
            constructions, references)
Section 2 — Stark-unit reach beyond d = n²+3 (which other
            dimensions are accessible, gap analysis)
Section 3 — (d-1)/d pattern in d=11, d=13 (does it appear?
            in what context?)
Section 4 — Exceptional Lie group prime dimensions
            (table of primes vs exceptional irreps)
Section 5 — Verdict (PRIVILEGED / GENERIC / UNDERSPECIFIED
            with reasoning)
```

---

## Notes for C-7RO when response comes back

**Decision tree:**

- **PRIVILEGED:** Paper 10 §5.5 framing is earned — keep it. Possibly even strengthen by adding the "no exceptional Lie group acts naturally in d=11 or d=13" observation as additional support for d=7's uniqueness.
- **GENERIC:** Rewrite §5.5 carefully. The unification claim weakens to "one example of a (d-1)/d pattern that may have analogues in other prime dimensions." Paper 10's main results (Theorem 1) are unaffected.
- **UNDERSPECIFIED:** Keep §5.5 conservatively framed. Add a footnote: "whether analogous patterns exist in d=11, d=13 is an open question."

**Likely outcome:** PRIVILEGED. The combination of (a) Stark-unit exact SIC, (b) exceptional Lie group natural action, (c) PSL(2,p) Klein-quartic-like covering, and (d) being a prime is genuinely rare — d=7 is the unique smallest case where all four hold. But verifying this with the literature is what makes Paper 10 §5.5 publishable rather than speculative.

**Side benefit:** Sub-question 4 (exceptional Lie group prime dimensions) might surface that d=11 has no exceptional structure but d=27 does (E_6's 27-dim rep is not prime, but interesting). This is the kind of observation that could seed a future paper or appendix.

---

## Lane status after sending

L6 → 🟡 IN PROGRESS — prompt sent, awaiting response.
