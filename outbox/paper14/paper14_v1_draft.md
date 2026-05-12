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

[DRAFT CONTINUATION NOTE: The old scaffolding for sections 6 and
7 remains below in this file and should be cleaned up in a later
editing pass. Sections 6 and 7 above are the current v1 prose;
the material below starting with the old section 6 scaffolding is
superseded and should be deleted before submission. Section 8.7
prose for AI/data substrate was drafted in the 30e3681 commit and
appears further down in the file. This drafting session continues
with the other section 8 subsections.]

### 8.1 Pharmacology (Copeland lineage) — placeholder, drafted elsewhere

[Drafting continues from here in the next session. Sections 8.1–8.6
have scaffolding further down the file; 8.7 AI/data is drafted in
full prose; section 8.8 synthesis is short. Restructuring into
clean v1.1 order is a post-v1-complete editorial task.]

## [LEGACY SCAFFOLDING BELOW — DO NOT USE, SUPERSEDED BY §§5–7 ABOVE]

## 6. Return-Path Machinery as a Multiscale Class

[OLD SCAFFOLDING — superseded by §6 above. The proteostasis field treats HSP70 ATP-cycling,
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

[The memory subsection here will additionally cite Page & Wootters
1983 and the recent 2025 Page-Wootters extensions to gravitational
time dilation as orthodox physics-foundations prior art for the
claim that time is a coupling-derived rather than backdrop
phenomenon. This places memory-as-dimensional-tether in a mature
research context.]

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

**8.7 AI and data substrate — model collapse as return-path
failure.** Shumailov et al. (2024, *Nature* 631:755-759,
doi:10.1038/s41586-024-07566-y) demonstrated empirically that
generative models trained recursively on data produced by
previous model generations undergo *model collapse*: tails of
the original distribution disappear, learned behaviors converge
to a point-estimate with very small variance, and the process
is universal across GMMs, VAEs, and LLMs. Theoretical follow-up
(Ren 2024, arXiv:2410.12954) established that this is a
statistical phenomenon that may be unavoidable under recursive
generative training in the absence of corrective real-data
circulation.

Zheng & Yan (2026, arXiv:2605.06347) extended this analysis from
model-internal recursive training to *coupled* human-AI dynamics,
modeling humans and language models as a single coupled dynamical
system with three variables (human cognitive capacity H, data
quality Q, model capability M) and feedback loop H → Q → M → H.
They identify three regimes: co-evolutionary enhancement, fragile
equilibrium, and degenerative convergence, with the system
transitioning through a transcritical bifurcation as the
cognitive-offloading parameter increases. From an information-
theoretic perspective, the degenerative regime corresponds to an
emergent information bottleneck along the feedback loop, with
entropy reduction reflecting loss of diversity rather than
beneficial compression. This proposal — that human-AI coupled
dynamics exhibit three qualitatively distinct attractors with the
degenerative one driven by recursive feedback failure — is the
minimal-model version of the framework's residence-pathology
principle at the AI/data substrate.

The framework reads both findings as instances of return-path-
machinery failure on the AI/data coupling substrate. The "return
path" at this substrate is circulation of non-synthetic, world-
grounded data and intact human cognitive engagement into the
training distribution. When recursive synthetic generation
dominates and cognitive offloading rises, the return path fails;
the coupled system residences in a degraded attractor with
reduced variance and lost diversity. This is structurally
identical to canalization at the psychiatric substrate (chronic
residence in deepened attractor canals), aggregation-pathology at
the molecular substrate (chronic residence in pathological
conformational states), and operator-sustained boundary operation
at the cardiac substrate (chronic residence past return-machinery
cutoff). The same R(s,c) two-axis observable applies: states are
model-distribution configurations; compartments are training-
data regimes; pathology is residence in degraded configurations
with reduced support and lost tail mass.

The framework's therapeutic prescription at this substrate — 
restore the return-path circulation, audit the coupling, refuse 
the singularity attractor — is consistent with the mitigation 
strategies proposed independently by Zheng & Yan: improved data 
curation, human-in-the-loop system design, and educational 
practices that preserve active cognitive engagement. The 
framework adds: these are not separate interventions but 
coordinate instances of return-path-machinery restoration, with 
a common observable (recovery time constant of the coupled 
system's response to perturbation).

**8.8 Synthesis across the extensions.** One principle; nine
substrate instances; individual-level R(s,c) observable applicable
uniformly; residence-pathology symptom grammar substrate-uniform.
The AI/data substrate (§8.7) is the most recently added
demonstration and provides empirical clinical-grade evidence at
production scale that the framework's principle operates outside
the biological / cognitive substrates where it was first developed.

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
