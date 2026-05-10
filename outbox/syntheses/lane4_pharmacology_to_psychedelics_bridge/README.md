# Lane 4: Pharmacology-to-Psychedelics Bridge

**Source:** ChatGPT Pro Deep Research, 2026-05-09
**File:** `residence_time_psychedelic_transitions.pdf`
**Prompt (implicit, from session context):** Survey the Copeland
residence-time pharmacology literature AND the psychedelic
restoration-of-transitions literature as two lanes of the same
principle.

## Headline finding

**This is the keystone bridge lane.** The report proposes, with
literature support at each link, the end-to-end mechanism chain
from molecular residence time to network-state transition
restoration:

Drug concentration(t) \u2192 bound receptor fraction(t) \u2192 residence
pattern (dwell time, washout persistence, pulse-bridging) \u2192
downstream signaling timing \u2192 network-level gain and coupling
changes \u2192 state-space geometry (dwell times, barriers, transition
probabilities) \u2192 phenomenology and therapeutic outcome.

Crucially: "That exact chain has not yet been demonstrated end-to-
end for classical psychedelics, but the pieces are now on the
table."

This is exactly what Paper 14's cross-substrate claim needs. Not a
proven mechanism (which would make the framework's novelty smaller)
but a literature-supported multiscale inference (which is what the
framework is).

## The one-sentence summary of the framework

From page 1 \u2014 cleanest statement of the principle in any of the
five lanes:

> "On the drug side, mean occupancy is a poor summary if what
> matters is whether binding persists through biologically
> meaningful intervals. On the neural side, 'which region is active'
> is a poor summary if what matters is dwell-time distribution,
> transition probability, hierarchy, and barrier height between
> recurrent network states. The parallel is not identity of
> mechanism; it is identity of explanatory variable: **temporal
> visitation statistics outperform static magnitude summaries**."

And the framework's defensibility boundary, verbatim from the
report:

> "Your proposed mapping \u2014 'occupancy temporal pattern > occupancy
> magnitude' to 'phenomenology as residence pattern, not region
> identity' \u2014 not merely rhetorical, but **analytically defensible,
> provided it is stated as a multiscale inference rather than as an
> already-proven mechanism**."

Paper 14 should state the claim in exactly these terms.

## Strongest pharmacology exemplars

Beyond what Lane 2 captured:

- **Lapatinib (EGFR/HER2, Wood 2004)** \u2014 only 1.6\u00d7 more affine than
  erlotinib but ~70\u00d7 slower dissociation; prolonged receptor
  tyrosine phosphorylation downregulation after washout.
- **CCR5 873140 (Watson 2005)** \u2014 extremely persistent blockade;
  reversal rate <0.004 h\u207b\u00b9, t\u00bd >136 h.
- **TTK inhibitor series (Uitdehaag 2017)** \u2014 anti-proliferative
  activity correlated with residence time more strongly than
  affinity; RT-guided optimization yielded persistent in vivo
  activity.
- **V2R ADPKD series (Zhang 2022)** \u2014 "residence time but not
  affinity correlated with efficacy." One of the cleanest modern
  "koff beats affinity" demonstrations.
- **D2 antipsychotics (inverse case)** \u2014 fast off-rate often
  preferable (extrapyramidal liability); prolonged residence
  *worsens* on-target side effects. This is the important
  counterexample: the framework should acknowledge that residence
  direction depends on substrate (some targets want visits, some
  want residence; the principle is that *temporal pattern matters*,
  not that *longer residence is always better*).
- **BTK (K4DD review)** \u2014 167 h residence time but occupancy
  dropped >50% within a day due to target resynthesis. Illustrates
  that residence time matters only when target turnover is slow.

## Strongest psychedelic restoration-of-transition papers

The report splits psychedelic literature into "expanded repertoire"
(precursor) vs "explicit restoration." The load-bearing explicit-
restoration cluster for Paper 14:

- **Carhart-Harris & Friston 2019 REBUS** \u2014 clearest theory paper;
  psychedelics relax overly precise high-level priors. *Explicit
  restoration framing.*
- **Doss et al. 2021** \u2014 psilocybin therapy increased cognitive
  flexibility for 4+ weeks with increased ACC\u2013PCC dynamic FC in
  MDD. *Explicit restoration, human clinical.*
- **Singleton et al. 2022** \u2014 LSD and psilocybin lowered energy
  required for transitions between recurrent brain states; for LSD
  flattening correlated with more frequent transitions and more
  entropic dynamics. **Cleanest paper for "transition probability /
  barrier height" framing.**
- **Daws et al. 2022** \u2014 antidepressant response rapid and sustained;
  correlated with decreased brain modularity and increased global
  integration. Strongest clinical "brain reset / reduced trapping"
  paper.
- **Nardou et al. 2023** \u2014 psychedelics reopened social reward
  learning critical period in mice; duration proportional to acute
  subjective-effect duration in humans; adulthood relearning
  accompanied by metaplastic restoration of oxytocin LTD. **Clearest
  plasticity-level analogue of "reopening locked transitions."**
- **Vohryzek et al. 2024** \u2014 whole-brain modeling explicitly
  identifying regions important for transition from depressive to
  healthy brain state. **Most direct published "locked state \u2192
  healthy transition" paper found.**
- **Deco et al. 2024** \u2014 psilocybin and escitalopram rebalance brain
  dynamics differently; depression as disrupted hierarchical
  orchestration.
- **Siegel et al. 2024** \u2014 longitudinal precision fMRI; persistent
  reduction in anterior hippocampus\u2013DMN connectivity for weeks
  after psilocybin. Persistent \"unlock.\"

Precursor / mixed (cite but don't lean on for therapeutic
restoration claim):

- Carhart-Harris 2014 entropic brain
- Tagliazucchi 2014 wider dynamical repertoire
- Lord 2019 metastable exploration
- Luppi 2021 LSD dynamic integration-segregation

## Critical three-level dissociation caveat (Ort 2023)

**Spontaneous state-sequence diversity, perturbational/causal
complexity (PCI), and long-term plastic reopening are not the same
observable.** Ort 2023: psilocybin increased spontaneous chaotic
activity but PCI did NOT increase.

Paper 14 must not conflate these three. When the framework says
"psychedelics restore transitions between locked states," it needs
to specify which of the three levels. Best synthesis: psychedelics
acutely change spontaneous state diversity (Level 1), probably
change plasticity substrate (Level 3 via Nardou) but do NOT
necessarily change PCI (Level 2) in the same way.

## Five testable experiments (psychedelic-specific, from this report)

1. **Matched-exposure, varied-koff 5-HT2A agonist panel.** Rodents
   or NHPs with matched peak occupancy / AUC but varied kinetics;
   measure widefield calcium, EEG complexity, dynamic FC, transition
   rates. Direct analog of lapatinib / A2A / V2R designs.
2. **Antagonist-termination experiment.** Use 5-HT2A antagonist with
   well-characterized kinetics to terminate ongoing psychedelic
   state. If neural-state transition rates collapse on the
   antagonist's occupancy timeline rather than bulk plasma
   concentration \u2192 strong cross-scale demonstration that temporal
   occupancy pattern matters more than magnitude. **This is the
   killer experiment \u2014 doesn't require new technology, just
   well-characterized kinetics.**
3. **Clinical occupancy-to-dynamics PK/PD model.** Psilocybin
   depression trial jointly modeling plasma psilocin, PET receptor
   occupancy, fMRI modularity, control-energy estimates, cognitive
   flexibility outcomes. Leading hypothesis: longer effective
   receptor engagement predicts greater post-acute reduction in
   modular trapping.
4. **Spontaneous vs perturbational dissociation.** Same protocol with
   resting EEG/fMRI and TMS-EEG. Test whether longer receptor
   engagement increases spontaneous state diversity without
   changing PCI, or whether separable kinetic regime also changes
   perturbational complexity. Operationalizes Ort caveat.
5. **Baseline rigidity as moderator.** Stratify by pre-drug
   dynamical rigidity (high modularity, low flexibility, deep
   modeled attractors, strong DMN trapping). Restoration account
   predicts larger effects in most-locked brains.

## The combined argument (one-sentence)

From page 11, directly quotable for Paper 14 abstract:

> "Copeland pharmacology teaches that efficacy can depend on how
> long a target remains occupied through biologically relevant
> intervals; psychedelic systems neuroscience increasingly teaches
> that therapy can depend on how easily the brain moves between
> recurrent states, not on whether it visits some wholly
> unprecedented region-defined state."

## What this lane adds to Paper 14 specifically

1. **A literature-backed mechanism chain** (five links) for Paper
   14's cross-substrate claim. Receptor dwell time modulates
   network barrier heights \u2014 not proven end-to-end but with
   pieces on the table.
2. **Five psychedelic-specific experiments** for the empirical
   program (\u00a711). Particularly the antagonist-termination experiment
   is concrete and tractable.
3. **The three-level dissociation caveat** (Ort 2023) sharpens
   the framework claim by preventing conflation.
4. **The one-sentence combined argument** usable in Paper 14
   abstract.
5. **The explicit-restoration cluster** of citations (Doss,
   Singleton, Daws, Nardou, Vohryzek, Deco, Siegel) for \u00a78.5 / \u00a78.6
   that load the cross-substrate claim beyond REBUS alone.
6. **The D2 inverse case** reminder: "longer residence wins" is
   not universal; the framework is about *temporal pattern
   mattering*, not about one direction always being better.
7. **The framework's defensibility boundary** stated explicitly:
   multiscale inference, not already-proven mechanism.

## Connection to framework artifacts

- `outbox/paper14/paper14_outline.md` \u2014 update \u00a72 (formal
  observable), \u00a78.5/\u00a78.6 (cross-substrate extensions), \u00a711
  (experimental agenda) with this lane's contributions.
- `outbox/syntheses/lane2_residence_time_pharmacology/` \u2014 Lane 4
  extends Lane 2 directly into the psychedelic domain.
- `outbox/syntheses/lane1_return_path_machinery/` \u2014 Lane 4's
  network-dynamical findings parallel Lane 1's DMN return-to-task-
  set framing.
- `outbox/syntheses/flow_grind_synthesis.md` \u2014 the visits-vs-
  residence distinction is now cleanly cited in both molecular
  pharmacology AND network neuroscience.

## Five-lane summary (updated)

- Lane 1: Return-path machinery across proteostasis / cancer /
  autonomic / depression. Closest umbrella: engineering resilience
  + allostasis.
- Lane 2: Copeland pharmacology residence-time at receptors.
- Lane 3a (Claude): Temporal residence in proteostasis.
- Lane 3b (ChatGPT Pro): Spatial residence in proteostasis.
- Lane 4 (this report): Pharmacology-to-psychedelics bridge.
  **Provides end-to-end mechanism chain + keystone one-sentence
  argument + killer antagonist-termination experiment.**

Five-lane convergent validation. Paper 14 is now over-seeded for
drafting.
