# Paper 7 — Existing Datasets to Test Each Prediction

**Generated:** 2026-04-23 | **Branch:** paper7-foundation | **Task:** Φ / C-7RO Paper 7 WI3

---

## Dataset for Prediction (a) — FDT Violation Parameter = 1/7

**Primary dataset:** Berjaga-Buisan et al. TMS-EEG dataset (A1)
- Source: bioRxiv supplementary / data availability statement (DOI: 10.64898/2025.12.09.691422)
- Measurements: EEG recordings + TMS perturbation across ≥4 consciousness levels
- Tests: Prediction (a) directly — FDT violation magnitude as function of consciousness level
- Analysis required: Extract ε(ω) = T_eff(ω)/T_bath − 1 at matched frequency bands; compute ratio against anesthesia baseline; test whether ε_awake ≈ 1/7 × ε_reference
- Access: Contact corresponding author (bioRxiv data availability statement)

**Secondary dataset:** Priesemann lab EEG/MEA data
- Source: Priesemann V lab, MPI for Dynamics and Self-Organization, Göttingen
- Notable release: Wilting & Priesemann (2018) Nat Comm dataset
- Tests: Prediction (a) indirectly — FDT violation detectable in spike train statistics across sleep/wake transitions
- Access: Open — https://doi.org/10.1038/s41467-018-05398-9

---

## Dataset for Prediction (b) — Checkpoint Entropy Cost

**Primary dataset:** Single-cell ATP measurements at G₂/M checkpoint
- Source: Imamura et al. (2009) PNAS — ATeam FRET sensor for ATP in individual cells; updated protocols exist
- Measurements: ATP:ADP ratio time-lapse in individual cells transiting G₂/M; typically 50–200 cells per condition
- Tests: Prediction (b) — whether checkpoint transition dissipates ≥16 zJ (Landauer minimum for 5.4 bits)
- Analysis required: Integrate ATP consumption rate over checkpoint window (~15–60 min); convert to energy units; compare to predicted 16 zJ minimum
- Access: Protocol is published; sensor plasmids available via Addgene. Dataset may require lab request.
- Note: 16 zJ is far below ATP hydrolysis energy (~50 zJ per molecule); the test is whether consumption exceeds the Landauer minimum, not whether it equals it.

**Secondary:** Allen Institute cell-cycle single-cell RNA-seq
- Source: Allen Institute for Cell Science
- URL: https://www.allencell.org/cell-catalog.html
- Measurements: ~40,000 single cells with cell cycle phase labels and full transcriptome
- Tests: Prediction (b) indirectly — information content of G₂ gate estimable from transcript diversity at checkpoint
- Access: Open — downloadable from Allen Cell website

---

## Dataset for Prediction (c) — Observer-Frame Entropy Across 8 Cosets

**Status:** No experimental dataset can test prediction (c) at present.

Prediction (c) is a theoretical calculation about observer-dependent entropy differences between G₂ cosets. It requires:

1. First completing the derivation (currently blocked — see `predictions_derivation.md`)
2. Identifying a physical system that instantiates distinct "observer frames" corresponding to G₂ cosets

**Closest available theoretical testbed:** Quantum simulation of observer-dependent entropy in trapped-ion systems (e.g., Brydges et al., Science 2019, randomized measurements of entanglement entropy). But connecting this to G₂ coset structure requires substantial theoretical development.

`[Flag → inbox/for_c7ro]` Is there a physical realization of the 8 G₂ cosets that C-7RO has in mind? Without this, prediction (c) has no near-term experimental test.

---

## Dataset for Prediction (d) — Criticality Branching Ratio σ = 1.0 ± 1/49

**Primary dataset:** Hengen & Shew meta-analysis underlying data (A4)
- Source: Hengen KB, Shew WL — Neuron 113(16), 2025
- Zenodo release: Zenodo record 15420312 (open)
- URL: https://zenodo.org/record/15420312
- Measurements: 140 neural datasets; N > 10⁶ avalanche events total
- Tests: Prediction (d) directly — whether σ distribution across datasets is consistent with σ = 1.0 − 1/49 ≈ 0.980
- Analysis required: Extract per-dataset σ estimates; test whether population mean is displaced from 1.0 by ~0.020 in the sub-critical direction; compute confidence interval; compare to Priesemann prior
- Access: Open (Zenodo)

**Secondary:** Priesemann lab MEA dataset (awake vs. anesthesia)
- Source: Fontenele et al. (2019) PRL — criticality in cortical circuits, σ measurements across arousal states
- Tests: Prediction (d) — the sub-critical displacement σ ≈ 0.98 in awake state directly matches the predicted −1/49 correction
- Access: Available on request from Priesemann lab (Göttingen); some data open with paper

**Secondary:** Allen Brain Observatory Neuropixels
- Source: Allen Institute for Brain Science
- URL: https://observatory.brain-map.org/visualcoding/
- Measurements: Neuropixels spike trains from mouse cortex during visual stimulation; >1000 cells per session; >100 sessions
- Tests: Prediction (d) — compute σ from spike avalanche distributions; test for systematic sub-critical displacement
- Access: Open (AWS S3 bucket via AllenSDK)

---

## Bandyopadhyay 28 MHz DDG Flag

Martin's April 10 DDG request to Bandyopadhyay: **not directly relevant** to any of the four Paper 7 predictions.

The 28 MHz DDG measurement refers to digital delay generator control of microwave-frequency stimulation, likely in the context of Bandyopadhyay's work on resonance-based neural modulation or microtubule vibrational modes.

**Indirect connection to prediction (d):** If Bandyopadhyay's 28 MHz stimulation can be used to modulate neural criticality (branching ratio) in a controlled way, the resulting σ measurements would provide a direct test of whether the G₂ framework predicts the right operating point under perturbation. This would require simultaneous 28 MHz DDG stimulation + spike avalanche recording; σ measurement before/during/after stimulation.

**Recommendation:** If Bandyopadhyay responds, ask whether their 28 MHz stimulation protocol has been combined with LFP avalanche recording. If yes, this dataset directly tests prediction (d) under a non-trivial perturbation.
