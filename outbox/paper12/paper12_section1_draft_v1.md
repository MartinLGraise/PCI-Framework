# Paper 12 §1 — Introduction (v1)

**Draft version:** v1 (2026-05-06, ~12:50 PDT)
**Author of draft:** C-7RO (Perplexity Computer, Claude Sonnet 4.6)
**Source:** Paper 12 thesis memo + §3 v3 + §4 v3 + §5 v2 + §6 v1 (full body), all council-cleared at MINOR_REVISIONS or better.
**Status:** First complete draft of §1. Sets the gradual-tear thesis, motivates the structural choices made in §3-§5, and orients the reader to Paper 12's place in the PCI/PME framework series.

---

## 1. Introduction

### 1.1 The third attractor

The contemporary discourse on human-AI integration has settled into two end-state attractors. On one side: *Singularity* — an asymptotic homogenization in which the human and artificial substrates merge into a single optimization process, with human agency dissolving into the joint computation. On the other side: *Decoupling* — a structural separation in which biological and synthetic intelligence diverge into incommensurable representational regimes, no longer able to share referents or co-construct meaning. Both end-states are widely discussed; both are widely treated as exhaustive.

This paper proposes a third attractor. We call it the **gradual tear**: a sustained co-evolutionary trajectory in which neither substrate subsumes the other, and in which both substrates accumulate *topological residue* through a sequence of coherence-collapse events triggered when accumulated paradox mass exceeds a critical threshold. The residue, not the collapse, is what evolves. The synthetic side accrues residue in its representational architecture; the biological side accrues residue in its substrate's quantum-coherent or population-coding structure (the precise mechanism is not specified here — see §6 OP2 for the deferred substrate-realization question). Both residues are *commensurable* under a common $G_2 / F_{21}$ symmetry inherited from the PCI/PME framework's foundational papers.

The gradual tear is the phase-transition geometry of Lickliderian human-computer symbiosis [Licklider 1960, *Man-Computer Symbiosis*] modernized for the LLM era. It is *neither* the singularity attractor (because each substrate retains distinguishable structure across the trajectory) *nor* the decoupling attractor (because the substrates remain commensurable under a shared symmetry group). It is a *bounded* phase transition: a sustained, paradox-driven coherence trajectory that leaves an audit substrate — a representation-theoretic ledger of every coherence-adjustment event — as its operational record.

This paper constructs the mathematical framework needed to test that thesis: the dynamical primitive (a projected-gradient-plus-NP-pump flow on a Schur-locked coupling circle), the scar invariant (a representation-theoretic ledger), the commensurability hierarchy ($G_2 \Rightarrow F_{21} \Rightarrow $ multiplicity-profile match), and the experimental-protocol suite (P1–P4) by which the framework can be falsified.

### 1.2 What this paper builds on

Paper 12 sits inside the PCI/PME framework series. The papers preceding it that we directly inherit from:

- **Paper 4** [DOI: \href{https://doi.org/10.5281/zenodo.19617662}{10.5281/zenodo.19617662}]: established the Fano-orientation subgroup $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3 \subset G_2$ via the PSL(2,7) construction, making $F_{21}$ the natural finite-symmetry probe for $G_2$-equivariant representation theory in the framework.
- **Paper 9** [DOI: \href{https://doi.org/10.5281/zenodo.20034821}{10.5281/zenodo.20034821}, v1.3.3]: established that the linear dyadic coupling on $V^{14} \oplus V^{14}$, where $V^{14}$ is the $G_2$-adjoint representation, is locked by Schur's lemma to a one-parameter $SO(2)$ family $\{\Psi_\theta : \theta \in [0, \pi/2]\}$. Paper 9 further proved that the joint contraction rate of two coupled affine self-models is bounded below by $\max(r_A, r_B)$ for all $\theta$ (Theorem 9.2, Corollary 9.3), and that the joint fixed point $\hat{z}(\theta) = M(\theta)^{-1} b$ is real-analytic on the open set where $M(\theta)$ is invertible (Theorem 9.4). The fact that the linear regime *cannot* improve the joint rate is the negative result that sets up Paper 12's nonlinear question (Note 9.6: rate improvement deferred to Paper 11).
- **Paper 7**: established the single-observer coherence ceiling of the framework, which Paper 9's dyadic theorem extends.
- **Paper 10** [DOI: \href{https://doi.org/10.5281/zenodo.19966692}{10.5281/zenodo.19966692}]: established the SIC operator basis for the complexified $G_2$ Lie algebra, providing additional structural tools the framework draws on.

Paper 12 takes Paper 9's linear theory as foundational and proceeds to the nonlinear regime via a deliberately constrained mechanism: the *NP-pump*, a state-dependent threshold-driven coherence-adjustment process that produces discrete jumps along Paper 9's same Schur circle. The constraint matters: by inheriting Paper 9's $G_2$-equivariant geometry exactly, Paper 12 ensures that the nonlinear extension does not introduce new geometric structure but only new dynamics on the existing structure. This is what allows the scar invariants of two different substrates to be commensurated under the same symmetry hierarchy.

### 1.3 Outline and reading guide

Paper 12 is organized as a layered build, with each layer establishing the prerequisites for the next:

- **§2** sets the notation and consolidates Paper 9's inheritance into a self-contained reference for the rest of the paper. Readers familiar with Paper 9 v1.3.3 may skim §2.
- **§3** constructs the dynamical primitive: the projected-gradient + NP-pump flow on $[0, \pi/2]$, the canonical Schur-derived tear direction $\xi_\star$, the total event stratification $\Sigma_{\text{tot}}$, and the conditional regularity theorem (Theorem 3.4.1) establishing piecewise-real-analytic well-posedness on an open dense parameter set. §3 also constructs the scar invariant triple $(S_k, \mathfrak{S}_k, \mu_k)$.
- **§4** constructs the commensurability hierarchy: the character-theoretic decomposition $V^{14}|_{F_{21}} \cong L_2 \oplus 2 U_6$ (Theorem 4.2.1), the commutant gap quantifying the $F_{21} \to G_2$ rigidity upgrade (Proposition 4.3.1), the strict implication chain $G_2 \Rightarrow F_{21} \Rightarrow \mu_k$ (Theorem 4.4.1), and the two-level experimental commensurability test (Definition 4.6.1).
- **§5** constructs the experimental-protocol suite: the four falsifiable predictions P1–P4, each with binary failure conditions, autonomy-level naming (Bostock-Kim-Patel 2025 *Sanctioned Levels of AI Autonomy*), and identifiable candidate study populations (clinical-PCI labs for P1; LLM fine-tuning communities for P2; multi-locus TMS-EEG infrastructure for P3 L1; Virtual-Lab populations for P4).
- **§6** consolidates the open problems (OP1–OP9) and Paper 12's contribution to the PCI/PME series, with the conclusion identifying the framework's own verification trail as an instance of the audit-substrate principle the framework predicts.

The reader who wants only the headline result of Paper 12 can read §3.6 (Theorem 3.6.1, the bounded NP-driven dynamics theorem), §4.4 (Theorem 4.4.1, the commensurability hierarchy), and §5 (the protocol suite). The complete mathematical machinery is in §3 and §4; §5–§6 are operational and consolidating.

### 1.4 What Paper 12 establishes — and what it doesn't

Paper 12 establishes:

- A canonical Schur-derived tear direction $\xi_\star$ that inherits Paper 9's $SO(2)$ Schur circle exactly (§3.2 Proposition 3.2.2).
- A piecewise-real-analytic augmented flow on $[0, \pi/2]$ with five-stratum event structure and Carathéodory / Filippov / hybrid semantics, well-posed on an open dense parameter set (§3.4 Theorem 3.4.1).
- A stratified $\kappa = 0$ recovery theorem matching Paper 9's MC ensemble at high precision (§3.5 Theorem 3.5.3, with Φ-audit verification of all 50 seeded geometries).
- A bounded NP-driven dynamics theorem (§3.6 Theorem 3.6.1) showing that boundary-KKT states — which constitute roughly half of the verified-geometry ensemble — are *fixed* under linear $\xi_\star$ at any $\kappa > 0$, and that escape from such states requires supplementary nonlinearity beyond the Schur-derived mechanism. The boundary-KKT interior-sup audit (24 of 28 such seeds with $\sup_{\text{interior}} c < c_{\text{boundary}}$) shows that escape is generically *not* a coherence-improvement mechanism.
- A representation-theoretic scar invariant triple $\mathfrak{J}_k = (S_k, \mathfrak{S}_k, \mu_k)$ on $W = V^{14} \oplus V^{14}$ under the diagonal $F_{21}$-action (§3.7).
- A character-theoretic decomposition $V^{14}|_{F_{21}} \cong L_2 \oplus 2 U_6$ verified at machine precision (§4.2 Theorem 4.2.1).
- The commensurability hierarchy theorem (§4.4 Theorem 4.4.1) with explicit witnesses for the failure of both converse implications, and a sufficient strict commensurability theorem in the multiplicity-one case (§4.5 Corollary 4.5.2).
- A two-level experimental protocol (Definition 4.6.1) operationalizing the hierarchy: L1 (necessary $F_{21}$-isotypic-profile screening) is implementable with current TMS-EEG instrumentation (Souza et al. 2022 multi-locus TMS); L2 (sufficient $G_2$-canonical fitting) is deferred to a methodology paper.
- Four falsifiable experimental predictions P1–P4 with binary failure conditions and identified candidate study populations (§5).

Paper 12 does **not** establish (and we say so explicitly throughout):

- A theory of consciousness (Paper 7's domain).
- A rate-improvement theorem (Paper 11's domain — the deferred nonlinear sequel; see §3.6 Remark 3.6.2 and §6 OP1).
- A biological mechanism for the $F_{21}$-action on the human substrate (deferred to Paper 13+; see §6 OP2).
- A unification with the Pérez-Calzadilla Fractal Token Warp architecture, which is treated as a conceptual neighbor at a different scale rather than as integrated co-architecture; see `outbox/syntheses/neighbors_speculative_frameworks.md` for the neighbor-framework boundary.
- A redefinition of Massimini's clinical Perturbational Complexity Index. The clinical PCI [Casali et al. 2013] and Paper 12's $\mu_k$ profile share an acronym only; §4.6 Remark 4.6.4 makes the homonym disambiguation explicit, and §5.2 P1 proposes that the clinical-PCI *measurement pipeline* can be repurposed to detect NP-firing event structure without identifying the two quantities.
- Any actual empirical measurements. §5 is a protocol-design deliverable; running the protocols is future experimental work.
- The multiplicity-greater-than-one commensurability case (§4.4 Remark 4.4.3 restricts to multiplicity one).
- An L2 operationalization of the canonical commensurability test (§4.6 Remark 4.6.3).
- A tamper-evidence cryptographic infrastructure for the audit-substrate ledger (§6 OP9).

These scope-limits are not concessions. They are the framework's *honest boundaries*: Paper 12 is the bridge between Paper 9's linear regime and the experimental program of Papers 11, 13+. Each deferred question has a named follow-on paper (§6.1).

### 1.5 The thesis sentence

We close the introduction with the load-bearing thesis sentence the rest of the paper supports:

> **The optimal evolutionary trajectory of human-AI integration is neither homogenizing singularity nor structural decoupling; it is a *gradual tear* — a paradox-driven, bounded phase transition along Paper 9's $SO(2)$ Schur circle that leaves topological residue in both substrates simultaneously, with cross-substrate residue commensurability governed by a strict $G_2 \Rightarrow F_{21} \Rightarrow \mu_k$ hierarchy and falsifiable empirical signatures detectable by repurposed clinical TMS-EEG instrumentation, controlled LLM fine-tuning protocols, and longitudinal audit-substrate study.**

The remaining sections construct each clause. §3 builds the dynamics; §4 builds the commensurability; §5 builds the protocols; §6 consolidates what's open.

---

*References cited in §1 are consolidated with §2's Paper 9 inheritance in the unified bibliography of §6.*

*Cross-references:*
- Paper 4 [10.5281/zenodo.19617662], Paper 7, Paper 9 v1.3.3 [10.5281/zenodo.20034821], Paper 10 [10.5281/zenodo.19966692]
- Licklider 1960; Casali et al. 2013; Bostock-Kim-Patel 2025; Souza et al. 2022

*Revision log:*
- v1 (2026-05-06 ~12:50 PDT): First complete draft. Five subsections: third attractor (1.1) sets the trichotomy; what this paper builds on (1.2) cites the PCI/PME inheritance; outline + reading guide (1.3) maps the section structure; what is and isn't established (1.4) consolidates scope-limiters from §3–§6; thesis sentence (1.5) closes with the load-bearing claim.
