# Lane 3: Proteostasis Literature Prior-Art Survey

**Source:** ChatGPT Pro Deep Research (adversarial review), 2026-05-09
**File:** `Pathology-as-Residence-Time_-A-Cross-Silo-Prior-Art-Survey-of-Proteostasis-Literature.pdf`
**Prompt:** Survey proteostasis literature for prior art of the claim
"pathology = residence where transits were design intent." Run in
adversarial mode against the thesis; prioritize math papers for the
"have they written it" check; include condensate / biomolecular-
condensate literature (Hyman, Brangwynne, Alberti) as part of the
scope but distinct from classical amyloid/prion work.

## Headline finding

**Partially anticipated in four silos; never unified. The unifying
statement + formal observable is the gap.**

The thesis has been stated:
- **Tier 1 within condensate silo:** Patel 2015 ("aberrant phase
  transitions lie at the heart of ALS"), Wolozin & Ivanov 2019
  ("SGs supposed to be transient... chronic persistent SGs"),
  Vanderweyde 2012 ("transient reversible SG formation necessary...
  hyperactive response leads to persistent SGs"), Zhang 2019
  ("chronic persistent or chronic intermittent SG assembly is
  intrinsically cytotoxic").
- **Tier 1 for IDR abundance:** Babu et al. 2011 — "IDPs must be
  available in appropriate amounts and not present longer than
  needed."
- **Tier 1 for one QC subsystem:** Alberti et al. 2017 coined
  "granulostasis" for the HSPB8-BAG3-HSP70 system.
- **Implicit in kinetic stabilization:** Kelly (tafamidis, PNAS
  2012), Knowles-Vendruscolo-Dobson "protein metastasis" /
  "supersaturation" (Nat Rev Mol Cell Biol 2014) — but opposite
  directionality (extending native residence rather than abolishing
  pathological residence).
- **Adjacent in gatekeeper residues:** Rousseau/Schymkowitz/Serrano
  TANGO/WALTZ — "safeguards against aggregation" — framed as
  entry-prevention, not exit-enforcement.
- **Adjacent in frustration theory:** Wolynes/Ferreiro — framed as
  altered *state patterns*, not altered *residence patterns*.
  "Frustration without escape" is explicitly NOT in the literature.
- **Adjacent in active matter:** Jülicher/Hyman/Weber non-equilibrium
  maintenance of transient states = the visits-regime at the physical
  level, but framed as physics not disease principle.

**No paper makes the cross-silo unifying claim.** Each silo has its
own local version. The Paper 14 contribution is the unification
plus the formal observable τ_R(s), not the residence-pathology
insight per se.

## Five explicit gaps the report identifies

1. A single principle statement that pathology in proteostasis
   disease is the temporal occupancy pattern of states whose
   transient sampling is the design intent — applicable to IDR
   ensembles, chaperone/QC cycles, condensate aging, amyloid
   metastability, and specific substrates (PrP, α-synuclein, tau,
   huntingtin, TDP-43, FUS).

2. A formal observable: τ_R(s) — residence-time metric on a Markov
   state model of native dynamics that distinguishes physiological
   visits from pathological residence as the primary disease
   variable. MSM machinery exists (Pande, Noé, Husic; Löhr 2021;
   Tancredi 2024) but has never been deployed as a disease-
   classification axis.

3. Symmetric formulation of kinetic stabilization: not just
   "stabilize native to extend visit" (Kelly) but also "destabilize
   pathological state to abolish residence" — unified rate-equation
   framework where both are residence-time interventions.

4. Reframing of HSP70 ATP-cycling, HSP90 client-dwell, UPS turnover,
   autophagy clearance, granulostasis, HSR/UPR/ISR as a single
   class: *non-residence enforcement machinery* with a common
   observable.

5. Extension of Wolynes/Ferreiro frustration theory to "frustration
   without escape" — physiological frustration becomes pathological
   when the system cannot escape a frustrated micro-minimum. Not
   stated in the frustration literature.

## Paper 14 structure recommended by the report

1. Frame as unification paper, not discovery paper.
2. Open by quoting Patel 2015 and Babu 2011 in the first three
   paragraphs. Acknowledge as strongest existing Tier-1 anchors.
   Then argue they are coordinate instances of one unarticulated
   principle.
3. §2 provides the master formalism: define τ_R(s), define design-
   intent τ_R bounds as evolved/network-imposed escape rates,
   define pathological regime as τ_R(s) escaping those bounds
   while s itself is unchanged. Build on Powers/Powers/Gierasch
   FoldEco (2012) for network rate-equation scaffold; Löhr 2021 /
   Tancredi 2024 for dwell-time distribution apparatus.
4. Apply to four canonical cases spanning all four tracks:
   - FUS in stress granules (Track 3 — strongest validation)
   - Huntingtin exon 1 in polyQ (Track 4 — Wolynes aggregation
     funnel)
   - HSP70/HSP90 client-dwell failure in chaperonopathy or
     α1-antitrypsin Z (Track 2)
   - Tau or α-synuclein conformational ensemble (Track 1)
5. Pre-empt "frustration without escape" objection by extending it
   explicitly. Send courtesy preprint to Ferreiro and Wolynes.
6. Differentiate aggressively from Kelly kinetic stabilization —
   the user's thesis is symmetric; pathology is ANY residence-
   where-transit-intended, not just inverse of native stabilization.

## Key cited Tier-1 anchors with DOIs

**Two-axis statements (closest combined prior art — ChatGPT survey):**
- Pytel & Fromm Longo 2025, *Am J Pathol*,
  doi:10.1016/j.ajpath.2025.07.011 (proteostasis network governs
  "timing, location, and stoichiometry" — names two of three axes)
- Bertolotti 2018, *Curr Opin Neurobiol*,
  doi:10.1016/j.conb.2018.03.004 (subcellular location of protein
  deposits)
- Kumar & Lapierre 2021, *Biophys Rev*,
  doi:10.1007/s12551-021-00890-x (dynamic protein partitioning)
- Giandomenico et al. 2022, *Trends Neurosci*,
  doi:10.1016/j.tins.2021.08.002 (compartment-specific neuronal
  proteostasis)

**Disease-class spatial-residence anchors (ChatGPT survey):**

*Amyloid — endocytic itinerary:*
- Koo & Squazzo 1994, doi:10.1016/S0021-9258(17)32449-3
- Gouras et al. 2000, PMID 10623648 (intraneuronal Aβ42)
- Das et al. 2013, PMID 23931995 (APP/BACE1 acidic-microdomain
  convergence)
- Roselli et al. 2023, doi:10.1007/s10571-023-01374-0
- Del Prete et al. 2017, PMID 27911326 (MAM/mitochondrial APP)

*Prion — topology and GPI anchoring (cleanest causal-localization
literature in all of neurodegeneration):*
- Hegde et al. 1998, PMID 9452375 (transmembrane PrP → disease)
- Chesebro et al. 2005, PMID 15933194 (anchorless PrP → amyloid
  without scrapie)
- Solomon et al. 2011, doi:10.1074/jbc.M110.214973 (mutant PrP
  toxicity requires plasma-membrane localization)
- Fehlinger et al. 2017, doi:10.1038/s41598-017-07260-2 (prion
  strain endocytic-route specificity)
- Gatdula et al. 2026, doi:10.1371/journal.ppat.1013911 (membrane-
  anchored PrP^Sc → synaptotoxicity)

*Tauopathy — multi-compartment mislocalization:*
- Ittner et al. 2010, doi:10.1016/j.cell.2010.06.036 (dendritic tau
  mediates Aβ toxicity)
- Hoover et al. 2010, PMID 21172610 (tau mislocalization to
  dendritic spines causes synaptic dysfunction)
- Ash et al. 2021, doi:10.1073/pnas.2014188118 (TIA1 potentiates
  tau phase separation)
- Lester et al. 2021, PMID 33848474 (tau aggregates as RNA-protein
  assemblies mislocalizing nuclear speckle components)
- Yuan et al. 2026, doi:10.1007/s00401-026-02979-7 (oligomeric tau
  → nuclear lamina invagination)

*PolyQ — NLS/NES targeting (cleanest class-wide localization
proof in neurodegeneration):*
- Saudou et al. 1998, PMID 9778247 (mutant huntingtin acts in the
  nucleus)
- Klement et al. 1998, PMID 9778246 (ataxin-1 nuclear localization
  required)
- Montie et al. 2009, PMID 19279159 (cytoplasmic retention of
  polyQ-AR ameliorates SBMA via autophagy)
- Simões et al. 2012, doi:10.1093/brain/aws177 (calpain inhibition
  prevents ataxin-3 nuclear localization)
- Yablonska et al. 2025, PMID 39779371 (N17 phosphorylation
  regulates mutant huntingtin mitochondrial targeting)
- Villavicencio Gonzalez & Zoghbi 2026, doi:10.1084/jem.20241336
  (recent class-level synthesis)

**ChatGPT proposed canonical statement (verbatim, p. 10):**

> "In proteinopathies, pathology is determined not only by which
> protein misfolds, but by where that protein resides and how long
> it dwells there: compartmental residence selects the local
> interactome, biophysical regime, and proteostasis machinery that
> convert the same precursor or conformer into a tolerated, cleared,
> propagating, or toxic species. Proteostasis pathways are therefore
> disease-modifying chiefly by controlling protein residence —
> routing proteins toward compartments that favor folding,
> sequestration, or clearance and away from compartments that license
> aberrant cleavage, templating, signaling, organelle damage, or
> spread."

This is a candidate-statement Paper 14 can build on. It already
combines spatial ("where that protein resides") and temporal ("how
long it dwells there") residence into a single sentence. Paper 14's
novelty is the formal observable + the cross-domain extension to
non-proteostasis substrates (pharmacology, fitness, phenomenology).

**Condensate silo (closest temporal-axis prior art — Claude survey):**
- Patel et al. 2015, *Cell*, doi:10.1016/j.cell.2015.07.047
  ("aberrant phase transitions lie at the heart of ALS")
- Wolozin & Ivanov 2019, *Nat Rev Neurosci*,
  doi:10.1038/s41583-019-0222-5
- Vanderweyde et al. 2012, *J Neurosci*,
  doi:10.1523/JNEUROSCI.1870-12.2012
- Zhang et al. 2019, *eLife*, doi:10.7554/eLife.39578 (experimental
  decoupling proving residence-as-pathology)
- Alberti & Hyman 2021, *Nat Rev Mol Cell Biol*,
  doi:10.1038/s41580-020-00326-6
- Alberti & Dormann 2019, *Annu Rev Genet*,
  doi:10.1146/annurev-genet-112618-043527
- Mittag & Pappu 2022, *Mol Cell*, doi:10.1016/j.molcel.2022.05.018
  (PSCP formal timescale-decoupling framework)
- Hughes & Eisenberg 2018, *Nat Struct Mol Biol*,
  doi:10.1038/s41594-018-0064-2 (LARKS vs zippers — residence-vs-
  visit at atomic structural level)

**IDR / IDP silo:**
- Babu et al. 2011, *Curr Opin Struct Biol* 21:432,
  doi:10.1016/j.sbi.2011.03.011 ("not present longer than needed")

**QC / chaperone silo:**
- Alberti, Mateju, Mediani, Carra 2017, *Front Mol Neurosci*,
  doi:10.3389/fnmol.2017.00084 ("granulostasis")
- Mateju et al. 2017, *EMBO J*, doi:10.15252/embj.201695957
- Balch, Morimoto, Dillin, Kelly 2008, *Science*,
  doi:10.1126/science.1141448 (founding proteostasis network paper)
- Powers, Powers & Gierasch 2012, *Cell Rep*,
  doi:10.1016/j.celrep.2012.02.011 (FoldEco master-equation model)
- Tancredi et al. 2024, *New J Phys* 26:073023,
  doi:10.1088/1367-2630/ad5def (Hsp90 HMM dwell-time distributions)

**Kinetic stability axis (implicit, opposite directionality):**
- Bulawa, Kelly et al. 2012, *PNAS*,
  doi:10.1073/pnas.1121005109 (tafamidis kinetic stabilization)
- Knowles, Vendruscolo, Dobson 2014, *Nat Rev Mol Cell Biol*,
  doi:10.1038/nrm3810 (protein metastasis / supersaturation)
- Vendruscolo, Knowles, Dobson 2011, *Cold Spring Harb Perspect
  Biol*, doi:10.1101/cshperspect.a010454

**MSM / kinetic apparatus (formal scaffold):**
- Löhr, Kohlhoff, Heller, Camilloni, Vendruscolo 2021,
  *Nat Comput Sci* 1:71–78, doi:10.1038/s43588-020-00003-w
  (VAMPNet/Koopman MSM of Aβ42)

## Benchmarks that would change the recommendation

- If Tier-1 cross-silo statement found in specialty subfields
  (serpinopathies, CFTR ER-residence, Gaucher's GBA, ferritin/prion-
  strain) — reduce novelty claim from "first articulation" to
  "extension and formalization."
- If pre-2026 Vendruscolo/Pappu/Hyman/Alberti/Wolynes review lays
  out the cross-silo claim explicitly — pivot Paper 14 to formal
  MSM observable + daemon-architecture / G₂ framing instead.
- If active-matter literature (Jülicher, Weber) has cast disease as
  "loss of dissipative residence prevention" — cite as Tier-2 and
  differentiate by biological/clinical generalization.

## Caveats flagged by the report

- Coverage: ~25 query lines; specialty subfields (serpinopathies
  kinetic trap, CFTR ER residence, Gaucher's lysosomal residence,
  β-thalassemia, lipid-droplet aging) not exhaustively covered.
- Frustration literature may contain unindexed conference talks /
  book chapters with "frustration without escape" verbatim — search
  Wolynes CTBP talks and Ferreiro preprints before final submission.
- PolyQ huntingtin/ataxin literature (Wetzel, Wolynes/Schafer/Zheng,
  Lashuel/Pappu) rich in transient-vs-persistent oligomer kinetics
  but not cast as residence-time pathology — gap supports novelty
  but check 2024–2026 reviews.
- Tier classifications are judgment calls.

## Connection to framework artifacts

- `outbox/syntheses/lane2_residence_time_pharmacology/` — pharmacology
  silo, Copeland visits-vs-residence framework, anchor for
  substrate-independent validation.
- `outbox/syntheses/flow_grind_synthesis.md` — cross-domain table
  connecting framework §3.5/§3.6, exercise, pharmacology, and now
  proteostasis.
- `outbox/syntheses/cross_domain_saturation_collapse.md` — fitness /
  cardiac domain with literature backing.
- Paper 12 v1.4 — substrate-side demonstration of §3.5/§3.6 topology.
- Paper 14 — cross-domain unification (now draftable at full scope
  with pharmacology anchor + proteostasis silos + framework topology).
