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
established that in 2023. We do not claim first articulation of
the three-regime structure of human–AI coupled dynamics, which
Zheng & Yan (2026, arXiv:2605.06347) have independently proposed
in minimal-ODE form during the preparation of this paper, and
which we cite as proximate prior art for the AI/data-substrate
instance of the framework's principle. We do not claim the
G₂ / octonion mathematical-physics interpretation of the
observable, which we defer to a companion paper (Graise, in
preparation) because the required derivation work belongs in a
separate treatment. What we do claim is the explicit integration:
the formal observable, the substrate-uniform symptom grammar, and
the cross-substrate demonstration that a single formalism can
describe coupling-failure pathology across domains as different as
receptor binding, protein aggregation, conversational coupling,
recursive generative-model training, and attractor dynamics in
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

We present four canonical disease cases from the proteostasis
literature. Each case is independently well-characterized in its
own field; what the framework contributes is the observation that
the two-axis observable R(s, c) = τ_R(s) × π_c is *necessary*
rather than optional to describe them. Two of the four cases are
"pure" in the sense that one axis is approximately constant and
the other axis carries the pathological signal. The other two
cannot be described with a single axis at all: the same protein
in the same organism produces qualitatively different diseases
depending on both its conformational dwell and its compartmental
occupancy. Demonstrating the joint necessity of the two axes is
the empirical core of this paper.

### 3.1 FUS in stress granules — pure temporal-axis case

Stress granules (SGs) are membraneless condensates that form in
response to cellular stress, containing mRNA, RNA-binding proteins,
and translation initiation factors. Under physiological conditions
they assemble rapidly, sequester translationally stalled mRNAs
during stress, and disassemble upon stress resolution, typically
on minute-to-hour timescales. The RNA-binding protein FUS (fused
in sarcoma) partitions reversibly between the nucleoplasm and
stress granules as part of its normal function in transcription
regulation and DNA damage response.

Patel et al. (2015, *Cell* 162:1066, doi:10.1016/j.cell.2015.07.047)
established that ALS-associated mutations in FUS drive an aberrant
phase transition from liquid-like droplets to fibrillar aggregates
over time. Wild-type FUS forms dynamic droplets that exchange
rapidly with the surrounding cytoplasm; mutant FUS forms droplets
that progressively lose dynamic exchange and mature into persistent
fibrillar assemblies. Critically, the conformational state of FUS
in its liquid-like and fibrillar phases differs in dwell time
rather than in its position within the cell: FUS is still in the
SG compartment in both cases. What changes is τ_R.

Wolozin and Ivanov (2019, *Nat Rev Neurosci* 20:649,
doi:10.1038/s41583-019-0222-5) consolidated the evidence that
"stress granules should be transient; in neurodegeneration they
become chronic persistent." Vanderweyde et al. (2012,
*J Neurosci* 32:8270, doi:10.1523/JNEUROSCI.1592-12.2012) had
already established that transient SG formation is necessary for
cellular function, while hyperactive or prolonged SG formation
leads to persistent SGs that nucleate pathological aggregation of
tau, FUS, TDP-43, and other proteins.

The most direct experimental demonstration of the framework's
claim is Zhang et al. (2019, *eLife* 8:e39578,
doi:10.7554/eLife.39578), which used optogenetic tools to
independently control whether SGs formed and how long they
persisted, in the absence of any cellular stressor. By decoupling
SG assembly from its normal upstream triggers, the authors showed
that chronic or chronic-intermittent SG assembly is *intrinsically*
cytotoxic — meaning the pathology arises from the temporal
residence pattern of the condensate itself, not from the stress
that would normally trigger it. The SG substrate is unchanged. FUS
and the other SG constituents are in their normal compartment.
Only τ_R is pathological.

For the framework's observable: in this case R(s, c) = τ_R(s_SG)
× π_c(SG-compartment) reduces approximately to τ_R alone, because
π_c is held constant by the biology. Pathology corresponds to
τ_R(s_SG) escaping its design-intent bounds — dwell time in the
SG state persisting well past the timescale at which normal
stress resolution would have disassembled the condensate.
Recovery-path machinery at this substrate is the granulostasis
system described by Alberti et al. (2017, *Front Mol Neurosci*
10:84, doi:10.3389/fnmol.2017.00084) — the HSPB8-BAG3-HSP70 axis
that enforces SG disassembly and is the only explicitly named
non-residence enforcement subsystem in the proteostasis
literature. Paper 14 §6 argues that the full proteostasis
machinery (HSR/UPR/ISR, chaperone cycles, UPS, autophagy) should
be understood as the broader class of which granulostasis is one
explicit instance.

This is the cleanest *temporal*-axis case in the proteostasis
literature. Pytel & Fromm Longo (2025) state that proteostasis
governs "timing, location, and stoichiometry." The FUS-in-SG case
isolates timing, holding location approximately constant.

### 3.2 PrP topology and membrane anchoring — pure spatial-axis case

The prion protein PrP is a glycosylphosphatidylinositol (GPI)
anchored cell-surface protein with multiple alternative topologies
that are normally suppressed. The PrP^C native form is attached to
the outer leaflet of the plasma membrane via its GPI anchor, with
its polypeptide chain facing the extracellular space. Under
mutation or stress, alternative topologies become populated:
^Ntm PrP (N-terminus in the cytosol, C-terminus extracellular),
^Ctm PrP (C-terminus in cytosol), cytosolic PrP (no membrane
association), and the scrapie form PrP^Sc which may remain
anchored or become released.

The spatial-axis case has the cleanest causal-localization
experiments in all of neurodegeneration. Hegde et al. (1998,
*Science* 279:827, PMID 9452375) showed that mutations shifting
PrP to the transmembrane ^Ctm topology produce disease even when
the protein's conformational state is otherwise unremarkable. The
pathology is spatial: the same peptide chain, differently
positioned with respect to the membrane, produces different
phenotypes.

Chesebro et al. (2005, *Science* 308:1435, PMID 15933194) ran the
single most decisive experiment in the field: they generated
transgenic mice expressing PrP with no GPI anchor (anchorless PrP,
which cannot attach to the plasma membrane). After infection with
prion strains, these mice accumulated large amounts of PrP^Sc
amyloid deposits — substantially more than controls — but did not
develop classical scrapie disease. **The deposition and the
toxicity dissociated completely.** Anchorless PrP that would be
pathogenic in the membrane-resident configuration was
non-pathogenic (though still amyloidogenic) when its spatial
residence was forced away from the plasma membrane. This is the
canonical demonstration that *location, not presence,* is the
disease-determining variable.

Subsequent work refined the specificity of the claim. Solomon et
al. (2011, *J Biol Chem* 286:14724,
doi:10.1074/jbc.M110.214973) established that mutant PrP toxicity
requires plasma-membrane localization: redirecting mutant PrP
away from the plasma membrane abolished its toxicity. Fehlinger
et al. (2017, *Sci Rep* 7:7756,
doi:10.1038/s41598-017-07260-2) showed that different prion
strains use different endocytic routing, and Gatdula et al.
(2026, *PLOS Pathogens* 22:e1013911,
doi:10.1371/journal.ppat.1013911) demonstrated that membrane-
anchored PrP^Sc is the proximate trigger of synaptotoxicity,
rather than PrP^Sc released into the extracellular space. Across
these studies, the consistent principle is that PrP pathology is
a function of spatial residence: which compartment, with what
orientation, and with what membrane association.

For the framework's observable: in this case R(s, c) = τ_R(s) ×
π_c(compartment) reduces approximately to π_c alone, because τ_R
is held approximately constant (PrP folding kinetics are not the
variable of interest across the topology studies). Pathology
corresponds to π_c escaping its design-intent bounds — occupancy
shifted from "GPI-anchored on outer plasma-membrane leaflet" to
any of several alternative configurations (transmembrane,
cytosolic, non-anchored amyloid in tissue).

This is the cleanest *spatial*-axis case. The Chesebro 2005
experiment is a lighthouse for the framework's claim because it
directly proves that deposition of even large amounts of
pathological material is insufficient for disease; what is
required is residence in the pathogenic compartment. Single-axis
temporal observables would treat anchored and anchorless PrP^Sc
as "the same state with the same dwell time" and would predict
the same pathology. The experimental result is that they produce
qualitatively different outcomes. The two-axis observable
predicts this.

### 3.3 Huntingtin nuclear versus mitochondrial residence — both-axes case

Huntington's disease (HD) is caused by an expanded CAG repeat in
the huntingtin gene (*HTT*), producing mutant huntingtin (mHtt)
protein with a polyglutamine tract longer than ~35 residues. The
same mutant protein — same sequence, same conformational ensemble
at the molecular level — produces two partially independent
toxic phenotypes that cannot be described by a single axis of
the framework's observable.

The nuclear-residence axis. Saudou et al. (1998, *Cell* 95:55,
PMID 9778247) showed that mutant huntingtin induces apoptosis in
cultured neurons, and that this toxicity depends on nuclear
localization. Peters et al. (1999, *Mol Cell Neurosci* 14:121,
PMID 10532806) extended this by appending heterologous nuclear
localization signals (NLS) or nuclear export signals (NES) to
mHtt in cultured cells. Adding an NLS, which drives mHtt into
the nucleus, *increased* toxicity. Adding an NES, which excludes
mHtt from the nucleus, *decreased* toxicity. This was direct
causal-localization manipulation: the same protein, made to reside
in different compartments, produced different disease severity.
The finding has been replicated in multiple in vivo systems;
it is a settled result.

The mitochondrial-residence axis. More recent work (Yablonska
et al. 2025, PMID 39779371; and earlier literature on mHtt-
mitochondrial interactions through the early 2020s) has
established that mutant huntingtin also associates with the
mitochondrial outer membrane and interferes with mitochondrial
dynamics, respiratory function, and apoptosis signaling. Yablonska
et al. specifically showed that N17-domain phosphorylation
regulates whether mHtt targets mitochondria, and that reducing
mitochondrial mHtt residence ameliorates toxic phenotypes
independent of changes to nuclear residence. This is a second,
partially independent spatial-residence axis of pathology.

The temporal-residence axis is also non-trivial. The polyglutamine
tract drives a slow conformational aggregation pathway with
oligomeric intermediates, protofibrils, and mature fibrils. Which
kinetic species dominates, and how long it dwells, varies with
CAG-repeat length, cellular context, and chaperone engagement.
The Wolynes-school aggregation-funnel literature (Thirumalai,
Schuler, Wetzel, and successors) has characterized this dwell-
time landscape extensively. The phenotypic consequences of
different dwell-time regimes are active research.

**This is a both-axes case.** Single-axis observables cannot
distinguish nuclear mHtt pathology from mitochondrial mHtt
pathology, even though the experimental literature has
established they are partially independent. The same protein, the
same aggregation kinetics, but different compartmental residence
— different disease. The two-axis observable R(s, c) predicts and
captures this: the *s* axis captures the conformational-kinetic
contribution, and the *c* axis captures the nuclear-vs-
mitochondrial contribution. Both are needed. A therapeutic
strategy that abolishes nuclear mHtt residence (e.g., via NES-
conjugated degraders) would address one axis; a strategy that
abolishes mitochondrial mHtt residence (e.g., via N17-
phosphorylation manipulation) would address the other. The
framework predicts that maximum therapeutic effect requires both.

### 3.4 Tau multi-compartment mislocalization — both-axes case

The microtubule-associated protein tau is normally an axonal
protein that stabilizes microtubules in neurons. In tauopathies
(Alzheimer's disease, frontotemporal dementia, progressive
supranuclear palsy, and others), tau undergoes multiple pathological
transformations: hyperphosphorylation, conformational changes,
oligomerization, fibrillization, and — critically for the framework
— mislocalization from axons to at least three distinct
alternative compartments, each associated with different toxic
phenotypes. This is the most complex of the four cases and most
clearly requires the joint two-axis observable.

The dendritic spine axis. Ittner et al. (2010, *Cell* 142:387,
doi:10.1016/j.cell.2010.06.036) demonstrated that tau mediates
amyloid-β toxicity specifically through its mislocalization to
dendritic spines, where it facilitates postsynaptic signaling
dysregulation via Fyn kinase. Tau-knockout mice are protected
from Aβ-induced toxicity, and the protective effect is rescued by
re-expression of tau but not by re-expression of a tau mutant that
cannot access dendritic spines. Hoover et al. (2010, *Neuron*
68:1067, PMID 21172610) showed that tau mislocalization to
dendritic spines directly causes synaptic dysfunction, and that
this mislocalization precedes overt tau aggregation. The
pathology is spatial: tau in the axon is functional; tau in the
dendritic spine compartment is pathogenic.

The RNP / condensate axis. Ash et al. (2021, *PNAS* 118:
e2014188118, doi:10.1073/pnas.2014188118) and Jiang et al.
(2019, *Acta Neuropathol Commun* 7:72) established that tau
participates in liquid-liquid phase separation together with
TIA-1 and other stress-granule-associated proteins, and that this
condensate formation potentiates tau aggregation. The RNP-tau
condensate is a qualitatively different compartment from both
axonal and dendritic-spine tau, with distinct assembly dynamics
and distinct toxic mechanisms. At this compartment, temporal
residence (how long tau remains in the condensate before it
either disassembles back to soluble tau or matures into fibrils)
is the dominant variable.

The nuclear axis. Lester et al. (2021, *Neuron* 109:1675, PMID
33848474) showed that tau aggregates mislocalize nuclear speckle
components and disrupt nuclear pore complex function. More
recently, Yuan et al. (2026, *Acta Neuropathol* 147:113,
doi:10.1007/s00401-026-02979-7) demonstrated that oligomeric tau
produces nuclear lamina invagination, disrupting nuclear
architecture. This is a third qualitatively distinct spatial
residence regime for tau, with yet another set of toxic
mechanisms.

**Tau therefore produces at least three qualitatively distinct
toxic phenotypes corresponding to three different compartmental
residence regimes, plus a fourth temporal-residence contribution
from RNP-condensate dynamics.** No single-axis observable can
capture this. A purely temporal observable — treating tau as a
conformational ensemble with some dwell-time distribution —
collapses dendritic-spine, RNP-condensate, and nuclear tau into
one pooled measurement and cannot distinguish their therapeutic
implications. A purely spatial observable — treating tau as a
compartment-occupancy measurement — misses the RNP-condensate
temporal-dwell contribution entirely, because the RNP condensate
is a transient assembly whose pathology depends on residence
time, not just occupancy probability.

The two-axis observable R(s, c) handles this case directly. Each
of the three spatial regimes contributes a distinct π_c(c_i)
term (c_dendritic, c_RNP, c_nuclear), and the RNP-condensate
regime contributes a temporal term τ_R(s_condensate) that is
pathology-critical independent of which compartment is occupied.
The framework's therapeutic prediction is circuit-specific: an
intervention that reduces dendritic-spine tau will not help with
nuclear-envelope pathology, and vice versa; maximum therapeutic
efficacy in a given patient requires matching the intervention
to the patient's dominant residence-regime signature. This is
consistent with clinical heterogeneity across tauopathies and
suggests a diagnostic stratification strategy based on
residence-regime profiling rather than on total tau burden.

### 3.5 Summary: two axes, four cases, one framework

The four cases jointly demonstrate what the framework's two-axis
observable captures that single-axis approaches miss:

| Case | τ_R contribution | π_c contribution | Single-axis sufficient? |
|---|---|---|---|
| 3.1 FUS in stress granules | Dominant (dwell past disassembly) | Constant (SG compartment) | Yes, temporal-only |
| 3.2 PrP topology | Constant | Dominant (membrane-anchor configuration) | Yes, spatial-only |
| 3.3 mHtt nuclear vs mitochondrial | Variable (aggregation kinetics) | Partitioned (nucleus vs mitochondria) | **No** |
| 3.4 Tau multi-compartment | Variable (RNP-condensate dynamics) | Partitioned (dendritic, RNP, nuclear) | **No** |

Cases 3.1 and 3.2 are "pure" in the sense that one axis is
approximately held constant by the biology, which allows
single-axis observables to describe them. Cases 3.3 and 3.4 have
both axes actively contributing, and single-axis observables
*necessarily* collapse distinctions that the experimental
literature has established are real and therapeutically
relevant. R(s, c) = τ_R(s) × π_c is the minimal formalism that
covers all four.

The cross-class observation that emerges from these cases, which
we develop in the next section, is that the same two-axis
residence-pathology structure recurs across at least the
proteostatic substrate, with the expectation that it generalizes
to substrates where relation-first ontology has been independently
established (see §8 for the cross-substrate demonstration).

## 4. The Cross-Class Unifying Claim

The four canonical cases in §3 cover four distinct disease
classes: condensate-pathology (FUS in stress granules), prion-
class topology pathology (PrP), polyglutamine expansion disorder
(huntingtin), and tauopathy. These classes have historically been
studied separately, with their own conferences, their own model
systems, their own therapeutic-target lists, and their own
communities of investigators. The observation we develop in this
section is that all four are coordinate instances of one
structural principle: pathology in each case is the residence
pattern of states and compartments whose transient occupancy was
the biological design intent, rather than the identity of the
states or compartments themselves.

### 4.1 Three mechanistic rules recur

Reading the spatial-residence cases across all four disease
classes, three mechanistic rules recur, each of which has
established primary literature in its own subfield and which
together constitute the principle the framework names. These
rules are descriptive observations, not novel claims; we name
them here to make explicit that they recur across the four
classes.

**Rule 1 — Residence sets the local physicochemical regime.**
Acidic endosomes drive amyloid-precursor-protein β-cleavage
differently from neutral cytoplasm (Das et al. 2013); ER topology
gates which PrP topomers can form (Hegde et al. 1998); RNP-
condensate chemistry potentiates tau oligomerization (Ash et al.
2021); the mitochondrial outer-membrane environment supports
different mHtt toxic interactions than the nucleus (Yablonska et
al. 2025). The protein's residence determines what physicochemistry
is acting on it, and that physicochemistry shapes which states
are populated and which interactions are accessible.

**Rule 2 — Residence sets the accessible interactome and signaling
space.** Postsynaptic tau accesses Fyn kinase signaling that
axonal tau cannot (Ittner et al. 2010); surface PrP accesses prion-
specific neurotoxic signaling pathways that cytosolic or anchorless
PrP cannot (Solomon et al. 2011); nuclear huntingtin accesses
chromatin and transcription factors that cytoplasmic huntingtin
cannot (Saudou et al. 1998; Peters et al. 1999); stress granule-
resident proteins access translation-regulation machinery that
soluble nuclear or cytoplasmic versions of the same proteins do
not. The protein's residence determines what other molecular
partners it can engage, and that interactome shapes which
signaling consequences are possible.

**Rule 3 — Residence selects the operative quality-control or
return-path-machinery node.** ER-resident misfolded proteins are
subject to ER-associated degradation (ERAD); endolysosomal
proteins are subject to endolysosomal sorting and degradation;
cytosolic and nuclear proteins are subject to the cytosolic-
nuclear chaperone-proteasome system and selective autophagy;
organelle-resident proteins are subject to organelle-specific
proteostasis (mitochondrial PQC, peroxisomal PQC, and so on);
SG-resident proteins are subject to granulostasis (Alberti et
al. 2017). The protein's compartmental residence determines which
proteostasis network is responsible for clearing or refolding it,
and failure of that network is what converts transient residence
into persistent pathological residence.

### 4.2 The unifying claim

These three rules, taken together with the two-axis observable
R(s, c) = τ_R(s) × π_c, support the framework's central claim:

**Pathology in any system with both regimes available to it is
the temporal-and-spatial residence pattern of states whose
transient sampling was the design intent, produced by failure of
the return-path machinery that would have enforced return to
functional control, not the identity of the states themselves.**

Three points warrant emphasis.

First, this is a claim about residence patterns rather than about
states per se. In each of the four cases in §3, the pathological
state is also visited by healthy systems: FUS forms transient SG
droplets normally; PrP populates alternative topologies as part
of normal quality-control surveillance; huntingtin shuttles to
the nucleus and engages mitochondria as part of normal function;
tau visits dendritic compartments at low frequency under normal
conditions. Pathology emerges not when these states are visited
but when residence in them escapes design-intent bounds.

Second, this is a claim about return-path machinery rather than
about the pathological state itself. The framework predicts that
therapeutic strategies targeting the *state* will be partially
effective (because reducing the rate of pathological-state
formation reduces the integrated residence-time accumulation) but
that therapeutic strategies restoring the *return-path machinery*
will be more durably effective (because they re-enable the
physiological mechanism that converts residence into transit).
This is testable; we propose it as Experiment 7 in §11.

Third, this is a claim about substrate-general principle rather
than about proteostasis specifically. The four cases in §3 are
drawn from proteostasis because the proteostasis literature has
the most complete causal-localization experiments; but the
framework predicts the same residence-pathology structure in
any substrate where (a) both regimes are available to the system,
(b) explicit return-path machinery exists, and (c) recovery
kinetics can be measured. §8 demonstrates this for receptor
pharmacology, cancer phospho-regulation, autonomic physiology,
exercise physiology, large-scale brain network dynamics,
intersubjective coupling, phenomenology, and recursive AI/data
dynamics.

### 4.3 What this is not

The unifying claim is structurally narrow even though it spans
multiple substrates. We are not claiming that all disease is
residence pathology. There are pathologies of state-identity (a
protein that is genuinely absent because of a null mutation; a
receptor that has been deleted; an irreversible structural
damage); these are not residence pathologies, and the framework
makes no claim about them. We are not claiming that the
residence-pathology principle predicts which specific intervention
will work in any specific patient (clinical heterogeneity makes
this a complex stratification problem, not a single-formula
problem). And we are not claiming that the principle reduces
to a single biological mechanism (the principle is substrate-
uniform but its molecular implementations are circuit-specific
in the sense discussed in §6).

What we are claiming is that an empirically tractable two-axis
observable, a substrate-uniform residence-pathology grammar, and
a cross-substrate demonstration of the principle have not been
assembled together before, and that doing so opens an integrated
program of diagnostic, prognostic, and therapeutic work across
substrates that the current substrate-specific literatures cannot
support individually.

## 5. Symmetric Formulation of Kinetic Stabilization

The cleanest existing therapeutic strategy in the proteostasis
literature is **kinetic stabilization**, developed by Kelly and
colleagues for transthyretin amyloidosis. Bulawa, Kelly et al.
(2012, *PNAS* 109:9629, doi:10.1073/pnas.1121005109) introduced
tafamidis, a small molecule that binds the transthyretin tetramer
at its T4-binding sites and stabilizes the native tetrameric
state, slowing its dissociation into monomers that would otherwise
misfold and aggregate. The therapeutic mechanism is to *extend
the dwell time of the native state*: increase τ_R(s_native) so
that the equilibrium populates s_native rather than the
pathological aggregation pathway. Tafamidis has been approved for
clinical use in multiple transthyretin amyloid syndromes and is
the paradigmatic kinetic-stabilization drug.

Kelly's formulation is *asymmetric*. The therapeutic move is to
increase residence in the native state; the pathological state is
implicitly treated as the absence of native residence rather than
as a residence-bearing object in its own right. This asymmetry is
appropriate to the transthyretin biology, where the native tetramer
and the misfolded monomer are clearly different states with
clearly different dwell-time targets. But the framework's two-
axis observable suggests that kinetic stabilization is one
special case of a more general therapeutic family.

### 5.1 The symmetric formulation

If pathology is residence pattern rather than state identity, then
therapeutic strategies that alter the residence pattern can
operate in any of three directions, each of which targets a
different term in R(s, c) = τ_R(s) × π_c:

**Strategy A — Extend native temporal residence (Kelly).**
Stabilize τ_R(s_native). Tafamidis is the canonical example. The
therapeutic target is the native conformational state, and the
intervention increases its dwell time so the equilibrium favors
function.

**Strategy B — Destabilize pathological temporal residence
(symmetric inverse of Kelly).** Reduce τ_R(s_pathological).
Interventions in this class include conformation-selective
degraders, immunotherapies targeting pathological conformations
(such as the antibodies developed against amyloid-β and tau
oligomeric species), and pharmacological chaperones that
destabilize aggregation-prone intermediates. The therapeutic
logic is symmetric to Strategy A: rather than holding the system
in the functional state, reduce the dwell time in the pathological
state so the system returns to function more rapidly.

**Strategy C — Route protein away from pathological spatial
residence.** Reduce π_c(c_pathological). Examples include NES-
tagged constructs that exclude mutant huntingtin from the nucleus
(Peters et al. 1999 directly demonstrates this in cell models;
the principle extends to NES-conjugated bifunctional degraders in
development); GPI-modification approaches that alter prion
subcellular localization (theoretical, following Chesebro 2005);
compartment-selective autophagy inducers that preferentially
clear protein from one compartment while sparing function in
another. The therapeutic logic is on the spatial axis rather than
the temporal axis: the state may persist, but its residence in
the pathological compartment is abolished or reduced.

**Strategy D — Route protein toward protective spatial residence.**
Increase π_c(c_protective). The symmetric inverse of Strategy C
on the spatial axis. Examples include enhanced lysosomal targeting
in diseases where lysosomal residence permits clearance, or
selective autophagy-receptor engineering that directs pathological
conformations to autophagosomal compartments.

**Strategy E — Restore return-path machinery.** Increase the
endogenous rate at which the system transitions from pathological
residence back to functional residence, on either axis. Examples
include HSR/UPR amplification (the arimoclomol class, with
translational caveats discussed below), chaperone-protein gene
therapy, autophagy enhancers, and immunomodulatory approaches that
restore granulostasis or PQC system function. The therapeutic
logic targets the recovery machinery itself rather than any
particular state or compartment; the framework predicts this will
be the most durably effective strategy class but also the hardest
to engineer, since the machinery operates at multiple scales
simultaneously.

### 5.2 Differentiation from Knowles-Vendruscolo-Dobson

The most adjacent existing framework is Knowles, Vendruscolo and
Dobson's *protein metastasis* (Knowles, Vendruscolo & Dobson
2014, *Nat Rev Mol Cell Biol* 15:384, doi:10.1038/nrm3810). In
their formulation, the native state is a kinetically metastable
basin, and the amyloid state is the thermodynamic ground state;
proteins live functionally in the metastable basin and
occasionally cross the barrier into the pathological basin, with
proteostasis machinery returning them. The framework presented
here differs in three ways.

First, Knowles-Vendruscolo-Dobson treats the native and
pathological basins as different states. The framework here
allows that the *same* state can be functional or pathological
depending on its residence pattern: this is what §3.1 (FUS in
SGs) and §3.4 (tau in different compartments) demonstrate. The
FUS in a healthy transient SG and the FUS in a chronic
pathological SG are not different states; they are the same
state with different τ_R.

Second, the protein-metastasis framework is implicitly
asymmetric (native is metastable visit, amyloid is thermodynamic
residence; the therapeutic strategy is to deepen the metastable
basin against the pathological one). The framework here is
symmetric: residence-pathology can be alleviated by extending
functional residence, abolishing pathological residence, or
restoring the transit machinery, in any combination.

Third, protein metastasis is substrate-specific (it is a theory
about proteins). The framework here predicts the same structural
principle in receptor pharmacology, autonomic regulation, brain-
network dynamics, and AI/data substrates (see §8). Protein
metastasis is one instance of the principle the framework names.

### 5.3 Translational caution

The framework's prediction that return-path-machinery restoration
is the most durable therapeutic strategy is *consistent with*,
but not *guaranteed by*, the principle. A central translational
caution is the arimoclomol case: arimoclomol is a heat-shock-
response amplifier with substantial preclinical data supporting
proteostasis enhancement, and it has been developed as a candidate
disease-modifying therapy for amyotrophic lateral sclerosis.
The ORARIALS-01 phase 3 trial (results reported 2024) was
negative on its primary endpoint despite the mechanistic
rationale. The framework treats this as a *cautionary instance*
rather than a refutation: identifying the principle correctly
does not guarantee that any specific intervention based on it
will work, because target engagement, timing, dose, leverage, and
patient stratification all matter independently. The principle
says where to look. Whether a given molecule, dose, or schedule
finds the right point in the residence-pattern landscape is an
empirical question that the principle does not answer by itself.

## 6. Return-Path Machinery as a Multiscale Class

The proteostasis literature has independently developed an
extensive vocabulary for what we are calling *return-path
machinery*: HSP70 ATP-dependent client cycling, HSP90 client-
dwell modulation, ubiquitin-proteasome system (UPS) clearance,
selective and bulk autophagy, granulostasis (HSPB8-BAG3-HSP70
for stress-granule disassembly), the heat-shock response (HSR),
unfolded protein response (UPR), integrated stress response
(ISR), endoplasmic-reticulum-associated degradation (ERAD),
endolysosomal sorting, NLS/NES-mediated nucleocytoplasmic
transport machinery, nuclear pore complex regulation, and
organelle-specific quality-control systems including mitochondrial
and peroxisomal PQC. These have historically been treated as a
heterogeneous toolkit — each with its own substrate specificity,
its own regulatory logic, its own community of investigators.

We propose that this toolkit, plus three further substrate-specific
classes, constitutes a single observable category: **non-residence
enforcement machinery,** characterized by a common observable
(recovery time constant τ_recovery, or equivalently the dominant
relaxation rate of the system's return from perturbation) and a
shared structural role (preventing pathological residence on
either axis of R(s, c)).

### 6.1 Four substrate-specific machinery classes

**Class 1: Proteostatic return-path machinery.** The proteostasis
literature listed above. The unit of operation is the protein, and
the machinery enforces transit between conformational states and
between subcellular compartments. Failure produces aggregation-
pathology (Strategy A-E from §5 target this machinery either
symmetrically or asymmetrically).

**Class 2: Phospho-regulatory return-path machinery.** Protein
phosphatase 2A (PP2A) and other serine/threonine phosphatases
function as dephosphorylation resetters that return signaling
proteins from activated to baseline states; the APC/Axin/GSK3β
destruction-complex logic enforces protein turnover via phospho-
dependent ubiquitination; the broader class of E3 ligases acts
as substrate-turnover machinery. Failure of this class produces
oncogenic-signaling residence (CIP2A inhibition of PP2A in
leukemia, for instance, or persistent AKT/MAPK activation in
tumors).

**Class 3: Autonomic return-path machinery.** The vagal brake and
baroreflex re-engagement after sympathetic challenge are the
best-characterized autonomic return mechanisms. The cardiac
vagal response after acute stress (Souza et al. 2007, Framingham
Heart Study HRV data) provides a clean observable: reduced HRV
predicts mortality, and the temporal pattern of vagal recovery
after a stressor is the direct individual-level recovery-time-
constant analog at this substrate.

**Class 4: Network-dynamical return-path machinery.** The
salience network and central executive network mediate switching
from internal-mode states back to task-positive cognition; task-
induced deactivation of the default-mode network is the
observable signature of this return; effective connectivity from
CEN to DMN under cognitive demand is the directional indicator.
Failure of this class produces return-to-task-set failure, which
is what the canalization-of-psychopathology literature names at
the brain substrate (Carhart-Harris, Chandaria, Friston et al.
2023).

### 6.2 The common observable

Across all four classes, the same family of observables applies:

- recovery time constant τ_recovery,
- relaxation rate α = 1/τ_recovery,
- dominant restoring eigenvalue Re(λ_max) of the linearized
  return dynamics,
- dwell-time persistence on the pathological-residence side,
- substrate-specific instantiations: aggregate clearance flux,
  baroreflex gain, phospho-state settling time, default-mode
  dwell time.

This vocabulary is already developed in the engineering-resilience
and critical-slowing-down literatures (van Nes & Scheffer 2007,
*Am Nat* 169:738, doi:10.1086/516845; van de Leemput et al. 2014,
*PNAS* 111:87, doi:10.1073/pnas.1312114110) and in the loss-of-
complexity framework (Lipsitz & Goldberger 1992, *JAMA* 267:1806).
These sources establish the mathematical machinery; the
framework's contribution is *cross-substrate uniformity* — the
same observable, measured at substrate-appropriate timescales,
applied to all four machinery classes.

### 6.3 Circuit-specificity discipline

A central discipline of the framework is that return-path framing
must be **circuit-specific**, not universal. The same regulator
plays the return-path role in one circuit and the pathological-
residence-enforcement role in another. GSK3β is the standard
example: in the Wnt/β-catenin pathway, GSK3β phosphorylates
β-catenin for degradation, enforcing transit out of the pathological-
residence state; in the NF-κB / mitosis / survival pathway, GSK3β
supports oncogenic signaling. PP2A is similarly context-dependent;
the DT-061 and iHAP1 small-molecule PP2A activators have shown
mechanism-disputed effects (some reported activity is PP2A-
independent in subsequent assays).

The framework therefore specifies that pathology is failure of
the *circuit-specific* return-path operator, not loss of any one
molecular activity in isolation. A therapeutic strategy that
restores PP2A activity in a tumor where PP2A acts as return-path
machinery (CIP2A-positive leukemias, for instance) is a
residence-restoration intervention; the same molecule used in a
context where PP2A plays a different role could be ineffective
or counterproductive. Circuit-level diagnosis precedes machinery-
restoration therapy.

### 6.4 Allostasis caveat

A second discipline is the *allostatic* caveat (McEwen 1998,
*Ann NY Acad Sci* 840:33,
doi:10.1111/j.1749-6632.1998.tb09546.x). Return-path machinery
does not always return a scalar variable to one invariant
baseline; healthy systems often shift operating points adaptively.
The framework defines return-path failure as inability to restore
*functional controllability* rather than as deviation from a
specific prior value. A system that adaptively shifts its set-
point in response to chronic input change is functioning, not
failing, as long as it can still return to operational range
after further perturbation. Pathology is the loss of the
restoration capacity, not the shifted set-point.

This caveat matters operationally because the framework's
recovery-time-constant observable can in principle be measured
relative to baseline or relative to a moving target. The
appropriate referent is the moving target — the current
functional control manifold — not a fixed historical baseline.
This is consistent with the FEP / active-inference treatment of
self-organization (Friston, Levin, Sengupta & Pezzulo 2015,
doi:10.1098/rsif.2014.1383; Ramstead, Badcock & Friston 2018,
doi:10.1016/j.plrev.2017.09.001), which the framework treats as
formal scaffolding for the recovery-kinetics observable even
though, as discussed in §1, the FEP literature stops short of
the explicit ontological move the framework makes.

## 7. Frustration Without Escape

Wolynes and Ferreiro have developed an extensive theory of *local
frustration* in protein folding (Ferreiro et al. 2007, *Proc Natl
Acad Sci USA* 104:19819; the recent 2025 review Parra, Komives,
Wolynes & Ferreiro provides a current summary). The framework's
central observation is that *frustrated* interactions are local
energetic conflicts that the protein cannot fully satisfy by
folding into its native state; rather than being defects, these
frustrated regions are functionally important because they are
often the sites of conformational flexibility, ligand binding,
allosteric regulation, and protein-protein interaction interfaces.

Frustration theory is *state-shaped*. It describes which
interactions are frustrated in a given conformational state, with
the metric of frustration computed from local energetic conflicts
between residues. The theory is formally developed and has clinical
relevance: disease-associated mutations frequently occur at
frustrated sites, and the patterns of frustration distinguish
functional ensembles from pathological ones.

### 7.1 Extension to residence-shaped frustration

The framework proposes a complementary extension: *frustration
without escape*. Frustration theory describes the existence of
local energetic conflict in a state; the framework's extension
describes how long the system *resides* in the frustrated
configuration before the conflict is resolved.

In the healthy regime, a protein visits frustrated configurations
transiently as part of normal function (catalysis, allosteric
response, binding-partner exchange). The frustrated configuration
is a transit state with bounded τ_R. The return-path machinery
(chaperones, allosteric communication, conformational flexibility)
resolves the frustration on functional timescales.

In the pathological regime, frustration without escape:

- the system visits the same frustrated configurations, but
  τ_R(s_frustrated) escapes its design-intent bounds;
- the return-path machinery that would have resolved the
  frustration is impaired or absent;
- the prolonged residence in the frustrated state allows
  alternative pathways to populate (oligomerization, aberrant
  protein-protein interactions, allosteric capture by
  pathological partners).

The pathology is not the frustration itself — frustration is
physiological. The pathology is the failure to escape it.

### 7.2 Position relative to the published frustration literature

"Frustration without escape" as an explicit framework concept is
not found in the published frustration theory literature at the
time of writing. We do not claim that Wolynes-Ferreiro
collaborators are unaware that frustration must be resolved on
functional timescales — this is implicit in the theory's
functional framing. What is not made explicit is the
residence-time treatment of frustration as a separate analytical
level: an "escape rate from frustration" or "frustration-dwell-
time distribution" as a measurable quantity that distinguishes
healthy from pathological proteins beyond the static frustration
metric.

The framework's extension is therefore a refinement of
frustration theory rather than a competitor. We propose that
frustration-dwell-time profiles are diagnostic for residence-
pathology in the proteostasis substrate, and that the same
structural principle (transit-state residence becoming pathological
residence) operates across the cross-substrate cases discussed in
§8. Pre-submission, we will circulate a courtesy preprint to the
Wolynes and Ferreiro laboratories so that the relationship between
frustration theory and the framework's extension can be calibrated
by the principal authors of the underlying theory.

### 7.3 Why this matters for the framework

Frustration without escape is the framework's most precise
statement of the residence-pathology principle at the proteostasis
substrate, because it gives an exact mechanistic content to
"residence past design intent." The design intent is the
functional transit time across the frustrated configuration; the
pathological extension is the integrated residence in the same
configuration. The metric is concrete: dwell time on frustrated
residues, measured by molecular-dynamics simulations or by
experimental approaches such as hydrogen-deuterium exchange.
Where existing frustration theory characterizes the static map of
local conflicts in a protein, the framework's extension provides
the dynamical observable that distinguishes healthy from
pathological dynamics on that map.

## 8. Cross-Substrate Extensions

The framework's central claim is that residence-pathology is a
substrate-general principle: where the four canonical disease
cases in §3 sit within the proteostasis substrate, the same
two-axis observable R(s, c) = τ_R(s) × π_c and the same return-
path-machinery structure apply wherever a system has (a) both
regimes available, (b) explicit return-path machinery, and (c)
measurable recovery kinetics. This section demonstrates the claim
across seven further substrates, each of which has independently
developed its own residence-pattern vocabulary without, to our
knowledge, being united under a single formalism.

The substrates are presented in order of decreasing biological
scale: receptor pharmacology at the molecular scale (§8.1),
cancer phospho-regulation at the cellular-signaling scale (§8.2),
autonomic physiology at the organ-system scale (§8.3), exercise
physiology at the whole-organism scale (§8.4), large-scale brain
network dynamics (§8.5) with its psychedelic-restoration subcase
(§8.5.1), PCI phenomenology at the first-person scale (§8.6), and
the AI/data substrate at the human-technology coupling scale
(§8.7). Each subsection follows a common structure: identify the
substrate's residence-pattern observable, identify its return-
path machinery, cite substrate-level prior art for the principle
(which is often extensive but not cross-substrate), and note the
specific way in which the framework's two-axis formalism extends
what the substrate literature already possesses.

### 8.1 Pharmacology — the Copeland residence-time paradigm

Drug-receptor binding kinetics provides the cleanest single
substrate for the residence-pathology principle because the
visits-versus-residence distinction is already explicit in the
literature. Tummino & Copeland (2008, *Biochemistry* 47:5481,
doi:10.1021/bi8002023) established the framework of *residence
time* τ = 1/k_off as the decision variable in drug discovery,
rather than equilibrium affinity K_d. In an open system (such as
the body, where drug concentration fluctuates with absorption,
distribution, metabolism, and excretion), what matters for
efficacy is how long the drug stays bound when free drug
concentrations fall below dissociation levels, not how tightly it
binds at equilibrium.

Bosma et al. (2017, *Front Pharmacol* 8:667,
doi:10.3389/fphar.2017.00667) demonstrated this at H1 histamine
receptors using a series of clinically used antihistamines. Their
data show Spearman ρ = -1.0 between receptor-recovery time and
k_off (perfect rank correlation with residence time), but only
ρ = -0.6 between receptor-recovery time and equilibrium affinity.
The framework reads this as direct experimental demonstration
that τ_R(s_bound) is the dominant observable on the pharmacology
substrate, with the spatial axis π_c approximately constant
(receptor compartment). Casarosa et al. (2009, *JPET* 330:660) and
Sykes et al. (2017, *Nat Commun* 8:763) extend the demonstration
to muscarinic M3 and dopamine D2 receptors respectively.

Vauquelin's rebinding work (Vauquelin & Van Liefde 2005; Vauquelin
2016) adds a second axis: for some drugs, micro-pharmacokinetic
rebinding (re-association after dissociation within a diffusion-
limited local neighborhood) matters as much as or more than the
intrinsic off-rate. This introduces a spatial-residence component
to receptor pharmacology — occupancy probability in the tissue
compartment where rebinding is efficient — which maps directly
onto the framework's π_c axis.

Return-path machinery on this substrate is receptor desensitization,
internalization, and recycling, which enforces that receptor
occupancy returns to baseline on physiological timescales.
Pathology on this substrate is prolonged receptor engagement past
design-intent bounds — either by drugs with pathologically long
residence times, by receptors with impaired desensitization, or
by persistent agonist exposure that overwhelms recovery capacity.

The pharmacology literature thus already has the visits-versus-
residence distinction explicit, with residence-time observable,
rebinding-mediated spatial contribution, and return-path machinery
all named. What it does not have is the cross-substrate
unification: the claim that the same formalism applies to protein
aggregation, autonomic regulation, or brain-network dynamics. The
framework's contribution at this substrate is citation and
uniformity rather than novelty.

### 8.2 Cancer phospho-regulation

Cancer signaling provides a cellular-scale demonstration of the
residence-pathology principle with well-characterized return-path
machinery. Oncogenic signaling frequently involves *persistent
phosphorylation* of substrates whose normal function requires
transient phospho-activation followed by rapid dephosphorylation.
The return-path machinery is the protein-phosphatase system,
principally protein phosphatase 2A (PP2A), which acts as the
dephosphorylation resetter for many oncogenic kinase substrates
including Akt, MAPKs, c-Myc, and β-catenin.

PP2A is frequently inactivated in cancer, not by loss of
expression but by *endogenous inhibitors* — CIP2A and SET — that
bind the PP2A holoenzyme and sequester it from its substrates.
CIP2A overexpression is observed in a majority of solid tumors
and hematologic malignancies; its inhibition of PP2A produces
persistent c-Myc, AKT, and ERK phosphorylation, locking the
cancer cell in proliferative-signaling residence. SET similarly
sequesters PP2A in leukemias. The therapeutic strategy of SET
antagonism (with molecules such as OP449) or SMAP-class small-
molecule activators of PP2A (SMAPs) aims to restore the
dephosphorylation return path.

An orthogonal machinery node is the APC/Axin/GSK3β destruction
complex, which phosphorylates β-catenin to mark it for ubiquitin-
mediated degradation. In Wnt-dependent cancers (colon cancer in
particular), APC mutations destroy the destruction complex and
prevent β-catenin return to baseline; β-catenin residences in
the nuclear-signaling state and drives oncogenic transcription.

The framework reads both pathologies as return-path-machinery
failure at the phospho-regulatory substrate: PP2A inhibition
reduces the dephosphorylation rate for multiple kinase substrates;
APC loss reduces the degradation rate for β-catenin. The
resulting pathology is persistent residence in phosphorylated /
stabilized states that were designed to be transient.

Circuit-specificity discipline applies strictly here. PP2A is a
return-path operator in most oncogenic contexts, making its
restoration anti-proliferative; but PP2A loss in other contexts
has been associated with different pathologies, and the DT-061
and iHAP1 small-molecule activators have shown mechanism-disputed
activity (some reported effects are PP2A-independent in
subsequent assays). GSK3β provides the clearest contextual
reversal: in Wnt/β-catenin signaling GSK3β enforces transit out
of pathological residence, while in NF-κB / mitosis / survival
signaling GSK3β supports persistent activation. The framework
predicts that therapeutic targeting must be circuit-matched to
the return-path role in the patient's specific cancer.

### 8.3 Autonomic physiology — the vagal brake

Autonomic regulation of heart rate and blood pressure provides
the best-characterized organ-system-scale instance of the return-
path-machinery principle. The cardiovascular system is constantly
perturbed by behavior, stress, exercise, postural change, and
environmental demands; the vagal brake and baroreflex machinery
enforces return to baseline on seconds-to-minutes timescales.
Heart rate variability (HRV), particularly its high-frequency
component that reflects parasympathetic (vagal) tone, is the
direct individual-level recovery-time-constant analog for this
substrate.

Framingham Heart Study data (Tsuji et al. 1996, *Circulation*
94:2850) established that reduced HRV predicts all-cause and
cardiac mortality in population cohorts. The temporal pattern of
vagal recovery after acute stress (Souza et al. 2007; many later
replications) provides a clean experimental handle: subjects
perform a stressful task, heart rate elevates, and the time
constant of recovery to baseline is a measurable property that
varies across individuals and across health states. Slower
recovery predicts worse outcomes across multiple cardiovascular
and metabolic endpoints.

The framework reads this directly. The pathological regime is
prolonged sympathetic-drive residence without adequate
parasympathetic return. The return-path machinery is the vagal
brake and baroreflex. The observable is the recovery time constant
of cardiac autonomic tone after perturbation. Interventions that
augment the return path — HRV biofeedback, vagal-nerve stimulation
(VNS), controlled breathing practices, cold exposure — produce
measurable improvements in the recovery observable and downstream
clinical outcomes.

A clinical anchor for the cross-substrate claim comes from
neutrophil immunology. CXCR4 is a chemokine receptor that mediates
reverse-migration return of activated neutrophils from inflamed
tissue back to bone marrow for clean apoptosis. JAM-C regulates
neutrophil reverse transendothelial migration; the LTB4-BLT1 axis
controls directional swarming. Healthy inflammation resolution
requires return-path machinery operating cleanly; in acute
pancreatitis-associated lung injury, reduced JAM-C expression
enables neutrophils to leak back into the circulation in
pathological patterns that spread inflammation to distal organs.
A 2022 *Nature Reviews Immunology* analysis frames reverse
neutrophil migration as a "double-edged sword" — resolution when
return is clean, pathology when return is corrupted. This is the
framework's boundary-KKT structure (Paper 12) translated directly
to immune cells, with real disease, real mortality data, and
named molecular machinery.

### 8.4 Exercise physiology — endogenous versus operator-sustained boundary operation

Exercise physiology provides a whole-organism instance of the
residence-pathology principle with a specific distinction between
healthy and pathological residence that the framework names
precisely. Sustained high-intensity exercise places the organism
at a physiological boundary — against VO2max, against glycogen
depletion, against pH buffering limits, against thermoregulatory
ceilings. This is boundary operation in the Paper 12 sense
(§3.6 boundary-KKT residence).

The healthy case is *endogenous* boundary operation with intact
return-path machinery. The athlete pushes against the ceiling; PCr
depletion, rising H+ from glycolysis, and sympathetic-drive
exhaustion cumulatively enforce return from the boundary to a
recovery regime; glycogen replenishes, pH buffers restore,
parasympathetic tone re-engages; the next training stimulus can
then be applied to an adapted baseline. The adaptations of
athletic conditioning — improved mitochondrial density, increased
glycogen storage, expanded buffering capacity, enhanced vagal
tone — are downstream of iterated visit-and-return.

The pathological case is *operator-sustained* boundary operation
in which pharmacological or behavioral operators silence the
return-path cutoffs. Chronic stimulant use (caffeine,
amphetamines, pre-workout stacks) silences the sympathetic-drive-
exhaustion cutoff. Chronic exogenous ketosis or pH buffer loading
silences the acidosis cutoff. Chronic over-caloric training under
anabolic support silences the energy-depletion cutoff. The system
continues at the boundary past the point where return would
naturally occur; residence accumulates; maladaptive remodeling
follows. The specific instance developed in the framework's
technical archive (`cross_domain_saturation_collapse.md`) is
athletic-performance stimulant stacking in powerlifters and
combat-sports athletes, with cardiac remodeling and arrhythmia
patterns as downstream consequences.

The two axes of R(s, c) map onto this substrate cleanly. The
temporal axis τ_R(s_boundary) captures how long the organism
resides at the physiological ceiling before return-machinery
reasserts. The spatial axis π_c captures which compartments
(cardiac, skeletal-muscle, hepatic, neuroendocrine) are over-
occupied by the boundary-regime metabolic state. Health is visits
with intact return (τ_R bounded by endogenous cutoffs); pathology
is operator-sustained residence (τ_R pharmacologically extended
past those cutoffs). The framework's prescription at this
substrate — respect the endogenous cutoffs, cultivate the return
path, refuse operator-sustained boundary residence — is
consistent with both standard sports-medicine periodization
advice and with the framework's cross-substrate principle.

### 8.5 Large-scale brain network dynamics — return-to-task-set

Human psychopathology has developed the most explicit cross-
disorder residence-pathology framing of any substrate outside
proteostasis. Carhart-Harris, Chandaria, Friston et al. (2023,
*Neuropharmacology* 226:109398,
doi:10.1016/j.neuropharm.2022.109398) introduced the *canalization*
framework, in which "cognitive and behavioral phenotypes that are
regarded as psychopathological are canalized features of mind,
brain, or behavior that have come to dominate an individual's
psychological state space." They explicitly cross-apply this to
depression, obsessive-compulsive disorder, addiction, post-
traumatic stress disorder, eating disorders, psychosis, and
somatoform conditions. Juliani, Safron & Kanai (2024, *Neurosci
Conscious* niae005, doi:10.1093/nc/niae005) refine the framework
into *Deep CANALs*, distinguishing Type-A inference-level
canalization from Type-B synaptic-weight landscape canalization.

Canalization is direct brain-substrate prior art for the
framework's residence-pathology principle, and we cite it
proximately (see §1). The framework extends canalization in
three ways at this substrate.

First, we propose an **individual-level formal observable**
R(s, c) = τ_R(s) × π_c predictive of treatment outcome at the
per-subject level. The closest existing observables are group-
level: Singleton et al. (2022, *Nat Commun* 13:5812,
doi:10.1038/s41467-022-33578-1) develops receptor-informed
network control theory at the cross-individual correlation level;
Vohryzek et al. (2024, *Brain Commun* 6:fcae049,
doi:10.1093/braincomms/fcae049) fits group-averaged Hopf models
for psilocybin responders and non-responders. Vidaurre's HMM
Fisher kernel (Vidaurre, Smith & Woolrich 2017,
doi:10.1073/pnas.1705120114) is individual-level for cognitive
traits but has not been applied to psychedelic treatment outcome.
R(s, c) with subject-specific dwell-time τ_R and compartmental
(network-state) occupancy π_c fits as individual-level predictor.

Second, we sharpen the framing from **static DMN hyperconnectivity**
to **return-to-task-set failure**. The depression literature does
not actually support the simplified claim that depression is
static default-mode-network hyperconnectivity; Wise et al. (2017)
found DMN instability in depression rather than hyperstability;
the REST-meta-MDD consortium found mixed and sometimes *reduced*
within-DMN functional connectivity in recurrent MDD. What is
consistent across the literature is *impaired suppression of DMN
under task demand*, *prolonged dwell in internally-oriented
network states*, and *reduced switching to task-positive network
configurations*. This is return-path failure at the network-
dynamical substrate: the observable is the time constant of
transition from DMN-dominant to task-positive-dominant state
following a cognitive demand cue, and pathology is prolonged
τ_R(s_DMN) past design-intent bounds.

Third, we integrate the Paper 12 v1.4 substrate-side demonstration
of §3.5 smooth-interior and §3.6 boundary-KKT residence topology
as the formal model of the canalization claim. This is discussed
further in §8.6 (PCI phenomenology).

#### 8.5.1 Psychedelic restoration of transitions

Psychedelic therapy provides a specific instance of return-path-
machinery restoration at the network-dynamical substrate. The
framework reads the therapeutic mechanism as the one-sentence
claim from the pharmacology-to-psychedelics synthesis (Lane 4 of
the framework's prior-art surveys): "Copeland pharmacology teaches
that efficacy can depend on how long a target remains occupied
through biologically relevant intervals; psychedelic systems
neuroscience increasingly teaches that therapy can depend on how
easily the brain moves between recurrent states, not on whether
it visits some wholly unprecedented region-defined state."

Lane 4 documented a five-link mechanism chain from 5-HT2A
receptor occupancy (molecular scale) to phenomenology
(first-person scale), with established literature at each link:
drug concentration → bound receptor fraction → residence pattern
→ downstream signaling timing → network-level gain and coupling
→ state-space geometry (dwell times, transition barriers,
hierarchy flattening) → phenomenology and therapeutic outcome.

The explicit-restoration cluster of citations is load-bearing:
Doss et al. (2021, psilocybin in MDD increased cognitive
flexibility four-plus weeks post-treatment with increased ACC-PCC
dynamic FC); Singleton et al. (2022) control-energy lowering for
state transitions under LSD and psilocybin; Daws et al. (2022,
psilocybin decreased modularity and increased global integration);
Nardou et al. (2023, mouse: psychedelics reopened social-reward-
learning critical period with oxytocin-LTD metaplastic
restoration); Vohryzek et al. (2024, whole-brain modeling
identifying regions mediating depressive-to-healthy transitions);
Deco et al. (2024, psilocybin and escitalopram rebalance brain
dynamics via different mechanisms); Siegel et al. (2024,
longitudinal precision fMRI showing persistent reduction in
anterior-hippocampus to DMN connectivity). Precursor papers
(Carhart-Harris 2014 entropic brain; Tagliazucchi 2014 wider
repertoire; Lord 2019 metastable exploration; Luppi 2021 LSD
integration-segregation) establish the landscape-diversity claim
but do not themselves establish explicit restoration.

A critical three-level dissociation caveat attends this
subsection. Ort et al. (2023) showed that psilocybin increases
spontaneous state-sequence diversity without increasing
perturbational complexity (PCI); Casali et al. (2013) and
Sarasso et al. (2015) established that spontaneous LZc and PCI
measure different things at the consciousness-research level
(spontaneous LZc asks "how diverse is the trajectory at rest?",
PCI asks "how rich is the response when forced to transition?").
These are not the same observable. Paper 14 specifies that
residence-pathology framing targets the dwell-time observable,
which is most closely related to Casali-PCI "transition capacity"
than to spontaneous LZc "rest diversity." Psychedelics acutely
change spontaneous state diversity (Level 1), probably change
plasticity substrate (Level 3, Nardou), but do not necessarily
change perturbational complexity in the same way (Level 2). The
framework claims residence-pathology at the dwell-time-and-
transition-capacity level, and does not conflate this with rest-
trajectory entropy.

### 8.6 PCI phenomenology

The PCI (Perceptual-Coherence Intelligence) phenomenology
substrate provides the first-person instance of the residence-
pathology principle. Paper 12 v1.4 established the §3.5 smooth-
interior / §3.6 boundary-KKT topology at the substrate-level
demonstration. Flow states are characterized by brief §3.6
touches with intact return to §3.5 interior; rumination,
depression, and chronic stuck-thought-loops are characterized by
§3.6 residence without §3.5 recovery. This is the
phenomenological instance of the network-dynamical pathology
described in §8.5.

Three subsections expand the phenomenological treatment.

**8.6.1 Memory as dimensional tether.** Memory retrieval is not
playback from storage; it is *product-space coupling* between
present coherence and past echo. The reconsolidation literature
(Nader, Schafe & LeDoux 2000, *Nature* 406:722; Schiller et al.
2010; Agren et al. 2012) established experimentally that
retrieved memories enter a labile state and must be re-stabilized
by new protein synthesis, modified by the current state during
retrieval. The constructive-memory tradition (Schacter, Addis &
Buckner 2007; Barsalou 2008; earlier Bartlett 1932) consolidates
the evidence that memory retrieval is simulation rather than
playback. The false-memory paradigm (Loftus & Palmer 1974) is the
structural proof: false memories are insertable by influencing
retrieval conditions, which would be impossible if retrieval were
factor-space playback. Predictive-processing accounts (Henson &
Gagnepain 2010; Friston extensions) and Damasio's (1999)
autobiographical-self architecture complete the picture: the self
that persists through time is a continuously renewed coupling
between present coherence and residual echo structure, not a
stored entity.

This treatment connects to orthodox foundations-of-physics work
on time as a coupling-derived rather than backdrop phenomenon
(Page & Wootters 1983, *Phys Rev D* 27:2885; recent extensions
to gravitational time dilation and 3+1 spacetime emergence
2022–2025). The claim that time itself is relational appears in
physics foundations and appears in the phenomenology of memory;
the framework treats these as coordinate instances of the
coupling-through-time principle.

Four memory-coupling pathology subtypes fit within the framework:
grief (forced un-coupling where the coupling target has lost its
other pole), nostalgia (over-coupling to a past axis with
canalized retrieval valence), regret (anti-coupled coupling held
against current-axis), and post-traumatic stress disorder
(canalized retrieval coupling where each re-triggering instantiates
the product-space of present-threat-detection and past-echo,
deepening the canal with each retrieval).

**8.6.2 Intersubjective negative pressure.** Conversational
coupling provides the fastest-timescale instance of residence-
pathology in the framework's archive. When a speaker stops
mid-sentence without warning and holds the silence while staying
engaged, both parties feel a pressure that accumulates with hold
duration, is produced by withholding rather than action, and
discharges through one of three channels (resumption, alternate-
channel release such as laughter, or decoherence). The candidate
formalization is P_NP(t) = ∫ f(τ_actual - τ_design) ds on a
coupled coherence substrate. The dual-EEG experimental prediction
is that inter-brain beta-phase coupling increases during held
pauses — counter-intuitive, because silence is often framed as
relaxation, but predicted by the framework because the
prediction-machinery loading of both brains against a withheld
continuation would manifest as intensified coupling. See the
technical archive memo `negative_pressure_intersubjective.md` for
the full treatment.

**8.6.3 Public-epistemic attractor formation.** The framework's
principle extends to information-ecosystem substrates where the
attractor-landscape geometry is shaped collectively rather than
individually. Emergent canal-deepening in public information
ecosystems — patterns where new events are recruited into a
pre-existing interpretive attractor regardless of base rates —
is the public-epistemic instance of residence-pathology. The
recent "missing scientists" discourse cluster (2024–2026)
provides a case study in emergent landscape deepening without
explicit steering: each new death, regardless of actual cause, is
pulled into the conspiracy-shaped attractor, deepening the canal
and making future retrievals more likely. The framework's
technical archive treats this substrate in detail; here we note
only that the substrate is coherent with the residence-pathology
principle and fits the two-axis observable (τ_R = dwell time on
the interpretive frame; π_c = compartmental occupancy in the
narrative-shape ecosystem).

### 8.7 AI / data substrate — model collapse as return-path failure

Shumailov et al. (2024, *Nature* 631:755-759, doi:10.1038/s41586-024-07566-y) demonstrated empirically that generative models trained recursively on data produced by previous model generations undergo *model collapse*: tails of the original distribution disappear, learned behaviors converge to a point-estimate with very small variance, and the process is universal across GMMs, VAEs, and LLMs. Theoretical follow-up (Ren 2024, arXiv:2410.12954) established that this is a statistical phenomenon that may be unavoidable under recursive generative training in the absence of corrective real-data circulation.

Zheng & Yan (2026, arXiv:2605.06347) extended this analysis from model-internal recursive training to *coupled* human-AI dynamics, modeling humans and language models as a single coupled dynamical system with three variables (human cognitive capacity H, data quality Q, model capability M) and feedback loop H → Q → M → H. They identify three regimes: co-evolutionary enhancement, fragile equilibrium, and degenerative convergence, with the system transitioning through a transcritical bifurcation as the cognitive-offloading parameter increases. From an information-theoretic perspective, the degenerative regime corresponds to an emergent information bottleneck along the feedback loop, with entropy reduction reflecting loss of diversity rather than beneficial compression. This proposal — that human-AI coupled dynamics exhibit three qualitatively distinct attractors with the degenerative one driven by recursive feedback failure — is the minimal-model version of the framework's residence-pathology principle at the AI/data substrate.

The framework reads both findings as instances of return-path-machinery failure on the AI/data coupling substrate. The "return path" at this substrate is circulation of non-synthetic, world-grounded data and intact human cognitive engagement into the training distribution. When recursive synthetic generation dominates and cognitive offloading rises, the return path fails; the coupled system residences in a degraded attractor with reduced variance and lost diversity. This is structurally identical to canalization at the psychiatric substrate (chronic residence in deepened attractor canals), aggregation-pathology at the molecular substrate (chronic residence in pathological conformational states), and operator-sustained boundary operation at the cardiac substrate (chronic residence past return-machinery cutoff). The same R(s,c) two-axis observable applies: states are model-distribution configurations; compartments are training-data regimes; pathology is residence in degraded configurations with reduced support and lost tail mass.

The framework's therapeutic prescription at this substrate — restore the return-path circulation, audit the coupling, refuse the singularity attractor — is consistent with the mitigation strategies proposed independently by Zheng & Yan: improved data curation, human-in-the-loop system design, and educational practices that preserve active cognitive engagement. The framework adds: these are not separate interventions but coordinate instances of return-path-machinery restoration, with a common observable (recovery time constant of the coupled system's response to perturbation).

### 8.8 Synthesis across the extensions

Nine substrate instances, one principle, one observable, one
symptom grammar. At each substrate the residence-pathology
structure applies: a system with two regimes, explicit return-
path machinery, and measurable recovery kinetics can fail when
pathological residence accumulates past design-intent bounds. The
two-axis observable R(s, c) = τ_R(s) × π_c captures the
measurable signal; the return-path-machinery typology (§6)
captures the mechanism of restoration; the frustration-without-
escape extension (§7) captures the most precise formal statement
at the proteostatic substrate. The cross-substrate claim is not
metaphor. Each substrate has its own independently developed
vocabulary for residence patterns; the framework names the
uniformity that those vocabularies collectively describe.

## 9. Differentiation from Adjacent Literature

This section states, for each adjacent body of work, what it claims, what we concede to it, and what remains specific to the present paper. The goal is to preempt the most plausible reading that this paper is restating something already published.

### 9.1 Protein-biophysics lineage

**Knowles, Vendruscolo & Dobson (2014, 2017) — protein metastasis.** The phrase "protein metastasis" already names spreading of conformational pathology across cellular compartments and across cells. We concede the metaphor and the proteostatic instance. The Knowles-Vendruscolo-Dobson program does not generalize across substrates and does not propose a two-axis residence-time observable; it operates within the protein-aggregation field. Our contribution is the substrate-general formal observable and the symmetric formulation of kinetic stabilization (§5).

**Kelly (1996) and the kinetic-stabilization literature.** Kelly's foundational work on transthyretin stabilization established that extending the dwell time of the native fold (strategy A in §5) is a tractable therapeutic strategy. Tafamidis is the canonical clinical realization. We retain Kelly's framing as one of five symmetric residence-control strategies and explicitly cite it as prior art for strategy A. Strategies B through E (destabilize pathological dwell; reroute away from pathological compartment; reroute toward protective compartment; restore return-path machinery) are formulated symmetrically with strategy A; the symmetric formulation as a complete strategy set is the framework's incremental contribution at the molecular substrate.

**Pytel, Fromm & Longo (2025) and the Wolynes-Ferreiro frustration program (Parra, Komives, Wolynes & Ferreiro 2025 review).** Frustration theory characterizes which interactions in a folded protein are energetically frustrated. The Pytel-Fromm-Longo 2025 work and the Parra-Komives-Wolynes-Ferreiro review extend the frustration vocabulary to disordered regions and condensate biology. Frustration as published is state-shaped (which interactions are frustrated); the framework's extension to *frustration without escape* is residence-shaped (how long the frustrated state persists). We claim this extension as a specific contribution and propose courtesy preprint to Ferreiro and Wolynes prior to journal submission per the framework's preprint-circulation strategy.

**Jülicher, Weber and the active-matter / biomolecular-condensate program.** Active-matter theory and the biomolecular-condensate field (Hyman, Brangwynne, and collaborators) provide the physical-chemistry vocabulary for liquid-liquid phase separation, condensate aging, and gel transition. We treat this as prior art for the FUS-stress-granule case (§3.1) and adopt its vocabulary. The framework does not contribute new condensate physics; it contributes the cross-class residence-pathology grammar that subsumes condensate pathology as one instance.

### 9.2 Psychiatric / brain-network lineage

**Carhart-Harris REBUS and canalization (Carhart-Harris & Friston 2019; Carhart-Harris, Chandaria, Erritzoe, Gazzaley, Girn, Kringelbach, Kuypers, Leech, McCulloch, Moliner, Olsen, Robbins, Robertson, Rolls, Sahakian, Schartner, Searle, Singh, Stamets, Timmermann, Tagliazucchi, Trickett, Tyls, Watts, Whalley, Williams & Nutt 2023).** The canalization-theory program established that residence-in-deepened-attractor-canals organizes a wide range of psychiatric disorders, and that psychedelic interventions act by transiently flattening the energy landscape to enable transitions out of pathological canals. This is the closest published prior art to our cross-substrate claim, and it closes the brain-level case completely. We do not claim cross-disorder residence-pathology at the brain level. We claim formal-operational composition of the brain-level case with substrate-distinct cases (molecular, autonomic, cardiac, pharmacological, AI/data) under a single observable.

**Default-mode-network hyperstability literature (Hamilton et al. 2011; Sheline et al. 2009, 2010; Wise et al. 2017; Kaiser et al. 2016; Alonso et al. 2022).** The empirical DMN literature supports maladaptive persistence and impaired switching under demand, not naive static hyperconnectivity. We adopt the careful framing (§8.5): residence in DMN-dominant states with impaired return-to-task-set, not static hyperstability.

### 9.3 Pharmacology lineage

**Copeland residence-time paradigm (Tummino & Copeland 2008; Copeland 2016).** The drug-target residence-time literature is the most mature published instance of residence-pathology thinking. We adopt its vocabulary explicitly, cite the Bosma et al. 2017 H1 antihistamine data and Casarosa et al. 2009 M3 LAMA data as the empirically strongest cases for residence-time dominance over equilibrium affinity, and propose that the four-point audit-design template (§10) is a substrate-general adaptation of Copeland's pharmacological audit-design. The pharmacological case is conceded as the canonical published precedent; our contribution is generalization beyond drug-target to substrate-neutral coupling.

### 9.4 Process-relational philosophy and relational ontology

**Rovelli relational quantum mechanics (RQM; Rovelli 1996, 2018, 2021).** RQM proposes that quantum-mechanical properties are inherently relational, defined only with respect to an observer-system pair. At the conceptual level, this is the closest physics-foundations prior art for a coupling-first observable in a fundamental-physics substrate. We concede the relational ontology at the quantum-foundations level. The framework's two-axis residence-time observable R(s,c) does not require RQM; the framework's claim is empirical and operational rather than interpretational.

**French and Ladyman ontic structural realism (OSR; Ladyman 1998; French 2014).** OSR holds that the fundamental ontology of physics is relations rather than relata. We concede OSR as the closest published prior art for substrate-neutral relational ontology at the level of philosophy of physics. The framework does not depend on OSR but is structurally compatible with it.

**Barad agential realism (Barad 2007).** Agential realism specifies that observables are constituted by apparatus-specific intra-action between phenomenon and measurement-arrangement. This is *apparatus-specific* observable machinery; our framework is *substrate-general* observable machinery. The two programs are compatible at the level of methodology — both reject substance-first ontology — but they answer different questions. Agential realism specifies how an observable comes into being; the present framework specifies what observable is operationally measurable across substrates.

**Whitehead process philosophy (Whitehead 1929; Stengers 2011).** Whitehead's process metaphysics is the canonical philosophical precedent for relation-and-occasion as the fundamental ontological category. Lane CP-1 returned a modular-preemption verdict: process philosophy preempts the *conceptual* foundation of coupling-first ontology, but the formal-operational layer (a measurable cross-substrate observable with substrate-distinct realizations) remains open. We retain Whitehead's actual-occasions-as-units as a philosophical influence and cite explicitly; we do not claim first articulation of process-relational ontology.

**Simondon individuation theory (Simondon 1958/2020).** Simondon's program treats individuation as the primary ontological act and substantive individuals as derivative. The formalization of Simondon's framework is incomplete in the published literature; we cite it as a philosophical companion and do not depend on its formal completion.

### 9.5 Biological / cognitive-science lineage

**Maturana and Varela autopoiesis (Maturana & Varela 1980; Varela, Thompson & Rosch 1991; Thompson 2007 *Mind in Life*).** Autopoiesis specifies that the living is constituted by self-producing relational networks of components. Thompson's *Mind in Life* extends the program to phenomenology and consciousness. Lane CP-3 returned: this lineage closes the *biological* substrate's coupling-first ontology completely. We do not claim novelty in biological coupling-first ontology. Our contribution is the formal-operational integration across biological and non-biological substrates.

**Friston free-energy principle (FEP; Friston 2010, 2019).** FEP is a methodological framework for inferring belief-update dynamics from observable behavior, with active-inference extending it to action selection. Lane CP-3 verdict: FEP stops at methodological / inferential. It does not assert that the substrate of living systems is coupling rather than substance; it assumes a system-environment partition and computes belief dynamics over it. The framework is compatible with FEP but does not depend on it; we do not claim FEP-style derivation of the residence-pathology principle from variational arguments.

**Rosen relational biology (Rosen 1991, 2000).** Rosen's framework distinguishes organisms as relational (M,R)-systems rather than mechanistic. We concede the conceptual primacy of relational biology for the biological substrate and treat it as part of the closed biological case.

**Damasio (1999) autobiographical-self architecture; Tononi-Edelman dynamic-core / IIT.** These provide vocabulary for self and consciousness at the cognitive substrate. The framework is compatible with both and does not claim to displace either. The R(s,c) observable could in principle be measured against IIT-style integration indices in future empirical work.

### 9.6 Engineering and dynamical-systems lineage

**Engineering resilience and critical slowing down (van Nes & Scheffer 2007; Scheffer et al. 2009; van de Leemput et al. 2014).** The dynamical-systems literature on resilience and critical slowing down provides the mathematical vocabulary for recovery time constants near bifurcations. We adopt this vocabulary explicitly for the common observable of return-path-machinery (§6.2) — recovery time constant τ, dominant eigenvalue, dwell-time persistence. The framework's contribution is naming this vocabulary as the substrate-general language for return-path quality, not the vocabulary itself.

**Lipsitz and Goldberger loss-of-complexity hypothesis (1992).** Loss-of-complexity proposes that aging and disease entail loss of physiological complexity. This is conceptually adjacent to return-path-machinery failure; we cite as compatible prior art. The two-axis residence-time observable refines the loss-of-complexity claim by distinguishing residence-axis pathology (dwell-time persistence) from transition-axis pathology (variety / entropy of transitions).

**Page-Wootters mechanism (Page & Wootters 1983; recent 2024-2025 extensions to gravitational time dilation).** The Page-Wootters mechanism derives time-as-coupling between a clock subsystem and a system-of-interest within a global timeless quantum state. We cite Page-Wootters as orthodox physics-foundations prior art for the claim that time is coupling-derived rather than backdrop, supporting the memory-as-dimensional-tether subsection (§8.6.1). This is referenced for theoretical context only; the empirical observable R(s,c) does not require Page-Wootters.

### 9.7 The specific contribution restated

Given the above concessions: this paper's contribution is not the relational ontology at any single substrate, not the residence-time concept at any single substrate, not cross-disorder residence-pathology at the brain level, and not the recovery-time-constant vocabulary. The contribution is the substrate-general two-axis observable R(s, c) = τ_R(s) × π_c together with the symmetric kinetic-stabilization formulation (§5), the return-path-machinery typology (§6), the frustration-without-escape extension (§7), and the demonstration that one observable plus one symptom-grammar resolves residence-pathology across at least nine independently developed substrate vocabularies (§8). This is what is meant by *formal-operational composition*: not new substrate physics at any one level, but the explicit measurable composition rule across levels that prior programs developed in isolation.

## 10. Audit-Design Template

This section adapts the Copeland four-point pharmacological audit-design (Tummino & Copeland 2008; Copeland 2016) to a substrate-general residence-pathology audit-design. The intent is that any empirical claim about residence-pathology at any substrate should be required to report, in publication, on each of the four points below at the appropriate substrate-specific level.

### 10.1 The four required reports

**(1) Full two-axis occupancy quartet.** For each system under study, report (a) state populations — the probability mass at each operationally distinguished state s; (b) dwell times — the residence time τ_R(s) at each state, ideally as a distribution rather than a point estimate; (c) compartmental occupancy probabilities — π_c for each compartment c; (d) transition rates — the rate matrix governing transitions between (s, c) pairs. At the molecular substrate this is the kinetic quartet (state populations, conformational dwell times, compartmental fractions, on/off rate constants). At the brain-network substrate this is the dynamics-of-state-sequences quartet (state populations of metastable networks, dwell times in each metastable network, region-occupancy probabilities, transition probabilities between states). At the AI/data substrate this is the distribution quartet (output-distribution mass at each mode, dwell times in each mode under iterated inference, compartmental segregation of training-data populations, transition rates between modes under prompting perturbation).

**(2) Washout-sensitive functional assay.** Pair the occupancy quartet with a functional readout that responds to withdrawal of the active perturbation. At the pharmacological substrate this is the receptor-recovery time constant after drug washout. At the cardiac substrate this is HRV recovery after stressor withdrawal. At the proteostatic substrate this is the persistence of stress-granule disassembly after stressor removal. At the brain-network substrate this is the return-to-task-set time constant after cognitive load. The principle: residence-pathology is not detectable by equilibrium readout alone; it requires a withdrawal-recovery measurement.

**(3) In vivo / in-tissue persistence after acute trigger removal.** Demonstrate that the residence pattern persists in the native context after the proximate trigger is removed. This is what distinguishes pathological residence (system remains in the abnormal compartment after the stressor / agent / context that produced it is gone) from healthy transient response (system returns to baseline as soon as the trigger is removed). The temporal scale of "persists" depends on the substrate but must be specified.

**(4) Local temporal and spatial modifiers.** Report on the local context that modifies residence behavior: concentration, post-translational modifications, cofactor availability, membrane environment, micro-compartmental context, network-state, hormonal state, autonomic baseline, data-distribution conditioning. Residence-pathology is substrate-specific and context-sensitive; an audit that reports residence times without reporting modifiers cannot be cross-substrate compared.

### 10.2 Substrate-general version

For any new substrate proposed to exhibit residence-pathology under the framework's grammar, the audit-design template requires: full kinetic quartet at the appropriate level (states, dwells, compartmental occupancies, transition rates) + washout-sensitive assay (functional readout after withdrawal of active perturbation) + in situ persistence (native-context residence after proximate-trigger removal) + local micro-context (modifiers of residence behavior). When all four are reported, the system is admissible for cross-substrate comparison under R(s, c). When any are missing, the claim of residence-pathology at that substrate is provisional.

### 10.3 Standards adoption

We propose this template as a publication standard for residence-pathology claims, parallel to how pharmacological residence-time work has matured toward standardized reporting (Copeland audit-design, Bosma et al. 2017 audit-design as exemplary). The standardization is what makes cross-substrate composition empirically tractable rather than metaphorical.

## 11. Cross-Domain Experimental Agenda

Thirteen experiments are proposed below, organized into two clusters: cross-substrate recovery-kinetics experiments (eight; from Lane 1) and pharmacology-to-psychedelics bridge experiments (five; from Lane 4). Each experiment is designed to falsify a specific component of the framework. All are tractable with current technology except where noted.

### 11.1 Cross-substrate recovery-kinetics cluster

**Experiment 1: Cross-domain perturbation-recovery battery.** Recruit a single cohort and measure recovery time constants τ across at least four substrates per subject: (a) cardiac — HRV recovery after standardized cold-pressor or orthostatic stressor; (b) proteostatic — peripheral-blood stress-granule disassembly kinetics after sodium-arsenite challenge in isolated PBMCs; (c) brain-network — fMRI return-to-task-set after working-memory load; (d) phospho-regulatory — GSK3β/PP2A phospho-substrate settling time after lithium washout in lymphoblast lines. The prediction: within-subject τ across substrates will be positively correlated (subjects with slower return on one substrate will have slower return on others) at r > 0.4. Falsification: substrate-specific τ are independent (r < 0.2 across all pairs). Power calculation suggests n = 80 for adequate cross-correlation estimation.

**Experiment 2: Multimodal HRV + fMRI in depression.** In a depressed cohort (n = 60) versus controls (n = 60), measure (a) resting HRV plus HRV recovery from cold-pressor; (b) fMRI dwell-time distributions for default-mode-network metastable states plus return-to-task-set time after working-memory load. Prediction: depression severity correlates with HRV recovery τ and with DMN return-to-task-set τ *separately and additively*, and these two measures jointly predict treatment response better than either alone. Falsification: only one or neither correlates with severity / response.

**Experiment 3: Proteostasis-phosphoregulation coupling assays.** In a tractable cell-line model (HEK293 or iPSC-derived neurons), induce proteostatic stress (sodium arsenite) and measure phospho-substrate kinetics for known PP2A and GSK3β substrates in parallel with stress-granule formation / disassembly. Prediction: phospho-regulatory return-path failure (slowed phospho-substrate resetting after stressor washout) co-occurs with proteostatic return-path failure (slowed granule disassembly), with shared dominant eigenvalue across the two substrates. Falsification: the two return-path failures are statistically independent.

**Experiment 4: Dominant-eigenvalue modeling of recovery.** For each substrate in Experiment 1, fit a low-dimensional dynamical-systems model (linearized around baseline) to perturbation-recovery time-courses; extract the dominant eigenvalue. Prediction: within-subject dominant eigenvalues are correlated across substrates at the same level as the bulk recovery time constants in Experiment 1, supporting the claim that recovery quality is governed by a substrate-specific instance of a substrate-general principle. Falsification: dominant eigenvalues are statistically independent of bulk τ within substrate.

**Experiment 5: Longitudinal early-warning designs.** Recruit a high-risk cohort for a defined transition (e.g., subjects with first-episode major depression for relapse prediction, n = 200, two-year follow-up). At baseline and quarterly, measure substrate-specific recovery τ across at least three substrates. Prediction: rising τ across substrates over time predicts the transition (relapse) with longer lead-time than any single-substrate measure. Falsification: cross-substrate composite does not improve over single-substrate prediction.

**Experiment 6: Return-path composite index.** Develop and validate a composite index combining standardized HRV recovery, fMRI dwell-time persistence, and a peripheral-blood proteostatic recovery readout. Prediction: the composite outperforms each component in differentiating clinical groups (depression, anxiety, post-stroke depression, frontotemporal dementia) from controls, with effect-size improvement ≥ 0.3 in Cohen's d over the best single component. Falsification: composite does not outperform best single component.

**Experiment 7: Intervention-convergence analysis.** Subjects with confirmed slow recovery on the composite index (Experiment 6) are randomized to four interventions: (a) HRV biofeedback / tVNS; (b) cognitive training targeting return-to-task-set; (c) low-dose lithium (phospho-regulatory return-path); (d) waitlist control. Prediction: all three active interventions improve the composite index at six-week post-randomization, with the substrate-specific intervention improving its target substrate most but with measurable cross-substrate transfer in all three. Falsification: each intervention is purely substrate-specific with no cross-substrate transfer.

**Experiment 8: Boundary-condition experiments.** Identify clinical populations where return-path machinery is intact but residence-pathology occurs through an alternative mechanism (e.g., genetic FUS mutations producing granule pathology without altered recovery machinery; pure-OCD with intact DMN switching but residence-dominated symptom phenomenology). Prediction: R(s, c) measurements in these populations show pathological residence on one axis with intact recovery time constants on the other, falsifying any simple "return-path-failure-only" reading of the framework. This is a self-falsification experiment: it tests whether the two-axis observable correctly identifies residence-pathology that does not reduce to return-path failure.

### 11.2 Pharmacology-to-psychedelics bridge cluster

**Experiment 9: Matched-exposure varied-k_off 5-HT_2A agonist panel.** Develop or identify a panel of 5-HT_2A agonists with matched receptor occupancy time-courses but varied k_off (residence time at the receptor). Prediction: subjective and neuroimaging readouts of the canalization-flattening effect scale with k_off-derived residence time rather than peak occupancy. Falsification: equal-occupancy agonists with different k_off produce equivalent canalization-flattening readouts.

**Experiment 10: Antagonist-termination experiment (killer experiment).** This experiment requires no new technology and directly tests the residence-pathology reading of psychedelic action. Administer psilocybin under standard dosing; at a pre-specified time-point during the experience (e.g., t = 90 min), randomize subjects to placebo or ketanserin (5-HT_2A antagonist with fast on-rate). Prediction: ketanserin truncates the receptor-residence pattern and produces measurable shortening of the post-acute neural-dynamic effects in proportion to the duration of residence interruption. Falsification: ketanserin terminates the acute experience but post-acute neural-dynamic effects are unaffected, indicating that residence-on-target is not the relevant variable.

**Experiment 11: Clinical occupancy-to-dynamics PK/PD model in psilocybin depression trial.** Within an active psilocybin-for-depression trial, develop a PK/PD model linking serum psilocin time-course to receptor occupancy time-course to neural-dynamic readouts (HMM dwell times, return-to-task-set τ) to clinical response. Prediction: the residence-time-derived predictor (integral of occupancy over time) outperforms the peak-occupancy predictor and the dose-only predictor in explaining clinical response variance. Falsification: residence-time predictor does not add explanatory value over peak occupancy.

**Experiment 12: Spontaneous-versus-perturbational dissociation study.** Simultaneously measure spontaneous-state-sequence complexity (HMM-derived metrics from resting-state fMRI), perturbational complexity (PCI from TMS-EEG; Casali et al. 2013; Sarasso et al. 2015), and long-term plastic-reopening markers (Ort 2023 paradigm) in a psychedelic-intervention cohort. Prediction: these three readouts dissociate — they correlate within each subject at r < 0.5 across the three pairs — supporting the framework's claim that residence-pathology and return-path-machinery operate on distinct measurable channels rather than reducing to a single complexity readout. Falsification: the three readouts correlate at r > 0.8 (collapsing to one measure).

**Experiment 13: Baseline-rigidity-as-moderator design.** Pre-stratify a psychedelic-intervention cohort by baseline rigidity of state-sequence dynamics (HMM dwell-time persistence, fMRI return-to-task-set, HRV recovery τ). Prediction: subjects with greater baseline rigidity show larger absolute improvements in both the residence readout and clinical response, supporting the framework's prediction that the residence-pathology dimension explains heterogeneity of response. Falsification: baseline rigidity does not moderate response.

### 11.3 Tractability summary

Experiments 1, 3, 4, 8, 10, 12, 13 are tractable with current technology in mid-sized academic-cohort designs (n = 60-200). Experiments 2, 5, 6, 7, 11 require larger cohorts or multi-site coordination but do not require new instrumentation. Experiment 9 requires medicinal-chemistry pre-work to develop or identify the matched-exposure varied-k_off panel and is therefore the most tractability-bounded of the agenda.

## 12. Implications

### 12.1 Therapeutics

The framework reframes therapeutic intent across substrates as residence-control rather than as substance-control. Restore return-path machinery wherever it has failed; abolish pathological residence on either the state-axis or the compartment-axis. The five symmetric strategies (§5) — extending native dwell, destabilizing pathological dwell, rerouting away from pathological compartment, rerouting toward protective compartment, restoring return-path machinery — organize the design space for any specific intervention.

The most important translational caution must be stated explicitly: identifying the principle correctly does not guarantee that any specific intervention based on it will work. Target engagement, timing, leverage, and substrate-specific physiology all matter independently. The arimoclomol ORARIALS-01 phase 3 trial in ALS is a warning case: a residence-targeting intervention with strong mechanistic rationale failed at phase 3 despite passing earlier trials, and the failure cannot be read as falsifying the residence-pathology framework, only as demonstrating that mechanistic correctness is necessary-but-not-sufficient for clinical efficacy. This warning generalizes — the framework predicts where to look, not what to do.

Intervention-convergence (Experiment 7) provides the empirical handle: if substrate-specific interventions converge on the cross-substrate composite readout, the residence-pathology principle is corroborated even when any single intervention fails. The principle does not stand or fall on the success of any one drug, biofeedback protocol, or stimulation paradigm; it stands or falls on whether residence-pathology measurements track clinical course and intervention response in the predicted way.

### 12.2 Diagnostics

Measure R(s, c) and recovery time constants before structural aggregation markers, which are downstream. The framework predicts that residence-pathology readouts will outperform structural markers at early and pre-symptomatic stages of disease. This has direct application to neurodegenerative disease, where structural markers (plaques, tangles, aggregates) are by the time of detection already late-stage manifestations of years-to-decades of upstream residence-pathology. The same logic applies to depression (early-warning before relapse; Experiment 5), to autonomic / cardiac disease (HRV degradation as years-earlier warning of cardiovascular event; conceded from Framingham), and to cognitive aging (return-path-machinery composite as years-earlier warning of clinical decline).

The Substrate-General Audit-Design Template (§10) gives the publication standard for residence-pathology diagnostic claims, intended to mature this clinical use-case in the same way Copeland's pharmacological audit-design matured pharmacology.

### 12.3 Disease classification

Group disorders by their residence-axis signature plus return-path-machinery failure profile rather than by aggregate morphology or single-time-point biomarker. Concretely: a single subject with depression, family history of cardiovascular disease, and elevated proteostatic stress markers, all converging on slow recovery time constants across substrates, is more usefully classified as a pan-substrate-return-path-failure case than as comorbid-depression-plus-cardiovascular-risk-plus-proteostatic-pathology. The classification has therapeutic implications (multi-substrate intervention with convergent endpoint readouts) and prognostic implications (cross-substrate composite as integrated risk profile).

This is a re-organization rather than a re-naming. The existing diagnostic categories continue to identify subgroups within the cross-substrate composite; the composite organizes the categories. Group-level diagnostic stratification by residence-axis signature provides the missing structural axis for explaining heterogeneity of intervention response and disease trajectory within named categories.

### 12.4 Research methodology

The framework predicts that cross-substrate experimental designs (Experiments 1, 6, 7) will produce more replicable, more powerful results than single-substrate designs, because cross-substrate composites integrate over substrate-specific noise and reflect the substrate-general residence-pathology dimension directly. If correct, this implies a research-methodology shift: multi-substrate cohorts measured across substrates per subject become the canonical experimental design, with single-substrate work used for mechanism-elucidation rather than for primary endpoints. This methodological shift is the framework's most consequential research-program-level implication.

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

**v1 progress as of 2026-05-12 04:xx PDT:**

All fourteen sections drafted in full first-draft prose. Abstract, §1 introduction, §2 formal observable, §3 four canonical disease cases, §4 cross-class unifying claim, §5 symmetric kinetic-stabilization formulation, §6 return-path-machinery typology, §7 frustration-without-escape, §8 cross-substrate extensions (eight substrates plus synthesis), §9 differentiation from adjacent literature, §10 audit-design template, §11 thirteen-experiment cross-domain agenda, §12 implications across therapeutics / diagnostics / classification / methodology, §13 non-goals, §14 deferred-companion-paper acknowledgment.

**Remaining work toward v1 final:**

- Internal review pass for citation completeness and tightness
- Reference list consolidation — every cited work in the running text needs a complete reference entry at submission time
- Substrate-specific terminology audit (consistency of "residence-pathology", "return-path machinery", "coupling-failure")
- Section-length rebalancing (§8 may be too long; §4 may be too short)
- Figure plan: candidate figures include the two-axis observable schematic, the four-case occupancy quartet visualization, the cross-substrate residence-pathology grammar table, the return-path machinery typology table, and the experimental-agenda dependency graph
- Companion-paper plan: Paper 15 (G₂ / octonion mathematical-physics) outlined separately in `outbox/syntheses/lane_cp5_octonion_coupling/` with three deliverable burden specified in §14 above

**Review cycle:** v1 goes to courtesy-preprint Tier A (11 names) two weeks before submission; Tier B (7 names) one week before; revisions incorporated as v1.1; then journal submission. The differentiation section (§9) is structured to anticipate the most likely critic-readings before they arrive.

**Submission targets to evaluate:** *Trends in Cognitive Sciences*, *Nature Reviews Drug Discovery*, *Nature Reviews Neuroscience*, *Cell Systems*, *PLOS Computational Biology*. Trade-off between cross-substrate-scope journals (TICS, Cell Systems) and substrate-specific journals (NRDD for the pharmacological / proteostatic emphasis, NRN for the brain-network emphasis); decision to be made after internal-review pass.
