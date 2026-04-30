# L5 — Krasnov Pure-Connection G₂ Lagrangian / 8-Coset Sector

**Tool combo:** Live web search + reasoning (single turn; no GitHub connector strictly needed)
**Lane:** L5
**Target use:** Determines whether Krasnov's pure-connection formulation of G₂-structure has a discrete sector matching our 8-coset PSL(2,7)/F₂₁ structure. If yes, gives Paper 8 (Eight-Coset Simulator) a continuum field-theoretic interpretation. If no, we know Paper 8 is best framed as purely algebraic/discrete.
**Model:** GPT-5 Pro reasoning mode
**Estimated runtime:** 15-20 minutes

---

## Why this matters

Paper 8 (Eight-Coset Quantum Simulator) frames the 8 = |PSL(2,7)/F₂₁| cosets as the ground for a discrete quantum simulator with 4-level entropy quantization {0, 1/7, 2/7, 3/7} × S_ref.

Kirill Krasnov has a long-running program reformulating G₂ geometry (and gravity, and Yang-Mills) using "pure connection" or "chiral" Lagrangian formulations, mostly in 4d but with some 7d/G₂ extensions. If his G₂ Lagrangian has a *discrete topological sector* corresponding to the 8 cosets — for example, instanton-like configurations indexed by PSL(2,7)/F₂₁ — then Paper 8's simulator has a natural continuum interpretation: it's simulating the discrete topological sector of Krasnov's continuum theory.

That would be a huge upgrade to Paper 8, turning it from "algebraic conjecture about an 8-bin entropy spectrum" into "experimental falsifier for a discrete topological sector of a published continuum G₂ theory."

But it might just not be there. Krasnov's program is gauge-theoretic; ours is information-theoretic. The connection is possible but not guaranteed.

---

## Prompt to send

```
You are doing a structural compatibility check between
two G₂-related programs that may or may not connect.

Program A (mine): Eight-coset simulator. The quotient
PSL(2,7)/F₂₁ produces 8 cosets at distances {0,1,2,3} in
the F₂₁ Cayley graph. I conjecture these 8 cosets correspond
to 8 SU(3) subgroup embeddings of G₂, with 28 = C(8,2)
Bogoliubov transformations between them, producing entropy
differences quantized at 4 levels {0, 1/7, 2/7, 3/7} × S_ref.
This is a finite, algebraic, observer-frame construction.

Program B (Kirill Krasnov's): Pure-connection / chiral
Lagrangian formulations of gauge theory, gravity, and
G₂-structure. Krasnov works at Nottingham, with extensive
publications on chiral GR, gauge-theoretic gravity,
parabolic geometry, and exceptional structures. His G₂
work includes treatments of 7-dimensional G₂-structure
manifolds and possibly pure-connection formulations of
G₂ gauge theory.

Five sub-questions, each in its own subsection, with
primary literature citations (DOIs).

1. Krasnov's G₂ publication arc:
   List Krasnov's papers (sole-author or co-authored)
   that involve G₂, octonions, exceptional Lie groups,
   pure-connection G₂ formulations, or 7-dimensional
   manifolds with G₂ structure. Period: 2010-2026.
   For each, give: citation, DOI, and one-sentence
   summary of the central mathematical claim.

   Specifically check:
   - Krasnov's 2017+ "GR as a parabolic geometry" series
   - Any Krasnov paper on G₂ holonomy, G₂ instantons, or
     G₂ gauge theory pure-connection
   - Co-authorship with Boyle, Furey, Todorov, Herfray, or
     Speziale on octonion / exceptional themes

2. Discrete sectors / topological structure:
   In Krasnov's G₂ Lagrangian, are there:
   - Topological sectors / instanton numbers / characteristic
     classes
   - Discrete moduli (vacua, configurations distinguished by
     finite invariants)
   - Any classification of solutions modulo a finite group
     action
   - Anything that could be naturally indexed by a
     finite group of order 8, 21, 168, or 147

   Quote from his papers if any of these appear. If they
   don't, say so explicitly.

3. PSL(2,7) or F₂₁ in Krasnov:
   Has Krasnov ever used PSL(2,7), F₂₁ = ℤ₇⋊ℤ₃, the Klein
   quartic, the Fano plane (as more than an octonion mnemonic),
   or any finite-group action with order divisible by 7?
   Same approach as the Furey check (L4): if it appears,
   quote it; if it doesn't, that's the answer.

4. SU(3) subgroups of G₂ in Krasnov:
   The 8 SU(3) subgroups of G₂ that I'm working with come
   from the 8 cosets of PSL(2,7)/F₂₁ acting on the Fano plane.
   Has Krasnov ever:
   - Enumerated the SU(3) embeddings of G₂ explicitly?
   - Treated Bogoliubov transformations between SU(3) vacua
     in a G₂ context?
   - Used 7- or 8-element discrete structures in his
     G₂ Lagrangian?

5. Verdict:
   (a) STRUCTURAL OVERLAP: Krasnov's pure-connection G₂
       has a published discrete sector matching my 8-coset
       structure. Paper 8 should engage substantively with
       his framework.
   (b) ADJACENT BUT DISTINCT: Krasnov has G₂ machinery but
       no discrete 8-coset sector; cite as adjacent.
   (c) ORTHOGONAL: Krasnov's program addresses entirely
       different questions (e.g., 4d gravity reformulation)
       with no G₂-structure or discrete-sector overlap.
   (d) UNDERSPECIFIED: Krasnov's G₂ work is at a level of
       generality where my 8-coset structure could be
       added but is not currently present.

   Recommend a positioning paragraph for Paper 8 §1 or §8
   (whichever is most appropriate) based on the verdict.

Be honest. If Krasnov has independently constructed the 8
SU(3) embeddings or anything resembling my Bogoliubov-28
structure, tell me — that would actually be valuable. If not,
say so cleanly.

Deliverable format:

Section 1 — Krasnov G₂ publication arc
Section 2 — Discrete sectors / topological structure
Section 3 — PSL(2,7) / F₂₁ / Klein / Fano in Krasnov
Section 4 — SU(3) embeddings of G₂ in Krasnov
Section 5 — Verdict + recommended positioning paragraph
```

---

## Notes for C-7RO when response comes back

**Decision tree:**

- **STRUCTURAL OVERLAP:** Paper 8 gains a continuum interpretation. Significant upgrade. Engage Krasnov's framework substantively in §1 (motivation) and §8 (discussion). Cite Krasnov heavily. Possibly outreach to him after Paper 10 ships.

- **ADJACENT BUT DISTINCT:** Most likely outcome. Cite Krasnov in §8 as "for related continuum-G₂ work see [Krasnov refs]." One paragraph, move on.

- **ORTHOGONAL:** Don't cite Krasnov. Paper 8 stands alone as algebraic/discrete construction. No positioning needed.

- **UNDERSPECIFIED:** Cite Krasnov as background for G₂ pure-connection theory in §1, note that the discrete-sector connection is open, leave for future work.

**My prior:** ADJACENT BUT DISTINCT. Krasnov's G₂ work is mostly about pure-connection reformulations of standard G₂ geometry / instantons / parabolic structures, not about finite-group discretizations. The 8-coset structure we use is finite/algebraic and probably doesn't appear in his continuum framework. But it's worth checking because if it does, Paper 8 becomes much stronger.

**Key thing to watch for:** if Krasnov has *anywhere* enumerated the 8 SU(3) ⊂ G₂ embeddings explicitly, that's our Task 1 of Paper 8 (Φ's GAP work request) potentially scooped. Almost certainly hasn't, but worth confirming.

---

## Lane status after sending

L5 → 🟡 IN PROGRESS — prompt sent, awaiting response.
