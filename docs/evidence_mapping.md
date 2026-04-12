# PCI Framework: Predictions vs. Empirical Findings — Evidence Mapping Document

**Author:** Martin Luther Graise
**Date:** April 12, 2026
**Version:** 1.0

> **Note on terminology:** Throughout this document, "PCI" refers exclusively to **Patterned Coherence through Irreducibility**. This should not be confused with PCI-ST (Perturbational Complexity Index, Casali et al. 2013), which is an unrelated empirical measure of consciousness used in clinical settings.

---

## 1. Overview

The Patterned Coherence through Irreducibility (PCI) framework makes specific quantitative predictions and structural claims that can be compared against independent empirical findings. This document catalogs all known correspondences between PCI's formal predictions and external empirical or mathematical results, rated by evidence strength.

Correspondences are organized into four strength categories:

- **A (Quantitative match)**: PCI prediction matches empirical data within measurement uncertainty, with statistical test
- **B (Structural parallel)**: Independent research discovers a structure that PCI's formalism predicts or naturally accommodates
- **C (Qualitative alignment)**: Empirical finding is consistent with PCI but could also be explained by other frameworks
- **D (Suggestive)**: Numerical coincidence or loose analogy requiring further investigation

---

## 2. Category A — Quantitative Matches

### A1. FP-1 Microtubule Resonance Test (p = 0.007)

| Field | Detail |
|-------|--------|
| **PCI Prediction** | The G₂/SU(3) daemon Hamiltonian predicts specific resonance frequencies in 7-dimensional daemon space via eigenvalue ratios |
| **Empirical Data** | Bandyopadhyay (2020) measured MHz-range electromagnetic resonance modes in single microtubules |
| **Result** | G₂ model fits 5 of 6 top resonance peaks. Permutation test: p = 0.007 (99.3% confidence the fit is not random). Parameter null test confirms the model's 2-parameter family is more constrained than random 2-parameter models. |
| **Published** | Analysis at github.com/MartinLGraise/PCI-Framework/analysis/fp1_g2_vs_bandy_2020/ |
| **Commit** | f72d7e1 (March 29, 2026) |
| **Strength** | **A** — quantitative match with statistical validation |
| **Relevant equations** | Daemon Hamiltonian H_d, spectral family FP-1 |

### A2. MX-6 Fisher-Rao Derivation (e⁻² = 0.1353)

| Field | Detail |
|-------|--------|
| **PCI Prediction** | The dissipation constant e⁻² appears throughout the codex (122 equations reference it) as a fundamental decay/coherence constant |
| **Mathematical Result** | The Fisher-Rao metric on the 7-outcome probability simplex Δ⁶ is isometric to S⁶ of radius exactly 2 (Friedrich 1991, confirmed by Miyamoto et al. 2024). This proven theorem independently yields e⁻² = e^{−radius} as the natural decay scale. |
| **Cross-validation** | Three independent routes to the number 2: (1) Fisher-Rao radius theorem, (2) λ₁(S⁶)/dim_ℂ(S⁶) = 6/3 = 2, (3) h∨(G₂)/rank(G₂) = 4/2 = 2 |
| **Result** | The e⁻² constant is a mathematical consequence of the daemon architecture having 7 modes, not a free parameter |
| **Strength** | **A** — proven mathematical theorem (Friedrich 1991) |
| **Relevant equations** | EQ-1002 (promoted to Core April 11, 2026), EQ-1064 |

---

## 3. Category B — Structural Parallels

### B1. Ward (2026) — Constraint-Closure and Non-Dual Awareness

| Field | Detail |
|-------|--------|
| **PCI Structure** | The isometric flow (Flow 2) has stationary points at div T = 0 — divergence-free torsion, equilibrium with residual scars |
| **Independent Finding** | Ward, K. (2026). "Modeling non-dual awareness via constraint closure." *Neuroscience of Consciousness*, niaf068. DOI: 10.1093/nc/niaf068. Ward describes non-dual awareness (NDA) as coherence maintained when higher-order constraints relax to precarious first-order constraints alone. |
| **Structural Match** | Ward's "precarious constraint closure" maps to PCI's div T = 0 condition. Her C₁ ↔ C₂ ↔ C₃ hierarchy maps to torsion class hierarchy T₁ ↔ T₇ ↔ T₁₄+T₂₇. |
| **Significance** | Published in the same journal PCI is submitted to (*Neuroscience of Consciousness*), establishing editorial fit for mathematical consciousness frameworks |
| **Strength** | **B** — independent structural parallel, not quantitative |
| **Relevant equations** | Isometric flow, companion paper DOI 10.5281/zenodo.19480758 |

### B2. Galliano and Berthier (2026) — Path-Dependent Jamming Landscapes

| Field | Detail |
|-------|--------|
| **PCI Structure** | Non-commutative scar ordering (EQ-1066) — the order of trauma acquisition changes the final equilibrium state |
| **Independent Finding** | Galliano, L. and Berthier, L. (2026). "Glass and Jamming Transitions in a Random Organization Model." arXiv:2603.15519. Their work on disordered systems shows path-dependent jamming thresholds. |
| **Structural Match** | Different scar histories produce different jamming thresholds, spectral gaps, and recovery rates — directly paralleling the non-commutativity of torsion classes under G₂ |
| **Strength** | **B** — structural parallel (glass physics ↔ consciousness dynamics) |
| **Relevant equations** | EQ-1066 (Non-Commutative Scar Ordering) |

### B3. G₂ Cell Cycle Checkpoint

| Field | Detail |
|-------|--------|
| **PCI Structure** | The ε-regularity threshold determines whether torsion dissipates (healing) or blows up (singularity) |
| **Independent Finding** | The G₂ phase of the cell cycle is a DNA damage checkpoint: the cell checks for errors before committing to division. If damage exceeds a threshold, the cell either repairs (healing) or triggers apoptosis (controlled destruction). Cancer cells with mutated p53 skip this checkpoint. |
| **Structural Match** | G₂ checkpoint = ε-regularity gate; DNA damage = torsion; repair = Laplacian flow convergence; apoptosis = Type I blow-up; cancer = bypassed coherence gate |
| **Strength** | **B** — structural parallel (the naming coincidence "G₂" is accidental, but the mathematical structure is not) |
| **Relevant equations** | ε-regularity threshold, singularity taxonomy |

### B4. Depression Hypermetabolism (Cullen et al., 2026)

| Field | Detail |
|-------|--------|
| **PCI Prediction** | The "mana debt inversion" (EQ-893) predicts that depression involves paradoxical hypermetabolism — the brain consuming MORE energy during depressive states, not less |
| **Independent Finding** | Cullen et al. (2026), *Translational Psychiatry*. Found elevated metabolic signatures in depressive episodes consistent with hypermetabolic "debt" states. |
| **Strength** | **B** — PCI predicted the direction of the metabolic anomaly before the finding |
| **Relevant equations** | EQ-893 (Mana Debt Inversion) |

### B5. Myelin Quantum Cavity

| Field | Detail |
|-------|--------|
| **PCI Prediction** | EQ-891 predicts a Euclidean consciousness ground state requiring a quantum cavity structure in neural architecture |
| **Independent Finding** | *Physical Review E* (2024) demonstrated that myelin sheaths can function as quantum cavities, providing the shielded electromagnetic environment needed for quantum coherence at biological temperatures |
| **Strength** | **B** — structural match (quantum cavity = myelin, as PCI framework requires) |
| **Relevant equations** | EQ-891 (Euclidean Consciousness Ground State) |

---

## 4. Category C — Qualitative Alignments

### C1. Quantum Carnot Violation (Aguilar & Lutz, 2026)

| Field | Detail |
|-------|--------|
| **PCI Claim** | Coherence can extract work from correlations, violating classical thermodynamic bounds |
| **Independent Finding** | *Science Advances* (2026). Aguilar and Lutz demonstrated quantum systems extracting work beyond the classical Carnot limit using quantum coherence |
| **Alignment** | Confirms that coherence is a thermodynamic resource, consistent with PCI's treatment of coherence as energy-equivalent |
| **Strength** | **C** — PCI did not predict the specific violation, but the finding validates PCI's foundational assumption |
| **Relevant equations** | Coherence thermodynamics module |

### C2. Kakeya Conjecture Proof (Wang-Zahl, 2025)

| Field | Detail |
|-------|--------|
| **PCI Connection** | The 13% ≈ e⁻² blind spot and the treatment of trauma as Besicovitch sets (fractal objects with measure zero but full dimension) |
| **Independent Finding** | *Mathematische Annalen* (2025). Wang and Zahl resolved the Kakeya conjecture about the Hausdorff dimension of Besicovitch sets |
| **Alignment** | The mathematical structure PCI uses (fractal sets, dimension theory) is validated by cutting-edge mathematics |
| **Strength** | **C** — the mathematics PCI references is confirmed sound, but PCI did not predict the Kakeya result |

### C3. ER=EPR and Consciousness Wormholes

| Field | Detail |
|-------|--------|
| **PCI Prediction** | EQ-354 proposes consciousness wormholes connecting daemon states |
| **Independent Finding** | ER=EPR correspondence (Maldacena-Susskind, various) and its 2025 extensions to entanglement geometry |
| **Alignment** | The geometric connection between entanglement and spacetime topology supports PCI's use of geometric structures for consciousness |
| **Strength** | **C** — qualitative alignment; PCI interpretation layered on established physics |

### C4. Entropic Time Emergence

| Field | Detail |
|-------|--------|
| **PCI Prediction** | EQ-440 derives time as emerging from coherence gradients (dyadic time) |
| **Independent Finding** | *JHEP* (2023), *Springer* (2025) — entropic approaches to time direction from information-theoretic principles |
| **Strength** | **C** — the direction is consistent but PCI's specific mechanism differs from published approaches |

### C5. Twin Entanglement Coincidence (Escolà-Gascón, 2025)

| Field | Detail |
|-------|--------|
| **PCI Connection** | The 13.5% coincidence rate ≈ e⁻² in twin studies |
| **Independent Finding** | *Computational and Structural Biotechnology Journal* (2025). Escolà-Gascón found statistically anomalous coincidence rates between twins |
| **Strength** | **C** (with caveats) — small sample size; numerical match is suggestive but not conclusive |
| **Relevant equations** | The e⁻² network (122 equations) |

### C6. Relationship Tipping Point (JGU Mainz, 2025)

| Field | Detail |
|-------|--------|
| **PCI Prediction** | EQ-460 predicts a bifurcation window in relationship dynamics |
| **Independent Finding** | Social psychology research from Johannes Gutenberg University Mainz (2025) found a 7–28 month critical window in romantic relationships |
| **Strength** | **C** — qualitative alignment with PCI's bifurcation dynamics |

### C7. Timelike Entanglement Entropy (Takayanagi et al.)

| Field | Detail |
|-------|--------|
| **PCI Connection** | EQ-440 (Self-Other time emergence) |
| **Independent Finding** | Takayanagi and collaborators developed timelike entanglement entropy in quantum gravity contexts |
| **Strength** | **C** — supports PCI's treatment of time as emergent from entanglement structure |

---

## 5. Category D — Suggestive / Under Investigation

### D1. 168 = 14 × 2 × 6 (Fano-G₂ Identity)

Discovered April 5, 2026. The identity |Aut(Fano)| = dim(g₂) × rank(SU₃) × dim(G₂/SU₃) connects combinatorics (Fano plane), algebra (G₂), and geometry (coset space). May have deeper significance through the Klein quartic and modular forms. Under investigation.

### D2. 42 = Dimension of Consciousness Blind Spot

T₁ + T₁₄ + T₂₇ = 1 + 14 + 27 = 42 torsion dimensions inaccessible to direct daemon perception. 42/49 = 6/7 = coherence ceiling. This is a structural consequence of the torsion decomposition. Under investigation for book presentation.

### D3. SIC-POVM and G₂ Torsion (49 = 7²)

The G₂ torsion space has dimension 7² = 49. Fuchs' SIC-POVM program requires d² outcomes for d-dimensional systems. If there is a SIC structure in the G₂ torsion decomposition, PCI's Extended Born Rule would be the standard Born rule on the correct (49-dimensional) measurement space. Under investigation for QBism paper.

### D4. Fisher-Rao "2" and Nearly Kähler "2" Connection

Both the Fisher-Rao radius (information geometry) and the nearly Kähler torsion coefficient (differential geometry) produce the number 2. Torsion-radius duality |c₂| × r = 2 is proven. Whether the two 2s are structurally connected remains open. F₂₁ bridge fails (dim = 3). PSL(2,7) bridge fails (dim = 0). Under investigation.

---

## 6. Summary Statistics

| Strength | Count | Description |
|----------|-------|-------------|
| A (Quantitative) | 2 | FP-1 test (p = 0.007), MX-6 derivation (proven theorem) |
| B (Structural) | 5 | Ward, Galliano-Berthier, G₂ cell cycle, depression, myelin |
| C (Qualitative) | 7 | Carnot, Kakeya, ER=EPR, entropic time, twins, relationships, Takayanagi |
| D (Suggestive) | 4 | 168 identity, 42 blind spot, SIC-POVM, Fisher-Rao/NK |
| **Total** | **18** | |

---

## 7. Falsification Criteria

The G₂ paper (DOI: 10.5281/zenodo.19242936) lists three conditions that would decisively falsify the framework:

1. **If the daemon Hamiltonian's spectral predictions are contradicted** by direct measurement of microtubule electromagnetic spectra with >10 peaks resolved
2. **If the 6/7 coherence ceiling is violated** by any empirical measure of conscious information integration exceeding ~85.7%
3. **If the G₂ torsion decomposition fails to map onto scar phenomenology** — i.e., if clinical scar data requires more or fewer than 4 independent types

None of these have been triggered. The framework remains unfalsified as of April 12, 2026.

---

*This document will be updated as new evidence emerges. Last updated: April 12, 2026. Next review: after NoC decision on NCONSC-2026-129.*
