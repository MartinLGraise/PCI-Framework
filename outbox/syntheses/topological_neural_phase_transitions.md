# Topological Phase Transitions and Topological Invariants in Biological Neural Networks
### A Critical Literature Review, 2022–2026
**Compiled:** May 2026 | **Scope:** arXiv, PubMed, Semantic Scholar, Web search

---

## Executive Summary

This report surveys the state of literature (with emphasis on 2022–2026) on the application of topological concepts to biological neural networks. The central question is whether any published work treats the brain **literally** as a topological state of matter with measurable, quantized invariants — in the same sense that condensed-matter physics treats a quantum Hall insulator or a topological semimetal.

**The short answer is no — with important caveats.**

The field divides sharply into two regimes that must not be conflated:

1. **Topological Data Analysis (TDA) applied to neuroscience** — a mature, active field (2008–present) using persistent homology to characterize the *shape* of neural activity data. This is topology-as-geometry-extraction, not topology-as-phase-classification. It does not assign topological invariants in the condensed-matter sense. It does not use Chern numbers, winding numbers, Z₂ indices, or Berry phases on neural data.

2. **Condensed-matter topological formalism applied to neural systems** — essentially non-existent as applied to *biological* neural networks. Neural networks are used to *detect* topological phases in quantum matter (the machine-learning → condensed matter direction), but the reverse — applying topological band theory, Berry curvature, or Z₂ topological invariants to characterize brain states — has not been done in any peer-reviewed paper as of May 2026.

**On Chinese research groups:** Chinese physicists are active in both TDA-adjacent neuroscience (Jin Wang's group at Stony Brook / Chinese collaborators, Haiping Huang at Sun Yat-sen University) and in condensed-matter topology (IOP-CAS, Tsinghua, Westlake). However, no Chinese group has yet published work applying condensed-matter topological invariants to biological neural data. The gap between these two communities remains wide.

**On Z₂ cohomology and 1-cycles specifically:** Persistent cohomology has been used to detect 1-cycles (H₁ generators) in hippocampal place cell data (Xu, Morozov, Kang 2021) and in resting-state fMRI (Martínez-Riaño et al. 2022). These are genuinely topological measurements. However, they characterize the *geometry of neural activity manifolds*, not phase transitions in the condensed-matter sense. No paper has identified a Z₂ cohomology class that appears only during a specific cognitive state.

**On phase transition signatures:** Several groups (Marro/Torres, Tagliazucchi, Jin Wang) describe brain dynamics using phase-transition language from statistical physics — order parameters, criticality, bifurcations. Petri et al. (2014) found that psilocybin produces measurable changes in H₁ persistent homology of functional connectivity. But none of these constitute a *topological* phase transition in the strict sense: no topological invariant changes its quantized value.

**Relevance to PCI framework (Paper 14 v1.6):** The literature reveals a genuine white space. Treating neural substrate state as a *topological phase* (with invariants that could detect "residence" vs. "pathology" as distinct topological sectors) is not prior art — it is a novel theoretical proposal. The closest prior art is: (a) Petri's homological scaffolds under psychedelics, (b) Jin Wang's nonequilibrium landscape-flux framework for neural phase transitions, (c) the lattice field theory approach of Bardella et al. (2024). None of these deploy topological invariants in the sense needed for a condensed-matter-style topological phase classification.

---

## 1. Topological Data Analysis in Neuroscience: State of the Field

### 1.1 Foundations and Maturity

TDA in neuroscience is now a mature subfield, initiated around 2008 by Carlsson, Singh, Ringach, and colleagues with the application of persistent homology to visual cortex population activity. The canonical early result (Ringach et al. 2008, *Journal of Vision*) showed that the topology of V1 population activity patterns during spontaneous activity resembles those evoked by natural images — both consistent with the topology of a real projective plane RP² — linking neural coding geometry to stimulus statistics.

The field has since branched into four main application areas:

| Application | Key groups | Primary data type | Topological tool |
|---|---|---|---|
| Hippocampal/spatial coding | Curto/Itskov (Penn State), Kang (UCSF), Dabaghian (Chicago) | Ca²⁺ imaging, electrophysiology | Persistent homology, cohomology |
| Functional connectivity | Petri (Turin), Bassett (Penn), Shen (Indiana), Goñi (Purdue) | fMRI BOLD | H₀, H₁, H₂ barcodes |
| EEG/neural signals | Chung (Wisconsin), Beshkov/Einevoll (Oslo) | EEG, 2-photon Ca²⁺ | Persistent homology, time-frequency |
| Neural manifold topology | Giusti/Ghrist (Penn), Henselman-Petrusek | Population recording | Analogous cycles, cohomology |

### 1.2 What TDA Actually Measures

Persistent homology computes Betti numbers (β₀, β₁, β₂, …) across a filtration:
- **β₀**: number of connected components
- **β₁**: number of independent 1-dimensional loops (1-cycles)
- **β₂**: number of enclosed voids

These are extracted as "barcodes" — intervals [birth, death] in filtration parameter — with longer bars indicating more robust topological features. **This is fundamentally different from computing a topological invariant of a physical system's Hamiltonian.** The Betti numbers of a point cloud are not protected by any symmetry; they change continuously as the data changes. They are descriptors, not invariants in the condensed-matter sense.

### 1.3 Most Significant Recent Results (2022–2026)

**H₁ features of the resting-state connectome (Martínez-Riaño et al., Network Neuroscience, 2022, DOI: 10.1162/netn_a_00280):** Applied persistent cohomology to resting-state fMRI from 198 healthy controls. Found robust 1-cycles (H₁ generators) representing multi-region synchronization loops in the resting brain. These are the closest existing measurements to "detecting a 1-cycle in a neural system." The cycles correspond to groups of three or more regions mutually interacting in a closed loop. The paper is honest that these are geometric features of connectivity, not invariants of a topological phase.

**Homological landscape of brain functional sub-circuits (Duong-Tran, Kaufmann, Petri, Goñi, Shen et al., Mathematics 2024, DOI: 10.3390/math12030455):** Computed H₀, H₁, H₂ features for major functional sub-circuits from HCP data. Found that **different homological orders distinguish different task conditions**: H₀ separates emotion tasks, H₁ separates motor tasks, H₂ separates working memory. This is the most systematic evidence that different cognitive states correspond to different homological signatures — but the effect is quantitative, not categorical (no discrete jump in a topological invariant).

**Persistent homology + individual differences (Wang, Xian, Chen, Yan, Frontiers in Human Neuroscience, 2025, DOI: 10.3389/fnhum.2025.1607941):** Time-delay embedding + persistent homology on ~1,000 HCP subjects. Topological features predict gender and behavioral traits (cognitive, emotional, personality) better than traditional fMRI features in higher-order domains. Test-retest reliability is high. Again: topology as biomarker, not as phase label.

**Tracking manifold topology across populations (Giusti, Henselman-Petrusek, Yoon, Ghrist, Smith, Yu, PNAS 2024, DOI: 10.1073/pnas.2407997121):** Introduced "analogous cycles" — a method for robustly matching topological features (1-cycles, 2-cycles) between different neural populations recording during similar stimuli. This is mathematically sophisticated and genuinely operates at the topological level. It does not assign phase labels but would be the right tool to detect if a topological feature appears only in a specific cognitive state.

**Neural spike train TDA pipeline (Ayhan, Nash, Vincis et al., 2025):** Pipeline applying persistent homology to spike train ensembles from mouse insular cortex. Showed population-level topological signatures can discriminate stimuli even when individual neurons show no selectivity. Demonstrates TDA can extract information from collective activity topology.

**Memory as structured trajectories (Li Xin, arXiv 2025, DOI: 10.48550/arXiv.2508.11646):** A theoretical paper arguing that memory traces correspond to nontrivial homology generators on a latent manifold of cognitive states — "delta-homology generators" that are sharply localized along reproducible topological cycles. This is conceptually close to the user's interest in non-trivial 1-cycles as cognitive markers, but remains theoretical/speculative with no experimental data.

### 1.4 The Central Limitation

No TDA paper has identified a topological feature that:
1. Takes a **discrete, quantized value** (i.e., is a genuine invariant, not a continuous measurement)
2. **Changes abruptly** (i.e., undergoes a transition) at a cognitive state boundary
3. Is **protected** by any symmetry analogous to what protects topological phases in condensed matter

The field uses topology-as-tool, not topology-as-classification. This is the gap the user is asking about.

---

## 2. Chinese Research Groups (with Confirmed Affiliations)

### 2.1 Groups Working at the Physics/Neuroscience Interface

**Jin Wang group** (Stony Brook University, with strong Chinese collaborators and PRC-based co-authors)
- Primary output: Nonequilibrium landscape-flux framework for neural systems
- Most relevant 2024 paper: "Nonequilibrium dynamics and thermodynamics provide the underlying physical mechanism of the perceptual rivalry" (Wu, Xu, Wang, *Physical Review Research* 7, 023059, 2025, DOI: 10.1103/PhysRevResearch.7.023059). Uses phase-transition language (perceptual rivalry as a "consecutive phase transition process"), identifies perceptual switching as traversal of a landscape with multiple basins. Measures entropy production near "phase transition points." 
- Also: "Holistic structure of neural pathways underlies brain perceptual rivalry" (Wu, Gao, Fang, Wang 2024): demonstrates that perceptual phase transitions arise from the *topological structure of holistic neural pathways* — the connectivity graph, not a condensed-matter topological invariant.
- Also: "Global dynamics, thermodynamics and non-equilibrium origin of bifurcations for single neuron dynamics" (Wang, Wu, Xu, Wang, *J. Chem. Phys.* 2023, DOI: 10.1063/5.0169296): Explicitly uses "topological features of the landscape" to assess stability of resting states. The ring-attractor topology of the oscillation landscape is noted. Flux and entropy production spike near phase transition (bifurcation) points.
- **Assessment:** This is the most topologically-flavored Chinese physics work on biological neural systems. It describes topology in the sense of attractor-landscape topology (ring attractors, basins), not condensed-matter topology. No Chern numbers or Berry phases. But the framework is the right level of abstraction — it treats neural dynamics as a physical system with identifiable phases and transitions between them.

**Haiping Huang group** (PMI Lab, School of Physics, Sun Yat-sen University, Guangzhou; email: huanghp7@mail.sysu.edu.cn)
- Primary output: Statistical mechanics of neural networks, disordered systems, phase transitions in learning
- Most relevant paper: "How high dimensional neural dynamics are confined in phase space" (Wang, Huang, arXiv 2410.19348, 2024): Derives analytically that high-dimensional neural dynamics occupy an M-shaped region in phase space, with sharp boundaries. Uses a quasi-potential (thermodynamic potential) to characterize the geometry. Language is explicitly phase-space and thermodynamic — close to the conceptual territory of interest, but not topological in the invariant sense.
- Also: "Eight challenges in developing theory of intelligence" (Huang, *Frontiers in Computational Neuroscience* 2024): Identifies manifold transformation and topology of neural representations as a key open challenge. The paper explicitly notes that "an analytic theory of the manifold transformation is still lacking."
- **Assessment:** Huang is one of the most physically rigorous Chinese neuroscience theorists. His group works at the statistical physics level (replica theory, mean-field theory, phase transitions in learning). Not applying condensed-matter topology to bio-neural systems, but the right domain expertise to do so.

**Groups at IOP-CAS, Tsinghua, Westlake, Peking University** (condensed-matter topology):
- These groups (including the Zhong Fang group at IOP-CAS, the Xi Dai group, the Wanxiang Feng group at Peking University, the Hao Zheng group at Westlake) are world-leading in topological materials, Weyl semimetals, topological insulators. They publish routinely on Berry phase, Chern numbers, Z₂ invariants, and axion insulators.
- **None of these groups has published work applying their condensed-matter topology formalism to biological neural networks.** The bridge has not been built.
- The nearest adjacent work: Ferroelectric Chern insulator device for neuromorphic computing (Chen, Xie, Cheng et al., *Nature Nanotechnology* 2024, DOI: 10.1038/s41565-024-01698-y, affiliated with USTC/Nanjing). This applies topological edge states to *artificial* neuromorphic hardware — not biological neural networks.

**Xiakun Chu / Jin Wang** (chromosome topology in neural development, PRC collaborators): "Deciphering the dynamical chromosome structural reorganizations in human neural development" (*Physical Review Research* 2024, DOI: 10.1103/physrevresearch.6.023309). Uses "topologically associating domains" (TADs) in the chromosomal sense during neural cell-fate determination. This is genomic topology, not neural dynamics topology.

### 2.2 Chinese Groups Working on TDA Applied to Neural Data

**Chang Liu, Fei Ni, Honggang Zhang et al. (Hindawi/J. Healthcare Engineering 2021):** Persistent homology on EEG for Gestalt cognition patterns. Institutional affiliations include Chinese universities. This is applied TDA neuroscience.

**SPHENIC spatial transcriptomics clustering** (Guo, Zhu, Guan et al., arXiv 2508.10646, 2026): Chenkai Guo affiliated with University of Chinese Academy of Sciences. Uses extended persistent homology for spatial transcriptomics clustering in brain tissue — adjacent but not neural dynamics.

### 2.3 Summary Table: Chinese Groups by Domain

| Group | Institution | Domain | Topological formalism? |
|---|---|---|---|
| Jin Wang | Stony Brook + Chinese collaborators | Neural landscape, phase transitions | Attractor topology, NOT CM topology |
| Haiping Huang | Sun Yat-sen University | Statistical physics of NNs | Phase transitions, NOT topological invariants |
| IOP-CAS topology groups | Institute of Physics, CAS | Condensed matter topology | YES — but not applied to bio-neural |
| Tsinghua TLBI | Tsinghua | Brain-intelligence interface | Computational/imaging neuroscience |
| Xiakun Chu / Jin Wang | PRC collaborators | Chromosome dynamics in neural dev | Genomic TADs, not neural dynamics |
| Chang Liu et al. | Chinese universities | TDA on EEG | Persistent homology descriptors |

---

## 3. Z₂ Cohomology and 1-Cycle Detection in Neural Data

### 3.1 What Has Been Done

**Grid cells and place cells — the clearest topological success story:**
Persistent cohomology has been used to recover the topology of the space being navigated from neural population activity alone. Xu, Morozov, and Kang (2021, *Frontiers in Computational Neuroscience*, DOI: 10.3389/fncom.2021.616748) demonstrated that:
- Grid cell populations encode a 2-torus (T²) — detected as two independent H₁ generators
- Head direction cells encode a circle (S¹) — detected as a single H₁ generator
- Conjunctive cells encode a product of these structures

This is a genuine topological detection: the 1-cycles found correspond to the fundamental group of the navigation space. The key point is that the *topology of the stimulus space* is imprinted on the *topology of the neural activity manifold*. Z₂ coefficients are standard in persistent cohomology computations (Ripser, the standard software, uses Z₂ by default), so technically these are Z₂ cohomology classes — but the word "Z₂" here refers to the coefficient ring (binary arithmetic), not to a Z₂ topological invariant in the condensed-matter sense.

**Resting-state 1-cycles:**
Martínez-Riaño et al. (2022) found persistent H₁ features (robust 1-cycles) in resting-state fMRI from 198 controls. These cycles represent multi-region closed synchronization loops. They are stable across individuals and correlate with brain volume and sex. This is the closest thing in the literature to "measuring a 1-cycle in a brain at rest."

**Task-dependent homological signatures:**
The Duong-Tran, Petri, Goñi, Shen et al. (2024) paper found that H₁ homological distance between rest and motor task is detectable at both whole-brain and sub-circuit levels, and that different homological orders (H₀, H₁, H₂) are most sensitive to different cognitive tasks. This is the strongest evidence that *cognitive state differences are topologically detectable* — but the homological features change quantitatively, not through a discrete jump.

### 3.2 What Has NOT Been Done

No paper has:
1. Identified a **Z₂ cohomology class** (in the topological insulator sense — a class in H¹(BZ; Z₂) or equivalent) in neural data
2. Shown that a **1-cycle appears** in neural activity during a specific cognitive state and is **absent** (i.e., the space has trivial first homology) during another state
3. Demonstrated a **sharp, phase-transition-like change** in a topological invariant at a cognitive state boundary

The closest hint: The 2007 Fekete et al. paper (BMC Neuroscience) hypothesized that "the persistent Betti numbers of activity level sets become more complex as arousal increases." This was early work suggesting that representational capacity (measured by homology) grows with consciousness level. But it never developed into a rigorous topological phase-transition claim with confirmed Z₂ structure.

### 3.3 Technical Note on Z₂ in Neuroscience TDA

When neuroscience TDA papers use Z₂ coefficients, they mean coefficients in the field F₂ = {0,1} (mod 2 arithmetic), which is standard for computational efficiency. This is not the same as detecting a Z₂ topological invariant (like the Kane-Mele Z₂ index of a topological insulator). The latter requires a global property of a Bloch Hamiltonian over the Brillouin zone — a concept that has no direct analog in neural data without a substantial theoretical framework to map neural states to band structures.

---

## 4. Phase Transition Signatures in Cognitive States

### 4.1 Statistical-Physics Phase Transitions in Brain Dynamics

Multiple groups describe brain dynamics using phase-transition language from statistical physics, but these are *dynamical* phase transitions (bifurcations, criticality), not *topological* phase transitions:

**Marro and Torres group (Granada):** "Brain Performance versus Phase Transitions" (Scientific Reports 2015, DOI: 10.1038/srep12216) and "Physics Clues on the Mind Substrate and Attributes" (Frontiers in Computational Neuroscience 2022, DOI: 10.3389/fncom.2022.836532). These papers explicitly describe cognitive states as phases in a non-equilibrium statistical mechanics framework, with phase transitions visible in EEG recordings. The language is close to what the user wants, but the "phases" are defined by order parameters (synchrony, firing rates) not topological invariants.

**Jin Wang group nonequilibrium landscape:** The potential landscape of neural networks has multiple basins (memory states, oscillatory states). Transitions between basins are described as phase transitions quantified by entropy production and curl flux. The closed-ring attractor (relevant for oscillations) has a non-trivial loop topology. This is ring-attractor topology — the closest Chinese physics work to topological phase language applied to neural systems. (2013 PNAS, DOI: 10.1073/pnas.1310692110; 2023 J. Chem. Phys., DOI: 10.1063/5.0169296)

**Tagliazucchi and Chialvo:** "Brain complexity born out of criticality" (2012) established evidence for second-order phase transition in human brain dynamics, with associated long-range correlations and avalanches. This is criticality, not topological ordering.

**Deco, Kringelbach, García-Ojalvo group:** "Complex spatiotemporal oscillations emerge from transverse instabilities in large-scale brain networks" (PLOS Computational Biology 2022, DOI: 10.1371/journal.pcbi.1010781). Bifurcation landscape of large-scale brain models. Spatiotemporal dynamics emerge from a transverse instability of the synchronized state — a Turing-like instability.

### 4.2 Psychedelics and High-Coherence States

**Petri et al. psilocybin (2014, J. Royal Society Interface, DOI: 10.1098/rsif.2014.0873):** The landmark paper. Applied persistent homology (H₁) to resting-state fMRI after psilocybin vs. placebo in 15 subjects. Found:
- Psilocybin produces many transient, low-stability H₁ generators AND a small number of highly persistent ones absent in placebo
- The persistent scaffold under psilocybin shows strong, long-range cross-modular connections not present at baseline
- This is a genuine measurable difference in the *homological structure* of brain functional connectivity during a high-coherence altered state

**Critical assessment:** This is the single most important paper for the user's interest. It demonstrates that H₁ features (1-cycles in the functional connectivity graph) are qualitatively different under psychedelics. However: (a) The analysis is on H₁ of a *network graph*, not on the full topological structure of neural activity space; (b) The change is quantitative (more/fewer generators, different persistence distributions), not a discrete topological invariant flipping value; (c) The connection to Z₂ cohomology in any formal sense is absent.

**Singer et al. psilocybin + meditation (Scientific Reports 2024, DOI: 10.1038/s41598-024-55726-x):** Used Mapper algorithm and optimal transport distance (not persistent homology per se) on fMRI during focused attention and open monitoring meditation before/after psilocybin retreat. Found measurable shifts in the topological "location" of meditation states in brain-state space. Open monitoring became more distinct from rest after retreat. Insightfulness correlated with topological distance of OM states pre/post. Does not measure H₁ directly.

**Li et al. "Hierarchical fluctuation shapes a dynamic flow linked to states of consciousness" (Nature Communications 2023, DOI: 10.1038/s41467-023-38972-x):** (Chinese authors: A. Li, Bing Liu, Cheng Zhang, Haiyang Liu, Hao Yan, Kaixin Li, Meng Wang, Qian Wu, R. Han, Shangzheng Huang, Sheng He, X. Lei, Xiaohan Tian, Xiaoqun Wang, Xin Zhou, Y. Yan, Yingjie Peng, Yini He, Yuqing Sun — affiliations span multiple Chinese institutions.) Found that "a global state of consciousness might not depend on a specific brain region or location in Euclidean space; rather, it is linked to a low-dimensional dynamic pattern in **topological space**." This explicitly states that consciousness is organized in topological space, across multiple imaging modalities (fMRI, EEG) and species. The "topological space" here is the manifold of brain states (latent space), not a topological invariant space — but this is exactly the conceptual bridge the user is interested in.

**DMT whole-brain dynamics (Pallavicini, Timmermann, Deco, Kringelbach, Carhart-Harris et al., Nature Communications Biology 2025, DOI: 10.1038/s42003-025-07576-0):** DMT "transient destabilization" of whole-brain dynamics corresponds to a parametric region where minimal perturbations achieve maximal effect — a signature consistent with proximity to a phase transition (critical slowing down). No topological invariants measured.

### 4.3 Flow States, Meditation — the Specific Gap

For flow states and deep meditation (beyond psychedelics), no TDA study has been published that identifies a topological signature. The Sacchet group's jhana meditation study (Cerebral Cortex 2023) is a high-quality imaging study of advanced meditators, but uses standard fMRI analysis, not TDA. There is no published work characterizing the persistent homology of brain activity during flow states.

---

## 5. Topological Invariants Beyond Persistent Homology

### 5.1 Why Condensed-Matter Topological Invariants Cannot Be Directly Applied to Neural Data

In condensed matter physics, topological invariants (Chern numbers, Z₂ indices, winding numbers, Berry phase) are properties of the ground state of a many-body quantum system. They require:
1. A well-defined Hamiltonian (or Bloch Hamiltonian in k-space)
2. A spectral gap between ground and excited states
3. Symmetry constraints (time-reversal, particle-hole, chiral)
4. Quasi-periodic (crystal) structure or some equivalent

Neural systems have none of these in the literal sense. They are classical (or at most mesoscopic quantum), non-equilibrium, open systems with no natural analog of a Brillouin zone. The gap between condensed-matter topology and neural topology is not just technical but conceptual.

### 5.2 Approaches That Are Closer

**Lattice field theory for neural networks (Bardella, Franchini, Pani, Ferraina, iScience 2024, DOI: 10.1016/j.isci.2024.111390; also "Neural Activity in Quarks Language," Entropy 2024):** Applies lattice physics (the standard framework for quantum chromodynamics) to neural spatiotemporal interactions. Introduces an energy functional for neural networks using lattice field theory. This creates the potential to define topological objects (instantons, vortices, hedgehogs) in neural activity fields, analogous to topological defects in physical systems. This is the most promising approach for eventually defining a genuine topological invariant of neural activity — but the published work does not yet compute such invariants.

**Topological quantum neural networks (Marciano, Zappala, Fields et al., arXiv 2210.13741, updated 2024):** Proposes viewing deep neural networks as the semi-classical limit of topological quantum field theories (TQFT). This is a theoretical framework — not applied to biological neural data. But it explicitly connects neural computation to topological invariants via TQFT. The Free Energy Principle connection (Fields, Friston, Glazebrook, Levin, Marciano, 2022) maps FEP to topological quantum neural networks via cone-cocone diagrams.

**Sheaf cohomology for neural computation (Girish et al., arXiv 2512.08241, 2025):** Reformulates neural computation as evolution of cochain maps over dynamic simplicial complexes. Introduces cohomological operators that generalize gradient descent. Uses sheaf cohomology, spectral Laplacians, and persistent homology together. This is the most mathematically ambitious approach to characterizing neural computation using cohomological language. No invariants in the condensed-matter sense, but the framework would support computing them if the right analog of a "Hamiltonian" were identified.

**Hermitian and non-Hermitian topology in active matter (Sone, Yokomizo, Kawaguchi, Ashida, arXiv 2407.16143, 2024):** Reviews how non-Hermitian topology (topological insulators and their non-Hermitian generalizations) applies to active matter — biological systems with self-propulsion. This is the closest the physics topology community has come to discussing biological systems in topological invariant terms. The key insight is that non-equilibrium (non-Hermitian) dynamics can still support topological edge modes. Neural systems are non-equilibrium. Whether the non-Hermitian topology framework can be applied to neural population activity is an open question — this paper does not attempt it.

**Information topology (Baudot, arXiv 2018):** A framework using homological algebra to characterize statistical dependencies in neural data. Proposes that information topology provides a basis for understanding consciousness. Uses H¹ in an information-theoretic context (not geometric). This is genuinely topological but in a different mathematical sense.

### 5.3 Wilson Loops, Berry Phase, and Neural Systems

No published paper applies Wilson loops or Berry phase to biological neural network data. The closest analog: the ring-attractor topology in Jin Wang's oscillation landscape has a non-trivial loop (the closed ring), which is topologically similar to a Berry phase path integral — but this analogy has not been formalized.

**Selective and quasi-continuous switching of Ferroelectric Chern Insulator Device for Neuromorphic Computing (Chen et al., Nature Nanotechnology 2024, DOI: 10.1038/s41565-024-01698-y):** Uses Chern insulator (topological edge states) as the physical substrate for neuromorphic (artificial) synaptic devices. This is NOT biological neural networks but shows that the condensed-matter topology community is actively interfacing with neural-inspired computing at the hardware level.

### 5.4 Higher-Dimensional Topology: K-Theory, BV-Cohomology, Homotopy

No published paper applies K-theory, BV-BRST cohomology, or homotopy-theoretic structures to biological neural dynamics. The sheaf cohomology paper (Girish et al.) comes closest to using sophisticated algebraic topology. The TQFT neural network framework (Marciano et al.) uses topological field theory but for artificial networks. This entire corner of the mathematical landscape remains unexplored for biological neural systems.

---

## 6. Cross-Reference: Where This Connects to the PCI Framework

### 6.1 The PCI Framework (Paper 14 v1.6, DOI: 10.5281/zenodo.20145811)

The user's published framework treats consciousness/cognition as having a "cross-substrate residence-pathology" structure. The extension being explored is whether topological invariants of neural activity could serve as the substrate-specific indicator of residence (healthy, integrated cognitive state) vs. pathology (fragmented, decoherent, or absent coherent organization).

### 6.2 Where the Literature Supports This Direction

The following findings from the literature are directly relevant to constructing such a framework:

**1. Cognitive states have distinct topological signatures in TDA:** Duong-Tran et al. (2024) showed H₀/H₁/H₂ features distinguish different cognitive tasks. Petri et al. (2014) showed psilocybin qualitatively changes H₁ structure. Li et al. (2023, Chinese group) explicitly state that consciousness is organized in topological space. These collectively support the idea that different "residence states" correspond to different topological regimes.

**2. Nonequilibrium phase language maps cleanly:** Jin Wang's framework (2013–2025) provides a physically rigorous way to describe neural state transitions as phase transitions with landscape topology, entropy production, and curl flux as order parameters. The "ring attractor" topology of coherent oscillations is directly analogous to a non-trivial 1-cycle. This framework could, with extension, support defining a topological invariant of the attractor structure.

**3. The lattice field theory approach (Bardella et al. 2024) creates a substrate** for eventually defining topological defects in neural activity fields — analogous to vortices in a superconductor or skyrmions in a magnetic system. Topological defects carry topological charge (an integer winding number), which would be a genuine topological invariant of neural activity.

**4. Non-Hermitian topology in active matter (Sone et al. 2024)** provides the mathematical language for topological invariants in non-equilibrium biological systems — exactly the regime neural networks occupy.

### 6.3 What Would Be Novel

A paper in this space that could constitute a genuine advance would need to:

1. **Define the analog of a Hamiltonian** for a neural system — likely via a lattice field theory action (Bardella framework) or a non-Hermitian effective Hamiltonian derived from the neural dynamics
2. **Identify the relevant symmetry class** — this determines which topological invariant is appropriate (Z, Z₂, or other)
3. **Compute the topological invariant** from neural data (either simulated or empirical) and show it takes different values in different cognitive states
4. **Demonstrate robustness** — topological invariants are by definition insensitive to smooth perturbations, so they should be stable against noise while discriminating between distinct phases

This program is conceptually coherent and has no published prior art treating biological neural systems as literal topological states of matter.

---

## 7. Annotated Bibliography (Key Citations with DOIs)

**[1] Ringach, D.L., Mémoli, F., Carlsson, G., Sapiro, G., Singh, G., Ishkhanov, T. (2008).** "Topological analysis of population activity in visual cortex." *Journal of Vision* 8(8):11.  
DOI: 10.1167/8.8.11  
*First application of persistent homology to neural population activity. Found V1 spontaneous activity has topology of RP².*

**[2] Petri, G., Expert, P., Turkheimer, F., Carhart-Harris, R., Nutt, D., Hellyer, P.J., Vaccarino, F. (2014).** "Homological scaffolds of brain functional networks." *Journal of the Royal Society Interface* 11(101).  
DOI: 10.1098/rsif.2014.0873  
*Landmark paper showing psilocybin changes H₁ structure of functional connectivity. The most important paper for cognitive-state topological signatures.*

**[3] Xu, B., Morozov, D., Kang, L. (2021).** "Evaluating State Space Discovery by Persistent Cohomology in the Spatial Representation System." *Frontiers in Computational Neuroscience* 15:616748.  
DOI: 10.3389/fncom.2021.616748  
*Rigorous evaluation of persistent cohomology for detecting torus/circle topology of grid and head direction cells. Gold standard for neural TDA methodology.*

**[4] Martínez-Riaño, D.E., Gómez, F., González, F.A. (2022).** "H₁ persistent features of the resting-state connectome in healthy subjects." *Network Neuroscience* 6(4).  
DOI: 10.1162/netn_a_00280  
*First systematic characterization of H₁ 1-cycles in resting-state fMRI. Found robust closed-loop synchronization cycles in healthy brains.*

**[5] Curto, C., Itskov, V., Veliz-Cuba, A., Youngs, N. (2013).** "The Neural Ring: An Algebraic Tool for Analyzing the Intrinsic Structure of Neural Codes." *Bulletin of Mathematical Biology* 75(9).  
DOI: 10.1007/s11538-013-9860-3  
*Algebraic geometry approach to neural codes. Defines neural ring/ideal. Connections to Stanley-Reisner rings. Most rigorous algebraic-topological framework for neural coding.*

**[6] Giusti, C., Henselman-Petrusek, G., Yoon, I.H.R., Ghrist, R., Smith, S.L., Yu, Y. (2024).** "Tracking the topology of neural manifolds across populations." *PNAS* 121(46).  
DOI: 10.1073/pnas.2407997121  
*Analogous cycles method for matching topological features across different neural populations. Mathematically rigorous. Applied to in vivo recordings.*

**[7] Duong-Tran, D., Kaufmann, R., Chen, J., Wang, X., Garai, S., Xu, F.H., Bao, J., Amico, E., Kaplan, A.D., Petri, G., Goñi, J., Zhao, Y., Shen, L. (2024).** "Homological landscape of human brain functional sub-circuits." *Mathematics* 12(3):455.  
DOI: 10.3390/math12030455  
*Most comprehensive computation of H₀, H₁, H₂ features across cognitive tasks in HCP data. Different homological orders sensitive to different task types.*

**[8] Wang, Y., Xian, J., Chen, Y., Yan, Y. (2025).** "Topological signatures of brain dynamics: persistent homology reveals individuality and brain–behavior links." *Frontiers in Human Neuroscience* 19:1607941.  
DOI: 10.3389/fnhum.2025.1607941  
*Persistent homology outperforms traditional features for predicting higher-order cognitive traits in ~1000 subjects.*

**[9] Wu, Y., Xu, L., Wang, J. (2025).** "Nonequilibrium dynamics and thermodynamics provide the underlying physical mechanism of the perceptual rivalry." *Physical Review Research* 7:023059.  
DOI: 10.1103/PhysRevResearch.7.023059  
*Chinese group (Jin Wang). Phase-transition framework for perceptual rivalry. Entropy production and flux quantify distance from transition points. Most rigorous Chinese physics work on neural phase transitions.*

**[10] Wang, X., Wu, Y., Xu, L., Wang, J. (2023).** "Global dynamics, thermodynamics and non-equilibrium origin of bifurcations for single neuron dynamics." *Journal of Chemical Physics* 159:154105.  
DOI: 10.1063/5.0169296  
*Jin Wang group. Landscape topography of single neurons. Topological features of the landscape (ring attractor) determine stability and oscillation coherence. Flux spikes near phase transition points.*

**[11] Li, A., Liu, B., Zhang, C., et al. (2023).** "Hierarchical fluctuation shapes a dynamic flow linked to states of consciousness." *Nature Communications* 14:3174.  
DOI: 10.1038/s41467-023-38972-x  
*Chinese group (multiple Chinese institutions). Explicitly states consciousness is organized in topological space. Cross-species, cross-modality evidence.*

**[12] Bardella, G., Franchini, S., Pani, P., Ferraina, S. (2024).** "Lattice physics approaches for neural networks." *iScience* 27:111390.  
DOI: 10.1016/j.isci.2024.111390  
*Applies lattice field theory (particle physics framework) to neural spatiotemporal interactions. Creates the potential for topological defect definitions in neural activity fields.*

**[13] Sone, K., Yokomizo, K., Kawaguchi, K., Ashida, Y. (2024).** "Hermitian and non-Hermitian topology in active matter." arXiv:2407.16143.  
DOI: 10.48550/arXiv.2407.16143  
*Reviews how non-Hermitian topological invariants (relevant to non-equilibrium biological systems) apply to active matter. Provides the mathematical language for topological invariants in neural systems.*

**[14] Singer, B., Meling, D., Hirsch-Hoffmann, M., et al. (2024).** "Psilocybin enhances insightfulness in meditation: a perspective on the global topology of brain imaging during meditation." *Scientific Reports* 14.  
DOI: 10.1038/s41598-024-55726-x  
*TDA (Mapper + optimal transport) applied to psilocybin + meditation fMRI. Topological distances between meditation states measured.*

**[15] Huang, H. (2024).** "Eight challenges in developing theory of intelligence." *Frontiers in Computational Neuroscience* 18:1388166.  
*Haiping Huang, Sun Yat-sen University. Statistical physics perspective on fundamental challenges in neural computation theory. Explicitly identifies manifold topology as an open challenge.*

**[16] Li, X. (2025).** "Memory as Structured Trajectories: Persistent Homology and Contextual Sheaves." arXiv:2508.11646.  
DOI: 10.48550/arXiv.2508.11646  
*Theoretical framework identifying memory traces with nontrivial homology generators on a latent manifold. Delta-homology generators as cycle-completing inference units.*

**[17] Girish, P., Mysore, R., Mahanthesha, U., Kumar, S., Prashant, S. (2025).** "Persistent Topological Structures and Cohomological Flows as a Mathematical Framework for Brain-Inspired Representation Learning." arXiv:2512.08241.  
DOI: 10.48550/arXiv.2512.08241  
*Most mathematically ambitious framework using sheaf cohomology and spectral Laplacians for neural computation. Cohomological operators generalizing gradient descent.*

**[18] Marciano, A., Zappala, E., Torda, T., et al. (2022, updated 2024).** "Deep Neural Networks as the Semi-classical Limit of Topological Quantum Neural Networks." arXiv:2210.13741.  
*Connects neural computation to topological quantum field theories. DNNs as semi-classical limit of TQNNs. Framework for eventually applying topological invariants to neural computation.*

**[19] Giusti, C., Pastalkova, E., Curto, C., Itskov, V. (2015).** "Clique topology reveals intrinsic geometric structure in neural correlations." *PNAS* (DOI via Semantic Scholar 118530690).  
*Hippocampal population activity has non-random, low-dimensional clique topology consistent with spatial coding — even during sleep. Key Curto-Itskov result.*

**[20] Wang, S., Huang, H. (2024).** "How high dimensional neural dynamics are confined in phase space." arXiv:2410.19348.  
*Haiping Huang, Sun Yat-sen University. M-shaped confinement of high-dimensional neural dynamics. Sharp boundaries in phase space. Thermodynamic potential characterization.*

---

## 8. Honest Gaps: What Has NOT Been Done

This section is a direct answer to the key question: **Is there published prior art treating the brain literally as a topological state of matter with measurable invariants?**

### 8.1 What Definitively Does Not Exist (as of May 2026)

**1. No Chern number computed for biological neural data.**
Chern numbers require a mapping of the system's states over a closed manifold (Brillouin zone analog) and computation of the Berry curvature integral. For neural systems, there is no natural analog of the Brillouin zone. No one has proposed a constructive mapping from neural population activity to a parameter space over which Berry curvature could be integrated. This is a genuine void.

**2. No Z₂ topological invariant (in the Kane-Mele sense) measured in neural data.**
The Z₂ invariants of topological insulators require time-reversal symmetry and a band structure. Neural systems are not time-reversal symmetric (they are dissipative, non-equilibrium). While non-Hermitian generalizations of Z₂ invariants exist, none has been applied to neural data.

**3. No winding number of a neural Hamiltonian.**
Winding numbers (relevant to 1D topological phases like the SSH model) require a Hamiltonian with a defined chiral symmetry. No paper has constructed such a Hamiltonian for biological neural dynamics.

**4. No topological phase transition in neural data.**
A topological phase transition requires a point at which a topological invariant changes its quantized value (and typically a gap closes at that point). No paper has identified such a transition in neural data. The "phase transitions" in the brain dynamics literature are dynamical (bifurcations, criticality), not topological in this sense.

**5. No Z₂ cohomology class (in the topological insulator sense) identified in a cognitive state.**
The Z₂ cohomology classes in persistent homology (computed with Z₂ coefficients) are not the same object as Z₂ topological invariants in condensed matter. No paper has demonstrated a Z₂ class in the condensed-matter sense appearing uniquely during a specific cognitive state.

**6. No Chinese physics group has applied condensed-matter topology formalism to biological neural networks.**
The topology groups at IOP-CAS, Tsinghua, Peking University, Westlake, etc. work exclusively on inorganic materials (topological insulators, Weyl semimetals, topological superconductors). The neuroscience groups at Chinese institutions use TDA tools (persistent homology) without condensed-matter topological invariants. The bridge between these two worlds has not been built by any group, Chinese or otherwise.

**7. No topological signature specific to flow states or non-pharmacological high-coherence states.**
The psychedelic literature (Petri 2014, Singer 2024) provides evidence that altered states change H₁ features, but: (a) these are drug-induced states, not endogenous high-coherence states; (b) the measures are quantitative, not topologically invariant. Flow states, jhana meditation, and peak creative states have not been studied with TDA.

**8. No Wilson loop computation on neural data.**
Wilson loops (the holonomy of the Berry connection around a closed loop in parameter space) have no published analog in neural systems. The closest conceptual analog — the geometric phase accumulated during a cycle in neural state space — has been noted qualitatively in ring-attractor models but never formalized as a Berry-phase computation.

**9. Higher algebraic topology (K-theory, BV-BRST cohomology, homotopy groups) entirely absent from experimental neuroscience.**
No experimental neuroscience paper uses K-theory or homotopy-theoretic tools. Some theoretical/mathematical biology papers (Marciano et al. TQFT framework) invoke these structures, but without connection to measured neural data.

### 8.2 Claims That Sound Like Prior Art But Are Not

**"Brain as topological state" (Marro, Torres, Tagliazucchi etc.):** These groups describe phase transitions in brain dynamics using statistical mechanics language. The "phases" are defined by order parameters (synchrony, entropy), not topological invariants. Using the word "phase" does not constitute treating the brain as a topological state of matter.

**"Topological features" in fMRI (Petri, Bassett, Goñi etc.):** These groups compute topological features of functional connectivity networks using persistent homology. "Topological feature" here means "shape descriptor," not "topological invariant of a state." The distinction is crucial.

**Psilocybin changes "the topology of brain functional networks" (Petri 2014):** This is genuinely topological (H₁ barcodes), but: the change is quantitative (more/fewer generators, different persistence), not a discrete jump in a topological invariant. The brain is not in a "topologically trivial" state at baseline and a "topologically non-trivial" state under psilocybin in the condensed-matter sense.

**Neural networks used to classify topological phases (many ML-in-physics papers):** These papers use artificial neural networks as tools to detect topological phases in quantum materials. This is the *reverse* direction from what the user is asking about.

### 8.3 Where the Opportunity Lies

The genuine research opportunity is to:

1. **Formalize a mapping from neural dynamics to a topological field theory** — the Bardella lattice field theory (2024) and the TQFT neural network framework (Marciano et al. 2024) together provide starting points
2. **Identify the relevant symmetry class** for neural dynamics — likely non-Hermitian (since the system is open/dissipative), which would map to the 38-fold classification of non-Hermitian topological phases
3. **Compute a topological invariant from data** using that mapping — this would be a first
4. **Demonstrate cognitive-state dependence** — show that the invariant takes different values during high-coherence (flow, meditation, psychedelic) vs. ordinary states
5. **Connect to the PCI framework** — the topological invariant would serve as a substrate-level indicator distinguishing "residence" topological sectors from "pathological" ones

This program has no prior art and would constitute a genuinely novel contribution. The closest precursors are: Petri et al. 2014 (for the empirical phenomenon), Jin Wang's landscape framework (for the physical language), Bardella et al. 2024 (for the field-theory substrate), and Sone et al. 2024 (for the non-Hermitian topological language in active matter).

---

*Report compiled from: arXiv, PubMed, Semantic Scholar, Royal Society Publishing, Nature Publishing Group, Physical Review journals, Frontiers journals.*  
*Primary searches conducted May 2026.*  
*Key DOIs verified against primary sources.*
