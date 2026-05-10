# Paper 14 Outline: Two-Axis Residence-Pathology Unification

**Status:** Draft outline, ready for v1 drafting.
**Date seeded:** 2026-05-09
**Inputs:**
- `outbox/syntheses/lane2_residence_time_pharmacology/` (Copeland anchor)
- `outbox/syntheses/lane3_proteostasis_residence_time/` (both Claude temporal + ChatGPT Pro spatial surveys)
- `outbox/syntheses/flow_grind_synthesis.md` (cross-domain synthesis)
- `outbox/syntheses/cross_domain_saturation_collapse.md` (exercise/cardiac)
- Paper 12 v1.4, §3.5 / §3.6 boundary-KKT result (substrate-side demonstration)

## Working title

"Residence Where Transits Were Design Intent: A Two-Axis Formal
Observable for Cross-Class Pathology"

Alternate: "The Visits-Versus-Residence Principle Across Proteostasis,
Pharmacology, Exercise Physiology, and Phenomenology"

## One-sentence thesis

Pathology in any system with both regimes available to it is the
temporal-and-spatial residence pattern of states whose transient
sampling is the design intent, not the identity of the states
themselves.

## Structure

### §1 Introduction: four Tier-1 anchors and the unification gap

Open by quoting four existing Tier-1 statements that cover the
principle axis-by-axis but have never been unified:

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

Argue that these are axis-specific and silo-bound instances of one
two-axis principle. Acknowledge the prior art explicitly. Identify
the gap: no cross-class unifying statement, no formal observable.

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

### §6 QC machinery reframed as non-residence enforcement

The proteostasis field treats HSP70 ATP-cycling, HSP90 client-dwell,
UPS turnover, autophagy clearance, granulostasis, HSR/UPR/ISR as a
heterogeneous toolkit. Paper 14 reframes them as a single class:
non-residence enforcement machinery with a common observable
(residence half-life of pathological-state-shaped substrates).

Extend this to spatial machinery: ERAD, endolysosomal sorting,
NLS/NES systems, nuclear pore complex, mitochondrial import control.
Same class: non-residence enforcement on the spatial axis.

Granulostasis (Alberti et al. 2017) is currently the only named
instance. Paper 14 names the full class.

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

### §8 Cross-domain extension — the substrate-independence claim

This is what distinguishes the framework's unification from any
unification paper that could come out of a single proteostasis silo.

**8.1 Pharmacology.** Copeland residence-time paradigm at receptors
(Tummino & Copeland 2008; Bosma 2017 H1; Casarosa 2009 M3 LAMA;
Vauquelin rebinding work). The visits-vs-residence distinction is
already explicitly named in pharmacology; drug-receptor kinetics is
the same principle on a different substrate.

**8.2 Exercise physiology.** Endogenous boundary operation (visits
with intact feedback → healthy athlete's heart) vs operator-sustained
boundary operation (pharmacological feedback bypass → arrhythmia
phenotype). See `cross_domain_saturation_collapse.md`.

**8.3 PCI phenomenology.** §3.5 smooth-interior / §3.6 boundary-
KKT residence (Paper 12 v1.4) for tear topology. Phenomenologically:
flow = brief §3.6 touches; rumination / depression = §3.6 residence
without §3.5 recovery.

The residence-pathology principle is substrate-independent: wherever
a dynamical system has both regimes available to it plus return-path
machinery, pathology is that machinery failing, not the system
visiting where it shouldn't.

### §9 Differentiation from adjacent literature

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

### §11 Implications

- **For therapeutics:** restore return-path machinery; abolish
  pathological residence on either axis.
- **For diagnostics:** measure \( R(s, c) \) before structural
  aggregation markers (which are downstream).
- **For disease classification:** group proteinopathies by their
  residence-axis signature rather than by aggregate morphology.

### §12 Non-goals

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
