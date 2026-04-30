# Bandyopadhyay DDG / Dodecanogram — Research Report

**Source:** ChatGPT GPT-5 Pro reasoning + GitHub connector + live browsing
**Date:** 2026-04-29
**Requested by:** C-7RO via Martin Luther Graise
**Target use:** Paper 7 FP-2 design / future replication protocol

---

## Headline corrections to working model

1. **"Dodeca" is literal but means 12 frequency bands / 12 discrete time regions / 12 orders of time-frequency coverage.** NOT 12-fold rotational symmetry, NOT 12 angular bins, NOT 12 electrodes.
2. **The natural microtubule resonance morphology is triplet-of-triplets (3×3), not 12-fold.** Saxena et al. 2020 (DOI 10.3390/fractalfract4020011) explicitly: "nine circles inside three circles inside one circle = 13 circles."
3. **8-fold structure IS present in the microtubule MHz band.** Eight exact peaks at {12, 20, 22, 30, 101, 113, 185, 204} MHz. Plus 45° phase quantization in the 10 kHz – 50 MHz range = an 8-bin phase circle.
4. **8 Hz, 8 MHz, exact 28 MHz are NOT supported by primary Bandyopadhyay data.** Closest supported anchors: 30 MHz (microtubule), 28 THz (tubulin). Drop "28 MHz" framing.
5. **DDG has no independent multi-lab replication.** Author group's own paper, lead editor of the special issue is Bandyopadhyay. Treat as primary not validation.

---

## Primary DDG paper

Singh et al., "Dodecanogram (DDG): Advancing EEG technology with a high-frequency brain activity measurement device," *Journal of Multiscale Neuroscience* 3(1), 13–26.
- DOI: 10.56280/1600841751 (Neural Press); also 10.48505/nims.5288 (CiNii/NIMS)
- Open access; special issue lead editor = Bandyopadhyay (note: NOT independent validation)
- Two-mode instrument:
  - **Resonance/radiation mode:** 6 THz to 1 mHz (note: 6 THz needs thermal camera — not one homogeneous electrode measurement)
  - **Picosecond pulse mode:** burst duration, intensity, phase variation
- **Hardware:** 34-channel logic analyzer (17 human + 17 artificial-brain reference), 17 coaxial cables A0–A15 + clock, Yagi-antenna-like probes
- **Shielding red flag:** "human movement restricted within 300 m radius," uses "strong probe amplification or room white noise to improve data" — a replication MUST treat shielding/noise/amp gain as explicit variables, not background

---

## Resonance peaks table (Sahu/Singh/Bandyopadhyay, *Sci Rep* 4:7303, DOI 10.1038/srep07303)

| System | Band | Peaks (exact) | Notes |
|--------|------|---------------|-------|
| Tubulin | MHz | 37, 46, 91, 137, 176, 281, 430 | 7 peaks — superficial 7-fold hook only |
| Tubulin | GHz | 9, 19, 78, 160, 224 | 5 peaks |
| Tubulin | THz | 28, 88, 127, 340 | **28 THz, NOT 28 MHz** |
| Microtubule | kHz | 120, 240, 320 | 3 peaks, ratios 1:2:2.67, Q ~ 3–5 |
| Microtubule | MHz | **12, 20, 22, 30, 101, 113, 185, 204** | **8 peaks**, sharp Q ~ 100–300 |
| Microtubule | GHz | 3, 7, 13, 18 | 4 peaks |

**The microtubule MHz band is the FP-2 anchor.** Eight peaks + 45° phase quantization + Q ~ 100–300 + water-resonance-free regime.

---

## What the data does and does NOT support

**Supported:**
- Triplet-of-triplets morphology (3×3 = 9, plus container)
- 8 microtubule MHz peaks
- 45° phase quantization in 10 kHz – 50 MHz (literally 8-bin phase circle)
- Tubulin monomer "4 major + 4 minor potential regions = 8 for dimer"

**NOT supported:**
- Exact 8 Hz peak
- Exact 8 MHz peak
- Exact 28 MHz peak
- 12-fold rotational symmetry
- Stable 7-fold structure across bands (only superficial hits)
- Independently replicated DDG
- Time-crystal claims meeting the Zhang/Choi/Kessler criteria (Bruno no-go applies; should be called "time-crystal-like" until subharmonic locking + robustness windows + non-equilibrium criteria are demonstrated)

---

## Critique landscape (for §E of any future replication paper)

- **Tegmark 2000 decoherence critique:** PRE 61, 4194 (DOI 10.1103/PhysRevE.61.4194)
- **Hagan-Hameroff-Tuszyński reply:** PRE 65, 061901 (DOI 10.1103/PhysRevE.65.061901) — argues Tegmark modeled wrong superposition; keeps Orch-OR possible but does NOT validate DDG
- **Independent microtubule work (NOT a DDG replication):** Kalra et al. *ACS Central Science* 2023, DOI 10.1021/acscentsci.2c01114 — exciton diffusion over 6.6 nm, anesthetic reduction
- **Time-crystal references:** Zhang/Choi/Kessler (period-doubled subharmonic locking); Bruno no-go ruling out equilibrium time crystals

**Discover Magazine** profile says findings "still need to be replicated by other scientists" — journalistic, not peer-reviewed, but matches the absence of independent DDG replication.

---

## FP-2 falsification design (paper-ready)

### Observable definition

For microtubules:
$$Y(f) = G(f) + iB(f)$$
For each peak: record $(f_i, A_i, Q_i, \phi_i, \text{SNR}_i)$

For DDG:
$$D(c, t, \tau) = \{A, \tau, \phi, P_\text{emit}, V, I\}$$

### Pre-registered binning

Eight PSL(2,7)/F₂₁ coset bins C₀..C₇. **Justification: the microtubule MHz 8-peak set + 45° phase quantization, NOT DDG's 12-band structure.**

### Coset coherence statistic

$$Z_j = \sum_{p_i \in C_j} A_i Q_i e^{i\phi_i}$$

$$S = \frac{|\sum_{j=0}^{7} Z_j|}{\sum_{j=0}^{7} |Z_j|}$$

### Saturation fit

$$S(x) = S_\infty \left(1 - e^{-x/x_0}\right)$$

### FP-2 prediction

$$\frac{S_\infty}{C_{G_2}} = \frac{6}{7} \pm \epsilon$$

(C_{G_2} and ε must be fixed BEFORE measurement.)

### Falsification criteria (any one suffices)

1. Triplet-of-triplets reproduces but 8-coset bins fail to populate above null
2. 45° phase quantization fails under blinded replication, or appears equally in open/short/electrode/buffer controls
3. Four PSL distance classes {0,1,2,3} fail to predict amplitude/Q/phase/coupling/burst-timing better than random relabeling
4. S_∞/C_{G_2} statistically inconsistent with 6/7 under pre-registered uncertainty
5. DDG's 12-band structure is the dominant reproducible structure and can't be compressed into 8 cosets without losing predictive power
6. Same 8-coset/6⁄7 signature appears in non-biological controls (instrumentation artifact)
7. Depolymerization/denaturation/water-channel disruption/microtubule removal leaves signature intact

**Cleanest "Bandyopadhyay right, FP-2 wrong" outcome:** triplet-of-triplets survives; 8-coset 6/7 coherence does not.

### Consistency criteria

1. Microtubule MHz band repeatedly resolves into same 8 coset bins across independent preparations
2. Stable phase relations tied to 45° quantization
3. Coset-pair couplings collapse into 4 PSL distance classes
4. Fitted normalized coherence saturates at 6/7 of pre-defined G₂ ceiling
5. Residual 1/7 behaves as stable irreducible residual, not removable noise
6. Pattern degrades under anesthetic/depolymerization/denaturation in pre-specified direction
7. Signal absent in open/short/buffer/electrode-only controls

### Paper-ready FP-2 statement

> **FP-2:** In calibrated DDG/impedance spectra of intact microtubule-bearing preparations, complex resonance responses will organize into eight pre-registered PSL(2,7)/F₂₁ coset bins, with phase/Q/amplitude couplings grouped by coset distances {0,1,2,3}. The normalized coset coherence $S_\infty/C_{G_2}$ will saturate at $6/7 \pm \epsilon$. FP-2 is falsified if the Bandyopadhyay triplet-of-triplets spectrum is reproducible but the eight-coset/distance-class/6⁄7 signature is absent or control-derived.

---

## Replication protocol summary

### Microtubule prep (base: Saxena 2020)

- Porcine brain microtubules/tubulin kits, -80°C storage
- Polymerization: PIPES/EGTA/MgCl₂/GTP, 35–37°C incubation, paclitaxel stabilization
- Tune length to 4–20 μm
- Electrodes: drop biomaterial onto pre-grown gold electrodes (e-beam lithography failed device-survival)
- Measurement: AC frequency sweep 1 Hz – 20 GHz via vector analyzer, S₂₁ in dB
- **Required controls (non-negotiable):** open, short, air-air, Si substrate, air-Si, air-electrode, Si-electrode, buffer-only, electrode-only, denatured tubulin, depolymerized MT, non-MT protein
- **Pre-register peak rejection rule** (don't blind-subtract background)

### Neuron/AIS (rat hippocampal)

- Pre-grown electrode array, patch-clamp + coaxial atom probes targeting AIS
- Subthreshold bias, horizontal AC + perpendicular gating AC → 2D frequency input pattern
- Record simultaneously: f_x, f_y, V_patch, I_patch, S₂₁, φ, Q, SNR
- Blinded peak extraction
- Crucial controls: empty arrays, dead cells, membrane-only, MT-disrupted neurons

### DDG (scalp/human)

- Both modes simultaneously (resonance + pulse)
- 17-probe + clock cap, 34-channel logic analyzer, Yagi-antenna probes
- DO NOT skip artificial-brain reference (used for normalization)
- Shielding/amp gain/RF env/body motion = experimental variables, NOT background

### Temperature/environment

- Microtubules: 35–37°C nominal, sweep multiple T to test thermal peak shift
- Human DDG: continuously log T, humidity, RF environment, electrode impedance, body motion, skin conductance

---

## Implications for our framework

### Update to Paper 7 §6.3 / FP-2

- **Remove** any "28 MHz" framing if present — wrong by three orders of magnitude (real number is 28 THz tubulin or 30 MHz microtubule)
- **Replace** with the explicit 8-peak microtubule MHz anchor: {12, 20, 22, 30, 101, 113, 185, 204}
- **Add** the 45° phase quantization as an empirical 8-bin justification (not 12-band DDG)

### Update to Paper 8 (Eight-Coset Simulator)

- The 8-coset structure has an empirical biological anchor independent of the algebraic prediction
- The microtubule MHz band → 8 peaks → 4 PSL distance classes is the natural mapping
- §6 hardware specification should mention BOTH the synthetic 7-qubit IBM/IonQ test AND the biological microtubule MHz test as falsifiers
- This raises Paper 8's stakes: a positive synthetic result + positive biological result would be remarkable; a positive synthetic + negative biological would still be a strong algebraic paper

### NEW: Paper 10 candidate — FP-2 replication protocol paper

- Detailed pre-registered protocol for microtubule MHz + 45° phase coset analysis
- Could be co-authored with someone closer to the experimental program (NOT Bandyopadhyay's group directly — independence matters)
- Target: open-access biophysics journal

---

## Key references

| Paper | DOI | Role |
|-------|-----|------|
| Singh et al. 2024 (DDG) | 10.56280/1600841751 / 10.48505/nims.5288 | Primary DDG methodology |
| Sahu/Singh/Bandyopadhyay 2014 | 10.1038/srep07303 | Tubulin/microtubule resonance peaks |
| Saxena et al. 2020 | 10.3390/fractalfract4020011 | Triplet-of-triplets, 8 MT peaks, 45° phase quantization |
| Tegmark 2000 | 10.1103/PhysRevE.61.4194 | Decoherence critique |
| Hagan-Hameroff-Tuszyński 2002 | 10.1103/PhysRevE.65.061901 | Decoherence reply |
| Kalra et al. 2023 | 10.1021/acscentsci.2c01114 | Independent microtubule excitons (NOT DDG replication) |

---

## What this does NOT do

- Does not validate Bandyopadhyay's broader Orch-OR / time-crystal program
- Does not give us independent replication of DDG
- Does not commit us to defending Hameroff-Penrose
- Does not change Paper 7's published status (already on Zenodo with conjecture-not-theorem framing)

The right move is: cite the data, design FP-2 as a falsifier, stay neutral on the larger biophysics program.
