# Paper 12 H1 Council Synthesis — §5 v2 + §6 v1 (2026-05-06 ~12:45 PDT)

**Six reviews, two sections.** All come back at MINOR_REVISIONS or STRONG_ACCEPT. No section needs structural rework. Paper 12 body is council-cleared.

## Verdicts

| Section | Opus | GPT-5.5 | Gemini | Aggregate |
|---|---|---|---|---|
| §5 v2 | MINOR | MINOR | MINOR | **MINOR_REVISIONS** |
| §6 v1 | MINOR | MINOR | **STRONG_ACCEPT** | **MINOR_REVISIONS** |

Round 1 → Round 2 transitions for §5:

- Opus 4.7: MINOR → MINOR (held; all 4 RES items resolved; new MINOR on cross-reference labels)
- GPT-5.5: **MAJOR → MINOR** ✅ (Pillar-4 threading fix landed cleanly)
- Gemini: STRONG_ACCEPT → MINOR (small step down — minor citation precision items, see below)

§6 round 1 (first pass):

- Opus 4.7: MINOR (OP statements need slight sharpening; closing self-reference acceptable but could be downgraded)
- GPT-5.5: MINOR (close-architecture reordering — what's built first, what's open second)
- Gemini: STRONG_ACCEPT (no audit-flag violations; FTW boundary handled correctly)

## What's MINOR-residual in §5 v2

**Opus:**
- **RES-S5-v2-1**: Cross-reference labels in §5 say "§3 v3 / §4 v3" — for the assembled paper, these will become "§3 / §4" without version qualifiers. Convert.
- **RES-S5-v2-2**: P4 sample size — text says "n ≥ 60 collaborations" but the power calc derives n ≈ 50 *per arm*, which is 100 total. The "60" should clarify "60 per arm" or "60 per arm, 120 total."
- **All four original RES items (RES-A through RES-D)**: RESOLVED.

**GPT-5.5:**
- Top "Pillar-delivery signpost" should be removed or compressed (internal control material doesn't survive in final prose).
- Glossary box could expand slightly (1–2 more entries: $\Psi_\theta$ Schur coupling, $F_{21}$).
- P1/P2 community references ("BIOMA / A-Lab analogue", "BindCraft-style") are analogical; for v3 say "BIOMA-style automated science workflows" with at least one specific paper.
- §5.6's consolidating table is good; could add one column with quantitative falsification thresholds.

**Gemini:**
- Hyperscanning citations are correct, but BIOMA / BindCraft / Yang-Yu Virtual Lab citations need DOIs or arxiv IDs (currently informal).
- Souza 2022 multi-locus TMS citation: confirmed real, well-placed.
- No audit-flag violations.
- One scope note: §5.5's "Cohen's d = 0.4 between arms" assumes the audit-substrate effect is measurable at moderate magnitude — Gemini suggests this be stated as a pre-registered hypothesis in the actual study, not asserted as guaranteed.

## What's MINOR-residual in §6 v1

**Opus:**
- OP1–OP9 are well-stated overall; OP1 (non-Schur escape mechanism) could be sharpened to specify "construct a non-equivariant correction term η(x) of order θ² with property X" — currently slightly under-specified.
- §6.4 closing self-reference: acceptable but should be downgraded from "is an early instance of" to "exemplifies."
- §6.2 tables accurate; Paper 9 v1.3.3 / Paper 11 / Paper 13+ positioning correct.

**GPT-5.5:**
- Section flow should reorder: §6.1 contribution (currently §6.2) → §6.2 open problems (currently §6.1) → §6.3 scope → §6.4 close. *What's built first, then what's open.*
- Two tables in §6.2 are informative, not redundant — keep both.
- §6.4 closing reach: "the gradual tear applies to Paper 12's own development" is reaching; downgrade to "the framework's verification trail exemplifies the audit-substrate principle" without claiming the gradual-tear dynamics applies to its own writing.
- Pillar 4 absence in §6 is fine since §5.6 handles it; no need to re-recap.

**Gemini:**
- All 4 standing audit flags COMPLIANT in §6.
- FTW handling in OP9: correctly scoped as neighbor reference, not integrated.
- Clinical-PCI disambiguation maintained throughout §6.
- §6.4 ambitious closing: stays in scope, doesn't drift to metaphysics.
- §6.2 tables: accurate.
- Open-problem scope: HONEST across OP1–OP9.

## Path forward

Two flavors of polish are easy and obvious; they can wait or be batched into Phase 2:

**§5 v3 (~20 min):**
- Cross-reference label cleanup
- P4 sample-size clarification
- Top-of-section metadata compression
- Glossary box expansion
- Specific paper references for BIOMA/BindCraft/Yang-Yu

**§6 v2 (~25 min):**
- Section reorder: contribution → open problems → scope → close
- §6.4 self-reference downgrade
- OP1 sharpening

**Total ~45 min for full Phase-2 polish.**

This polish does *not* block §1+§2 drafting (H2). The MINOR residuals are paragraph-level, not architecture-level. We can either:
(i) run H2 (§1+§2) immediately and batch §5 v3 + §6 v2 into final assembly polish, OR
(ii) apply §5 v3 + §6 v2 polish first, then H2.

Recommendation: **(i) run H2 first** — momentum is here, the residuals don't block, and assembly will likely surface a few additional polish items anyway. Batch all polish at end.

---

*Six reviews stored at:*
- §5 v2: opus47_section5_v2 / gpt55_section5_v2 / gemini31pro_section5_v2
- §6 v1: opus47_section6 / gpt55_section6 / gemini31pro_section6
