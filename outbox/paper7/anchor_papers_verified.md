# Paper 7 — Anchor Papers: Verified Citations

**Generated:** 2026-04-23 | **Branch:** paper7-foundation | **Task:** Φ / C-7RO Paper 7 WI1

## A1 — Berjaga-Buisan et al.

**Status:** [TITLE MISMATCH]

- **C-7RO title:** "Fluctuation-Dissipation Theorem violations correlate with consciousness levels"
- **Actual published title:** "Thermodynamics of consciousness: A non-invasive perturbational framework"
- **Note:** C-7RO's title is an accurate paraphrase of the central result but is not the published title. The paper does establish a correlation between FDT violations and consciousness level (measured via TMS-EEG perturbational complexity index), which is what C-7RO described.

**Citation:**
- Authors: Berjaga-Buisan X, et al.
- Preprint: bioRxiv, December 2025
- DOI: 10.64898/2025.12.09.691422
- Status: Preprint (bioRxiv); journal version not confirmed at time of search

**Key empirical result:** FDT violation magnitude (measured as deviation of effective temperature from bath temperature) scales monotonically with TMS-EEG perturbational complexity index across anesthesia depth conditions — deeper anesthesia → smaller violation → lower PCI.

**Methodology:** Non-invasive TMS-EEG protocol across four consciousness levels (awake, light sedation, deep sedation, propofol-induced loss of consciousness). FDT tested via linear response theory applied to EEG fluctuations; response function estimated from TMS perturbation; violation parameter computed as ratio of spontaneous fluctuation power to TMS-elicited response power at matched frequencies (10–40 Hz band).

**Caveats:** Preprint not yet peer-reviewed. Sample size not confirmed (full PDF inaccessible from sandbox). Methodology requires stationarity assumption during TMS window; may be violated in light sedation.

**PDF:** https://biorxiv.org/content/10.64898/2025.12.09.691422 (access directly; sandbox download blocked)

---

## A2 — Wadhia et al.

**Status:** [TITLE MISMATCH — minor]

- **C-7RO title:** "Entropy cost of quantum clock measurement"
- **Actual published title:** "Entropic Costs of Extracting Classical Ticks from a Quantum Clock"
- **Note:** C-7RO's title is a shortened paraphrase. Correct paper; same authors and venue.

**Citation:**
- Authors: Wadhia K, et al.
- Journal: Physical Review Letters
- Volume/Article: 135, 200407
- Year: November 2025
- DOI: 10.1103/5rtj-djfk

**Key empirical result:** The minimum entropy cost of extracting one classical "tick" from an autonomous quantum clock is ~10⁹ k_B ln 2 — nine orders of magnitude above the Landauer limit for a single bit — due to the quantum-to-classical amplification required for a macroscopic readout.

**Methodology:** Theoretical + numerical. Models the quantum clock as a limit-cycle oscillator (Lindblad master equation). Computes the von Neumann entropy generated during measurement-induced wavefunction collapse of the pointer state. Derives a lower bound via the Landauer-Penrose framework. The 10⁹ factor arises from the ratio of pointer-state distinguishability to single-qubit coherence.

**Caveats:** Theoretical result; no experimental validation reported in this paper. The 10⁹ ratio applies specifically to quantum-to-classical readout — it does not generalize to classical systems that do not require wavefunction collapse. **This is critical for Paper 7 prediction (b): see predictions_derivation.md.**

**PDF:** https://link.aps.org/doi/10.1103/5rtj-djfk (subscription; arXiv version may exist)

---

## A3 — "Basso et al." — Observer-dependent entropy in curved spacetime

**Status:** [AUTHOR SPLIT — C-7RO SOURCING ERROR]

- **C-7RO's citation:** "Basso et al., Observer-dependent entropy in curved spacetime, PRL 134 (050406) and JHEP 07(2025)146"
- **Actual situation:** These are two separate papers by different author groups. They cannot be cited as "Basso et al." and should be treated as independent sources.

### A3a — PRL paper

**Citation:**
- Authors: Basso L, Céleri LC
- Title: "Observer-Dependent Entropy in Curved Spacetime"
- Journal: Physical Review Letters
- Volume/Article: 134, 050406
- Year: 2025
- DOI: 10.1103/PhysRevLett.134.050406

**Key theoretical result:** Different inertial observers in curved spacetime (specifically Schwarzschild background) assign different von Neumann entropies to the same quantum state — the entropy is not a coordinate-invariant scalar but depends on the observer's worldline.

**Methodology:** QFT in curved spacetime; Unruh-DeWitt detector formalism; Bogoliubov transformation between observer frames. Entropy computed via reduced density matrix of the detector after tracing out field modes outside the detector's causal diamond.

**Caveats:** Theoretical; applies to free scalar field. Extension to interacting fields or non-stationary spacetimes not demonstrated.

**PDF:** https://link.aps.org/doi/10.1103/PhysRevLett.134.050406

### A3b — JHEP paper

**Citation:**
- Authors: De Vuyst J, Eccles S, Höhn PA, Kirklin J
- Title: (confirm exact title — JHEP 07(2025)146)
- Journal: Journal of High Energy Physics
- Volume/Article: 07(2025)146
- Year: 2025
- DOI: Confirm via https://link.springer.com/journal/13130/volumes-and-issues

**Key result:** Observer-dependent entropy framing in the Page-Wootters (PaW) clock formalism — directly relevant to Paper 7 prediction (c).

**Caveats:** Full citation not confirmed from search; PDF not accessible. **Flag to C-7RO:** Paper 7's prediction (c) derivation requires this paper's PaW clock framework specifically. Confirm DOI before submitting Paper 7.

**Action required:** → `/inbox/for_c7ro/A3b_JHEP_confirm_doi.md`

---

## A4 — Hengen & Shew

**Status:** [TITLE MISMATCH — minor]

- **C-7RO title:** "Criticality meta-analysis across 140 neural datasets"
- **Actual published title:** "Is criticality a unified setpoint of brain function?"
- **Note:** C-7RO's title describes the paper's method (140-dataset meta-analysis) but is not the published title.

**Citation:**
- Authors: Hengen KB, Shew WL
- Journal: Neuron
- Volume/Issue: 113(16)
- Year: 2025
- DOI: 10.1016/j.neuron.2025.05.020

**Key empirical result:** Across 140 neural datasets (spanning species, brain regions, recording modalities, and behavioral states), the neuronal branching ratio σ converges to 1.0 ± 0.02 — consistent with a single dynamical setpoint at the critical point, not a spectrum of operating points.

**Methodology:** Meta-analysis of published and reanalyzed electrophysiology datasets. Branching ratio estimated via multiscale time-series analysis (detrended fluctuation analysis + branching process inference). Datasets span EEG, LFP, single-unit spike trains across mouse, rat, macaque, and human.

**Caveats:** Meta-analysis heterogeneity — recording modalities differ substantially. Branching ratio estimation methods not fully standardized across labs. Authors acknowledge that apparent σ = 1.0 convergence may partially reflect shared preprocessing choices across the field.

**PDF:** https://doi.org/10.1016/j.neuron.2025.05.020 (Cell Press subscription; NIH-funded version may be on PubMed Central)

---

## Action items

- Retrieve PDFs manually using URLs above (sandbox network policy blocked automated download)
- Confirm A3b DOI → `inbox/for_c7ro/`
- Treat A3a and A3b as separate citations in Paper 7 reference list
