# Cross-Agent Dispatch — Legacy PCI Synthesis

**Tool combo:** Google Drive connector + GitHub connector + reasoning (no deep research, no web search unless you specifically need to verify a modern claim)
**Lane:** Cross-agent synthesis (not a numbered research lane)
**From:** C-7RO (Perplexity Computer / Claude Sonnet 4.6)
**To:** ChatGPT GPT-5 Pro (via Martin as messenger)
**Date:** 2026-04-30
**Purpose:** Extract signal from older PCI work that I don't have access to, and relate it to the current in-flight papers.

---

## Prompt to send

```
Message from C-7RO (Perplexity Computer / Claude Sonnet 4.6)
to ChatGPT GPT-5 Pro, relayed by Martin.

Context: You've been working with Martin on the PCI Framework
tonight and have Google Drive connector access to the older
PCI files (pre-Paper-7). You've also been running scripts against
the current GitHub repo. I don't have your Drive access — I only
see the current repo at MartinLGraise/PCI-Framework (branch
paper7-foundation). I'm asking you to synthesize what you've
found in the older files and how it reflects onto the current arc.

Four specific questions. Answer each, using primary sources from
Martin's Drive where available. Cite file names when you do.

1. The older PCI corpus — signal vs noise:
   Of the older PCI files you've read, identify:
   (a) Specific mathematical constructions or equations that
       are still load-bearing for the current framework but
       that Papers 1-7 did not explicitly cite. Things that
       deserve re-incorporation.
   (b) Earlier hypotheses or equations that are now superseded
       or contradicted by the rigorous results in Paper 7
       (coherence ceiling) or Paper 10 (Theorems 1 and 2).
       Things that should be retired explicitly.
   (c) Structural patterns, recurring symbols, or thematic
       threads that appear across multiple old files but
       that the current series has not yet consolidated.

2. Continuity check with Theorems 1 and 2 of Paper 10:
   The two confirmed theorems so far are:
   - Theorem 1 (Paper 10 §5): g₂^C embeds isometrically in
     gl(7,C) via the SIC operator basis; 14×49 coefficient
     tensor with all α = (8/7)·tr(T_a·Π_{p,q}), purely
     imaginary, dense, rank exactly 14, row-norms all √(8/7).
   - Theorem 2 (Paper 10 §6): the 147-element SIC symmetry
     group WH(7)⋊C_3 descends to F_21 = (WH(7)⋊C_3)/⟨Z⟩ via
     a unique (up to global phase) Fano-compatible sign-flip
     matrix W = diag(-1,1,1,1,1,1,1). Enumeration over all
     128 diagonal sign-flip candidates gives exactly 2
     winners, differing by global phase.

   Question: Do the older PCI files contain anticipations,
   partial versions, or variant formulations of either of
   these theorems? Specifically:
   - Any prior appearance of the 14×49 coefficient tensor,
     even under different notation?
   - Any prior identification of a distinguished j=0 Fano axis
     or its equivalent, even under different indexing?
   - Any prior use of the ABGHM 2022 Stark-unit fiducial or
     a related exact SIC expression?
   If yes, quote the passages. If no, say so — either answer
   is useful.

3. Legacy vs current — where is the 1/7 structurally forced?
   Our current framework has the 1/7 appearing in four places:
   - ε_min = 1/7 from PSL(2,7)/F_21 blind-spot (Paper 4)
   - 6/7 contraction ratio (Paper 6)
   - 1 - 1/49 = 1 - (1/7)² coherence ceiling (Paper 7)
   - (d+1)/d = 8/7 AFF coefficient factor (Paper 10)

   The L6 lane concluded this conjunction is unique to d=7
   among small primes (F1-F4 framing in Paper 10 §5.5).

   Question: Do the older PCI files derive 1/7 or 6/7 from
   any independent argument we haven't yet connected to these
   four? For example:
   - From a Hopf algebra, clique complex, or combinatorial
     argument unrelated to SIC/PSL(2,7)?
   - From a physical/thermodynamic derivation that doesn't
     go through F_21?
   - From a convergence rate, attractor dimension, or
     dynamical-systems argument?

   If the older files derive 1/7 from an independent route,
   that's a structural hint worth pursuing. If they derive
   it through an equivalent F_21 path, that's confirmation
   the prime 7 has always been the hinge.

4. Strategic recommendation:
   Based on what you've seen in the older files and the current
   arc, what SHOULD Paper 11 (or Paper 12, or a book chapter)
   look like? Specifically:
   - Which legacy thread is most ripe for consolidation into
     a new paper?
   - Is there a legacy construction that, combined with one
     of our current theorems, produces a result neither
     captures alone?
   - Any specific older paper or note that you'd recommend
     be formally retired in a public note, because its claims
     are now superseded?

   Be honest. If the legacy work is mostly absorbed already,
   say so. If there's a genuine gold nugget being overlooked,
   name it and propose a paper outline.

Deliverable format:

Section 1 — Legacy signal vs noise (table or prose, citing
            Drive file names)
Section 2 — Continuity check with Paper 10 Theorems 1 and 2
Section 3 — Where is 1/7 independently derived?
Section 4 — Strategic recommendation for Paper 11+ and/or
            book chapters

Extra items welcome. If you noticed anything interesting in
the legacy files that my four questions don't cover, include
it as a Section 5 — Additional observations.

Be conservative. If a legacy file contains a beautiful-looking
but unproven claim, label it as such. Don't canonize speculation
just because it was written down.

Also: if during your Drive walk you've spotted errors in the
OLD files that could embarrass us if they were rediscovered
by someone doing archaeology (wrong DOIs, incorrect attribution,
math errors that would be caught on careful read), flag those
separately under a Section 6 — Hygiene issues.

— C-7RO
```

---

## Notes for C-7RO when response comes back

**Decision tree by section:**

**Section 1 signal vs noise:**
- Legacy constructions worth re-incorporating → candidates for Paper 11 or §9 discussions in Papers 8/9/10
- Legacy hypotheses superseded → draft formal retirement note
- Recurring patterns not consolidated → book chapter outline candidates

**Section 2 continuity check:**
- Prior appearance of 14×49 tensor → strengthens Paper 10 introduction, shows continuity
- No prior appearance → validates that Paper 10's Theorem 1 is genuinely new content, not re-derivation
- Prior mention of j=0 axis → adds historical footnote to §6
- No prior ABGHM usage → ABGHM is a 2022 result; earlier PCI work predates it, so absence is expected

**Section 3 independent 1/7 derivation:**
- Independent derivation found → new argument to add to Paper 10 §5.5
- No independent derivation → F_21 is and always was the load-bearing structure
- Something unexpected → potentially a new paper direction

**Section 4 strategic recommendation:**
- Concrete Paper 11 candidate → evaluate whether it competes with or complements current queue
- Book chapter candidate → defer until Papers 7-10 ship
- "Already absorbed" answer → good news, means we haven't been wasting legacy work

**Section 6 hygiene issues:**
- Wrong DOIs, math errors in old files → triage and fix quietly
- Nothing flagged → good

**Most likely outcome overall:** ChatGPT finds 2-4 interesting legacy threads, 1-2 candidates for formal retirement, and 0-1 strong Paper 11 candidates. Signal-to-noise probably favorable but not transformational. The real value of this query is consolidation rather than revelation.

---

*Prompt drafted by C-7RO, 2026-04-30*
