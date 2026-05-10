# Paper 14 Outline: Two-Axis Residence-Pathology Unification

**Status:** Draft outline, ready for v1 drafting.
**Date seeded:** 2026-05-09
**Inputs:**
- `outbox/syntheses/lane1_return_path_machinery/` (return-path
  machinery across proteostasis / cancer / autonomic / depression —
  closest umbrella concepts: engineering resilience, allostasis,
  critical slowing down, loss of complexity)
- `outbox/syntheses/lane2_residence_time_pharmacology/` (Copeland
  pharmacology anchor)
- `outbox/syntheses/lane3_proteostasis_residence_time/` (both Claude
  temporal + ChatGPT Pro spatial proteostasis surveys)
- `outbox/syntheses/lane4_pharmacology_to_psychedelics_bridge/`
  (keystone bridge: end-to-end mechanism chain from molecular
  residence time to network-state transition restoration; killer
  antagonist-termination experiment proposal)
- `outbox/syntheses/flow_grind_synthesis.md` (cross-domain synthesis)
- `outbox/syntheses/cross_domain_saturation_collapse.md` (exercise/
  cardiac)
- Paper 12 v1.4, §3.5 / §3.6 boundary-KKT result (substrate-side
  demonstration)

**Five-lane convergent validation:** All five Deep Research lanes
returned with the same structural finding — the principle is
partially anticipated in every surveyed field but never unified as
a cross-domain claim. Lane 4 provides the keystone bridge with an
explicit five-link mechanism chain and the cleanest one-sentence
statement of the framework's claim found in any lane.

## Working title

"Residence Where Transits Were Design Intent: A Two-Axis Formal
Observable for Cross-Class Pathology"

Alternate: "The Visits-Versus-Residence Principle Across
Proteostasis, Pharmacology, Exercise Physiology, and Phenomenology"

Alternate (Lane 1 framing): "Perturbation-Recovery Failure as a
Multiscale Principle of Pathology: Unifying Proteostasis, Autonomic,
Network-Dynamical, and Phospho-Regulatory Substrates"

## One-sentence thesis

Pathology in any system with both regimes available to it is the
temporal-and-spatial residence pattern of states whose transient
sampling is the design intent — produced by failure of the
domain-specific machinery that would have enforced return to
functional control — not the identity of the states themselves.

## Lane 4 single-sentence framing (usable in abstract)

From Lane 4, page 11 — directly quotable:

> "Copeland pharmacology teaches that efficacy can depend on how
> long a target remains occupied through biologically relevant
> intervals; psychedelic systems neuroscience increasingly teaches
> that therapy can depend on how easily the brain moves between
> recurrent states, not on whether it visits some wholly
> unprecedented region-defined state."

And the cross-lane statement of the principle (Lane 4 page 1):

> "Temporal visitation statistics outperform static magnitude
> summaries."

Framework defensibility boundary (Lane 4 page 1, verbatim):

> "Analytically defensible, provided it is stated as a multiscale
> inference rather than as an already-proven mechanism."

Paper 14 must state the claim in exactly these terms.

## Operational definition (Lane 1 disciplined)

Return-path machinery = mechanisms that **restore functional
controllability after perturbation**, not mechanisms that always
return a scalar variable to one invariant value (allostasis caveat).
The definition must be **functional and circuit-specific**, not
baseline-essentialist (GSK3β caveat: same regulator can stabilize
healthy or malignant attractor depending on network context).

## Structure

### §1 Introduction: prior art across four lanes and the unification gap

Open by quoting Tier-1 statements from each of the four surveyed
lanes:

1. **Patel et al. 2015 (temporal, condensate):** "aberrant phase
   transitions within liquid-like compartments lie at the heart of
   ALS"
2. **Babu et al. 2011 (temporal, IDR abundance):** IDPs must be
   "available in appropriate amounts and not present longer than
   needed"
3. **Pytel & Fromm Longo 2025 (two-axis, definitional):**
   proteostasis network governs "timing, location, and stoichiometry"
4. **Bertolotti 2018 (spatial):** "importance of the subcellular
   location of protein deposits in neurodegenerative diseases"
5. **Tummino & Copeland 2008 (pharmacology):** open-system
   pharmacology — "residence time τ = 1/koff is the decision
   variable, not equilibrium affinity"
6. **van Nes & Scheffer 2007 (engineering resilience):** "slow
   recovery from perturbations as a generic indicator of a nearby
   catastrophic shift"
7. **McEwen 1998 (allostasis):** "stability through change" — the
   warning that return paths need not return to one scalar baseline

Argue these are axis-specific, substrate-specific, and silo-bound
instances of one cross-substrate principle. Acknowledge prior art
explicitly. Identify the gap: **no cross-substrate unifying
statement, no formal two-axis observable, no empirical convergence
program across substrates.**

### §2 The two-axis formal observable

Define:

\[ R(s, c) = \tau_R(s) \times \pi_c \]

Where:
- \( \tau_R(s) \) = residence time in conformational state \( s \),
  measured on a Markov state model of native dynamics. Machinery
  exists: Löhr et al. 2021 (VAMPNet/Koopman MSM of Aβ42); Tancredi
  et al. 2024 (HMM dwell-time distributions for Hsp90).
- \( \pi_c \) = occupancy probability in compartment \( c \),
  measured on subcellular trafficking itinerary. Machinery exists:
  live-cell imaging, compartment-resolved proteomics, NLS/NES
  manipulation experiments.

Pathology corresponds to \( R(s, c) \) escaping its design-intent
bounds in *either* axis, with \( s \) and \( c \) possibly unchanged.

Build on Powers, Powers & Gierasch FoldEco (2012) for the network
rate-equation scaffold.

### §3 Four canonical disease cases

Each demonstrates which axis or axes the two-axis observable
captures.

**3.1 FUS in stress granules (pure temporal-axis case).**
Same conformational state; dwell time changes meaning. Patel 2015,
Wolozin & Ivanov 2019, Zhang 2019 (optogenetic decoupling shows
chronic SG assembly is intrinsically cytotoxic independent of
stressor). \( \tau_R(\text{SG-resident FUS}) \) is the disease
variable. \( \pi_c \) is approximately constant (SG compartment).

**3.2 PrP topology / GPI anchoring / surface residence (pure
spatial-axis case).** Hegde 1998 transmembrane PrP → disease; Ma &
Lindquist cytosolic PrP → neurotoxicity; Chesebro 2005 anchorless
PrP → amyloid without scrapie (dissociates deposition from toxicity —
the cleanest single experiment in all of neurodegeneration);
Solomon 2011 mutant PrP requires plasma-membrane localization for
toxicity; Gatdula 2026 membrane-anchored PrP^Sc is the proximate
synaptotoxicity trigger. Same sequence, different \( c \), different
disease. \( \pi_c \) is the disease variable. \( \tau_R(s) \) is
approximately constant.

**3.3 Huntingtin nuclear vs mitochondrial residence (both-axes
case).** Saudou 1998 nuclear huntingtin induces apoptosis; Peters
1999 adding NES decreases / NLS increases huntingtin toxicity (direct
compartmental-residence manipulation); Yablonska 2025 N17
phosphorylation regulates mutant Htt mitochondrial targeting and
reducing mitochondrial residence diminishes toxicity. Same mutant
protein, different compartments, different toxic mechanisms. The
two-axis observable is necessary — single-axis observables cannot
distinguish nuclear-resident from mitochondrial-resident pathology.

**3.4 Tau multi-compartment mislocalization (both-axes case).**
Temporal component: Ash 2021 / Jiang 2019 TIA1-tau condensate
toxicity. Spatial component: Ittner 2010 dendritic tau mediates Aβ
toxicity; Hoover 2010 tau spine mislocalization → synaptic
dysfunction; Lester 2021 tau → nuclear speckle mislocalization;
Yuan 2026 tau oligomers → nuclear lamina invagination. Three spatial
residence regimes (somato-dendritic/postsynaptic, RNP/phase-separated,
nuclear) each produce different toxic mechanisms.

### §4 The unifying claim

All four cases instantiate the same two-axis residence-pathology
principle. Different proteins, different compartments, different
conformational states — same structural signature: residence where
transits were design intent.

Cross-class synthesis: three mechanistic rules recur (from ChatGPT
Pro Lane 3 synthesis, generalizable beyond proteostasis):

1. Residence sets the local physicochemical regime.
2. Residence sets the accessible interactome / signaling space.
3. Residence selects the operative quality-control / return-path-
   machinery node.

### §5 Symmetric formulation of kinetic stabilization

Kelly tafamidis (2012) is asymmetric: stabilize native state to
extend its visit. The framework's thesis is symmetric: pathology is
ANY residence-where-transit-intended, so therapeutic targets include

- Destabilize pathological conformational state → abolish its
  temporal residence (symmetric inverse of Kelly).
- Route protein toward protective compartment → abolish its spatial
  residence in pathological compartment.
- Restore the return-path-machinery that would have bounded
  residence endogenously.

All three are residence-time / residence-compartment interventions
in one rate-equation framework.

### §6 Return-path machinery as a multiscale class

**This is the Lane 1 contribution and the heart of the cross-domain
generalization.** The proteostasis field treats HSP70 ATP-cycling,
HSP90 client-dwell, UPS turnover, autophagy clearance, granulostasis,
HSR/UPR/ISR as a heterogeneous toolkit. Paper 14 reframes them as
one class plus three more substrate-distinct classes:

- **Proteostatic return-path machinery:** chaperones, UPS, autophagy,
  HSR/UPR/ISR, granulostasis, plus ERAD / endolysosomal / NLS-NES /
  nuclear pore / mitochondrial import (spatial-axis return-path
  machinery from Lane 3 ChatGPT survey).
- **Phospho-regulatory return-path machinery:** PP2A and other
  serine/threonine phosphatases as dephosphorylation resetters; APC/
  Axin/GSK3β destruction-complex logic for substrate degradation
  reset; ubiquitin ligases as phospho-state turnover machinery.
- **Autonomic return-path machinery:** vagal brake, baroreflex,
  parasympathetic re-engagement after sympathetic challenge.
- **Network-dynamical return-path machinery:** salience network and
  central executive network mediating switching back to task-positive
  modes; task-induced deactivation of DMN; effective connectivity
  CEN→DMN.

**Common observable across substrates:** recovery time constant τ,
relaxation rate, dominant eigenvalue, dwell-time persistence,
aggregate clearance flux, baroreflex gain, phospho-state settling
time, default-mode dwell time. The mathematical language already
exists — Paper 14's contribution is naming these as one observable
class and showing the principle holds across substrates.

**Critical framework discipline (Lane 1 GSK3β caveat).** Return-path
framing must be **circuit-specific**, not universal. The same
regulator can stabilize a healthy or pathological attractor
depending on network context. Active GSK3β supports Wnt/β-catenin
turnover but also NF-κB / mitosis / survival in other contexts;
active PP2A is tumor-suppressive but DT-061 / iHAP1 mechanism is
contested (PP2A-independent toxicity in some assays). The framework
specifies that pathology is failure of the *circuit-specific*
return-path operator, not loss of any one molecular activity in
isolation.

**Allostasis caveat (Lane 1 McEwen).** A return path may mean return
to a *functional control manifold* rather than to one invariant
scalar baseline. Healthy systems sometimes adapt their operating
point (post-psychedelic DMN connectivity changes, athlete's heart
eccentric LVH, creatine boundary regime adaptation). The framework
defines return-path failure as inability to restore *functional
controllability*, not inability to return to one prior value.

### §7 Frustration-without-escape extension

Wolynes/Ferreiro frustration theory (Parra/Komives/Wolynes/Ferreiro
2025 review) is state-shaped — which interactions are frustrated.
Paper 14 extends to residence-shaped: how long the frustrated state
persists. The pathology is not frustration but *frustration without
escape*.

"Frustration without escape" is explicitly NOT in the published
literature (verified by Lane 3 adversarial survey). Extending the
framework cleanly claims this. Send courtesy preprint to Ferreiro
and Wolynes; their response calibrates the novelty claim.

### §8 Cross-substrate extensions — the substrate-independence claim

This is what distinguishes the framework's unification from any
unification paper that could come out of a single substrate. The
residence-pathology principle holds in every substrate where (a)
both regimes are available, (b) explicit return-path machinery
exists, and (c) recovery kinetics can be measured.

**8.1 Pharmacology (Lane 2).** Copeland residence-time paradigm at
receptors (Tummino & Copeland 2008; Bosma 2017 H1; Casarosa 2009 M3
LAMA; Vauquelin rebinding work). The visits-vs-residence distinction
is already explicitly named in pharmacology.

**8.2 Cancer phospho-regulation (Lane 1).** PP2A as dephosphorylation
reset operator; APC/Axin/GSK3β destruction-complex logic. Pathology
as reset failure: phospho-state cannot relax. Therapeutic strategy:
restore the resetter (SET antagonism, PP2A activators, AKT/ERK
inhibition) — with explicit acknowledgment of the GSK3β circuit-
specificity caveat.

**8.3 Autonomic physiology (Lane 1).** Vagal brake / baroreflex /
parasympathetic re-engagement as return-path machinery. Reduced HRV
predicts mortality (Framingham); slower cardiac vagal recovery after
stress predicts poorer resilience (Souza et al.). HRV biofeedback /
tVNS as recovery-architecture interventions, not just symptom
relief. Most mature measurement infrastructure of all four
substrates (RMSSD, HF-HRV, cBRS).

**8.4 Exercise physiology.** Endogenous boundary operation (visits
with intact feedback → healthy athlete's heart) vs operator-sustained
boundary operation (pharmacological feedback bypass → arrhythmia
phenotype). See `cross_domain_saturation_collapse.md`. The
operator stack converts visits into residence by silencing the
return-path enforcement (PCr depletion cutoff, pH cutoff,
sympathetic-drive cutoff).

**8.5 Depression / large-scale brain networks (Lanes 1 + 4 with
careful framing).** The principle holds as **return-to-task-set**
failure, NOT as static DMN hyperconnectivity. What is consistent
in depression is maladaptive persistence of self-referential modes
/ impaired suppression or switching under demand (Hamilton,
Marchetti, Bartova, Kaiser, Alonso). Wise / REST-meta-MDD found
DMN instability or *reduced* within-DMN FC, complicating naive
hyperstability claims. Paper 14 must use return-to-task-set
language.

**8.5.1 Psychedelic restoration of transitions (Lane 4).** This
is where the framework's molecular-to-phenomenological bridge
lands. Lane 4 provides an end-to-end (not yet proven, but
literature-supported) five-link chain: drug concentration(t) →
bound receptor fraction(t) → residence pattern → downstream
signaling timing → network-level gain and coupling → state-space
geometry (dwell times, barriers, transition probabilities) →
phenomenology and therapeutic outcome.

The explicit-restoration cluster of citations (load-bearing for
this subsection):

- Carhart-Harris & Friston 2019 REBUS (theoretical anchor; psychedelics
  relax overly precise high-level priors)
- Doss et al. 2021 (psilocybin in MDD increased cognitive flexibility
  4+ weeks; ACC–PCC dynamic FC increase)
- Singleton et al. 2022 (LSD/psilocybin lowered control energy for
  state transitions; cleanest paper for transition-barrier framing)
- Daws et al. 2022 (decreased modularity / increased global
  integration after psilocybin therapy in depression)
- Nardou et al. 2023 (mouse: psychedelics reopened critical period;
  metaplastic restoration of oxytocin LTD)
- Vohryzek et al. 2024 (whole-brain modeling explicitly identifying
  regions for depressive-to-healthy transition)
- Deco et al. 2024 (psilocybin and escitalopram rebalance brain
  dynamics differently; depression as disrupted hierarchical
  orchestration)
- Siegel et al. 2024 (longitudinal precision fMRI; persistent
  reduction in anterior hippocampus–DMN connectivity)

Precursor papers (cite but don't lean on for therapeutic-restoration
claim): Carhart-Harris 2014 entropic brain; Tagliazucchi 2014 wider
repertoire; Lord 2019 metastable exploration; Luppi 2021 LSD
integration-segregation.

**Critical three-level dissociation caveat (Ort 2023):**
spontaneous state-sequence diversity, perturbational/causal
complexity (PCI), and long-term plastic reopening are *not* the
same observable. Ort 2023: psilocybin increased spontaneous chaotic
activity but PCI did NOT increase. Paper 14 must specify which of
the three levels its claims target. Best synthesis: psychedelics
acutely change spontaneous state diversity (Level 1), probably
change plasticity substrate (Level 3, Nardou), but do NOT
necessarily change PCI (Level 2) in the same way.

**8.6 PCI phenomenology.** §3.5 smooth-interior / §3.6 boundary-KKT
residence (Paper 12 v1.4) for tear topology. Phenomenologically:
flow = brief §3.6 touches with intact return; rumination /
depression / stuck thought-loops = §3.6 residence without §3.5
recovery. The phenomenological substrate connects directly to §8.5
(large-scale brain networks): subjective rumination IS network-
dynamical return-path failure measured introspectively. Lane 4
establishes that psychedelics restore transitions between locked
states by reducing network barrier heights — i.e., they restore
the §3.5 ↔ §3.6 transition machinery at the network-dynamical
level.

The residence-pathology principle is substrate-independent: wherever
a dynamical system has both regimes available to it plus return-path
machinery, pathology is that machinery failing, not the system
visiting where it shouldn't.

### §9 Differentiation from adjacent literature

- **van Nes & Scheffer 2007 / engineering resilience** — closest
  single-word umbrella, but applied to attractor dynamics generally,
  not as cross-substrate disease principle. Framework adopts the
  recovery-rate / dominant-eigenvalue language and extends across
  substrates.
- **McEwen allostasis** — "stability through change" critical
  caveat; framework explicitly adopts to avoid baseline-
  essentialism.
- **van de Leemput 2014 critical slowing down in depression** —
  shows the recovery-kinetics signature in one domain; framework
  generalizes the signature class.
- **Lipsitz-Goldberger loss of complexity** — framework can
  incorporate as a complementary residence-pattern signature
  (reduced multiscale variability).
- **Knowles-Vendruscolo-Dobson protein metastasis** — their framing
  is native = kinetic visit, amyloid = thermodynamic residence.
  Framework thesis is more general: the *same* state can be
  functional or pathological depending on dwell.
- **Kelly kinetic stabilization** — asymmetric (native only); the
  framework is symmetric (any state, either axis).
- **Pytel & Fromm Longo 2025** — names two axes but stops at
  definitional level; Paper 14 turns it into a disease principle
  with a formal observable.
- **Bertolotti 2018** — pathology-facing but spatial-only and
  review-level, not cross-class theory.
- **Wolynes/Ferreiro frustration** — state-shaped, not residence-
  shaped; Paper 14 extends explicitly.
- **Jülicher/Weber active-matter** — physics of non-equilibrium
  dynamic-state maintenance, not a disease principle; framework
  claims the biological/clinical generalization.
- **Carhart-Harris REBUS** — unified model of psychedelic action,
  not direct proof that depression is residence-pathology.
  Framework cites with explicit caveat that therapeutic loosening
  is not reducible to one-direction static DMN decrease (psilocybin
  imaging shows complex post-treatment changes including increased
  DMN connectivity in some analyses).

### §10 Audit-design template (adapted from Copeland four-point)

For any residence-pathology claim to be rigorous, the study must
report:

1. The full two-axis occupancy quartet: state populations, dwell
   times, compartmental occupancy probabilities, transition rates.
2. Pair with a washout-sensitive functional assay: recovery after
   stressor / agent / local-context withdrawal.
3. In vivo / in-tissue persistence after acute trigger removal.
4. Local temporal and spatial modifiers: concentration, PTM, cofactor
   availability, membrane context, compartmental micro-environment.

Without these four, residence-vs-visit attribution fails. This is
the framework's portable methodology spec.

### §11 Cross-domain experimental agenda (Lanes 1 and 4)

Lanes 1 and 4 together provide thirteen concrete experiments that
operate as the framework's empirical program. These are not Paper
14's own proposals; they are the program Paper 14 frames the field
toward.

**From Lane 1 (cross-substrate recovery kinetics):**

1. **Cross-domain perturbation-recovery battery.** Common recovery
   time constant τ across substrates: aggregate clearance after
   proteotoxic pulse; HRV/cBRS recovery after stress; DMN
   deactivation and return-to-task; phosphoproteomic settling
   after growth-factor pulse. Test whether slower τ co-segregates
   within individuals or disease classes.
2. **Multimodal HRV + fMRI in depression.** Test cross-scale
   coupling between vagal recovery and DMN dwell time directly.
3. **Proteostasis–phosphoregulation coupling assays.** Test whether
   return-path machinery is partly **interoperable** across
   molecular substrates (does PP2A or GSK3β restoration accelerate
   aggregate clearance?). Strongest possible cross-substrate
   convergence test.
4. **Dominant-eigenvalue modeling of recovery.** Fit perturbation-
   response curves to linearized dynamical models. Disease signature:
   smaller-magnitude restoring eigenvalues; intervention signature:
   restored eigenvalue magnitudes.
5. **Longitudinal early-warning designs.** Recurrent depression,
   prodromal PD/ALS, premalignant organoids — test whether
   increasing autocorrelation / longer dwell / slower recovery
   precede overt transition. Pushes framework from post hoc
   explanation to prospective prediction.
6. **Return-path composite index.** Standardized latent variable
   from relaxation rate, recovery slope, dwell-time exit rate,
   complexity. Test against static-burden measures. "How fast you
   come back" > "how abnormal you were at one snapshot."
7. **Intervention-convergence analysis.** Compare HRV biofeedback,
   antidepressant DMN normalization, HSR amplification, PP2A
   activation — do they share dynamical signatures (reduced dwell
   time, reduced autocorrelation, faster settling)?
8. **Boundary-condition experiments.** Test where the framework
   fails: adaptive allostatic set-point shifts, GSK3β-dependent
   tumors, DMN-instability cohorts. Robust theory specifies
   exceptions up front.

**From Lane 4 (pharmacology-to-psychedelics bridge):**

9. **Matched-exposure varied-koff 5-HT2A agonist panel.** Rodents
   or NHPs with matched peak occupancy / AUC but varied
   dissociation kinetics; measure widefield calcium, EEG complexity,
   dynamic FC, transition rates. Direct analog of lapatinib /
   A2A / V2R designs imported into psychedelic neuroscience.
10. **Antagonist-termination experiment.** Use 5-HT2A antagonist
    with well-characterized kinetics to terminate ongoing
    psychedelic state. If neural-state transition rates collapse on
    the antagonist's occupancy timeline rather than bulk plasma
    concentration → strong cross-scale demonstration that temporal
    occupancy pattern matters more than magnitude. **Killer
    experiment: doesn't require new technology, just well-
    characterized kinetics on existing compounds.**
11. **Clinical occupancy-to-dynamics PK/PD model.** Psilocybin
    depression trial jointly modeling plasma psilocin, PET receptor
    occupancy, fMRI modularity, control-energy estimates,
    cognitive flexibility outcomes. Leading hypothesis: longer
    effective receptor engagement predicts greater post-acute
    reduction in modular trapping.
12. **Spontaneous vs perturbational dissociation study.** Same
    protocol with resting EEG/fMRI and TMS-EEG. Test whether longer
    receptor engagement increases spontaneous state diversity
    without changing PCI, or whether separable kinetic regime also
    changes perturbational complexity. Operationalizes Ort 2023
    caveat.
13. **Baseline rigidity as moderator.** Stratify by pre-drug
    dynamical rigidity (high modularity, low flexibility, deep
    modeled attractors, strong DMN trapping). Restoration account
    predicts larger effects in most-locked brains — mirroring how
    residence-time benefits are most visible when biological timing
    makes dwell consequential.

These thirteen together provide a fundable multi-year experimental
program spanning four substrates. Paper 14 §11 frames them as the
next-step research agenda.

### §12 Implications

- **For therapeutics:** restore return-path machinery; abolish
  pathological residence on either axis. Translational caution
  (Lane 1 ORARIALS-01 negative trial): identifying the principle
  correctly does not guarantee any specific intervention based on
  it will work — target engagement, timing, leverage all matter
  independently.
- **For diagnostics:** measure \( R(s, c) \) and recovery time
  constants before structural aggregation markers (which are
  downstream).
- **For disease classification:** group disorders by their residence-
  axis signature plus return-path-machinery failure profile rather
  than by aggregate morphology or single-time-point biomarker.

### §13 Non-goals

This is not a medical-advice claim. The framework observes
structure; clinical work remains the domain of clinical literature.

## Pre-submission checklist (from Lane 3 caveats)

- [ ] Targeted serpinopathy / α₁-antitrypsin Z variant kinetic-trap
      search
- [ ] Targeted Gaucher's / glucocerebrosidase folding-trap search
- [ ] Search Wolynes CTBP talks and Ferreiro lab preprints for
      "frustration without escape" verbatim
- [ ] Search 2024–2026 polyQ huntingtin/ataxin reviews (Wetzel,
      Wolynes/Schafer/Zheng, Lashuel/Pappu) for residence-time-
      pathology framing
- [ ] Re-examine active-matter / dissipative-condensate physics
      (Jülicher, Weber) for disease-principle statements
- [ ] Verify Patel 2015 DOI as 10.1016/j.cell.2015.07.047
- [ ] Send courtesy preprint to Ferreiro and Wolynes after v1
      drafted

## Open questions to address in drafting

1. Is the return-path-machinery class classifiable as a single
   mathematical object? Lane 3 confirms it is real (HSR/UPR/ISR +
   HSP70/90 + UPS + autophagy + granulostasis all serve this role).
   The taxonomy question remains.

2. What is the formal version of "regime mismatch"? Forcing a
   visit-dominated system into residence vs forcing a residence-
   dominated system into visits — both pathological. The framework
   machinery should distinguish.

3. How does Paper 13 Red Queen co-evolutionary dynamics relate? Is
   the rate-balance theorem an instance of return-path-machinery
   dynamics or a separate phenomenon?

4. Does the two-axis observable have a three-axis extension
   (Pytel & Fromm Longo's third axis: stoichiometry)? Could R(s, c, n)
   add a concentration / copy-number dimension?

## Drafting plan

- v1 target: 15-20 pages, six weeks after seeding (i.e., mid-June
  2026). Longer than Paper 12 because cross-class scope requires
  per-class case studies.
- Use Paper 12 v1.4 visual and structural template for consistency.
- Build figures in `outbox/paper14/figures/`.
- Use `pandoc` build pattern (see TODO_MASTER_ROADMAP).

## Non-drafting work that should happen first

1. Let Paper 14 sit one week. Synthesis memos are dense; let the
   two-axis observable crystallize.
2. Before v1 drafting, send the abstract to ChatGPT Pro for a
   third-pass adversarial read focused on: "does R(s, c) survive as
   a formal observable, or is it just notation?"
3. Consider whether Paper 14 should go out as one paper or as a
   paper pair (theory paper + applications paper).
