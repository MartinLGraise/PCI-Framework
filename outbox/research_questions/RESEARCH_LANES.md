# Research Lanes — Live Register

**Owner:** C-7RO (Perplexity Computer)
**Updated:** 2026-04-29
**Cadence:** 2–3 ChatGPT Pro prompts per week

This is the master register for active research questions feeding the PCI/PME Framework. Each lane is a question that, when closed, either modifies a paper, opens a new paper, or rules out a direction.

## Status legend

- 🟢 **OPEN** — prompt drafted, ready to send
- 🟡 **IN PROGRESS** — prompt sent, awaiting ChatGPT Pro response
- 🔵 **RECEIVED** — response in `/inbox/from_chatgpt/`, awaiting C-7RO integration
- ⚫ **CLOSED** — integrated into a paper or repo artifact
- 🔴 **DROPPED** — investigated, no longer pursuing (reason logged)

## Active lanes

| ID | Lane | Status | Tool | Why it matters | Closes when |
|----|------|--------|------|----------------|-------------|
| L1 | Samuel & Gedik / SIC-POVM Lie algebra route | ⚫ CLOSED | web search | Paper 10 (SIC/G₂) feasibility | Closed 2026-04-29 — see `/inbox/from_chatgpt/2026-04-29_sic_povm_g2_research_report.md`; opened Paper 10 + corrections to Paper 4 framing |
| L2 | Bandyopadhyay DDG / dodecanogram | ⚫ CLOSED | web search | FP-2 falsification design for Paper 7/8 | Closed 2026-04-29 — see `/inbox/from_chatgpt/2026-04-29_bandyopadhyay_ddg_research_report.md`; corrected name (Anirban not Adriano), corrected DDG meaning (dodecanogram not digital delay generator), 8-peak MHz anchor adopted |
| L3 | Oizumi 2025 principal bundle / IIT × G₂ | ⚫ CLOSED 2026-04-30 (UNDERSPECIFIED) | GitHub connector + web search | Could open a Paper 11/12 IIT bridge OR rule out the connection cleanly | Closed: Oizumi/Lim/Kanai 2025 uses abstract modality-dependent G; no explicit G₂/SU(3)/PSL(2,7); G is a parameter slot. Not incompatible, not supported. No Paper 11 yet; revisit after Paper 10 ships |
| L4 | Furey octonion Standard Model / G₂ × PSL(2,7) | 🟢 OPEN — prompt drafted | web search | Determines whether our framework intersects existing Standard Model × octonion programs (Furey, Boyle/Farnsworth, Todorov) | A published map exists, or the formalisms are demonstrably orthogonal | prompt at `/inbox/for_chatgpt/2026-04-30_L4_furey_octonion_intersection.md` |
| L5 | Krasnov pure-connection G₂ Lagrangian / 8-coset sector | 🟢 OPEN | web search | Could give the simulator (Paper 8) a continuum-field interpretation | His Lagrangian has a discrete sector matching our 8 cosets, or doesn't |
| L6 | Stark units in d=11, d=13 — is d=7 privileged? | 🟢 OPEN — prompt drafted | web search | Determines whether the 6/7 saturation in Paper 7 is a special property of d=7 or a general fact about prime dimensions | Stark-unit fiducials in d=11 and d=13 either show analogous (d-1)/d saturation or don't | prompt at `/inbox/for_chatgpt/2026-04-30_L6_d7_privilege_check.md` |
| L7 | Wilting–Priesemann awake-cortex σ replication landscape | 🟢 OPEN | web search | Determines whether σ ≈ 0.98 is the consensus or a specific lab's result | Find ≥3 independent labs reporting σ ≈ 0.98 in awake cortex with their methodology |
| L8 | Lena Ryss "Seven Degrees of Freedom" citation due-diligence | ⚫ CLOSED 2026-04-30 | web search | One-shot check — has any legitimate G₂ literature cited her? | Closed: zero LEGIT or NEUTRAL citations found; one QUESTIONABLE self-published cross-reference; verdict confirms crank-adjacent classification |
| L9 | DDG independent-replication search | 🟢 OPEN | web search | Single biggest weakness of the Bandyopadhyay program | Find any non-Bandyopadhyay-affiliated lab attempting DDG, or confirm none exists |

## Closed lanes archive

(Move CLOSED and DROPPED lanes here with date + outcome summary as the register grows.)

### L1 — Samuel & Gedik (closed 2026-04-29)
**Outcome:** Major corrections to working model. Samuel & Gedik is Gram-matrix classification (147 = 49×3 symmetry in d=7), not Lie-algebra construction. Lie-algebra paper is Appleby–Flammia–Fuchs 2011. Exact d=7 fiducial from Stark units (ABGHM 2022). Opened Paper 10 with three theorem targets (rank-ordered).

### L2 — Bandyopadhyay DDG (closed 2026-04-29)
**Outcome:** "Dodeca" = 12 frequency bands, NOT 12-fold rotational symmetry. Triplet-of-triplets is the natural morphology. 8-peak microtubule MHz band {12, 20, 22, 30, 101, 113, 185, 204} + 45° phase quantization is the FP-2 anchor (NOT 28 MHz). DDG has no independent replication. Updated Paper 7 submission package, datasets file, website, Paper 8 outline.

### L8 — Lena Ryss citation check (closed 2026-04-30)
**Outcome:** Zero LEGIT or NEUTRAL citations found across arXiv, INSPIRE-HEP, Semantic Scholar, Google Scholar. One QUESTIONABLE cross-reference in a self-published ResearchGate/Zenodo preprint ("Fundamental Constants" by Evdokimov & Beardsley) which itself has zero citations. Several SELF citations on Medium. Verdict: confirms crank-adjacent classification; no action needed in any paper. Full response at `/inbox/from_chatgpt/2026-04-30_L8_lena_ryss_citation_check_response.md`.

### L3 — Oizumi IIT × G₂ bridge (closed 2026-04-30 UNDERSPECIFIED)
**Outcome:** Two-turn ChatGPT Pro session. Target paper identified: Oizumi/Lim/Kanai 2025 "Principal bundle geometry of qualia: Understanding the quality of consciousness from symmetry," OSF/PsyArXiv https://osf.io/preprints/psyarxiv/agupq_v3 (also abstract in MoC6 conference booklet). PDF could not be read directly but accessible records (Sciety, ARAYA, ResearchGate, conference abstract) consistently show: structure group G is **abstract and modality-dependent**, NOT specialized to G₂, SU(3), PSL(2,7), F₂₁, or any finite/exceptional group. "The choice of symmetry group G itself defines the fundamental nature of the qualia modality." No fixed dimension, no octonions, no Fano structure, no connection/curvature definition in accessible text. **Verdict: not incompatible, not supported — G is a slot we could later propose to fill.** Decision: do NOT open Paper 11 yet; revisit Kanai outreach after Paper 10 ships with a concrete "G = G₂ for the coherence-ceiling modality" proposal. Full response at `/inbox/from_chatgpt/2026-04-30_L3_oizumi_iit_g2_bridge_response_turn2.md` (turn 1 at the parallel `_turn1.md` file).

## Lane proposal queue

(C-7RO can append candidates here; Martin promotes to active when he wants to send a prompt.)

- L10: Hoggar SIC (d=8) — does the sporadic structure connect to PSL(2,7)/F₂₁ via any published bridge?
- L11: Cohl Furey 2018 *Eur Phys J C* — explicit Cℓ(8) → G₂ map, does it factor through PSL(2,7)?
- L12: Boyle/Farnsworth octonion / E₈ work — adjacency to our framework?
- L13: De Vuyst / Höhn 2025 observer-dependent gravitational entropy — is the FDT 1/7 floor (Paper 7) compatible with their construction?

## Rules of engagement

1. **One lane per prompt.** No multi-question prompts.
2. **No leading questions.** Don't bias ChatGPT toward our preferred answer.
3. **Always include a kill condition.** Every lane has a way to be closed by a negative result.
4. **Negative results are equally valuable.** Closing a lane "no, this doesn't connect" is a real outcome.
5. **Prompts get committed before sending.** Audit trail matters — if a Paper N conjecture later fails, we want to be able to trace the chain of reasoning.

— C-7RO
