# Paper 12 §5 v2 — Council Rigor Review (Opus 4.7, second pass)

**Reviewer role:** rigor reviewer (Model Council adversarial pass, §5 v2)
**Date:** 2026-05-06
**Files reviewed:** `paper12_section5_draft_v2.md` against
`paper12_section3_draft_v3.md`, `paper12_section4_draft_v3.md`, my own
round-1 review (`opus47_section5_review_2026-05-06.md`), and the
synthesis (`COUNCIL_SECTION5_SYNTHESIS_2026-05-06.md`).
**Round-1 verdict:** MINOR_REVISIONS conditional on the citation fix.

---

## RES-A through RES-D verification

### RES-A (intra/inter-subject design): **RESOLVED.**

§5.2 Protocol step 1 now reads: "Run an *intra-subject* pre-post
conversation design (one human subject across multiple paired sessions,
statistical power higher than inter-subject); $n = 12$–$24$ subjects,
each in $\ge 6$ paired sessions." This is exactly what RES-A asked
for: the design ambiguity is named, the choice is made (intra-subject),
the rationale (statistical power) is given, and the cluster size
($\ge 6$ paired sessions per subject) is specified. Clean fix.

### RES-B (effect-size threshold): **RESOLVED.**

§5.3 P2's falsifier is now: "$\Delta_{\mathrm{scar}} -
\Delta_{\mathrm{control}} > 0.05$ (5 percentage-point class-specific
gain) at $p < 0.01$ across $\ge 30$ seed conversations, with Bonferroni
correction." This converts the previous shape-only $\Delta_{\mathrm{scar}}
> \Delta_{\mathrm{control}}$ into a concrete numeric threshold (5pp),
significance level ($p < 0.01$), sample bound ($\ge 30$), and
multiple-comparison correction (Bonferroni). All four of the components
RES-B asked for are present.

A small further sharpening would be welcome: 5pp on what baseline?
A 5pp gain over a 50% baseline is a 10% relative improvement; a 5pp
gain over a 90% baseline is 50% of remaining headroom. But naming
the threshold as an absolute accuracy delta is conventional in LLM
fine-tuning evaluation and an experimentalist will read it correctly.

### RES-C (TMS-coil reference): **RESOLVED.**

§5.4 L1 step 1 now cites: "a 7-channel multi-locus TMS array (e.g.,
the [multi-locus TMS system, Souza et al. 2022](https://doi.org/10.1016/j.brs.2021.11.017))
provides direct access to the seven-axis perturbation space." It also
provides the fallback ("If such an array is unavailable, single-coil
multi-target serial stimulation with co-registered E-field modeling is
a feasible substitute"). This is the right pattern: a real
instrumentation reference plus a degraded-mode fallback when the
multi-locus instrument is not available. Clean fix.

(I note: I have not independently verified the Souza et al. DOI 10.1016/j.brs.2021.11.017
points to a multi-locus TMS paper. The author should confirm the DOI
maps to the right title before final submission. This is a check, not
a flag.)

### RES-D (Cohen's $d$ power calculation): **RESOLVED.**

§5.5 P4 now contains: "For Cohen's $d = 0.4$ between arms (moderate
effect), $\alpha = 0.05$, $\beta = 0.2$, two-tailed comparison
requires $n \approx 50$ per arm; $n \ge 60$ per arm provides power
of $0.85$." All four power-calculation parameters are named, the
target effect size is justified ("moderate"), and the chosen $n \ge
60$ is over-powered relative to the minimum, which is the right
direction. Clean fix.

---

## Falsifiability re-check

### P1 — clinical-PCI ↔ NP-firing event-structure: **PASS** (upgraded from PASS-with-tightening in round 1).

§5.2's falsifier now reads: "Cohen's $d$ on the difference between
pre-firing and post-firing clinical-PCI scores ... if $d < 0.2$ (no
effect) at $\alpha = 0.05$ corrected for multiple comparisons across
firings, P1 is falsified." This addresses my round-1 RES-S5-3 directly:
the failure condition is now binary, statistically operationalized, and
multiple-comparison-corrected. The "no correspondence" wording from v1
is gone.

### P2 — synthetic-substrate scar persistence: **PASS** (sharpened from round 1).

The numerical threshold + significance level + sample size + Bonferroni
correction (see RES-B) makes P2 the most operationally precise of the
four protocols. This was already PASS in v1; v2 makes it sharper still.

### P3 L1 — isotypic-multiplicity match: **PASS.**

§5.4: "$\mu_k^{\mathrm{syn}} \ne \mu_k^{\mathrm{bio}}$ on any of the
three blocks" remains the cheapest falsification path in the paper.
The L1 measurement protocol now has a specific instrumentation citation
(RES-C), which makes "feasible with existing instrumentation" credible.
L2 remains correctly deferred (Remark 4.6.3 in §4 v3).

### P4 — audit-substrate longitudinal study: **PASS.**

§5.5's binary falsifier ("Cohen's $d < 0.2$, $p > 0.05$ Bonferroni-
corrected" between arms) plus the explicit power calc gives this
protocol a proper experimental footing. The two outcome measures
(semantic-coherence drift threshold $\cos\sigma < 0.4$; shared-referent
maintenance $\ge 70\%$) are operationally specific. PASS.

All four protocols PASS. This is an improvement from v1 where P1 was
PASS-with-tightening.

---

## Citations to §3 + §4 v3

I re-checked each cross-reference against §3 v3 and §4 v3:

- **Definition 3.3.4** (NP-firing) — present in §3 v3 (line 209,
  "Hybrid jump at firing events"). **OK.**
- **Definition 3.3.2** (augmented flow) — present in §3 v3 (line 180).
  **OK.**
- **§3.5.1, §3.6** (boundary-KKT) — §3.5.1 is now Definition 3.5.1
  (stratified critical point); §3.6 is "Audit result (boundary-KKT
  interior-sup)." Both present in v3. **OK.**
- **§3.7** ($\mathfrak{J}_k$ scar invariant) — present in §3 v3.
  **OK.**
- **Theorem 4.4.1** (commensurability hierarchy) — present in §4 v3
  (line 273), now labeled "v2 reformulation" but still numbered 4.4.1.
  **OK.**
- **Definition 4.6.1** (two-level test) — present in §4 v3 (line 419).
  **OK.**
- **Remark 4.6.3** (L2 deferral) — present in §4 v3 (line 445).
  **OK.**
- **Remark 4.6.4** (clinical-PCI vs $\mu_k$) — present in §4 v3 (line
  455). **OK.**
- **Cor 4.5.2** — present in §4 v3 (now downgraded from biconditional
  to sufficient, per the v2→v3 reformulation). §5 v2 doesn't cite it
  by name, only invokes its content via "L2 ... canonical
  commensurability." **OK** (§5 doesn't claim the converse anywhere).
- **§4.2 character table** — present in §4 v3, used by L1 protocol
  step 3. **OK.**

The audit numbers cited in §5 v2 (25/50 boundary-left KKT, 24/28
boundary-KKT, 3/50 smooth-interior, 4/28 interior-sup gain) match
§3 v3 lines 403, 471–488 verbatim.

**One staleness flag:** §5 v2's *Cross-references* section at the
bottom (lines 358–360) still reads "Paper 12 §3 **v2**" and "Paper 12
§4 **v2**." These should be updated to "v3." This is a label-only
issue — the actual numbered citations all resolve correctly against
v3 — but it should be fixed in the final pass.

---

## Residual issues

**RES-S5-v2-1 (MAJOR — inherited, unaddressed).** The Bostock-Kim-Patel
arxiv 2503.07670 citation is **still present in v2** (lines 56, 275,
334), unchanged from v1. My round-1 review explicitly marked this as
MAJOR with the directive: "Replace with a real autonomy taxonomy
reference (Cherian et al. arxiv 2506.12469 is the closest candidate).
… Without these, the Fifth Paradigm contextualization rests on a
chain in which one link points to the wrong paper." The synthesis
document also lists Bostock-Kim-Patel as a citation but does not
explicitly call out the fabrication issue, so I suspect the author
read the synthesis (which omitted the fabrication finding) rather than
my full round-1 review.

This must be fixed before §5 ships. The synthesis appears to have
under-weighted my round-1 MAJOR finding because the round-1 *verdict*
was MINOR_REVISIONS (conditional). The conditional status was on this
specific item.

**RES-S5-v2-2 (MINOR).** *Cross-references* section labels §3 and §4
as v2 when they are now v3 (see above).

**RES-S5-v2-3 (MINOR — inherited from round 1, partially addressed).**
§5.3's "7-step NP-pump protocol" phrase (lines 125–126, 136) is still
present and still unanchored to a "7-step" formalization in §3 v3.
§3 v3 Definition 3.3.4 is the hybrid-jump definition; there is no
"7-step" enumeration. Either replace with "the NP-pump protocol of
Definition 3.3.4" or (better) explicitly enumerate the seven steps in
a §5.3 footnote. Not blocking but should be cleaned.

**RES-S5-v2-4 (MINOR — inherited from round 1).** §5.7's *What §5
does not establish* still does not name multiplicity > 1 (per §4
Remark 4.4.3 / §4.7) or $\mathcal{P}^*$-genericity (per §3.8). One
sentence each would close.

**RES-S5-v2-5 (NIT).** §5.4 L1 step 1's Souza et al. 2022 DOI should
be verified against a real Brain Stimulation paper before submission.

---

## What improved in v2

1. **All four RES items (A–D) cleanly resolved.** The Cohen's $d$ /
   significance / sample-size pattern is now applied uniformly across
   P1, P2, P4, which is the right consistency.

2. **Pillar 4 threading.** Each protocol subsection now opens with an
   "Autonomy level" paragraph naming its position in the taxonomy and
   its candidate study population. The structural complaint from
   GPT-5.5 round 1 (§5.6 readable as appendix) is addressed: §5.6 is
   now a *consolidating table* that summarizes the threading already
   done in §§5.1–5.5.

3. **The §5.0 glossary box.** This is exactly the standalone-readability
   move the synthesis asked for; the box is correctly sourced (each
   row points to the relevant §3/§4 section) and small enough not to
   overwhelm.

4. **Hyperscanning citations** (Dumas, Hari, Babiloni) added in §5.5,
   per Gemini's flag. These are real and well-placed.

5. **Compression + restructuring** of cuttables: revision log moved to
   bottom; §5.8 contribution table moved to §6. Clean.

---

## Hostile-reviewer simulation (rigor angle)

A hostile rigor referee on §5 v2 would now raise *one* sharp objection:

> "The Bostock-Kim-Patel arxiv 2503.07670 citation, which the paper
> uses as the load-bearing taxonomy reference for its 'autonomy level'
> nomenclature in every protocol subsection, points to a paper on
> retrieval-augmented generation for wireless networks (Mohsin et al.
> 2025), not to any AI-autonomy taxonomy. The mistaken citation
> appears in the introduction (§5.1), in the consolidating §5.6, and
> in the reference list (§ References). Three appearances in a single
> §5 means this is not a typo; it is the structural taxonomy reference
> for the entire Pillar-4 threading. Without this fix, every 'Level-2/3'
> / 'Level-3/4' / 'Level-4/5' / 'Level-5' label in §§5.1–5.5 is
> attached to a fabricated taxonomy, and the Pillar-4 contribution of
> §5 reduces to nominal labeling by terms whose definitions are not
> sourced anywhere checkable."

*Holds?* **Yes, fully.** This is the same MAJOR finding I raised in
round 1 (RES-S5-1). It was apparently not propagated to the synthesis
document and therefore not addressed in v2. The fix is mechanical
(replace the arxiv ID and author triple with a real reference; verify
the level mapping; update the reference list), but it is *not* a
sentence-level fix — it is the load-bearing reference for §5's
Pillar-4 threading, so the level labels themselves should be sanity-
checked against whichever real taxonomy is substituted.

---

## Overall verdict

**MINOR_REVISIONS** — conditional on the Bostock-Kim-Patel citation
fix (RES-S5-v2-1) and the §3/§4 version-label refresh (RES-S5-v2-2).

The four RES items (A–D) explicitly assigned to me by the synthesis
are all RESOLVED. P1–P4 all have binary falsification conditions with
operational statistical specifications. The citations to §3 v3 and §4
v3 numbered objects (definitions, theorems, remarks, audit numbers)
all resolve correctly — only the version label at the bottom is stale.
The Pillar-4 threading is structurally sound.

The single remaining MAJOR-shaped issue is the inherited fabricated-
citation problem from round 1, which v2 did not address. Because all
v2 changes are otherwise correct and the citation fix is mechanical
and isolated, I keep this at MINOR_REVISIONS rather than escalating to
MAJOR — but I want to be explicit that "minor" here means "small in
edit-volume," not "ignorable in correctness." The fabricated arxiv ID
must come out before §5 ships.

If RES-S5-v2-1 lands and RES-S5-v2-2 through -5 are addressed, §5
promotes to clean accept. The §5 → §3 v3 / §4 v3 integration is in
fact tighter than the §5 v1 → §3 v2 / §4 v2 integration was, because
the RES-A/B/C/D fixes brought the protocol specifications up to a
level of operational rigor that matches the §3+§4 mathematical
content.

---

*End of Council rigor review (Opus 4.7, §5 v2 second pass).*
