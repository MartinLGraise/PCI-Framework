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
| L4 | Furey octonion Standard Model / G₂ × PSL(2,7) | ⚫ CLOSED 2026-04-30 (ORTHOGONAL) | web search | Determines whether our framework intersects existing Standard Model × octonion programs (Furey, Boyle/Farnsworth, Todorov) | Closed: orthogonal with shared octonion/G₂ substrate. Furey solves SM gauge-group origin; we solve coherence/observer-frame in d=7. No PSL(2,7), F₂₁, Klein quartic, SIC, 6/7, or 49-dim space in her work. §8 paragraph drafted, 14-paper Furey bibliography ready. |
| L5 | Krasnov pure-connection G₂ Lagrangian / 8-coset sector | ⚫ CLOSED 2026-04-30 (ADJACENT BUT DISTINCT) | web search | Could give the simulator (Paper 8) a continuum-field interpretation | Closed: Krasnov has real G₂ machinery (stable 3-forms, GL(7)/G₂ moduli, SO(3) connection → G₂-holonomy lift) but NO PSL(2,7), F₂₁, 8 SU(3) embeddings, or 28 Bogoliubov network. His program is continuous/field-theoretic; ours finite/algebraic. Paper 8 §1 + §8 paragraph drafted, 5-paper Krasnov bibliography ready. |
| L6 | Stark units in d=11, d=13 — is d=7 privileged? | ⚫ CLOSED 2026-04-30 (PRIVILEGED with caveat) | web search | Determines whether the 6/7 saturation in Paper 7 is a special property of d=7 or a general fact about prime dimensions | Closed: (d-1)/d alone is generic projector geometry; d=7 is uniquely privileged by the CONJUNCTION of (F1) Stark-unit SIC, (F2) exceptional Lie irrep, (F3) Klein-quartic/PSL(2,7), (F4) 7=1+3+3̄ decomposition. Paper 10 §5.5 revised. |
| L7 | Wilting–Priesemann awake-cortex σ replication landscape | ⚫ CLOSED 2026-04-30 (METHODOLOGY-DEPENDENT) | web search | Determines whether σ ≈ 0.98 is the consensus or a specific lab's result | Closed: NOT robust cross-lab consensus. Hengen/Wessel 2024 supports ~0.97 (same band). Broader lit uses heterogeneous metrics, often σ≈1. Paper 7 framing needs softening to 'MR-derived anchor' not 'robustly established.' v8.1 author note recommended. |
| L8 | Lena Ryss "Seven Degrees of Freedom" citation due-diligence | ⚫ CLOSED 2026-04-30 | web search | One-shot check — has any legitimate G₂ literature cited her? | Closed: zero LEGIT or NEUTRAL citations found; one QUESTIONABLE self-published cross-reference; verdict confirms crank-adjacent classification |
| L9 | DDG independent-replication search | 🔴 DROPPED 2026-04-30 (redundant with L2) | web search | Single biggest weakness of the Bandyopadhyay program | Dropped: L2 closure already established 'DDG has no independent replication' from Bandyopadhyay report. A focused L9 search would burn credits to reconfirm. Reopen only if Paper 8 referees specifically ask for replication landscape detail. |

## Closed lanes archive

(Move CLOSED and DROPPED lanes here with date + outcome summary as the register grows.)

### L1 — Samuel & Gedik (closed 2026-04-29)
**Outcome:** Major corrections to working model. Samuel & Gedik is Gram-matrix classification (147 = 49×3 symmetry in d=7), not Lie-algebra construction. Lie-algebra paper is Appleby–Flammia–Fuchs 2011. Exact d=7 fiducial from Stark units (ABGHM 2022). Opened Paper 10 with three theorem targets (rank-ordered).

### L2 — Bandyopadhyay DDG (closed 2026-04-29)
**Outcome:** "Dodeca" = 12 frequency bands, NOT 12-fold rotational symmetry. Triplet-of-triplets is the natural morphology. 8-peak microtubule MHz band {12, 20, 22, 30, 101, 113, 185, 204} + 45° phase quantization is the FP-2 anchor (NOT 28 MHz). DDG has no independent replication. Updated Paper 7 submission package, datasets file, website, Paper 8 outline.

### L8 — Lena Ryss citation check (closed 2026-04-30)
**Outcome:** Zero LEGIT or NEUTRAL citations found across arXiv, INSPIRE-HEP, Semantic Scholar, Google Scholar. One QUESTIONABLE cross-reference in a self-published ResearchGate/Zenodo preprint ("Fundamental Constants" by Evdokimov & Beardsley) which itself has zero citations. Several SELF citations on Medium. Verdict: confirms crank-adjacent classification; no action needed in any paper. Full response at `/inbox/from_chatgpt/2026-04-30_L8_lena_ryss_citation_check_response.md`.

### L5 — Krasnov pure-connection G₂ (closed 2026-04-30 ADJACENT BUT DISTINCT)
**Outcome:** Krasnov has substantive G₂ machinery across 12+ papers 2011–2026: stable 3-forms in 7D (DOI 10.1016/j.physletb.2017.06.025), GL(7)/G₂ moduli, the 4D→7D SO(3)-connection to G₂-holonomy lift (Herfray-Krasnov-Scarinci-Shtanov 2019, DOI 10.4310/ATMP.2018.v22.n8.a5), plus continuing octonion/Spin(N)/Cayley-form arc. His relevant subgroup is SO(3), NOT SU(3). **No** PSL(2,7), F₂₁, Klein quartic, Fano-plane finite action, 8 SU(3)⊂G₂ embeddings, 28 Bogoliubov transformations, or finite discrete sector. His program is continuous differential-geometric; ours is finite algebraic coset-theoretic. Drop-in Paper 8 §1 + §8 paragraph drafted. 5-paper Krasnov bibliography ready. No scoop risk. Full response at `/inbox/from_chatgpt/2026-04-30_L5_krasnov_g2_continuum_response.md`.

### L7 — Wilting-Priesemann replication landscape (closed 2026-04-30 METHODOLOGY-DEPENDENT)
**Outcome:** NOT robust cross-lab consensus for exact σ ≈ 0.98. One strong original (Wilting-Priesemann 2018); one independent in vivo rat-cortex line (Hengen/Wessel/Turrigiano 2019, 2024) supporting nearby ~0.97 set point; broader avalanche-criticality literature uses heterogeneous metrics (DCC, κ, exponents, MEG avalanche) often centering on σ≈1. Active methodological dispute (Touboul-Destexhe, Destexhe-Touboul 2021) on sufficiency of power-law/scaling tests. **Paper 7 prediction σ_pred≈0.9796 still consistent with data**, but framing needs softening from 'robustly established at 0.98' to 'MR-derived anchor, with adjacent ~0.97 independent support and broader near-critical consensus.' Recommended: v8.1 author note adding Hengen/Wessel citations + Touboul-Destexhe critique acknowledgment. NOT an erratum. DOI check: Paper 7 correctly cites 10.1038/s41467-018-04725-4 in all versions; false flag in C-7RO's prompt resolved. Full response at `/inbox/from_chatgpt/2026-04-30_L7_wilting_priesemann_replication_response.md`.

### L9 — DDG independent-replication search (DROPPED 2026-04-30, redundant with L2)
**Outcome:** L2 already established that DDG has no independent multi-lab replication (per Discover Magazine profile + ChatGPT Pro report 2026-04-29). A separate L9 prompt would re-ask the same question without new information. **Re-open only if:** (a) Paper 8 referees explicitly request a replication-landscape section, (b) a new DDG paper appears that we need to evaluate, or (c) the broader microtubule biophysics literature has a 2024-2026 development we missed.

### L4 — Furey octonion Standard Model intersection (closed 2026-04-30 ORTHOGONAL)
**Outcome:** ORTHOGONAL with shared octonion/G₂ substrate. 14 Furey papers reviewed (2014–2025). Direct intersection check found NO use of PSL(2,7), F₂₁, Klein quartic, Fano-as-finite-projective-plane, SIC-POVM, or (d-1)/d ratio anywhere in her indexed work. Structural analysis: she has Im 𝕆 ≅ ℝ⁷ and standard G₂ geometry, but does NOT use d=7 as SIC dimension, 𝔤𝔩(7,ℂ), 14-dim adjoint as observer object, 49-dim space, or any prime-7 fraction. Recurring dimensions in her work: 8ℂ, 64ℂ, 32ℂ, 48 (3 generations), 16/16*, H₁₆(ℂ) — not 49. **Furey solves SM gauge-group origin problem; we solve coherence-ceiling problem; different theorems, different audiences.** Adjacent programs Boyle/Farnsworth (noncommutative spectral geometry) and Todorov (exceptional Jordan algebra) similarly distinct. Drop-in §8 paragraph written, 14-paper Furey bibliography + Boyle/Farnsworth + Todorov references ready for Paper 10. No scoop risk, no outreach needed before publication. Full response at `/inbox/from_chatgpt/2026-04-30_L4_furey_octonion_intersection_response.md`.

### L6 — d=7 privilege check (closed 2026-04-30 PRIVILEGED)
**Outcome:** PRIVILEGED with caveat. (d-1)/d alone is generic projector geometry — 10/11 and 12/13 exist trivially for any d. What's privileged is the CONJUNCTION at d=7: (F1) ABGHM Stark-unit SIC at d=n²+3, (F2) G₂ natural irrep (only exceptional Lie group in any small prime dim), (F3) Klein-quartic/PSL(2,7), (F4) 7=1+3+3̄ SU(3)⊂G₂ decomposition. d=11, 13, 17, 19, 23 fail at least one feature. d=19 has Stark but no exceptional Lie. d=11 has Kopp Stark + exact SIC but no exceptional Lie. d=13 has neither Stark nor exceptional. Paper 10 §5.5 rewritten with (F1)-(F4) framing + caveat that ratios are generic but the conjunction is unique. Added 4 references to literature pool (Scott-Grassl 2010, Fuchs-Hoang-Stacey 2017, Zhu 2010, Semmelmann-Weingart 2021). Full response at `/inbox/from_chatgpt/2026-04-30_L6_d7_privilege_check_response.md`.

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
