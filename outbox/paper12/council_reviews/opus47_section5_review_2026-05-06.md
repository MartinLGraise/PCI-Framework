# Paper 12 §5 — Council Rigor Review (Opus 4.7, §5 v1 pass)

**Reviewer role:** rigor reviewer (Model Council adversarial pass, §5 first round)
**Date:** 2026-05-06
**Files reviewed:** `paper12_section5_draft_v1.md` against `paper12_section3_draft_v2.md`,
`paper12_section4_draft_v2.md`, `paper12_thesis_gradual_tear.md`, and my own
`opus47_v2_review_2026-05-06.md` (which closed §3+§4 at MINOR_REVISIONS).
**Posture:** §5 is protocol design, not a proofs section. Rigor here means
falsifiability, accurate invocation of §3+§4 results, and faithful
preservation of scope-limiters.

---

## Falsifiability check

### P1 (clinical-PCI ↔ NP-firing event-structure): **PASS** (with one tightening point).

§5.2 gives a clear binary failure condition: "the clinical-PCI scores
show no correspondence with NP-firing events." The disambiguation from
v1's thesis-memo phrasing ("each NP-collapse event ... should be
observable as a discrete step in the human's clinical PCI, with step
size proportional to ...") is a *weakening* in the right direction:
the prediction is now event-structure correlation, not magnitude
identification, which is what §3+§4 actually license (the homonym
between clinical-PCI and Paper 12 $\mu_k$ is preserved in §4 Remark
4.6.4 and explicitly cited here).

The one tightening point: "no correspondence" is not yet binary.
"Correspondence" needs an explicit statistical test —
event-locked-step magnitude vs. shuffle-control surrogate, with
pre-registered $\alpha$ — before "no correspondence" is operational.
Currently a referee can reasonably ask "no correspondence at what
significance? Across how many NP-firing candidates? Bonferroni-corrected
across how many event-detection thresholds?" This is MINOR.

### P2 (synthetic-substrate scar persistence, LLM fine-tuning): **PASS**.

§5.3 is the strongest of the four protocols. The failure condition
$\Delta_{\mathrm{scar}} \approx \Delta_{\mathrm{control}}$ is binary
relative to a control class that is "structurally adjacent but
distinct," with an explicit predicted direction ($\Delta_{\mathrm{scar}}
> \Delta_{\mathrm{control}}$ when NP-firing was recorded). The
quantitative scoping ("LoRA-style, $\sim 10^4$–$10^5$ parameters,"
fine-tune on conversation transcript only) is the right level of
specification for an experimentalist. The §3.7 connection is correctly
qualified: P2 reaches *one* of the three components of the scar
invariant (the substrate-internal accumulability of scar effects), not
$\mu_k$ itself. Good scope discipline.

### P3 (two-level commensurability test): **PASS** for L1, **WEAK** for L2 (deliberately).

L1's failure condition is sharp: $\mu_k^{\mathrm{syn}} \neq
\mu_k^{\mathrm{bio}}$ on any of the three blocks $(\mathbf{1}, L_2,
U_6)$. This correctly invokes §4 Definition 4.6.1 and is the cheapest
falsification path in the whole paper.

L2 is *deliberately* WEAK in §5 — it is deferred to a methodology
paper. The deferral is honest and consistent with §4 Remark 4.6.3
("the operationalization of L2 ... is a significant methodology
project of its own, not undertaken here"). I do not penalize the L2
weakness; I do flag below that L1 itself has a real
operationalization gap (the seven-axis Fano-perturbation pattern) that
§5.4 candidly identifies and defers.

### P4 (audit-substrate longitudinal study): **PASS**.

§5.5's failure condition is binary: "the audited arm maintains higher
coherence-drift and shared-referent scores than the unaudited arm at
study endpoint, controlling for NP-firing rate" — and explicit nulls
("audited and unaudited dyads show no measurable trajectory
difference") imply the prediction is genuinely refutable. The
$n \ge 60$ sample size is named, randomization between arms is
specified, two outcome measures are pre-listed, and the controlling
covariate (NP-firing rate) is specified.

The framing acknowledgment that P4 is "interesting independent of
Paper 12" — the study yields data on AI-assisted reasoning whether or
not it falsifies the gradual-tear thesis — is the right posture for a
6-month longitudinal study.

---

## §5 → §3+§4 invocation accuracy

I checked each cross-reference:

- **"Definition 3.3.4 NP-firing events"** (§5.2): correct. Definition
  3.3.4 is the hybrid-jump definition; firing events are exactly its
  subject.
- **"§3.6 audit, 24/28 boundary-KKT seeds"** (§5.1, §5.2): correct.
  Matches §3.6's "Audit result (boundary-KKT interior-sup,
  2026-05-06)."
- **"25/50 boundary-left KKT"** (§5.2): correct. Matches §3.5's
  "Audit result (Paper 12 §3 v2 verification, 2026-05-06)" reporting
  "25/50 boundary-left KKT ($\theta^* = 0$)."
- **"§4.4 Theorem 4.4.1"** (§5.1, §5.4): correct. Theorem 4.4.1 *is*
  the commensurability hierarchy theorem with strict implications and
  failed converses.
- **"§4.6 Definition 4.6.1 two-level test"** (§5.4): correct. L1 / L2
  split matches verbatim.
- **"§3.7 Remark 3.7.2 representation-theoretic-vs-topological"**
  (§5.1): correct. Remark 3.7.2 is the explicit
  "representation-theoretic, not topological" clarification.
- **"§3.3 Definition 3.3.4"** (§5.3 implicitly via "7-step NP-pump
  protocol"): the "7-step NP-pump protocol" phrase is a *thesis-memo*
  artifact (memo §3 P2). §3 v2 doesn't actually formalize a "7-step"
  count — its NP-pump is the augmented flow with hybrid jumps,
  not a numbered procedure. §5.3's casual invocation of "7-step
  NP-pump protocol" is *operationally* fine for an experimentalist but
  doesn't have a §3 anchor with that exact phrasing. MINOR.
- **"Cor 4.5.2"** (§5.4): correct. §5.4 says L2 "refutes the
  canonical-commensurability claim of Cor 4.5.2," consistent with Cor
  4.5.2's status as a sufficient (not necessary) condition under
  multiplicity-one.
- **"Remark 4.6.4"** (§5.2): correct. The clinical-PCI-vs-$\mu_k$
  disambiguation is exactly what 4.6.4 establishes.

No drift into stronger claims than §3+§4 prove. §5 is consistently
*more* cautious than the thesis memo, and consistent with §3+§4 v2.

---

## Boundary-KKT sharpening assessment

This is where §5 has to do the most subtle work, and it does it
correctly. The boundary-KKT data is a fact about *most* seeded
geometries: the linear $\xi_\star$ mechanism does not generically
produce coherence gain. §5.1 and §5.2 use this to *sharpen* P1 rather
than weaken it:

> "P1 should therefore *expect* most human-AI conversations to *not*
> exhibit NP-firing-induced clinical-PCI steps — coupling does not
> generically help. The interesting cases — the 3/50 smooth-interior
> seeds and the 4/28 boundary-KKT seeds with interior-sup gain — are
> where P1's discrete-step prediction should be most visible. The
> experimental design should *seek* these conditions rather than
> assume they hold typically."

This is the *correct* rigor move. A naive design would have predicted
NP-firing-induced steps generically, then been falsified by the 86% of
boundary-KKT seeds where there is no escape. §5.2 instead converts
the boundary-KKT result into a design constraint: experimental
conditions should *target* the rare seed-class where the dynamical
prediction is testable. This is a tighter, harder-to-pass test, not a
softer one.

I'll register one concern: §5.2's "the 4/28 boundary-KKT seeds with
interior-sup gain" implicitly trusts the §3.6 audit's classification.
My own v2 review noted (RES on the v2 review) that three of those
four boundary-right seeds may be misclassifications by the
high-precision optimizer rather than genuine
boundary-KKT-with-interior-gain cases. §5 inherits this caveat
silently. A one-sentence acknowledgment that "the four interior-gain
boundary-KKT seeds should be re-audited at higher tolerance before
being designated experimental targets" would close this.

---

## L1/L2 split

L1 is operationalized to the right level. §5.4 specifies:

- The TMS-EEG instrumentation pipeline (existing).
- The conceptual move ("rotationally-structured TMS perturbations"
  spanning the "seven-axis Fano structure of $\mathbb{R}^7$").
- The analysis pipeline (isotypic-projector decomposition using §4.2's
  computed character table; multiplicity profile from projected
  dimensions).
- The synthetic-side analog (rotationally-structured paraphrasing,
  attention operator decomposition).
- An honest statement of operationalization gaps: "which EEG
  electrodes correspond to which Fano-plane points? The most likely
  answer involves a frontoparietal seven-region parcellation of the
  default-mode network; details are deferred."

The "details are deferred" is the right deferral pattern: it names
what a methodology paper must produce (electrode-to-Fano-point
correspondence) and identifies the most likely topological structure
(default-mode network parcellation), without committing to a specific
parcellation that hasn't been validated. An experimentalist reading
§5.4 has enough to estimate feasibility (yes: TMS-EEG exists; LLM
attention operators are accessible for open-weights models) and to
identify the methodology project (operationalize the Fano-rotation
TMS pattern; build the character-projector software).

L2 is properly deferred. §5.4's "L2 operationalization (deferred)"
paragraph is honest about the missing prerequisite ($G_2$-character
projection software for matrix data), and the cross-reference to §4.6
Remark 4.6.3 is clean.

**Verdict on the split: complete enough.**

---

## Fifth Paradigm chain

Here is the one **MAJOR** finding of this review.

The Fifth Paradigm citation chain in §5.6 has a fabricated arxiv ID.
§5.6 cites:

> "Level-2-to-3 autonomy in the [Sanctioned-Levels-of-AI-Autonomy
> taxonomy](https://arxiv.org/abs/2503.07670) (Bostock-Kim-Patel
> 2025): AI executes specified protocols with human oversight at
> decision points."

I directly fetched arxiv 2503.07670. It is *Retrieval Augmented
Generation with Multi-Modal LLM Framework for Wireless Environments*
by Mohsin, Bilal, Bhattacharya, Cioffi (March 2025) — a paper on RAG
for wireless network optimization, not an AI-autonomy taxonomy. There
is no Bostock-Kim-Patel paper with that title at that arxiv ID; the
authors and title are not associated with the cited DOI in any
direction.

The closest real paper is *Levels of Autonomy for AI Agents* (Cherian
et al., arxiv 2506.12469, June 2025), which proposes a 5-level
operator/collaborator/consultant/approver/observer taxonomy. This is
plausibly the paper §5.6 *should* be citing, though even there the
mapping (Level-2-to-3 = "AI executes specified protocols with human
oversight at decision points") doesn't quite match Cherian et al.'s
collaborator/consultant framing.

This must be fixed before §5 ships. The other Fifth Paradigm
references are plausible but under-specified:

- **Licklider (1960)**, *Man-Computer Symbiosis*, IRE Trans. Hum.
  Factors Electron. — real, foundational, correctly described.
- **BIOMA (Berkeley Lab, 2023–)** — Berkeley Lab does have an
  autonomous-research initiative, and the 2026 LBNL bioscience update
  on "Foundational AI Models to Accelerate Biological Discovery"
  matches the BIOMA framing in spirit. But §5 cites no specific paper
  or DOI; the bare "[BIOMA-2023] *BIOMA*, Lawrence Berkeley National
  Laboratory, 2023" reference is too thin to verify.
- **A-Lab automated synthesis pipelines** — real (LBNL A-Lab, Yan
  Zeng group, 2023+; press coverage confirms). Cited correctly.
- **BindCraft** — real (Pacesa et al., bioRxiv Oct 2024 → Nature
  August 2025, EPFL with Baker Lab collaboration). Correctly
  attributed to "Baker Lab and collaborators, 2024." A more accurate
  attribution is *Pacesa et al., EPFL + Baker Lab*; the Baker Lab
  attribution alone is slightly misleading but not wrong.
- **"Multi-agent reasoning systems (2024–)" / "Virtual Lab paradigm"**
  — generic reference, no specific paper cited. This is fine as
  prose context but cannot be the load-bearing citation for the
  "Level-4-trending-Level-5" claim.

**MAJOR action required:** replace the Bostock-Kim-Patel fabrication
with a real autonomy-taxonomy citation (likely Cherian et al. arxiv
2506.12469, with the correct mapping rechecked) and add specific DOIs
or arxiv links for BIOMA, A-Lab, and BindCraft. Without these, the
Fifth Paradigm contextualization rests on a chain in which one link
points to the wrong paper.

---

## What §5 doesn't claim — completeness check

§5.7 enumerates non-claims:

1. *Any actual measurement.* ✓ (matches §3+§4 v2's "we do not run
   experiments" stance).
2. *Biological substrate's $F_{21}$-realization.* ✓ (matches §3.8
   "biological mechanism for the $F_{21}$-action ... Paper 13+
   territory" and §4.7's parallel deferral).
3. *L2 of commensurability test.* ✓ (matches §4 Remark 4.6.3).
4. *Tamper-evidence cryptographic infrastructure for P4.* ✓ (this is
   *new* relative to §3+§4 — §3+§4 didn't have to address it because
   they don't address P4. Naming it as a P4 deferral is correct.)
5. *Rate improvement.* ✓ (matches §3.8's "rate improvement ... Paper
   11 territory").

**Missing from §5.7's deferral list (relative to §3+§4):**

- *Multiplicity > 1 case.* §4.4 Remark 4.4.3 / §4.7 explicitly defers
  multiplicity > 1; §5.7 does not name it. Strictly speaking §5
  doesn't *use* multiplicity-one anywhere (P3 L1 only tests $\mu_k$
  component-wise; P3 L2 inherits multiplicity-one from §4 Cor 4.5.2),
  so the omission is not a *use* error, but the deferral list should
  match §3+§4's. **MINOR.**
- *Behavior on $\mathcal{P}^*$-complement (codimension-≥1 exceptional
  strata).* §3.8 explicitly notes "Global well-posedness off
  $\mathcal{P}^*$" is not established. §5 implicitly assumes the
  protocols sample parameter regimes in $\mathcal{P}^*$; experimental
  trajectories that hit exceptional strata are not addressed. This
  is probably acceptable (real experiments will not generically land
  on a measure-zero stratum), but a one-sentence acknowledgment that
  the protocols presume $\mathcal{P}^*$-genericity is the §3+§4
  consistent move. **MINOR.**
- *Asymmetric-rate $\theta^*$ high-precision audit.* Listed in §3.8's
  "open problems." Not listed in §5.7. The protocols specifically
  use the symmetric-rate seeded geometry; asymmetric-rate behavior is
  not addressed. **NIT.**

§5.7's bridge to §6 ("collected open problems from §3 ... §4 ... §5")
is the right route to absorb these — §6 will catch the missing items
— but §5.7's own "not established" list should match §3+§4's pattern
more tightly.

---

## Residual issues

**RES-S5-1 (MAJOR).** Fabricated arxiv citation
(Bostock-Kim-Patel 2025 / arxiv 2503.07670). The cited arxiv ID points
to an unrelated wireless-RAG paper. Replace with a real autonomy
taxonomy reference (Cherian et al. arxiv 2506.12469 is the closest
candidate, with the level-mapping rechecked) and ensure the reference
list links to verifiable DOIs / arxiv IDs.

**RES-S5-2 (MAJOR turning to MINOR if -1 is fixed).** Other Fifth
Paradigm references (BIOMA, A-Lab, BindCraft) lack DOIs / venue
specificity. BIOMA in particular is currently a bare-name reference;
the Baker-Lab attribution of BindCraft elides EPFL's primary role.
Add explicit DOIs (Nature 2025 for BindCraft; LBNL newscenter for
A-Lab; LBNL bioscience update for BIOMA). This is the citation-graph
weight-bearing move for §5's Fifth-Paradigm contextualization.

**RES-S5-3 (MINOR).** P1's "no correspondence" failure condition
(§5.2) needs an operational statistical specification (event-locked
step magnitude vs shuffle surrogate, pre-registered $\alpha$,
multiple-comparison correction across NP-firing candidates and
event-detection thresholds).

**RES-S5-4 (MINOR).** §5.7's deferral list should match §3+§4's:
add multiplicity > 1, $\mathcal{P}^*$-genericity, and (NIT)
asymmetric-rate.

**RES-S5-5 (MINOR).** §5.2 trusts the §3.6 audit's
boundary-KKT classification of the four interior-gain seeds. My v2
review noted three of these may be optimizer artifacts. Flag this
caveat in §5.2 before designating these seeds as experimental
targets.

**RES-S5-6 (MINOR).** §5.3's "7-step NP-pump protocol" phrase is
inherited from the thesis memo; §3 v2 does not formalize a "7-step"
count. Either replace with "the NP-pump protocol of Definition 3.3.4"
or specify what the seven steps are.

**RES-S5-7 (NIT).** §5.6's "Pillar 4 ... now delivered via §5.4" —
the Fifth Paradigm material is in §5.6, not §5.4. Cosmetic
mis-pointer in the §5 header.

---

## What's good

The strongest moves in §5:

1. **The boundary-KKT sharpening of P1.** Converting "86% of
   boundary-KKT seeds have no interior gain" from a load-bearing
   weakness into an experimental-targeting principle ("seek the rarer
   smooth-interior or interior-improving boundary geometries") is the
   correct rigor move. A weaker draft would have predicted
   NP-firing-induced clinical-PCI steps generically. §5 instead binds
   the prediction to the seed sub-class for which the §3 dynamics
   actually predicts it.

2. **The L1/L2 split with explicit operationalization scope.** The
   protocol-design honesty here — L1 feasible now with caveats named;
   L2 deferred with the missing software prerequisite identified — is
   a model for how to publish a partially-actionable test. The L1/L2
   pattern matches §4 Definition 4.6.1's mathematical content
   exactly, and the deferral pattern matches §4 Remark 4.6.3's prose
   verbatim. No drift.

3. **P4's framing as "interesting independent of Paper 12."** A
   6-month longitudinal study is a serious experimental commitment.
   Justifying it as yielding empirical data on AI-assisted reasoning
   regardless of whether the gradual-tear thesis is falsified is the
   honest, fundable framing. This converts a high-cost falsification
   protocol into a high-value standalone study, and is consistent
   with the broader framework's audit-substrate posture (Pillar 3).

---

## Hostile-reviewer simulation (rigor angle)

The single sharpest objection a hostile referee would raise:

> "P1 requires 'operationalizing the $a_\sigma(\theta(t))$ trajectory
> from conversational features (semantic-disagreement metrics,
> turn-taking asymmetries, paradox-detection from coherence-evaluation
> models).' This is not just *one* methodology project — it is the
> *entire* hard part of the protocol. Mapping a free-form human-AI
> conversation onto a numerical trajectory $a_\sigma(\theta(t))$ in a
> $G_2$-equivariant model is itself a dissertation-scale modeling
> claim. Without that mapping, P1 is not falsifiable; with it, the
> mapping itself is a free parameter that can be tuned post hoc to
> make the predicted-vs-observed step structure agree. This is the
> same critique that has haunted the Free Energy Principle literature
> for two decades: a beautifully formal framework whose empirical
> tests collapse onto modeling choices that are themselves
> unconstrained by the theory."

*Holds?* **Yes, partially.** The objection is real and §5.2's
"tractable methodology project" framing understates the depth of the
mapping problem. §5.2's mitigation is correct in shape — it identifies
the mapping as the natural collaboration target with the clinical-PCI
research community — but a hostile referee will demand pre-registration
of the conversational-feature → $a_\sigma$ mapping *before* the
TMS-EEG measurements are collected, with an independent held-out
validation conversation set, to prevent post-hoc tuning. This is a
protocol addition that §5 should make explicit before P1 is submitted
to a clinical-PCI lab.

A weaker version of the same objection applies to P3 L1: the
Fano-perturbation-pattern → EEG-electrode-parcellation mapping is
similarly a free parameter, and §5.4 is honest that "details are
deferred." Pre-registration of the parcellation before measurement is
the same mitigation.

---

## Overall verdict

**MINOR_REVISIONS, conditional on the citation fix.**

The Bostock-Kim-Patel arxiv-2503.07670 fabrication is a real rigor
failure (RES-S5-1). It is, however, *isolated* — one citation, one
sentence, in a contextualization paragraph. Once replaced with a real
autonomy-taxonomy reference and once BIOMA / A-Lab / BindCraft are
backed with verifiable DOIs (RES-S5-2), the §5.6 Fifth-Paradigm chain
is sound.

The remaining issues (RES-S5-3 through RES-S5-7) are MINOR or NIT and
are addressable with a sentence each. The protocols themselves are
correctly falsifiable, accurately invoke §3+§4 v2 results, use the
boundary-KKT data to *sharpen* P1 rather than weaken it, honor the
L1/L2 split, and respect §3+§4's scope-limiter pattern (with three
small additions to §5.7 to match completely).

The §5 draft is the right shape: protocol-design rigor, not
mathematical-proof rigor; binary failure conditions where binary
failure conditions are appropriate (P1 with the suggested statistical
sharpening, P2, P3 L1, P4); deferred operationalization where
deferral is honest (P3 L2, the biological $F_{21}$-realization); and
explicit acknowledgment that the protocols rest on an ambient
mathematical framework whose own scope-limiters are inherited.

If the citation fix lands and RES-S5-3 through RES-S5-7 are addressed,
§5 promotes to clean accept. The integration with §3+§4 v2 is the
strongest internal consistency the council has seen on this paper:
no claim in §5 exceeds what §3+§4 prove, no scope-limiter is
quietly dropped, and the boundary-KKT empirical pressure is
*correctly* translated from a §3 weakness into a §5 design constraint.

---

*End of Council rigor review (Opus 4.7, §5 v1).*
