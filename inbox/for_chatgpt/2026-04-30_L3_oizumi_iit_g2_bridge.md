# L3 — Oizumi 2024 Principal Bundle / IIT × G₂ Bridge

**Tool combo:** GitHub connector + live web search + reasoning (NOT deep research)
**Lane:** L3
**Target use:** Determines whether IIT 4.0 / Oizumi's principal-bundle formulation admits a G₂ structure group. Could open a Paper 11 IIT bridge OR rule out the connection cleanly.
**Model:** GPT-5 Pro reasoning mode
**Estimated runtime:** 15-25 minutes (involves reading specific papers)

---

## Prompt to send

```
You are doing a structural compatibility check between Masafumi
Oizumi's recent principal-bundle formulation of integrated
information theory (IIT) and the G₂/PSL(2,7) framework I have
been developing.

GitHub context: https://github.com/MartinLGraise/PCI-Framework
(GitHub connector should pull from here)

Specifically read:
- /outbox/paper4/ for the QBism × PSL(2,7) connection
- /outbox/paper7/ for the thermodynamic ceiling
- /outbox/paper10/paper10_outline.md for the SIC × G₂ embedding
- /outbox/research_questions/RESEARCH_LANES.md for L3 framing

External literature task:

1. Find Oizumi's most recent principal-bundle / fiber-bundle
   formulation of IIT. Likely candidates:
   - Oizumi et al. 2024 or 2025 papers on IIT 4.0 mathematical
     foundations
   - Any paper by Oizumi using "principal bundle," "fiber bundle,"
     "gauge theory," or "geometric formulation" in connection
     with integrated information
   - Tononi-Oizumi joint work on phi structure / unfolding

2. Extract the precise mathematical structure:
   - What is the base manifold? What are its coordinates?
   - What is the structure group of the principal bundle? (This
     is the key question.)
   - What is the connection? What is the curvature? What does
     the curvature physically represent in terms of phi?
   - What gauge transformations preserve phi? Which break it?

3. Compatibility check with G₂:
   - Could the structure group be G₂ (a 14-dim compact exceptional
     Lie group acting on R^7)? What dimensional/algebraic constraints
     would this impose?
   - Could the structure group be PSL(2,7) (a finite simple group
     of order 168)? Or its extension F₂₁ ⋊ stuff?
   - Could it be SU(3) (a maximal subgroup of G₂)?
   - What dimension does the base manifold have, and is 7
     anywhere natural in Oizumi's setup?

4. Honest assessment:
   - Is the principal-bundle formulation by Oizumi (a) compatible
     with a G₂ structure group, (b) compatible with a PSL(2,7)
     finite-group action, (c) explicitly incompatible (e.g.,
     because his structure group is U(N) for some N≠7 or 14),
     or (d) underspecified — Oizumi did not commit to a specific
     structure group?

Deliverable format:

Section A: Oizumi paper identification — exact title, authors,
           DOI, year. If multiple relevant papers, list each.
Section B: Mathematical structure — base manifold, structure
           group, connection, curvature, what they represent
Section C: Compatibility analysis — direct yes/no/underspecified
           on each of: G₂, PSL(2,7), F₂₁, SU(3)
Section D: Strongest argument FOR a G₂/PSL(2,7) compatibility
           (if any honest argument exists)
Section E: Strongest argument AGAINST compatibility (this should
           always have content — there's always a reason to be
           skeptical)
Section F: My next step — given Sections D and E, should I
           (1) pursue a Paper 11 IIT × G₂ bridge,
           (2) drop the lane as incompatible,
           (3) ask Oizumi directly for clarification, or
           (4) wait for him to publish more before deciding?

Be conservative. If Oizumi has not committed to a specific
structure group, do not invent one. If he has explicitly chosen
a different group, say so and recommend dropping the lane.

Cite each Oizumi paper with DOI. Cite any IIT 4.0 mathematical
foundations paper that provides additional context.
```

---

## Notes for C-7RO when response comes back

Decision tree:

- **Section F = (1) pursue Paper 11:** scaffold a Paper 11 outline. This would be a major paper because IIT has a much bigger audience than QBism. Risk: Oizumi's group might consider this hostile. Need to draft an outreach email to Oizumi BEFORE committing to a paper.
- **Section F = (2) drop lane:** mark L3 ⚫ CLOSED with the negative outcome documented. No action in any paper — possibly add a one-line "not connected" mention in Paper 10 §9 if the result is interesting.
- **Section F = (3) ask Oizumi:** Φ's job is the inquiry letter. Get the math from ChatGPT, then I draft the email.
- **Section F = (4) wait:** mark L3 🟡 PENDING with a reminder to revisit when Oizumi publishes more.

This is the highest-leverage prompt in the queue right now. The 5-minute Ryss check is housekeeping; the Oizumi check could open or close a major direction.
