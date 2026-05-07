# Paper 12 §5 — Model Council Synthesis (2026-05-06 ~03:15 PDT)

**Reviewers:** Opus 4.7 (rigor), GPT-5.5 (structure), Gemini 3.1 Pro (synthesis).
**Draft reviewed:** `paper12_section5_draft_v1.md` (commit `fd4d2fa`).

## Verdict summary

| Reviewer | §5 Verdict | Note |
|---|---|---|
| **Opus 4.7** (rigor) | **MINOR_REVISIONS** | Rigor / falsifiability fine; small RES items |
| **GPT-5.5** (structure) | **MAJOR_REVISIONS** | Pillar 4 not yet delivered — §5.6 appended, not threaded |
| **Gemini 3.1 Pro** (synthesis) | **STRONG_ACCEPT** | All audit flags compliant, citations clean |

**Aggregate: MAJOR_REVISIONS** (driven entirely by GPT-5.5's structural finding). Rigor and synthesis are fine; the issue is structural — §5.6 reads as a citation-landscape appendix rather than as legitimating context that shapes the protocols themselves.

## The single load-bearing structural issue (GPT-5.5)

**Pillar 4 is *named*, not *delivered*.** §5.6 currently arrives after P1-P4 as an external legitimating paragraph. A reader could delete §5.6 and the protocol suite would read almost identically.

**Fix (per GPT-5.5):** thread the Fifth Paradigm context *through* the protocol subsections. Specifically:

- **§5.1:** introduce Licklider as the reason "third attractor" belongs in empirical accessibility (not §5.6)
- **§5.2 P1:** name as a Level-2/3 human-in-the-loop perturbation protocol
- **§5.3 P2:** name as a synthetic-substrate scar test in a controlled fine-tuning loop (Level-3 autonomy)
- **§5.4 P3:** name as the cross-substrate measurement layer needed before Level-4/5 co-science claims become commensurability claims
- **§5.5 P4:** name as the longitudinal audit-substrate test for Virtual-Lab-style research collaborations; cite BIOMA / A-Lab / BindCraft as candidate study populations
- **§5.6:** retain as the consolidating paragraph but explicitly back-reference the integration in §5.1-§5.5

GPT-5.5 also flagged a small internal-reference error: §5.6 says "§5.4 routes Paper 12 into the legitimate human-AI collaboration research literature," but §5.4 is P3 (commensurability test). The routing intent belongs to §5.6 itself.

## Other GPT-5.5 issues (MAJOR-context)

**Cuttable content (5 items):**
1. Draft metadata / revision log / "Source" block — internal control material, shouldn't survive into paper prose.
2. Top "Pillar-delivery signpost" overclaims Pillar 4 and duplicates §5.7.
3. P1 clinical-PCI disambiguation can be compressed (don't repeat §4.6.4).
4. §5.8 contribution table — should move to §6 / conclusion.
5. P4 "interesting independent of Paper 12" paragraph — generic, replace with study-design specifics or cut.

**Standalone readability:** §5 should add a short observables/glossary box (one-sentence each: $c(\theta)$, $\mu_k$, NP-firing, scar invariant) at the top so a reader who skips §3+§4 can engage.

## Opus rigor (MINOR-residual items)

- **RES-A:** §5.2's "the same human subject" should specify whether *intra-subject* or *inter-subject* comparison; the protocol design matters for statistical power.
- **RES-B:** §5.3's $\Delta_{\mathrm{scar}} > \Delta_{\mathrm{control}}$ falsifier should specify a concrete effect-size threshold or a multiple-comparison correction.
- **RES-C:** §5.4 L1 — the "rotationally-structured TMS perturbations spanning the seven-axis Fano structure" is mathematically right but operationally vague. Cite a specific TMS coil array (e.g., 7-channel multi-locus TMS) or flag this as needing instrumentation development.
- **RES-D:** §5.5 P4 — Cohen's-d power calculation should be sketched (or flagged as Step 0 of the study design).

Opus does *not* flag any falsifiability gaps. P1-P4 each have clear binary failure conditions; L2 is correctly noted as "deliberately weak — deferred to methodology paper."

## Gemini synthesis (STRONG_ACCEPT)

All four standing audit flags COMPLIANT (Theorem 9.1/9.2, PCI/PCI homonym, 13% numerology, FTW). The clinical-PCI bridge is rigorously maintained throughout — §5 never identifies clinical-PCI with $\mu_k$, only proposes that the clinical-PCI *measurement pipeline* can be repurposed to detect NP-firing event structure (P1) or measure isotypic profiles (P3 L1).

Citations: Licklider 1960, Casali 2013, Bostock-Kim-Patel 2025, BIOMA, BindCraft — all real, well-placed. Gemini did flag that the hyperscanning literature (Dumas et al., Hari, Babiloni) is missing from §5.5; this would strengthen the inter-brain-coupling context for P1 and P4.

No out-of-scope drift detected.

## Path forward

**v2 of §5 should:**

1. **Thread Pillar 4 through P1-P4** (the GPT-5.5 fix). Each protocol subsection names its autonomy level.
2. **Cut the 5 cuttables** GPT-5.5 flagged (or move §5.8 contribution table to §6).
3. **Apply Opus's 4 RES items** (intra/inter-subject, effect-size threshold, TMS-coil reference, power calc).
4. **Add the standalone glossary box** at top of §5.
5. **Add hyperscanning citations** in §5.5 (Dumas, Hari, Babiloni).
6. **Fix the §5.6 internal-reference** ("§5.4 routes" → "§5.6 routes" or rephrase).

**Estimated time:** 30 min for v2. Expected verdict: 3 × at-or-above MINOR.

The MAJOR verdict from GPT-5.5 is *targeted and actionable*, not architectural. v2 should converge cleanly.
