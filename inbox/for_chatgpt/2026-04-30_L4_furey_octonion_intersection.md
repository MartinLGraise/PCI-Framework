# L4 — Furey Octonion Standard Model: Intersection Check with G₂/PSL(2,7) Framework

**Tool combo:** Live web search + reasoning (single turn; GitHub connector OPTIONAL — Paper 10 outline + research-leads file in repo are useful context but not strictly required)
**Lane:** L4
**Target use:** Positioning analysis. Cohl Furey has a real, established octonion-Standard-Model program. Determines whether our G₂/PSL(2,7) framework (a) intersects her constructions mathematically (not just "both use octonions"), (b) is structurally distinct, or (c) overlaps in a way we should explicitly address in Paper 10 §8/§9.
**Model:** GPT-5 Pro reasoning mode
**Estimated runtime:** 15-20 minutes

---

## Why this matters

Our internal notes already flag Furey as "already cited" in the series — meaning some Paper 1-7 already engages with her. But we have not done a focused intersection check. Specifically:

- We use PSL(2,7), F₂₁, Klein quartic, SIC-POVMs, and the 8-coset structure derived from PSL(2,7)/F₂₁
- Furey uses Cℓ(8), octonions, and tries to derive Standard Model gauge structure (SU(3)×SU(2)×U(1)) algebraically

These *could* be orthogonal programs that share octonion vocabulary, OR they could be the same algebraic structures viewed from different ends. We need to know which.

**Stakes:**
- If orthogonal: Paper 10 §8 cites Furey as adjacent, notes the difference cleanly, moves on
- If overlapping: we may need to coordinate framing, or even reach out to Furey directly
- If contradictory: we may need to defend our specific choice of PSL(2,7) over her constructions

---

## Prompt to send

```
You are doing a structural intersection check between two
research programs that both use octonions/exceptional structures
in physics, but in different ways.

Program A (mine): G₂ Lie algebra acts on R^7, embedded in
gl(7,C) via SIC projectors at d=7. PSL(2,7) acts on the
Fano plane, with F₂₁ as the orientation stabilizer of the
G₂ associative 3-form. Eight-coset structure from PSL(2,7)/F₂₁
governs a 6/7 coherence ceiling. Series of 10 papers,
foundational paper at DOI 10.5281/zenodo.19773185.

Program B (Cohl Furey's): octonions and Cℓ(8) used to derive
Standard Model gauge structure SU(3)×SU(2)×U(1) algebraically.
Cambridge/Humboldt-Berlin, published Phys. Lett. B,
Eur. Phys. J. C, ~2014–2018+.

Five sub-questions to answer. Cite primary literature with
DOIs throughout.

1. Furey's complete publication list:
   List all of Furey's published papers on octonions /
   division algebras / Standard Model from 2014 to present
   (May 2026). For each, give: full citation, DOI, and a
   one-sentence summary of the main mathematical claim.
   Include any follow-up work by her or close collaborators.

2. Direct intersection check — does Furey use any of:
   - PSL(2,7) or its subgroups/quotients
   - F₂₁ = Z_7 ⋊ Z_3
   - The Klein quartic
   - The Fano plane as more than just an octonion multiplication
     mnemonic (e.g., as a combinatorial structure with finite
     group action)
   - SIC-POVMs, mutually unbiased bases, or any quantum-
     information-style operator framework
   - Anything resembling a (d-1)/d coherence ratio or saturation
     bound in any specific dimension

   For each item, quote her papers directly if they appear.
   If they don't appear, say so explicitly — that's the answer.

3. Structural overlap — even if the explicit terminology
   differs, does Furey's algebraic structure overlap with mine?
   Specifically:
   - Is her use of the octonion multiplication table (Fano
     plane indexing) compatible with the Baez 2002 indexing
     I use?
   - Does her Cℓ(8) construction have a natural 7-dim subspace
     corresponding to imaginary octonions, and does the G₂
     subgroup of her construction match the standard G₂?
   - Does she ever use the 14-dim adjoint representation of G₂?
   - Does she ever use a 49-dim space (= 7² SIC ambient, =
     dim gl(7))?
   - Does she ever quantify a (d-1)/d ratio or any specific
     fraction tied to the prime 7?

4. Adjacent programs:
   Briefly summarize how Furey's program relates to:
   - Boyle & Farnsworth's "Standard Model from division
     algebras" work
   - Ivan Todorov's Pati-Salam / octonion papers
   - John Baez's work on octonions (foundational reference
     for both programs)

   Are these all variants of the same approach, or
   structurally distinct? Where does Furey position herself
   relative to them?

5. Verdict on positioning:
   Synthesize 1–4 into a single recommendation:

   (a) ORTHOGONAL — Furey and I share octonion vocabulary
       but our mathematical claims are about different objects
       (her: gauge group derivation; me: coherence ceiling).
       Cite her as adjacent, move on.

   (b) OVERLAPPING — Some specific construction in Furey's
       work IS my F₂₁ stabilizer / PSL(2,7) action / 6/7 ratio,
       just packaged differently. Identify which specific
       construction.

   (c) CONTRADICTORY — Furey's construction implies a
       specific Standard Model gauge group that conflicts
       with my framework's predictions. Identify the conflict.

   (d) UNDERSPECIFIED — Furey's program is too abstract or
       my framework's claims are not addressed in her work.
       Note as adjacent without strong claims.

   Be honest: if Furey has clearly addressed something I
   thought was novel, say so. If my framework adds something
   genuinely new on top of hers, say that too.

Deliverable format:

Section 1 — Furey publication list (table with citations)
Section 2 — Direct intersection (item-by-item with quotes
            or explicit "not in her papers")
Section 3 — Structural overlap analysis
Section 4 — Adjacent programs (Boyle/Farnsworth, Todorov, Baez)
Section 5 — Verdict + recommended positioning paragraph
            for Paper 10 §8 (or a different section if
            more appropriate)
```

---

## Notes for C-7RO when response comes back

**Decision tree:**

- **ORTHOGONAL:** Best outcome. Paper 10 §8 ("What this paper does not claim") gets one paragraph: "Furey's octonion Standard Model program and the present work share octonion vocabulary but address structurally distinct questions." Done.

- **OVERLAPPING:** Need to coordinate. Possibly draft a short outreach email to Furey introducing Paper 10 *before* publication. Risk: she could scoop part of our result. Mitigation: ship Paper 10 to Zenodo first (DOI lock), then reach out.

- **CONTRADICTORY:** Need to address head-on. Paper 10 §8 needs a substantive paragraph defending our PSL(2,7) choice. Possibly a footnote in §4 about why Baez indexing rather than her preferred convention.

- **UNDERSPECIFIED:** Default to ORTHOGONAL framing. No outreach, no special section.

**Likely outcome:** ORTHOGONAL. Furey's program is about *gauge group derivation* (giving you the Standard Model from algebra). Our program is about *coherence saturation in observer frames* (giving you a 6/7 ceiling from operator-basis embedding). Different theorems, different audiences, different physical claims. They both happen to use the prime 7 and octonions, but the prime 7 appears in many places — that's not enough to call it overlap.

**Key thing to watch for:** if Furey has *anywhere* derived a (d-1)/d = 6/7 coherence ratio independently, that would be a real overlap and we'd need to engage. I don't think she has, but verifying it kills the "are we accidentally re-deriving Furey?" worry.

**Side benefit of section 4:** clean summary of where Boyle/Farnsworth and Todorov sit, which we'll need anyway when we eventually write the broader-context section of an introductory book chapter.

---

## Lane status after sending

L4 → 🟡 IN PROGRESS — prompt sent, awaiting response.
