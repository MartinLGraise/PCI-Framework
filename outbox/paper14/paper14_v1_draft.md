# Residence Where Transits Were Design Intent: A Cross-Substrate Formalism for Coupling-Failure Pathology

**Author:** Martin L. Graise
**Affiliation:** Independent researcher
**ORCID:** 0009-0006-8003-3938
**Date:** 2026-05-12 (v1 drafting in progress)
**Status:** DRAFT. Target: Paper 14 of the PCI Framework series.
Intended for journal submission after v1 review, v1.1 revisions,
and courtesy-preprint circulation per the three-tier schedule in
`outbox/syntheses/lane_cp6_synthesis.md`.

## Abstract

Relation-first ontology has been independently established at
multiple substrates: in fundamental physics through relational
quantum mechanics (Rovelli 1996) and ontic structural realism
(French & Ladyman 2003); in biology through autopoiesis (Maturana
& Varela 1980), relational biology (Rosen 1991), closure-of-
constraints (Mossio & Montévil 2015), and active inference
(Friston 2010, Friston et al. 2015-2025); at the brain-substrate
level for cross-disorder psychopathology through canalization
theory (Carhart-Harris, Chandaria, Friston et al. 2023); and
philosophically through process metaphysics (Whitehead 1929) and
individuation theory (Simondon 1958). What has not been established
is a single explicit measurable coupling-first observable and
structural realization that integrates these substrate-level
relational ontologies into one empirically tractable formalism,
with a downstream pathology grammar. This paper contributes that
formal-operational composition. We introduce an individual-level
two-axis residence-time observable R(s,c) = τ_R(s) × π_c, combining
temporal dwell in a state s with spatial / compartmental occupancy
probability π_c. Pathology corresponds to R escaping design-intent
bounds in either axis, with s and c possibly unchanged. We
demonstrate the formalism across six substrates: receptor
pharmacology, proteostasis (with both temporal condensate-aging and
spatial compartmental-mislocalization cases), autonomic physiology,
large-scale brain network dynamics, intersubjective conversational
coupling, and public-epistemic attractor formation. Four canonical
disease cases (FUS in stress granules, PrP topology, Huntingtin
nuclear-versus-mitochondrial residence, tau multi-compartment
mislocalization) demonstrate that the two-axis observable is
necessary rather than optional: single-axis observables cannot
distinguish them. We propose a cross-substrate experimental program
of thirteen experiments with a common recovery-time-constant
observable. We offer the framework as explicit integration of
modular prior art rather than as first articulation of any
substrate-level claim.

## 1. Introduction

The claim that relations are ontologically prior to relata — that
coupling or process is the substrate and components are derived
from it — has been made, in various forms, by philosophers and
scientists working in at least five distinct research traditions
over the past century. In fundamental physics, Rovelli's relational
quantum mechanics treats quantum states as existing only relative
to other systems, with no absolute state (Rovelli 1996; Di Biagio &
Rovelli 2022; Calosi & Riedel 2024). Ontic structural realism
argues that fundamental ontology is structure rather than objects
with properties, with objects being nodes within relational
structure (French & Ladyman 2003; Ladyman & Ross 2007; French
2014). Karen Barad's agential realism denies that there are
pre-existing independent relata and treats phenomena as primary
(Barad 2007), with extensions into psychology (Scholz 2024) and
social theory (Zanotti 2025). In biology, Maturana and Varela's
autopoiesis treats life as self-producing organization rather than
as a property of components (Maturana & Varela 1980). Rosen's
relational biology formalizes organisms as categories of relations
with closure-to-efficient-causation (Rosen 1991). Mossio and
Montévil's closure-of-constraints framework makes the formal
biology-of-relation move most rigorously (Montévil & Mossio 2015;
Bich 2024). And Friston's free-energy principle treats particles,
organisms, agents, and communicating ensembles within a common
Markov-blanket framework (Friston 2010; Friston, Levin, Sengupta &
Pezzulo 2015; Kuchling et al. 2020; Ramstead, Badcock & Friston
2018; Friston et al. 2024; Friston et al. 2025). At the brain-
substrate level, canalization theory unifies depression,
obsessive-compulsive disorder, addiction, post-traumatic stress
disorder, eating disorders, psychosis, and somatoform conditions
under a single principle of cognitive-and-behavioral phenotypes as
canalized features of mind, brain, or behavior that have come to
dominate an individual's psychological state space (Carhart-Harris,
Chandaria, Friston et al. 2023), with refinements in Deep CANALs
work (Juliani, Safron & Kanai 2024). And philosophically, Whitehead
(1929), Simondon (1958), and the dependent-origination tradition
in Buddhist philosophy have articulated process-first and
relation-first ontologies in various forms, with recent formal
engagement extending these positions (Stenner 2024; Del Fabbro &
Weaver 2025; Ho et al. 2022).

These are distinct research programs operating on different
substrates with different methods. What they share is a commitment
to treating relation, process, or coupling as ontologically prior
to whatever might be taken as the discrete components of the
system in question.

What has *not* been established across these traditions is a
single explicit measurable coupling-first observable. Each
substrate-level program either stays at the conceptual or
metaphysical level (Whitehead, Simondon, Barad) or provides formal
machinery that applies within its domain without extending as a
single observable across substrates (Rovelli within quantum;
Maturana-Varela within biology of cognition; Mossio within
organizational biology; Carhart-Harris within psychopathology).
Friston's free-energy principle comes closest to a substrate-
general formalism but in his published work stops short of the
explicit ontological claim that coupling is primary across all
substrates uniformly — his characteristic idiom is that systems
"can be described as" or "look as if" they minimize free energy,
which is methodological rather than ontological commitment.

Nor has any of these programs produced what we will call a
*downstream pathology grammar*: a principled account of what goes
wrong when coupling structure fails, stated at the formal level and
applied uniformly across substrates. Canalization theory comes
closest at the brain substrate, and it has profoundly influenced
this paper's approach, but it is not applied as a cross-substrate
principle outside of psychopathology.

The contribution of this paper is the formal-operational
composition of these substrate-level programs into one empirically
tractable formalism. We introduce a two-axis residence-time
observable that operates uniformly across substrates and expresses
a substrate-uniform residence-pathology principle: **pathology in
any system with both regimes available to it is the temporal-and-
spatial residence pattern of states whose transient sampling was
the design intent, produced by failure of the return-path
machinery that would have enforced return to functional control,
not the identity of the states themselves.**

We are explicit about what this contribution is not. We do not
claim first articulation of relation-first ontology at any
substrate level; that territory is densely occupied by the authors
cited above. We do not claim first articulation of cross-disorder
residence-pathology at the brain substrate; canalization theory
established that in 2023. We do not claim the G₂ / octonion
mathematical-physics interpretation of the observable, which we
defer to a companion paper (Graise, in preparation) because the
required derivation work belongs in a separate treatment. What we
do claim is the explicit integration: the formal observable, the
substrate-uniform symptom grammar, and the cross-substrate
demonstration that a single formalism can describe coupling-failure
pathology across domains as different as receptor binding, protein
aggregation, conversational coupling, and attractor dynamics in
public information ecosystems.

This claim is narrower than some formulations of the framework's
thesis might suggest. It is also stronger for being narrower. Six
adversarial prior-art surveys conducted in preparation for this
paper (documented in the framework's technical archive) have
repeatedly forced the concession that substrate-level relation-
first ontology is not the contribution; what remains genuinely
open after those surveys is the formal-operational composition
with the individual-level observable and the pathology grammar.
That is what this paper delivers.

The paper is organized as follows. Section 2 defines the two-axis
observable R(s,c) = τ_R(s) × π_c and establishes the machinery
needed to measure it. Section 3 presents four canonical disease
cases — FUS in stress granules, PrP topology, Huntingtin nuclear-
versus-mitochondrial residence, and tau multi-compartment
mislocalization — that demonstrate both axes of the observable are
necessary rather than optional. Section 4 states the cross-class
unifying claim. Section 5 presents the symmetric formulation of
kinetic stabilization. Section 6 identifies return-path machinery
as a multiscale class across four substrates. Section 7 extends
Wolynes-Ferreiro frustration theory to residence-shaped rather
than state-shaped pathology. Section 8 demonstrates the cross-
substrate extensions in seven further domains. Section 9
differentiates the framework from adjacent literature. Section 10
proposes an audit-design template for cross-substrate claims.
Section 11 proposes thirteen experiments as a cross-domain
empirical program. Section 12 discusses implications. Section 13
states non-goals. Section 14 acknowledges the deferred companion
paper.

## 2. The Two-Axis Residence-Time Observable

### 2.1 Definition

For a system whose dynamics can be described on a Markov state
model over conformational or functional states *s* ∈ *S*, and
whose components can occupy compartments *c* ∈ *C*, we define the
**two-axis residence observable**:

\[ R(s, c) = \tau_R(s) \times \pi_c \]

where:

- \( \tau_R(s) \) is the **temporal residence time** in state *s*,
  measured as the mean dwell time on the Markov state model of
  native dynamics. Single-subject estimation machinery exists in
  the neuroscience literature (Vidaurre, Smith & Woolrich 2017 HMM
  Fisher kernel; Löhr et al. 2021 VAMPNet/Koopman MSM of Aβ42;
  Tancredi et al. 2024 HMM dwell-time distributions for Hsp90).
- \( \pi_c \) is the **spatial residence**, or compartmental
  occupancy probability, measured by single-cell trafficking
  assays, live-cell imaging, compartment-resolved proteomics, or
  equivalent machinery depending on substrate. The compartmental-
  occupancy framework is well-developed in subcellular biology
  (Bertolotti 2018; Kumar & Lapierre 2021; Giandomenico et al.
  2022) and in network neuroscience through regional-occupancy
  metrics (Kaiser et al. 2016; Vidaurre et al. 2017).

**Design-intent bounds** for both τ_R and π_c are substrate-
specific functional ranges established by evolved or engineered
return-path machinery. A state has a design-intent τ_R if the
system's normal function requires dwell in s within some range
[τ_min, τ_max]; a compartment has a design-intent π_c if the
system's normal function requires occupancy probability within
[π_min, π_max]. These bounds are not universal constants;
they are determined by the specific return-path machinery operating
in the substrate of interest.

**Pathology** corresponds to R(s, c) escaping its design-intent
bounds in *either* axis, with *s* and *c* possibly unchanged. This
is the critical feature: pathology is not a wrong state or a wrong
compartment, but a deviation in residence pattern for states and
compartments that are entirely normal in other contexts.

### 2.2 Why two axes are necessary

The two-axis structure is empirically necessary rather than
theoretically convenient. Section 3 presents four canonical disease
cases. Two of them (FUS in stress granules, PrP topology) require
only one axis — the temporal in the FUS case, the spatial in the
PrP case. The other two (Huntingtin nuclear-versus-mitochondrial
residence, tau multi-compartment mislocalization) cannot be
described with a single axis: the same mutant protein produces
qualitatively different pathology depending on both its
conformational dwell time and its compartmental occupancy. A
single-axis observable necessarily collapses these distinctions,
which matters for diagnostic and therapeutic stratification.

### 2.3 Relation to existing formalisms

The formal machinery required to measure R(s, c) already exists in
the neuroscience, cell biology, and pharmacology literatures, but
has not been integrated across substrates as a single observable.
In single-subject neuroscience, Vidaurre et al. (2017) developed
HMM Fisher kernels for individual-level dwell-time prediction of
cognitive traits; Singleton et al. (2022) used receptor-informed
network control theory to estimate state-transition energies at
the group level; Vohryzek et al. (2024) fit whole-brain models to
responder and non-responder groups under psilocybin therapy. In
cell biology, Hsp90 client dwell-time distributions (Tancredi et
al. 2024) and MSM-based Aβ42 conformational dynamics (Löhr et al.
2021) provide τ_R at the molecular level, with compartmental
occupancy π_c estimated by conventional imaging and proteomics
approaches. In pharmacology, residence-time τ = 1/k_off is
standard practice following the Copeland framework (Tummino &
Copeland 2008; Bosma et al. 2017; Sykes et al. 2017).

What this paper adds is the unified two-axis formulation applied
uniformly across substrates as a single empirically tractable
formalism. The individual-level (single-subject, single-cell, or
single-system) nature of the observable is load-bearing: group-
level relational metrics exist across substrates, but none combines
both axes into a single predictor of coupling-failure outcome at
the individual level.

### 2.4 Note on mathematical structural realization

The framework's underlying mathematical structure — the symmetry
of coherent coupling structures and the specific role of non-
associative algebra — involves considerations that substantially
exceed the scope of this paper. Existing literature uses octonion
and G₂ structures in symmetry analysis, compactification, and
particle-physics foundations (Baez 2002; Joyce 2000; Dubois-
Violette 2016; Todorov & Dubois-Violette 2018; C. Furey 2018;
Marrani, Corradetti & Zucconi 2025; Singh 2026). We have not found
prior publications making the stronger ontological interpretation
that we propose, and the derivation work required to establish
that interpretation rigorously belongs in a separate treatment. We
defer that interpretation to a companion paper (Graise, in
preparation) whose burden is to (i) derive why non-associativity
should be read as irreducible relationality rather than merely
algebraic failure of reassociation; (ii) show why G₂ specifically,
rather than some broader exceptional or categorical structure, is
the right symmetry notion for coherent coupling; and (iii) define
at least one concrete invariant or observable from associators or
G₂-equivariant quantities that distinguishes coherent from failed
coupling. Paper 14's observable R(s, c) does not depend on the
mathematical interpretation proposed there, and is stated here in
substrate-neutral terms.

## 3. Four Canonical Disease Cases

### 3.1 FUS in stress granules — pure temporal-axis case

[To be drafted in v1 continuation. Covers Patel et al. 2015
demonstration of aberrant phase transitions in ALS; Wolozin &
Ivanov 2019 chronic persistent stress granules; Zhang et al. 2019
optogenetic decoupling showing chronic SG assembly is intrinsically
cytotoxic. The FUS conformational state is unchanged; only τ_R
changes. π_c is approximately constant (the SG compartment).]

### 3.2 PrP topology and GPI anchoring — pure spatial-axis case

[To be drafted. Covers Hegde et al. 1998 transmembrane PrP →
disease; Chesebro et al. 2005 anchorless PrP → amyloid without
scrapie (dissociates deposition from toxicity — the cleanest
single experiment in neurodegeneration); Solomon et al. 2011
mutant PrP requires plasma-membrane localization for toxicity;
Gatdula et al. 2026 membrane-anchored PrP^Sc. Same sequence;
different π_c; different disease. τ_R approximately constant.]

### 3.3 Huntingtin nuclear versus mitochondrial residence — both-axes case

[To be drafted. Covers Saudou et al. 1998 nuclear huntingtin →
apoptosis; Peters et al. 1999 adding NES decreases / adding NLS
increases huntingtin toxicity (direct compartmental-residence
manipulation); Yablonska et al. 2025 N17 phosphorylation regulates
mutant Htt mitochondrial targeting. Same mutant protein; different
compartments; different toxic mechanisms; temporal metastability
also varies; single-axis observables cannot distinguish nuclear
from mitochondrial pathology.]

### 3.4 Tau multi-compartment mislocalization — both-axes case

[To be drafted. Temporal component: Ash et al. 2021 / Jiang et al.
2019 TIA1-tau condensate toxicity. Spatial component: Ittner et al.
2010 dendritic tau mediates Aβ toxicity; Hoover et al. 2010 tau
spine mislocalization → synaptic dysfunction; Lester et al. 2021
tau → nuclear speckle mislocalization; Yuan et al. 2026 tau
oligomers → nuclear lamina invagination. Three spatial residence
regimes, each producing distinct toxic mechanisms in the same
protein.]

## 4. The Cross-Class Unifying Claim

[To be drafted. All four canonical cases instantiate the same
two-axis residence-pathology principle. Three mechanistic rules
recur across the four spatial-axis classes (from the Lane 3
ChatGPT Pro synthesis, generalizable beyond proteostasis):
residence sets the local physicochemical regime; residence sets
the accessible interactome and signaling space; residence selects
the operative quality-control / return-path-machinery node. The
cross-class claim is that these three rules, together with the
two-axis observable, generate a substrate-uniform residence-
pathology grammar.]

## 5. Symmetric Formulation of Kinetic Stabilization

[To be drafted. Kelly's tafamidis-kinetic-stabilization framework
(Bulawa, Kelly et al. 2012) is asymmetric: stabilize the native
state to extend its dwell. The framework proposed here is
symmetric: pathology is any residence-where-transit-intended, so
therapeutic targets include (a) destabilizing the pathological
state to abolish its temporal residence (symmetric inverse of
Kelly); (b) routing a protein toward a protective compartment to
abolish spatial residence in a pathological compartment; (c)
restoring the return-path machinery that would have bounded
residence endogenously. All three are residence-time / residence-
compartment interventions in one rate-equation framework.
Differentiation from Knowles-Vendruscolo-Dobson "protein metastasis"
(2014), whose framing has native as kinetic visit and amyloid as
thermodynamic residence as different states; the framework's thesis
is more general.]

## 6. Return-Path Machinery as a Multiscale Class

[To be drafted. The proteostasis field treats HSP70 ATP-cycling,
HSP90 client-dwell, UPS turnover, autophagy clearance,
granulostasis (Alberti et al. 2017), HSR/UPR/ISR, ERAD,
endolysosomal sorting, NLS/NES systems, and nuclear pore complex
machinery as a heterogeneous toolkit. Paper 14 reframes them as
one class plus three substrate-distinct sibling classes:
proteostatic return-path machinery; phospho-regulatory return-path
machinery (PP2A phosphatases and other serine/threonine resetters;
APC/Axin/GSK3β destruction-complex logic; ubiquitin ligases as
phospho-state turnover machinery); autonomic return-path machinery
(vagal brake, baroreflex, parasympathetic re-engagement); and
network-dynamical return-path machinery (salience network and
central executive network mediating switching back to task-positive
modes; task-induced deactivation of default-mode network;
effective connectivity CEN→DMN).

Common observable across substrates: recovery time constant τ,
relaxation rate, dominant eigenvalue, dwell-time persistence,
aggregate clearance flux, baroreflex gain, phospho-state settling
time, default-mode dwell time. The mathematical language already
exists in engineering resilience literature (van Nes & Scheffer
2007; van de Leemput et al. 2014) and in loss-of-complexity
frameworks (Lipsitz & Goldberger 1992); the framework's
contribution is naming these as one observable class and showing
the principle holds across substrates.

Critical discipline: return-path framing must be circuit-specific
rather than universal (GSK3β supports Wnt/β-catenin turnover but
also NF-κB / mitosis / survival in other contexts; the framework
specifies that pathology is failure of the circuit-specific return-
path operator, not loss of any one molecular activity in
isolation). Allostasis caveat (McEwen 1998): return path may mean
return to a functional control manifold rather than to one
invariant scalar baseline; the framework defines return-path
failure as inability to restore functional controllability.]

## 7. Frustration Without Escape

[To be drafted. Wolynes-Ferreiro frustration theory (Parra,
Komives, Wolynes & Ferreiro 2025 review) is state-shaped — which
interactions are frustrated. Paper 14 extends to residence-shaped:
how long the frustrated state persists. The pathology is not
frustration but frustration without escape. "Frustration without
escape" is explicitly not in the published frustration-theory
literature at the time of writing; this extension is claimed as a
specific contribution. Courtesy preprint to Ferreiro and Wolynes
before submission, per the framework's preprint-circulation
strategy.]

## 8. Cross-Substrate Extensions

[To be drafted as subsections 8.1-8.7, following the structure in
`outbox/paper14/paper14_outline.md`. Brief summaries:]

**8.1 Pharmacology (Copeland lineage).** Tummino & Copeland 2008
open-vs-closed-system framing; Bosma et al. 2017 H1 antihistamine
data (Spearman ρ = −1.0 for receptor-recovery vs k_off; only −0.6
vs equilibrium affinity); Casarosa et al. 2009 M3 LAMA
bronchodilation; Vauquelin rebinding work. The visits-versus-
residence distinction is already explicit in pharmacology; the
framework imports this vocabulary.

**8.2 Cancer phospho-regulation.** PP2A as dephosphorylation reset
operator; APC/Axin/GSK3β destruction-complex logic; SET/CIP2A
inhibition and SMAPs as therapeutic strategies; GSK3β circuit-
specificity caveat.

**8.3 Autonomic physiology.** Vagal brake / baroreflex /
parasympathetic re-engagement as return-path machinery; reduced
HRV as mortality predictor (Framingham); cardiac vagal recovery
after stress; HRV biofeedback and tVNS as recovery-architecture
interventions.

**8.4 Exercise physiology.** Endogenous boundary operation (visits
with intact feedback → healthy athlete's heart) versus operator-
sustained boundary operation (pharmacological feedback bypass →
arrhythmia phenotype). Operator stack converts visits into
residence by silencing return-path enforcement (PCr depletion
cutoff, pH cutoff, sympathetic-drive cutoff). Material from
`outbox/syntheses/cross_domain_saturation_collapse.md`.

**8.5 Depression and large-scale brain networks.** Principle holds
as return-to-task-set failure rather than as static DMN
hyperconnectivity (Hamilton et al. 2011; Wise et al. 2017; Kaiser
et al. 2016; Alonso et al. 2022). Careful framing required — the
literature does not support naive DMN hyperstability claims; it
supports maladaptive persistence and impaired switching under
demand.

**8.5.1 Psychedelic restoration of transitions.** Concede
canalization (Carhart-Harris et al. 2023) as brain-level prior
art. Five-link mechanism chain from Lane 4: drug concentration(t)
→ bound receptor fraction(t) → residence pattern → downstream
signaling timing → network-level gain and coupling → state-space
geometry → phenomenology. Explicit-restoration cluster (Doss 2021;
Singleton 2022; Daws 2022; Nardou 2023; Vohryzek 2024; Deco 2024;
Siegel 2024). Three-level dissociation caveat (Ort 2023 + Casali
2013 + Sarasso 2015): spontaneous state-sequence diversity,
perturbational/causal complexity (PCI), and long-term plastic
reopening are not the same observable.

**8.6 PCI phenomenology.** §3.5 smooth-interior / §3.6 boundary-
KKT residence (Paper 12 v1.4) for tear topology. Phenomenologically:
flow = brief §3.6 touches with intact return; rumination /
depression / stuck thought-loops = §3.6 residence without §3.5
recovery. Three subsections:

- **Memory as dimensional tether.** Memory retrieval is product-
  space coupling between present coherence and past echo, not
  playback from storage (reconsolidation literature: Nader, Schafe
  & LeDoux 2000; Schiller et al. 2010; Agren et al. 2012;
  constructive-memory tradition: Schacter, Addis & Buckner 2007;
  Barsalou 2008; Bartlett 1932; false-memory paradigm: Loftus &
  Palmer 1974; predictive processing: Henson & Gagnepain 2010;
  Friston extensions; Damasio 1999 autobiographical-self
  architecture). From `outbox/syntheses/memory_as_dimensional_tether.md`.
  Subtypes of memory-coupling pathology: grief, nostalgia, regret,
  PTSD.

- **Intersubjective negative pressure.** Coupling between
  conversational participants as product-space substrate; withhold
  of expected continuation generates felt pressure via integration
  of residence excess. Candidate equation P_NP(t) = ∫ f(τ_actual
  − τ_design) ds. Dual-EEG experimental prediction: inter-brain
  beta-phase coupling increases during held pause (counter-
  intuitive; falsifiable). From
  `outbox/syntheses/negative_pressure_intersubjective.md` and
  `outbox/syntheses/eight_anchors_negative_pressure_cluster.md`.

- **Public-epistemic attractor formation.** Substrate-neutral
  version of the attractor-landscape steering observation:
  emergent canal-deepening in public information ecosystems as
  residence-pathology at the epistemic substrate. Missing-
  scientists discourse as a case study in emergent landscape
  deepening without explicit steering. [Substrate-neutral only;
  specific internal framework references preserved in the
  framework's technical archive but not paper material.]

**8.7 Synthesis across the extensions.** One principle; eight
substrate instances; individual-level R(s,c) observable applicable
uniformly; residence-pathology symptom grammar substrate-uniform.

## 9. Differentiation from Adjacent Literature

[To be drafted. See the outline in
`outbox/paper14/paper14_outline.md` for full roster. Key
differentiations: Knowles-Vendruscolo-Dobson protein metastasis;
Kelly kinetic stabilization; Pytel & Fromm Longo 2025; Wolynes-
Ferreiro frustration; Jülicher-Weber active-matter; Carhart-Harris
REBUS; Rovelli RQM; French-Ladyman OSR; Barad agential realism
(apparatus-specific observable machinery, not substrate-general);
Maturana-Varela autopoiesis; Friston FEP (methodological not
ontological); Rosen relational biology; Thompson Mind in Life;
Whitehead (actual-occasions-as-units retained); Simondon
(individuation theory; formalization incomplete); engineering
resilience (van Nes & Scheffer); critical slowing down (van de
Leemput); loss of complexity (Lipsitz-Goldberger); canalization.]

## 10. Audit-Design Template

[To be drafted. Adapted from Copeland four-point audit design:
(1) Full two-axis occupancy quartet (state populations, dwell
times, compartmental occupancy probabilities, transition rates);
(2) Paired with a washout-sensitive functional assay (recovery
after stressor/agent/local-context withdrawal); (3) In vivo /
in-tissue persistence after acute trigger removal; (4) Local
temporal and spatial modifiers (concentration, PTM, cofactor
availability, membrane context, compartmental micro-environment).
Substrate-general version: full kinetic quartet at the appropriate
level + washout-sensitive assay + in situ persistence + local
micro-context.]

## 11. Cross-Domain Experimental Agenda

[To be drafted. Thirteen experiments organized as:]

**From Lane 1 (cross-substrate recovery kinetics):**

1. Cross-domain perturbation-recovery battery
2. Multimodal HRV + fMRI in depression
3. Proteostasis-phosphoregulation coupling assays
4. Dominant-eigenvalue modeling of recovery
5. Longitudinal early-warning designs
6. Return-path composite index
7. Intervention-convergence analysis
8. Boundary-condition experiments

**From Lane 4 (pharmacology-to-psychedelics bridge):**

9. Matched-exposure varied-k_off 5-HT_2A agonist panel
10. Antagonist-termination experiment (killer experiment —
    doesn't require new technology)
11. Clinical occupancy-to-dynamics PK/PD model in psilocybin
    depression trial
12. Spontaneous-versus-perturbational dissociation study
13. Baseline-rigidity-as-moderator design

## 12. Implications

[To be drafted briefly.]

**Therapeutics.** Restore return-path machinery; abolish
pathological residence on either axis. Translational caution:
identifying the principle correctly does not guarantee any
specific intervention based on it will work — target engagement,
timing, and leverage all matter independently (arimoclomol ORARIALS-
01 phase 3 negative as warning case).

**Diagnostics.** Measure R(s, c) and recovery time constants
before structural aggregation markers (which are downstream).

**Disease classification.** Group disorders by their residence-
axis signature plus return-path-machinery failure profile rather
than by aggregate morphology or single-time-point biomarker.

## 13. Non-Goals

This paper is not a medical-advice claim. The framework observes
structure; clinical work remains the domain of clinical literature.
This paper does not claim first articulation of relation-first
ontology at any substrate level. It does not claim first
articulation of cross-disorder residence-pathology at the brain
level (canalization theory established that in 2023). It does not
claim the mathematical-physics interpretation of the observable,
which is deferred to a companion paper.

## 14. Acknowledgment of Deferred Companion Paper

The framework's underlying algebraic structure — specifically the
interpretation of G₂ symmetry as the symmetry of coherent coupling
structures and of octonion non-associativity as expressing
irreducible relationality — requires substantial derivation work
beyond this paper's scope. We identify that work as belonging in a
separate treatment (Graise, in preparation) whose burden is three
deliverables: (i) derive why non-associativity should be read as
irreducible relationality rather than merely algebraic failure of
reassociation; (ii) show why G₂ specifically, rather than some
broader exceptional or categorical structure, is the right
symmetry notion for coherent coupling; and (iii) define at least
one concrete invariant or observable from associators or G₂-
equivariant quantities that distinguishes coherent from failed
coupling. The present paper's observable R(s, c) does not depend
on that companion paper's interpretation and is stated here in
substrate-neutral terms.

---

## Drafting status and next steps

**v1 progress as of 2026-05-12 01:xx PDT:**

- §1 Introduction: **DRAFTED** — 3 tight paragraphs establishing
  prior art, identifying the gap, stating the contribution,
  acknowledging non-goals and the deferred companion paper.
- §2 Formal observable: **DRAFTED** — definition, two-axis
  necessity argument, relation to existing formalisms, deferral
  note for mathematical structural realization.
- §§3-14: **OUTLINED** — structural scaffolding in place; each
  section has a clear scope note and citation clusters ready for
  prose. Continuation drafting in v1.1 sessions.

**Remaining v1 work:**
- §3 four canonical disease cases (highest priority after §1/§2;
  core of the paper)
- §4 cross-class unifying claim (short; follows from §3)
- §§5-7 structural sections (rate-equation framing; drafting is
  mechanical once the disease cases are in)
- §8 cross-substrate extensions (longest section; seven substrate
  subsections plus synthesis; this is where most prose still needs
  writing)
- §9 differentiation (list-based; mostly complete from outline)
- §§10-14 short sections (audit design, experimental agenda,
  implications, non-goals, deferred paper ack)

**Target for v1 completion:** Two more focused drafting sessions
of ~4 hours each should bring §3-§8 to complete first-draft prose.
§§9-14 can be drafted in one follow-up session.

**Total estimated remaining effort:** ~10-14 hours of focused
drafting from this current state. Considerably less than the prior-
art survey campaign that preceded it, because the scaffolding is
dense and the citation work is done.

**Review cycle:** v1 goes to courtesy-preprint Tier A (11 names)
two weeks before submission; Tier B (7 names) one week before;
revisions incorporated as v1.1; then journal submission.
