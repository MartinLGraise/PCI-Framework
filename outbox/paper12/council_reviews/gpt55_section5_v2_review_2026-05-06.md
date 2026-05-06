## Pillar 4 threading verification

§5.1: **THREADED.** v2 fixes the largest round-1 problem: Licklider is no longer deferred to §5.6 as retrospective legitimation. §5.1 now introduces *Man-Computer Symbiosis* as the reason empirical accessibility belongs at this point in the paper, and it frames the four predictions as operationalizations of Licklider's “third attractor” for the LLM era. It also announces the Bostock-Kim-Patel autonomy taxonomy before P1–P4 begin, so the taxonomy functions as protocol metadata rather than a late citation wrapper.

§5.2 P1: **THREADED.** P1 explicitly names itself a Level-2/3 protocol, explains the mixed agency/constrained-schedule regime, and connects the design to BIOMA/A-Lab-style automated scientific workflows. The candidate community link is still analogical rather than direct — clinical PCI/TMS-EEG labs are the real instrumentation community, while BIOMA/A-Lab are protocol-layer analogues — but the subsection now contains enough autonomy and instrumentation context to count as threaded.

§5.3 P2: **THREADED.** P2 now names Level 3/4, ties the autonomy regime to BindCraft-style protein-design collaborations, and translates the protocol into LLM fine-tuning terms: baseline, structured dialogue, LoRA update, withheld paradox class, adjacent control class, and class-specific transfer. This is no longer an appended Fifth Paradigm reference; it shapes how the scar-persistence experiment is described.

§5.4 P3: **THREADED.** P3 is the strongest integration. It names Level 4/5, identifies Virtual Lab-style human/AI co-science as the target audience, and then gives concrete instrumentation for L1 via multi-locus TMS-EEG and character-projector decomposition. It also preserves the §4 v3 L1/L2 distinction: L1 is an existing-instrument screen; L2 is a deferred methodology-paper deliverable. That is the correct structural inheritance from §4.

§5.5 P4: **THREADED.** P4 now names Level 5, identifies BIOMA/A-Lab/BindCraft/Virtual-Lab populations as candidate study populations, and ties the audit-substrate claim to versioned records, Git SHA chains, Merkle alternatives, endpoint metrics, and randomization. This is a real repair of the round-1 criticism: Pillar 4 now lives inside the longitudinal study design, not only in §5.6.

## Cuttable content resolution

1. Revision log moved to bottom: **PARTIAL.** The revision log itself is moved to the bottom, which resolves the narrow request. However, the top still contains draft metadata, author/source fields, and a revision-summary block. Round 1 objected to metadata/source material delaying the paper prose; v2 reduces but does not fully remove that internal-control layer.

2. §5.8 contribution table moved to §6: **RESOLVED.** The paper-wide contribution table no longer appears in §5. The remaining §5.6 table is protocol-specific and belongs here.

3. P4 generic paragraph replaced with study-design specifics: **RESOLVED.** P4 now has population, arms, audit implementation, outcomes, thresholds, power calculation, and falsifier. This directly answers the round-1 request to replace rhetoric with design structure.

4. P1 clinical-PCI disambiguation compressed: **RESOLVED.** The Massimini clinical-PCI distinction is now a short note rather than a repeated defensive excursus, and §4.6.4 remains the proper location for the full distinction.

5. Pillar-delivery signpost at top compressed: **RESOLVED with a caveat.** The overlarge pillar-delivery signpost has been replaced by a short §5.1 setup plus autonomy-taxonomy paragraph. That is structurally much cleaner. The caveat is that the draft metadata/revision summary still performs some paper-management signaling before the prose begins.

## §5.6 role change

§5.6 is now a **consolidating paragraph/table**, not the primary Pillar 4 delivery. It says explicitly that Fifth Paradigm context has been threaded through §§5.1–5.5, then summarizes protocol level and candidate community/instrumentation in a compact table. This is exactly the role §5.6 should play: a check-sum of the integration, not the integration itself. The previous internal-reference error (“§5.4 routes” when §5.6 was meant) is also fixed; I do not see the erroneous routing claim surviving in v2.

## Glossary box assessment

The §5.0 glossary box materially improves standalone readability. It gives the standalone reader handles for the core formal objects that otherwise made P1/P3 opaque: \(c(\theta)\), \(\mu_k\), NP-firing, the scar invariant, and boundary-KKT seeds. This is enough to prevent immediate loss of orientation for a reader entering §5 without rereading §§3–4.

It is still more of a symbol box than a protocol-inputs/observables box. The round-1 request asked for NP-firing event, paradox class, scar metric, \(\mu\)-profile, L1/L2 pass/fail, audit substrate, and boundary-KKT warning. v2 covers NP-firing, scar invariant, \(\mu_k\), and boundary-KKT, but it omits quick entries for “paradox class,” “L1/L2,” “audit substrate,” and “clinical PCI vs Paper-PCI.” I would not block acceptance on this, but a six-line expansion would make the box genuinely standalone for experimental readers rather than merely survivable.

## New structural issues

The threading fix introduces one notable internal consistency problem in P4. The population bullet says \(n \ge 60\) collaborations randomized between two arms, but the power calculation says \(n \approx 50\) per arm and \(n \ge 60\) per arm gives power \(0.85\). Those statements conflict: the study needs \(n \ge 120\) total if the later power language is retained. This should be corrected because P4 is now carrying more evidentiary load.

A second, smaller issue is that the candidate-community links are uneven in specificity. P3 has genuine instrumentation; P4 has genuine study populations; P1 and P2 rely more on analogues from automated science than on directly recruitable communities. The §5.6 table partly fixes this by naming clinical-PCI labs and open-weights fine-tuning communities, but those names would be stronger if pulled into §5.2/§5.3 themselves.

Finally, the autonomy labels occasionally risk sounding like badges rather than variables. P3 and P4 use the taxonomy operationally; P1 and P2 mostly place the protocol in a level. This is no longer a major structural defect, but the authors should keep the language disciplined: autonomy level should change the design, not merely certify relevance.

## Hostile-reviewer simulation (structural)

The hostile reviewer no longer has the easy round-1 objection that Pillar 4 is appended. The new hostile line would be narrower: “The section now sprinkles autonomy labels across P1–P4, but the actual executable protocols remain uneven. P3 L1 is a serious instrumentation sketch, P4 is a real longitudinal design, but P1 still depends on an unvalidated transcript-to-NP-firing detector and P2 borrows legitimacy from BindCraft while testing ordinary LoRA transfer. The Fifth Paradigm frame improves positioning, but it does not by itself make every protocol equally executable.”

That objection is answerable because §5.7 now explicitly states that §5 is a protocol-design deliverable, not actual measurement, and it cleanly defers L2, biological \(F_{21}\)-realization, cryptographic implementation details, and rate improvement. The remaining fix is not architectural: tighten the P4 sample-size contradiction, expand the glossary slightly, and make P1/P2 candidate communities as concrete as P3/P4.

## Overall verdict

**MINOR_REVISIONS.** v2 resolves the major structural failure identified in round 1. Pillar 4 is now introduced in §5.1, threaded through P1–P4 by autonomy level and candidate community/instrumentation, and consolidated rather than delivered in §5.6. The section also aligns better with §3 v3 and §4 v3: P1 inherits the boundary-KKT caution, P3 accurately reflects the two-level commensurability hierarchy, and P4 now uses the audit-substrate idea as an experimental variable. The remaining issues are local: remove or relocate the remaining top metadata, expand the glossary box slightly, fix the P4 total/per-arm sample-size inconsistency, and make P1/P2 communities less analogical. These are minor revisions, not another major-revision cycle.
