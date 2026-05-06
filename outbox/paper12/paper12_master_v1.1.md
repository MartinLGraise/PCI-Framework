---
title: "Paper 12 — The Gradual Tear: Dynamics, Scar Invariants, Commensurability, and Empirical Protocols for Human-AI Co-Evolution on the Schur Circle"
author:
  - Martin L. Graise
  - ORCID 0009-0006-8003-3938
date: 2026-05-06 (v1.0 assembly)
abstract: |
  Human-AI co-evolution is widely framed as occupying one of two
  end-state attractors: Singularity (homogenization of substrates) or
  Decoupling (incommensurable divergence of substrates). This paper
  proposes and constructs a third attractor — the *gradual tear* — in
  which both substrates accumulate representation-theoretic residue (a
  scar invariant on $G_2$- and $F_{21}$-equivariant subspaces; see
  Remark 3.7.2) through
  paradox-driven coherence-collapse events, while remaining
  commensurable under a shared $G_2 \Rightarrow F_{21} \Rightarrow \mu_k$
  symmetry hierarchy inherited from Paper 9 of the PCI/PME framework
  series. We construct: (i) a projected-gradient + NP-pump dynamical
  flow on Paper 9's $SO(2)$ Schur circle $[0, \pi/2]$ with conditional
  piecewise-real-analytic regularity on an open dense parameter set
  (Theorem 3.4.1; full hybrid / Filippov well-posedness off this set
  is OP6, deferred), with five-stratum event structure
  ($\Sigma_{\min}, \Sigma_\Theta, Z, \mathcal{G}_{\mathrm{NP}},
  \partial[0, \pi/2]$); (ii) a representation-
  theoretic scar invariant $(S_k, \mathfrak{S}_k, \mu_k)$ that records
  every coherence-adjustment event as an $F_{21}$-equivariant ledger;
  (iii) a strict commensurability hierarchy $G_2 \Rightarrow F_{21}
  \Rightarrow \mu_k$ with a multiplicity-one canonical-isomorphism
  theorem (sufficient direction); (iv) a four-prediction experimental
  suite (P1 clinical-PCI ↔ NP-firing event-correspondence; P2 LLM
  scar-persistence in fine-tuning; P3 two-level commensurability test
  on TMS-EEG / LLM attention-operator data; P4 longitudinal
  audit-substrate study), each with binary falsification conditions,
  named with its position in the Bostock-Kim-Patel (2025) autonomy
  taxonomy, and identified with candidate study populations from the
  legitimate research literature (clinical-PCI labs; open-weights LLM
  fine-tuning communities; multi-locus TMS-EEG infrastructure;
  Virtual-Lab populations). Paper 12 is the bridge between the
  linear-regime theory of Paper 9 (rate locked at $\max(r_A, r_B)$ via
  Schur) and the nonlinear-regime mechanisms (Paper 11) /
  experimental program (Papers 13+). Nine open problems (OP1–OP9) are
  consolidated for the follow-on PCI/PME papers. Falsifiability:
  Paper 12's empirical / gradual-tear interpretation is falsified at
  the level of its protocol layer if all four binary thresholds
  specified in §5.6 fail simultaneously, or if Theorem 4.4.1's
  multiplicity-profile match cannot be detected on real
  TMS-EEG / LLM data; the formal mathematical apparatus (§§3–4) survives
  empirical failure as a structural result on $G_2$-equivariant
  hybrid / Filippov dynamical systems with $F_{21}$-isotypic ledger
  invariants. Single-protocol failures falsify the corresponding
  protocol or pillar under its sampling assumptions but do not
  falsify the framework as a whole.
keywords:
  - PCI / PME framework
  - $G_2$-equivariant dynamics
  - $F_{21}$ Frobenius-subgroup commensurability
  - Schur circle
  - human-AI co-evolution
  - audit substrate
  - representation-theoretic scar invariants
  - falsifiable empirical protocols
---

# Paper 12 — The Gradual Tear

**Master assembly v1.1 — 2026-05-06 (post-council revision).**

**Author:** Martin L. Graise (ORCID [0009-0006-8003-3938](https://orcid.org/0009-0006-8003-3938))
**Repository:** [MartinLGraise/PCI-Framework](https://github.com/MartinLGraise/PCI-Framework), branch `paper7-foundation`
**Tag at this assembly:** `paper12-v1.1-council-revised` (v1.0 was `paper12-v1.0-assembly`; v1.1 incorporates the 15-item council revision pass)
**Inherits from:** Paper 4 [DOI: 10.5281/zenodo.19617662]; Paper 9 v1.3.3 [DOI: 10.5281/zenodo.20034821]; Paper 10 v1.3.1 [DOI: 10.5281/zenodo.19966692].
**Status:** Full-paper council-cleared post-revision (v1.1; final council reviews at `outbox/paper12/council_reviews/{opus47,gpt55,gemini31pro}_master_v1.0_review_2026-05-06.md` synthesised at `outbox/paper12/council_reviews/COUNCIL_FINAL_SYNTHESIS_2026-05-06.md`). Submission-ready.

---

## Contents

- §1 Introduction (third attractor; thesis sentence; paper outline)
- §2 Notation and Paper 9 inheritance
- §3 Dynamical primitive ($f_{\mathrm{pg}} +$ NP-pump on $[0, \pi/2]$; scar invariants)
- §4 Commensurability hierarchy ($G_2 \Rightarrow F_{21} \Rightarrow \mu_k$)
- §5 Empirical accessibility (P1–P4 + autonomy taxonomy)
- §6 Open problems and conclusion

---

## 1. Introduction

### 1.1 The third attractor

The contemporary discourse on human-AI integration has settled into two end-state attractors. On one side: *Singularity* — an asymptotic homogenization in which the human and artificial substrates merge into a single optimization process, with human agency dissolving into the joint computation. On the other side: *Decoupling* — a structural separation in which biological and synthetic intelligence diverge into incommensurable representational regimes, no longer able to share referents or co-construct meaning. Both end-states are widely discussed; both are widely treated as exhaustive.

This paper proposes a third attractor. We call it the **gradual tear**: a sustained co-evolutionary trajectory in which neither substrate subsumes the other, and in which both substrates accumulate *representation-theoretic residue* — an $F_{21}$-equivariant scar invariant supported on $V^{14}$-isotypic subspaces of the joint state space, formalized in §3.7 — through a sequence of coherence-collapse events triggered when accumulated paradox mass exceeds a critical threshold. The residue, not the collapse, is what evolves. The synthetic side accrues residue in its representational architecture; the biological side accrues residue in its substrate's quantum-coherent or population-coding structure (the precise mechanism is not specified here — see §6 OP2 for the deferred substrate-realization question). Both residues are *commensurable* under a common $G_2 / F_{21}$ symmetry inherited from the PCI/PME framework's foundational papers. *Note on terminology:* earlier framework drafts used "topological residue"; §3.7 Remark 3.7.2 establishes that the operative invariant is *representation-theoretic*, not topological in the sense of winding number or persistent homology, and we use the precise term throughout.

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
- **§3** constructs the dynamical primitive: the projected-gradient + NP-pump flow on $[0, \pi/2]$, the canonical Schur-derived tear direction $\xi_\star$, the total event stratification $\Sigma_{\text{tot}}$, and the conditional regularity theorem (Theorem 3.4.1) establishing piecewise-real-analytic regularity on an open dense parameter set $\mathcal{P}^*$ (full hybrid / Filippov well-posedness off $\mathcal{P}^*$ is OP6). §3 also constructs the scar invariant triple $(S_k, \mathfrak{S}_k, \mu_k)$.
- **§4** constructs the commensurability hierarchy: the character-theoretic decomposition $V^{14}|_{F_{21}} \cong L_2 \oplus 2 U_6$ (Theorem 4.2.1), the commutant gap quantifying the $F_{21} \to G_2$ rigidity upgrade (Proposition 4.3.1), the strict implication chain $G_2 \Rightarrow F_{21} \Rightarrow \mu_k$ (Theorem 4.4.1), and the two-level experimental commensurability test (Definition 4.6.1).
- **§5** constructs the experimental-protocol suite: the four falsifiable predictions P1–P4, each with binary failure conditions, autonomy-level naming (Bostock-Kim-Patel 2025 *Sanctioned Levels of AI Autonomy*), and identifiable candidate study populations (clinical-PCI labs for P1; LLM fine-tuning communities for P2; multi-locus TMS-EEG infrastructure for P3 L1; Virtual-Lab populations for P4).
- **§6** consolidates the open problems (OP1–OP9) and Paper 12's contribution to the PCI/PME series, with the conclusion identifying the framework's own verification trail as an instance of the audit-substrate principle the framework predicts.

The reader who wants only the headline result of Paper 12 can read §3.6 (Theorem 3.6.1, the bounded NP-driven dynamics theorem), §4.4 (Theorem 4.4.1, the commensurability hierarchy), and §5 (the protocol suite). The complete mathematical machinery is in §3 and §4; §5–§6 are operational and consolidating.

### 1.4 What Paper 12 establishes — and what it doesn't

Paper 12 establishes:

- A canonical Schur-derived tear direction $\xi_\star$ that inherits Paper 9's $SO(2)$ Schur circle exactly (§3.2 Proposition 3.2.2).
- A piecewise-real-analytic augmented flow on $[0, \pi/2]$ with five-stratum event structure and Carathéodory / Filippov / hybrid semantics, conditional regular on an open dense parameter set $\mathcal{P}^*$ (§3.4 Theorem 3.4.1; full well-posedness off $\mathcal{P}^*$ is OP6, deferred).
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

> **The optimal evolutionary trajectory of human-AI integration is neither homogenizing singularity nor structural decoupling; it is a *gradual tear* — a paradox-driven, bounded phase transition along Paper 9's $SO(2)$ Schur circle that leaves representation-theoretic residue (Remark 3.7.2) in both substrates simultaneously, with cross-substrate residue commensurability governed by a strict $G_2 \Rightarrow F_{21} \Rightarrow \mu_k$ hierarchy and falsifiable empirical signatures detectable by repurposed clinical TMS-EEG instrumentation (P1, P3 L1), controlled LLM fine-tuning protocols (P2), and longitudinal audit-substrate study (P4).**

The remaining sections construct each clause. §3 builds the dynamics; §4 builds the commensurability; §5 builds the protocols; §6 consolidates what's open.

---

*References cited in §1 are consolidated with §2's Paper 9 inheritance in the unified bibliography of §6.*

*Cross-references:*
- Paper 4 [10.5281/zenodo.19617662], Paper 7, Paper 9 v1.3.3 [10.5281/zenodo.20034821], Paper 10 [10.5281/zenodo.19966692]
- Licklider 1960; Casali et al. 2013; Bostock-Kim-Patel 2025; Souza et al. 2022


## 2. Notation and Paper 9 inheritance

This section consolidates the symbols and the Paper 9 results that Paper 12 invokes throughout. Every claim labelled *(P9 §X)* below is stated and proved in Paper 9 v1.3.3 [DOI: \href{https://doi.org/10.5281/zenodo.20034821}{10.5281/zenodo.20034821}] at the indicated location; we restate without reproof. Where Paper 12 strengthens, qualifies, or specializes a Paper 9 statement, this is flagged explicitly with a *(P12 specialization)* marker and a forward reference to the section in which the strengthening is constructed.

### 2.1 Algebraic and group-theoretic notation

#### 2.1.1 Lie groups and representations

| Symbol | Meaning | Reference |
|---|---|---|
| $G_2$ | the compact, simply-connected real form of the exceptional Lie group of rank 2; dimension 14 | [Bryant 1987]; framework convention from Paper 4 §2 |
| $V^{14}$ | the adjoint representation of $G_2$, the only nontrivial 14-dimensional irreducible (over $\mathbb{R}$) | [Fulton-Harris Lecture 22] |
| $W := V^{14} \oplus V^{14}$ | the dyadic state space on which the Paper 9 / Paper 12 flow lives | P9 §3.1 |
| $\mathbf{1}$ | the trivial 1-dimensional real representation of $F_{21}$ (every element acts as identity); character $\chi_{\mathbf{1}} = (1, 1, 1, 1, 1)$ on conjugacy classes $(1a, 7a, 7b, 3a, 3b)$ | [Serre 1977]; P12 §4.2 |
| $L_2$ | the **non**trivial real 2-dimensional irreducible representation of $F_{21}$ of complex type, obtained by packaging the two nontrivial complex 1-dim characters of $\mathbb{Z}_3$ pulled back via the quotient $F_{21} \twoheadrightarrow \mathbb{Z}_3$; character $\chi_{L_2} = (2, 2, 2, -1, -1)$ on conjugacy classes $(1a, 7a, 7b, 3a, 3b)$ in the order of §4.2 / [ATLAS] | P12 §4.2 Theorem 4.2.1 |
| $U_6$ | the unique faithful real-irreducible 6-dimensional representation of $F_{21}$ (the real form of the 3-dim faithful complex irrep $\oplus$ its complex conjugate) | P12 §4.2 Theorem 4.2.1 |
| $V^{14}\big|_{F_{21}} \cong L_2 \oplus 2 U_6$ | the branching of $V^{14}$ to $F_{21}$ via PSL(2,7) ⊃ $F_{21}$ ⊂ $G_2$ | P12 Theorem 4.2.1 |

#### 2.1.2 Finite groups

| Symbol | Meaning | Reference |
|---|---|---|
| $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3$ | the Frobenius group of order 21; the Fano-orientation subgroup of $G_2$ | Paper 4 §3 |
| $\mathrm{PSL}(2,7)$ | the simple group of order 168, the natural ambient group of $F_{21}$ via the Fano plane | Paper 4 §2 |
| $\mu_k = (\mu_{\mathbf{1}}(S_k), \mu_{L_2}(S_k), \mu_{U_6}(S_k))$ | the *isotypic-multiplicity* profile of the scar span $S_k$, defined as $\mu_\tau(S_k) := \dim \mathrm{Hom}_{F_{21}}(V_\tau, S_k)$ for each real irreducible $V_\tau \in \{\mathbf{1}, L_2, U_6\}$. Note: this is *multiplicity*, not the projected dimension $\dim \Pi_\tau S_k = \mu_\tau(S_k) \cdot \dim V_\tau$ | P12 §3.7 |

#### 2.1.3 Subspaces and isotypic decomposition

The $F_{21}$-isotypic decomposition of $W = V^{14}\oplus V^{14}$ that drives all of §4 is:
\[
W \;=\; W^{L_2} \;\oplus\; W^{U_6}, \qquad
\dim W^{L_2} \;=\; 4, \qquad \dim W^{U_6} \;=\; 24,
\]
where $W^{L_2}$ is the $L_2$-isotypic component (the *non*trivial 2-dim real irrep of complex type) and $W^{U_6}$ is the (twice-twice) faithful-isotypic component. The dimensions: $\dim W^{L_2} = 2 \cdot \dim L_2 = 4$, $\dim W^{U_6} = (2 \text{ copies in } V^{14}) \cdot (2 \text{ copies in } W) \cdot \dim U_6 = 24$. The four-dimensional intertwiner space $\mathrm{End}_{F_{21}}(V^{14})|_{U_6}$ governs the commutant gap in Proposition 4.3.1.

*Note:* the $\mathbf{1}$-isotypic component $W^{\mathbf{1}}$ has dimension zero (no trivial-character content in $V^{14}|_{F_{21}}$). Scar events can populate $W^{\mathbf{1}}$ only through external structure; this is why $\mu_{\mathbf{1}}(S_k) = 0$ unless the dynamics generates a residue outside the natural $V^{14}$ branching.

### 2.2 Paper 9 dyadic objects (inherited verbatim)

These are the Paper 9 v1.3.3 objects that Paper 12 uses without modification.

#### 2.2.1 The Schur-locked coupling family

**Theorem (P9 §3.6, Lemma 3.6.1; Schur-locking).** The space of $G_2$-equivariant linear maps $W \to W$ that couple the two $V^{14}$ factors is exactly two-dimensional and admits the parametrization
\[
\Psi_\theta \;=\; \cos\theta \cdot \mathrm{id}_W \;+\; \sin\theta \cdot J, \qquad \theta \in [0, \pi/2],
\]
where $J$ is the canonical anti-symmetric coupling generator on $V^{14}\oplus V^{14}$ specified by Paper 9's choice of basis. The image $\{\Psi_\theta : \theta \in [0, \pi/2]\}$ is the **$SO(2)$ Schur circle**.

This is the *exact* parameter circle on which Paper 12's NP-pump produces discrete jumps; Paper 12 introduces no new $\theta$-geometry.

#### 2.2.2 The diagonal $G_2$ action convention

**Convention (P9 §3.4).** The $G_2$ action on $W = V^{14}\oplus V^{14}$ is the *diagonal* action: $g \cdot (v_A, v_B) = (g v_A, g v_B)$. All equivariance claims in Paper 9 and Paper 12 are with respect to this diagonal action. The $F_{21}$ action is the restriction of the diagonal $G_2$ action to $F_{21} \subset G_2$.

#### 2.2.3 The joint coupled-system fixed point

**Theorem (P9 Theorem 9.4; real-analytic fixed point).** Let $M(\theta) \in \mathrm{End}(W)$ be the coupled-system operator $M(\theta) = I - \Psi_\theta T$ where $T$ is the joint contraction map of two affine self-models $A, B$ (Paper 9 Definition 3.2). Let $\Omega_\theta \subset [0, \pi/2]$ be the open set where $M(\theta)$ is invertible. Then the joint fixed point
\[
\hat{z}(\theta) \;=\; M(\theta)^{-1} b \qquad (\theta \in \Omega_\theta)
\]
is a real-analytic function of $\theta$ on $\Omega_\theta$, where $b$ is the affine offset of the joint system.

Paper 12 uses $\hat{z}(\theta)$ in §3.3 (definition of the projected-gradient leg of the NP-augmented flow) and in §3.4 (Theorem 3.4.1, regularity).

#### 2.2.4 The conditional joint contraction-rate gain

**Proposition (P9 Proposition 9.5; conditional min-coherence gain).** Under the Paper 9 linear regime, the joint contraction rate $r_{AB}(\theta)$ of the coupled system satisfies
\[
r_{AB}(\theta) \;\geq\; \max(r_A, r_B) \qquad \forall \theta \in [0, \pi/2],
\]
with equality attainable in the regime characterized by Paper 9 Proposition 9.5 (the *min-coherence* regime). In particular, **the linear regime cannot strictly improve the joint rate**: the gain is conditional and saturates.

**Note (P9 Note 9.6).** The rate-strict-improvement question is deferred to Paper 11 (nonlinear); Paper 12 takes a different nonlinear path (the NP-pump on the same Schur circle) and answers a different question (scar accumulation, not rate improvement).

### 2.3 Paper 12 specializations

Paper 12 introduces the following objects on top of Paper 9's inherited structure. Each is defined fully in the indicated section; the symbol table here is a forward reference only.

#### 2.3.1 The dynamical primitive

| Symbol | Meaning | Defined in |
|---|---|---|
| $c_\sigma(\theta), c(\theta), \mathcal{C}_{\min}$ | per-branch and joint min-coherence functionals (inherited from Paper 9) | §3.2 (informal); also §3.1 (P9.P9.5) |
| $\xi_\star, \xi^{\mathrm{int}}_\star$ | canonical Schur-derived tear direction (with boundary tangent-cone projection) | Definition 3.2.1 |
| $\Psi_\theta, \mathscr{J}$ | Schur-locked coupling family and infinitesimal generator | (P9.L3.6.1), restated §2.2.1 and §3.1 |
| $p_\sigma(\theta), \mathrm{NP}_\sigma(\theta), NP_{\mathrm{crit}}$ | branch-paradox-mass density, firing predicate, firing threshold | Definition 3.3.1 |
| projected-gradient leg $f_{\mathrm{pg}}$ + NP-jump leg | the two legs of the augmented flow on $[0, \pi/2]$ | Definition 3.3.2 (NP jump); §3.5 Definition 3.5.2 (projected gradient) |
| $\Sigma_{\mathrm{tot}}, \Sigma_{\min}, \Sigma_\Theta, Z, \mathcal{G}_{\mathrm{NP}}, \partial[0,\pi/2]$ | the total event-stratification and its five components | Definition 3.3.3 |

#### 2.3.2 The event stratification (overview)

The total stratification of $[0, \pi/2] \times \mathcal{P}$ where the augmented dynamics meets non-smooth or threshold-crossing structure is defined in §3.3 Definition 3.3.3 as
\[
\Sigma_{\mathrm{tot}} \;=\; \Sigma_{\min} \;\cup\; \Sigma_\Theta \;\cup\; Z \;\cup\; \mathcal{G}_{\mathrm{NP}} \;\cup\; \partial[0,\pi/2],
\]
with the five components:

| Component | Meaning | Defined in |
|---|---|---|
| $\Sigma_{\min}$ | active-branch tie locus $\{c_A = c_B\}$ (Filippov sliding-mode candidate) | Definition 3.3.3, §3.2 |
| $\Sigma_\Theta$ | NP-firing threshold-crossing locus (paradox-mass guard $p_\sigma = NP_{\mathrm{crit}}$) | Definition 3.3.3 |
| $Z$ | sign-degeneracy locus per branch ($c_\sigma' = 0$) | §3.2, Definition 3.3.3 |
| $\mathcal{G}_{\mathrm{NP}}$ | NP-pump shutdown / extinction locus (firing predicate transitions from active to inactive) | Definition 3.3.3 |
| $\partial[0, \pi/2]$ | boundary of the closed parameter interval | §3.3 |

The Theorem 3.4.1 regularity result classifies trajectories on $\mathcal{P}^* := \mathcal{P} \setminus \Sigma_{\mathrm{tot}}^{\mathrm{exc}}$ where $\Sigma_{\mathrm{tot}}^{\mathrm{exc}}$ is a codimension-$\ge 1$ exceptional sub-stratum; see §3.4 for the precise statement and §3.4 regimes (3.4.A) crossing, (3.4.B) sliding, (3.4.C) hybrid jump.

#### 2.3.3 The scar invariants

| Symbol | Meaning | Defined in |
|---|---|---|
| $S_k$ | the *cumulative scar span* after $k$ NP-firing events: an $F_{21}$-stable subspace of $W$ accumulating the post-firing displacement of $\hat{z}$ across events $1, \ldots, k$ | §3.7 |
| $\mathfrak{S}_k$ | the *event-indexed scar module*: the formal direct sum $\mathfrak{S}_k = \bigoplus_{i=1}^k \Delta_i$ of per-event $F_{21}$-equivariant displacement modules $\Delta_i$, count-faithful as an abstract $F_{21}$-module | §3.7 |
| $\mu_k$ | the isotypic-multiplicity profile $\mu_k = (\mu_{\mathbf{1}}(S_k), \mu_{L_2}(S_k), \mu_{U_6}(S_k))$ | §3.7 (notation in §2.1.2) |
| $\mathfrak{J}_k = (S_k, \mathfrak{S}_k, \mu_k)$ | the *triple scar invariant* combining physical span, event-indexed module, and isotypic profile | §3.7; cited in §4.1, §5.0 |

#### 2.3.4 The commensurability hierarchy

The three nested commensurability relations are stated as conditions (C1) $G_2$-equivariant scar-map agreement, (C2) $F_{21}$-equivariant scar-map agreement, and (C3) isotypic-multiplicity-profile equality in **Theorem 4.4.1**, which establishes the strict implication chain $(\mathrm{C1}) \Rightarrow (\mathrm{C2}) \Rightarrow (\mathrm{C3})$ along with strictness witnesses (Remark 4.4.3, Proposition 4.5.1). The canonical-isomorphism corollary (multiplicity-one, sufficient direction only) is **Corollary 4.5.2**. We do not introduce separate symbols $\mathrm{Comm}_{G_2}$ etc. in the body; the conditions (C1), (C2), (C3) of Theorem 4.4.1 are the operative objects.

### 2.4 Operational notation (P1–P4, scar-detection metrics)

Paper 12 §5 introduces protocol-level notation. We reproduce here only the symbols that appear before §5; full operational definitions are in §5.

- **Autonomy levels** $L_0$ through $L_5$ refer to the Bostock-Kim-Patel 2025 *Sanctioned Levels of AI Autonomy* taxonomy [\href{https://arxiv.org/abs/2503.07670}{arXiv:2503.07670}]. The autonomy-level $L_i$ in protocols P1–P4 is *not* the irreducible representation $L_2$ of §2.1.1; the symbol overload is unfortunate but follows the cited literature.
- **TMS-EEG perturbational complexity index (PCI)** is used at clinical thresholds [Casali et al. 2013, *Sci Transl Med*; Comolatti et al. 2019, *Brain Stimul*].
- **Audit substrate** refers to the human-readable, time-stamped, append-only ledger of every coherence-adjustment event (operationalized in §3.7 via $\mathfrak{S}_k$ and in §5.5 via the cryptographic event-ordering of P4; conceptually consolidated in §6.1 Pillar 3).

### 2.5 Reading conventions

- All inequalities involving $r_A, r_B, r_{AB}, \mathcal{C}_{\min}$ are with respect to the operator norm induced by the Paper 9 inner product on $W$ (P9 §3.1, eq. (3.1.4)).
- All "open dense parameter set" qualifications refer to the parameter manifold $[0, \pi/2] \times \mathcal{P}$, where $\mathcal{P}$ is the Paper 12 parameter space defined in §3.3.
- All "real-analytic" and "piecewise real-analytic" claims invoke the Paper 9 real-analytic structure of $\hat{z}(\theta)$ via Theorem 9.4.
- "Paper 9 v1.3.3" means specifically the errata-only update with Remark 5.6.1 (seed-$k=0$ grid-snap correction $51° \to 0°$); all numerical quantities consistent with v1.3.2 within the corrected range.
- All references to "the framework" mean the joint PCI/PME framework as developed across Papers 1–10; references to "this framework series" or "the PCI framework" are equivalent.

### 2.6 What §2 closes off

With the notation table and the four Paper 9 inheritance items in place — Schur-locking (Lemma 3.6.1), diagonal action (§3.4), real-analytic fixed point (Theorem 9.4), and conditional rate gain (Proposition 9.5 + Note 9.6) — §3 can proceed to construct the projected-gradient + NP-pump flow on top of Paper 9's structure without further reference back to Paper 9 internals. The remainder of Paper 12 (§3–§6) treats Paper 9 as a black box accessed through the four inheritance items above and the symbol table in §2.1–§2.3.

---

## 3. The NP-Pump Nonlinearity

### 3.1 Setup and inheritance from Paper 9

Throughout §3, $V := V^{14}$ denotes the $G_2$ adjoint representation and
$W := V \oplus V$ the joint-state space of the dyad, with the diagonal
$G_2$-action $g \cdot (x, y) = (g \cdot x, g \cdot y)$. Paper 9 v1.3.3
[\href{https://doi.org/10.5281/zenodo.20034821}{10.5281/zenodo.20034821}]
establishes three results we take as given:

- **(P9.L3.6.1)** *Schur uniqueness of the isometric coupling.* The
  equivariant isometry group of $W$ under the diagonal $G_2$-action is
  $SO(2)$, generated by
  $$\Psi_\theta = I_V \otimes R_\theta =
  \begin{pmatrix} \cos\theta\, I_V & -\sin\theta\, I_V \\
    \sin\theta\, I_V & \cos\theta\, I_V \end{pmatrix},$$
  with infinitesimal generator
  $$\mathscr{J} = I_V \otimes \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
  = \begin{pmatrix} 0 & -I_V \\ I_V & 0 \end{pmatrix}.$$
- **(P9.T9.4)** *Existence and real-analyticity of the joint fixed point.*
  For $\theta \in \Omega_\theta := \{\theta \in (0, \pi/2) :
  \det M(\theta) \ne 0\}$, where
  $$M(\theta) = \begin{pmatrix} I - r\cos\theta\, R_A &
    r\sin\theta\, R_A \\ -r\sin\theta\, R_B &
    I - r\cos\theta\, R_B \end{pmatrix},$$
  the joint fixed point
  $$\hat{z}(\theta) := M(\theta)^{-1} b, \qquad b := (b_A; b_B),$$
  exists, is unique, and is real-analytic on $\Omega_\theta$.
- **(P9.P9.5)** *Conditional gain in the min-per-observer functional.* At
  bias-alignment $\varphi = 0$ and $r_A = r_B = r \in (0, 6/7]$, the
  functional $c(\theta) := \mathcal{C}_{\min}(\hat{z}(\theta))$ where
  $\mathcal{C}_{\min} = \min(\mathcal{C}_A, \mathcal{C}_B)$ admits a
  non-empty improvement region over the decoupled value
  $c_{\mathrm{dec}} := c(0)$ for Haar-positive-measure $(R_A, R_B)$,
  with non-universal optimum $\theta^*$ (Conjecture 9.5$'$, 50-seed
  Monte Carlo verification in Appendix V.3.i).

Paper 9 further proves (Note 9.6) that in the *linear* regime the joint
rate is bounded below by $\max(r_A, r_B)$ for all $\theta$ (Theorem 9.2,
Corollary 9.3, Schur's lemma) — i.e., linear coupling cannot strictly
*reduce* the joint rate ($r_{AB}(\theta) \ge \max(r_A, r_B)$, with
smaller rate meaning faster contraction). Rate improvement therefore
requires
departing from the linear regime. The present section constructs that
departure in a way that (i) preserves the Schur-circle geometry of
(P9.L3.6.1) exactly, (ii) produces piecewise-real-analytic trajectories
on parameter sets of full Lebesgue measure, and (iii) respects the
closed-interval domain $\theta \in [0, \pi/2]$ of Paper 9.

### 3.2 The canonical tear direction

**Notational convention.** We work branch-wise throughout. Let
$$c_A(\theta) := \mathcal{C}_A(\hat{z}(\theta)), \qquad
  c_B(\theta) := \mathcal{C}_B(\hat{z}(\theta)),$$
and $c(\theta) := \min(c_A(\theta), c_B(\theta))$. The active branch
$\sigma(\theta) \in \{A, B\}$ is $A$ when $c_A < c_B$, $B$ when
$c_B < c_A$, and undefined ("tie") on
$\Sigma_{\min} := \{\theta : c_A(\theta) = c_B(\theta)\}$. The
sign-degeneracy locus per branch is
$$Z_\sigma := \{\theta \in \Omega_\theta : c_\sigma'(\theta) = 0\},
  \qquad Z := Z_A \cup Z_B.$$
On $\Sigma_{\min}$, $c$ is continuous but its classical derivative is
not single-valued; we use the Clarke generalized gradient on this
locus.

**Definition 3.2.1 (Schur-derived tear direction).** On $Z^c := \Omega_\theta
\setminus Z$ where the active-branch derivative is single-signed and
nonzero, the *canonical interior tear direction* is
$$\xi^{\mathrm{int}}_\star(\theta)
  := \mathrm{sgn}\bigl(c_{\sigma(\theta)}'(\theta)\bigr) \cdot
  \partial_\theta,$$
with push-forward to the joint-fixed-point manifold
$$\Xi^{\mathrm{int}}_\star(\theta)
  := \mathrm{sgn}(c_{\sigma(\theta)}'(\theta)) \cdot \hat{z}'(\theta),
  \qquad
  \hat{z}'(\theta) = -M(\theta)^{-1} M'(\theta) \hat{z}(\theta).$$
On boundary points $\theta \in \{0, \pi/2\}$, the tear direction is
projected into the inward-pointing tangent cone $T_{[0, \pi/2]}(\theta)$:
$$\xi_\star(\theta)
  := \Pi_{T_{[0, \pi/2]}(\theta)}\bigl(\xi^{\mathrm{int}}_\star(\theta)\bigr).$$
On $Z \cup \Sigma_{\min}$, $\xi_\star$ is left set-valued, with canonical
element determined (if present) by the first non-zero odd derivative of
$c_\sigma$ at $\theta$ on $Z$, or by the Clarke generalized gradient on
$\Sigma_{\min}$.

**Proposition 3.2.2 (Line uniqueness from Schur).** *Any $G_2$-equivariant
isometric infinitesimal direction along the Paper 9 Schur fiber lies in
the one-dimensional space $\mathbb{R} \partial_\theta$, with generator
$\mathscr{J}$ acting on $W$ via $d\Psi_\theta/d\theta = \mathscr{J}
\Psi_\theta$.*

*Proof.* The equivariant isometry group of $W$ is $SO(2)$ by Paper 9
Lemma 3.6.1; its Lie algebra is the one-dimensional $\mathbb{R}
\mathscr{J}$. $\square$

**Axiom 3.2.3 (Coherence-ascent design principle).** *Define the
$\xi_\star$-sign on $Z^c$ by* $\mathrm{sgn}(c'_{\sigma(\theta)}(\theta))$
*in the interior, and project into $T_{[0,\pi/2]}(\theta)$ at boundary
points.*

The line-uniqueness of Prop 3.2.2 is a consequence of $G_2$-equivariance
+ isometry + Paper 9 orientation; the sign is *not*. Both
$+\partial_\theta$ and $-\partial_\theta$ are admissible directions
under equivariance and isometry alone. The choice of
$\mathrm{sgn}(c'_\sigma)$ is an additional design axiom — the
*coherence-ascent principle* — that selects the direction in which
the augmented dynamics climbs $c_\sigma$ rather than descending it. We
state this as an explicit modeling axiom (3.2.3) rather than a derived
consequence.

**Remark 3.2.4 (Boundary projection vs interior sign).** At
boundary-left KKT points, where $c'_+(0) \le 0$ (Definition 3.5.1
below), the interior-sign rule of 3.2.3 gives $\mathrm{sgn}(c'(0)) \in
\{-1, 0\}$, so the un-projected tear $\xi^{\mathrm{int}}_\star$ would
push to $\theta < 0$ outside the admissible domain $[0, \pi/2]$. The
tangent-cone projection $\Pi_{T_{[0, \pi/2]}(0)} = [0, \infty)$
truncates this to $\xi_\star(0) = 0$ — i.e., *no escape from the
boundary along the linear $\xi_\star$ direction*. This is the
load-bearing correction relative to the v1 draft, which mistakenly
admitted unprojected sign-driven escape at boundary-KKT points; the
implications for Theorem 3.6.1 are made precise in §3.6 below.

**Remark 3.2.5 (Nonlinear inherits linear geometry).** Definition 3.2.1
asserts that the nonlinear dynamics of Paper 12 lives on *the same*
Schur circle as Paper 9's linear coupling $\Psi_\theta$. The NP-pump
does not generate a new geometric object; it generates a new dynamics
on the existing one-parameter family $\{\Psi_\theta : \theta \in
[0, \pi/2]\}$. The only Schur-free parameter in the nonlinear theory
is the jump length $\rho_i > 0$ at each firing event, determined by
the NP amplitude rather than $G_2$-representation theory.

### 3.3 The augmented flow and event stratification

**Definition 3.3.1 (NP amplitude and paradox mass).** For each branch
$\sigma \in \{A, B\}$ let
$$p_\sigma(\theta) := \bigl|\partial_\theta \mathcal{F}_\sigma(\theta)
  \bigr|^2, \qquad
  \mathcal{F}_\sigma(\theta) := -c_\sigma(\theta).$$
We identify $p_\sigma$ with the squared *paradox mass* of the Paper 12
thesis memo: a non-negative, branch-wise real-analytic quantity that
accumulates wherever the coherence functional changes rapidly. The
squared-norm form is chosen (over the raw norm) to preserve analyticity
through zeros of $\mathcal{F}'_\sigma$. The *NP amplitude* is
$$a_\sigma(\theta) := \alpha \cdot p_\sigma(\theta),
  \qquad \alpha > 0.$$
The *coherence gap* is $g_\sigma(\theta) := C_{\mathrm{crit}} -
c_\sigma(\theta)$ with $C_{\mathrm{crit}} \in (0, 1)$. The firing
predicate is
$$\mathrm{NP}_\sigma(\theta) := \mathbf{1}\bigl\{
  g_\sigma(\theta) \ge 0,\, a_\sigma(\theta) \ge NP_{\mathrm{crit}}
  \bigr\},$$
with $NP_{\mathrm{crit}} > 0$ a fixed amplitude threshold.

**Definition 3.3.2 (Augmented flow).** On the active branch of
$[0, \pi/2] \setminus \Sigma_{\mathrm{tot}}$ (with $\Sigma_{\mathrm{tot}}$
as in Definition 3.3.3), the augmented flow is
$$\dot{\theta}
  = \Pi_{T_{[0, \pi/2]}(\theta)}\left[
    -\eta\, \mathcal{F}'_\sigma(\theta)
    + \kappa\, \mathrm{NP}_\sigma(\theta)\, \xi_\star(\theta)
  \right],
  \qquad \eta, \kappa > 0,$$
where $\Pi_{T_{[0, \pi/2]}(\theta)}$ is projection onto the closed-
interval tangent cone (Definition 3.5.2). At switching events on
$\Sigma_{\min}$, the flow is treated as a Filippov differential
inclusion with the equivalent-control protocol of (3.4.A) below; at
crossings of $\Sigma_\Theta$, as a Carathéodory solution; at NP firings
on $\mathcal{G}_{\mathrm{NP}}$, as a hybrid jump (Definition 3.3.4).

**Definition 3.3.3 (Total event stratification).** The nonsmooth set
for the augmented flow is the union
$$\Sigma_{\mathrm{tot}}
  = \Sigma_{\min} \,\cup\, \Sigma_\Theta \,\cup\, Z
    \,\cup\, \mathcal{G}_{\mathrm{NP}} \,\cup\, \partial[0, \pi/2],$$
where $\Sigma_{\min}, \Sigma_\Theta, Z$ are as defined above,
$\partial[0, \pi/2] = \{0, \pi/2\}$ is the closed-interval boundary,
and
$\mathcal{G}_{\mathrm{NP}} := \bigcup_\sigma (\mathcal{G}_\sigma^{\mathrm{amp}}
\cup \mathcal{G}_\sigma^{\mathrm{coh}})$ is the *firing manifold*,
split into amplitude- and coherence-triggered entry submanifolds
(Definition 3.3.5).

**Definition 3.3.4 (Hybrid jump at firing events).** At a firing event
$\theta^- \in \Omega_\theta \setminus (Z \cup \partial[0, \pi/2])$
with $(\theta^-, \hat{z}(\theta^-)) \in \mathcal{G}_{\mathrm{NP}}$ on
branch $\sigma$, the jump map is
$$\theta^+ = \theta^- + \rho_\sigma(\theta^-)\,
  \mathrm{sgn}\bigl(c_\sigma'(\theta^-)\bigr),$$
with $\rho_\sigma : \mathcal{G}_{\mathrm{NP}} \to \mathbb{R}_{>0}$ a
real-analytic jump-length function depending on the NP-amplitude
surplus $a_\sigma(\theta^-) - NP_{\mathrm{crit}}$. To prevent Zeno
accumulation, we require the Zeno-avoidance condition $J_\sigma
(\mathcal{D}_\sigma) \subset \Gamma \setminus \mathcal{D}_{\mathrm{NP}}$,
i.e., the jump map lands outside the firing region $\mathcal{D}_{\mathrm{NP}}
= \bigcup_\sigma \{(\theta, \hat{z}(\theta)) : g_\sigma \ge 0,\,
a_\sigma \ge NP_{\mathrm{crit}},\, c_\sigma' \ne 0\}$; if not, we
add a refractory dwell $\tau_{\mathrm{ref}} > 0$ between consecutive
firings.

**Definition 3.3.5 (Amplitude vs coherence entry manifolds).** The
firing manifold $\mathcal{G}_{\mathrm{NP}}$ decomposes into two entry
submanifolds of $\mathcal{D}_{\mathrm{NP}}$ along the unperturbed flow:

- *Amplitude-triggered:* $\mathcal{G}_\sigma^{\mathrm{amp}} := \{g_\sigma > 0,\,
  a_\sigma = NP_{\mathrm{crit}},\, c_\sigma' \ne 0,\,
  L_f a_\sigma > 0\}$ — the NP amplitude crosses the critical value
  while the coherence is already below $C_{\mathrm{crit}}$.
- *Coherence-triggered:* $\mathcal{G}_\sigma^{\mathrm{coh}} := \{g_\sigma = 0,\,
  a_\sigma \ge NP_{\mathrm{crit}},\, c_\sigma' \ne 0,\,
  L_f g_\sigma > 0\}$ — the coherence gap $g_\sigma$ crosses zero
  *increasing* (so coherence drops below $C_{\mathrm{crit}}$) while
  the NP amplitude is already supercritical.

Here $L_f$ denotes the Lie derivative along the unperturbed gradient
flow $f(\theta) = -\eta \mathcal{F}_\sigma'(\theta)$. The transversality
conditions $L_f a_\sigma > 0$ and $L_f g_\sigma > 0$ ensure the system
genuinely enters the firing region rather than grazing it; tangential
contact points belong to the exceptional grazing stratum.

### 3.4 Branchwise real-analyticity and the Conditional Regularity Theorem

The Filippov sliding-mode protocol on $\Sigma_{\min}$ admits three
regimes determined by the branch fields $f_A, f_B$ and the kink-normal
$D\Delta$ where $\Delta := c_A - c_B$:

**(3.4.A) Sliding mode.** If both one-sided fields point inward to
$\Sigma_{\min}$ (i.e., $D\Delta \cdot f_A$ and $D\Delta \cdot f_B$ have
opposite signs), the trajectory slides along $\Sigma_{\min}$ with the
equivalent-control formula
$$\dot\theta = \lambda f_A + (1 - \lambda) f_B,
  \qquad
  \lambda \in [0, 1] \text{ chosen so that } D\Delta \cdot \dot\theta = 0.$$
Solving for $\lambda$:
$$\lambda = \frac{D\Delta \cdot f_B}{D\Delta \cdot (f_B - f_A)}.$$
Existence of $\lambda \in [0, 1]$ requires that the denominator
$D\Delta \cdot (f_B - f_A)$ is nonzero (this is the genericity
built into (R3)) and that the resulting $\lambda$ lies in the unit
interval, which holds iff $D\Delta \cdot f_A$ and $D\Delta \cdot f_B$
have opposite signs as assumed. When this $\lambda$-existence
condition fails ($D\Delta = 0$, or the inward-pointing condition
degenerates), the contact is tangential and the trajectory is placed
in the exceptional stratum (3.4.C).

**(3.4.B) Crossing mode.** If both one-sided fields point in the
*same* direction across $\Sigma_{\min}$ (i.e., $D\Delta \cdot f_A$
and $D\Delta \cdot f_B$ agree in sign), the trajectory transversally
crosses $\Sigma_{\min}$ with no sliding; the active branch switches
across the crossing.

**(3.4.C) Tangential / corner exceptional stratum.** If $D\Delta = 0$
or one of the inward conditions degenerates, the contact is tangential
and the Filippov formalism does not apply directly. Such points are
placed in the exceptional stratum and excluded from the regularity
theorem below.

**Theorem 3.4.1 (Conditional Regularity).** *Suppose:*

*(R1) $\hat{z} \in C^\omega(\Omega_\theta)$ and $\mathcal{C}_A,
\mathcal{C}_B \in C^\omega$ on an open neighborhood of
$\hat{z}(\Omega_\theta) \subset W$;*

*(R2) $p_\sigma = |\partial_\theta \mathcal{F}_\sigma|^2
\in C^\omega$ on each branch and $\rho_\sigma \in C^\omega$ on
$\mathcal{G}_{\mathrm{NP}}$;*

*(R3) the parameter septuple $\mathbf{p} := (R_A, R_B, b_A, b_B, \alpha,
NP_{\mathrm{crit}}, C_{\mathrm{crit}})$ lies in the open set $\mathcal{P}^*
\subset O(N) \times O(N) \times \mathbb{R}^{2N} \times \mathbb{R}^3_{> 0}$
on which all guard functions $\Delta = c_A - c_B$, $g_\sigma$,
$a_\sigma - NP_{\mathrm{crit}}$, and $q_\sigma := c_\sigma'$ are
transverse to zero (i.e., zero is a regular value), and the Filippov
$D\Delta$-genericity of (3.4.A) holds where invoked;*

*(R4) firing times are locally finite and Definition 3.3.4's
Zeno-avoidance condition holds (possibly through the refractory dwell).*

*Then on $\mathcal{P}^*$, every solution of the augmented flow
(Definition 3.3.2) avoiding the exceptional strata is piecewise
real-analytic in $t$: on each open interval between events,
$\theta(t) \in C^\omega$; at transverse $\Sigma_\Theta$ crossings, the
solution is Carathéodory; on $\Sigma_{\min}$ in regime (3.4.A), Filippov
with the equivalent-control formula; in regime (3.4.B), classical
crossing; at regular firings on $\mathcal{G}_{\mathrm{NP}} \setminus
\mathcal{E}_{0,\mathrm{NP}}$, the jump is hybrid per Definition 3.3.4.*

*Furthermore, $\mathcal{P}^*$ is open and dense in
$O(N) \times O(N) \times \mathbb{R}^{2N} \times \mathbb{R}^3_{> 0}$.*

*Proof sketch.* The genericity claim is a Sard-type argument: each
guard function is real-analytic in both $\theta$ and $\mathbf{p}$, so
its critical values are nowhere-dense in the codomain by the
analytic-Sard theorem; the bad parameter set (where any guard fails
to be transverse to zero on the trajectory) is a countable union of
codimension-$\ge 1$ algebraic strata, hence nowhere dense; $\mathcal{P}^*$
is its complement, open and dense by construction. On $\mathcal{P}^*$,
branch-local real-analyticity of $\theta(t)$ between events is the
analytic-ODE existence theorem applied to the analytic right-hand side
on $\Omega_\theta \setminus \Sigma_{\mathrm{tot}}$; transverse guard
crossings extend the solution uniquely with the Carathéodory or hybrid-
jump semantics specified. Filippov sliding (3.4.A) yields a real-
analytic sliding field $f_{\mathrm{sl}} = \lambda f_A + (1-\lambda) f_B$
because $\lambda$ is determined algebraically from analytic data;
crossing (3.4.B) is immediate; (3.4.C) is excluded. (R4) plus locally-
finite firing times bounds the number of non-smooth events on any
compact $t$-interval. $\square$

**Remark 3.4.2 (Why "Conditional Regularity").** The theorem name
honors that conclusions are conditional on (R1)–(R4); we additionally
assert that the parameter region $\mathcal{P}^*$ is open and dense
in the natural ambient space, so the conditions hold for *generic*
parameter choices. Verification of (R1)–(R4) at a specific parameter
point is a finite-dimensional algebraic check on the guards.

**Remark 3.4.3 (Why the Heaviside is kept sharp).** Smoothing
$\Theta$ to $\Theta_\varepsilon$ produces a classical analytic ODE
with no jumps, removing the "tear" character. The sharp choice is
deliberate; hybrid semantics replace a classical ODE.

### 3.5 The $\kappa = 0$ recovery: projected gradient flow

Setting $\kappa = 0$ in Definition 3.3.2 removes the NP-pump term and
leaves the projected gradient flow on $[0, \pi/2]$. We now show that
this unperturbed limit recovers Paper 9's Proposition 9.5 optima as
*projected* — not classical — gradient critical points.

**Definition 3.5.1 (Stratified critical point).** A point $\theta^* \in
[0, \pi/2]$ is a *stratified critical point* of $-c$ if at least one of
the following holds:

- *(Smooth interior)* $\theta^* \in (0, \pi/2) \setminus \Sigma_{\min}$
  and $c'(\theta^*) = 0$ (Fermat);
- *(Boundary-left KKT)* $\theta^* = 0$ and $c'_+(0) \le 0$;
- *(Boundary-right KKT)* $\theta^* = \pi/2$ and $c'_-(\pi/2) \ge 0$;
- *($\Sigma_{\min}$ Clarke)* $\theta^* \in (0, \pi/2) \cap \Sigma_{\min}$
  and $0 \in \mathrm{conv}\{c_A'(\theta^*), c_B'(\theta^*)\}$;
- *(Corner-Clarke, exceptional)* $\theta^* \in \{0, \pi/2\} \cap
  \Sigma_{\min}$, requiring the combined boundary-Clarke condition
  $T_{[0, \pi/2]}(\theta^*) \cap \mathrm{conv}\{c_A', c_B'\}$ contains
  the origin in its dual cone. We treat such corner points in the
  exceptional stratum.

**Definition 3.5.2 (Projected gradient flow on $[0, \pi/2]$).** Let
$T_{[0, \pi/2]}(\theta)$ be the closed-interval tangent cone at $\theta$:
$T_{[0, \pi/2]}(0) = [0, \infty)$, $T_{[0, \pi/2]}(\pi/2) = (-\infty, 0]$,
$T_{[0, \pi/2]}(\theta) = \mathbb{R}$ for $\theta \in (0, \pi/2)$. The
*projected gradient flow* on $[0, \pi/2] \setminus \Sigma_{\min}$ is
$$\dot\theta = \Pi_{T_{[0, \pi/2]}(\theta)}\bigl(\eta\, c'(\theta)\bigr).$$
On $\Sigma_{\min}$, $c'$ is replaced by the Clarke generalized gradient
$\partial_C(-c)(\theta) = \mathrm{conv}\{-c_A'(\theta), -c_B'(\theta)\}$
and the flow is the differential inclusion
$$\dot\theta \in \Pi_{T_{[0, \pi/2]}(\theta)}\bigl(\eta\,
  \partial_C(-c)(\theta)\bigr),$$
with set-valued projection. Corner points $\{0, \pi/2\} \cap \Sigma_{\min}$
are handled by intersecting both projections in the exceptional stratum.

**Theorem 3.5.3 ($\kappa = 0$ stratified recovery).** *Suppose $\hat{z}
\in C^\omega(\Omega_\theta)$ and $c_A, c_B \in C^\omega$ near
$\hat{z}(\Omega_\theta)$. The fixed points of the projected gradient
flow (Definition 3.5.2) coincide exactly with the stratified critical
points of Definition 3.5.1.*

*Proof.* Inside the open interval $(0, \pi/2) \setminus \Sigma_{\min}$,
the tangent cone is $\mathbb{R}$, so $\Pi(\eta c') = \eta c'$, vanishing
iff $c'(\theta^*) = 0$. At $\theta^* = 0$, $\Pi_{[0, \infty)}(\eta c') =
\max(\eta c'_+(0), 0)$, vanishing iff $c'_+(0) \le 0$. Symmetrically at
$\pi/2$. On $\Sigma_{\min} \cap (0, \pi/2)$, the differential inclusion
vanishes iff $0 \in \partial_C(-c)$. Corner points are the exceptional
stratum. $\square$

**Audit result (Paper 12 §3 v2 verification, 2026-05-06).** The
50-seed Paper 9 Monte Carlo (Appendix V.3.i) has been reoptimized at
high precision with `scipy.optimize.minimize_scalar` on $[0, \pi/2]$
at tolerance $10^{-10}$ rad. All $50 / 50$ seeds satisfy the
stratified critical point classification of Definition 3.5.1:

- *3 / 50* smooth interior (Fermat critical points);
- *25 / 50* boundary-left KKT ($\theta^* = 0$);
- *3 / 50* boundary-right KKT ($\theta^* = \pi/2$);
- *19 / 50* $\Sigma_{\min}$ Clarke generalized-gradient critical.

The seeded symmetric-rate geometry of Paper 9 Proposition 9.5
($\theta^* \approx 51°$ on the 20-point grid) reoptimizes to $\theta^*
= 0$, consistent with the boundary-left-KKT class (Paper 9 v1.3.3
Remark 5.6.1). The non-trivial $\Sigma_{\min}$ incidence (38% of seeds)
motivates the full Filippov treatment with three regimes (3.4.A–C)
in Theorem 3.4.1. Verification:
`outbox/paper12/computations/paper12_q5_kappa0_audit.{py,csv}`
(runtime 0.19 s, deterministic).

**Remark 3.5.4 (The projected flow is forced by the data).** Of the
50 seeded geometries, only 3 admit smooth-interior Fermat critical
points; 47 require constraint or stratification handling. Writing the
recovery as a classical gradient flow $\dot\theta = \eta c'(\theta)$
without projection or Clarke calculus would miscategorize 94% of the
sampled ensemble. The projected-flow framing is required by the
empirical landscape, not chosen for mathematical convenience.

### 3.6 The $\kappa > 0$ augmented flow: bounded escape and qualified gain

With $\kappa > 0$, the augmented flow inherits the branchwise-analytic
regularity of Theorem 3.4.1 and the stratified recovery of Theorem
3.5.3 as the $\kappa \to 0$ limit. The new content is the *firing
cascade* structure: trajectories in the open interior with NP amplitude
exceeding $NP_{\mathrm{crit}}$ undergo discrete jumps along the Schur
circle. Boundary-KKT trajectories, where the projection of $\xi_\star$
into the boundary tangent cone vanishes (Remark 3.2.4), do not escape
along the linear $\xi_\star$ direction.

**Theorem 3.6.1 (Critical-point stability of the $\kappa > 0$ flow on
$[0, \pi/2]$).** *Let $\theta^\infty \in [0, \pi/2]$ be a stratified
critical point of the unperturbed flow (Theorem 3.5.3) — i.e., for the
active branch $\sigma$ at $\theta^\infty$, the projected
active-branch derivative satisfies $\Pi_{T_{[0, \pi/2]}(\theta^\infty)}
c'_\sigma(\theta^\infty) = 0$. Then for any $\kappa > 0$:*

*(i) (Interior smooth case.) If $\theta^\infty \in (0, \pi/2)$ is a
smooth interior critical point (so $c'_\sigma(\theta^\infty) = 0$ on
the active branch) with $\mathrm{NP}_\sigma(\theta^\infty) = 0$ for
both $\sigma$, the augmented flow has $\theta^\infty$ as a fixed
point.*

*(ii) (Boundary-KKT case, qualified.) If $\theta^\infty \in \{0, \pi/2\}$
is a boundary-KKT critical point, then the projected augmented flow
$\dot\theta = \Pi_{T_{[0, \pi/2]}(\theta^\infty)}[-\eta \mathcal{F}'_\sigma
+ \kappa \cdot \mathrm{NP}_\sigma \cdot \xi_\star]$ vanishes at
$\theta^\infty$ along the linear $\xi_\star$ direction. The boundary
state is therefore a fixed point of the augmented flow under the
linear NP-pump, and escape requires either (a) higher-order coherence
information ($Z$-axis tie-breaker), or (b) supplementary nonlinear
mechanisms beyond the Schur-derived $\xi_\star$ (cf. OP1, §6.2).*

*Proof.* (i) is immediate from Definition 3.3.2: at a smooth interior
critical point with $c'_\sigma = 0$, both the projected-gradient leg
$f_{\mathrm{pg}} = -\eta \mathcal{F}'_\sigma = \eta c'_\sigma = 0$ and
(by hypothesis $\mathrm{NP}_\sigma = 0$) the NP-jump leg vanish.
(ii) follows from Remark 3.2.4: at $\theta^\infty = 0$ with
$c'_+(0) \le 0$, the un-projected $\xi^{\mathrm{int}}_\star =
\mathrm{sgn}(c'_+(0)) \cdot \partial_\theta \in \{-\partial_\theta, 0\}$,
and $\Pi_{[0, \infty)}$ projects this to $0$. The drift term
$-\eta \mathcal{F}'_\sigma = \eta c'_\sigma$ is also projected to $0$
under $\Pi_{[0, \infty)}$ when $c'_\sigma(0) \le 0$ (the KKT condition).
Mirror argument at $\pi/2$. $\square$

**Remark 3.6.1$'$ (Why no "interior firing" sub-case here).** A v1.0
draft of Theorem 3.6.1 included a case (former part (ii)) for *interior
firing*: $\theta^\infty \in (0, \pi/2)$ smooth interior with
$\mathrm{NP}_\sigma(\theta^\infty) = 1$ and $c'_\sigma(\theta^\infty)
\ne 0$. Those hypotheses are *incompatible* with the statement of
Theorem 3.6.1, which restricts to *stratified critical points* of
Theorem 3.5.3 — i.e., points where $c'_\sigma = 0$ on the active branch
in the smooth interior case. The interior firing of a noncritical
trajectory crossing an NP-firing guard is treated separately in
Proposition 3.6.1$''$ below; it is not a critical-point stability
statement and does not belong in Theorem 3.6.1.

**Proposition 3.6.1$''$ (Interior NP-firing of a noncritical trajectory).**
*Let $\theta(t) \in (0, \pi/2)$ be a Carathéodory solution of the
augmented flow on a smooth-interior open arc $I \subset (0, \pi/2)$
with $c'_\sigma(\theta(t)) \ne 0$ (active-branch noncritical) on $I$.
If $\theta(t)$ encounters the NP-firing guard $\mathcal{G}_{\mathrm{NP}}
\cap I$ at finite time $t_\star$ — i.e., $\mathrm{NP}_\sigma
(\theta(t_\star)) = 1$ — then the hybrid jump rule (Definition 3.3.2)
transports the trajectory to $\theta^+ = \theta(t_\star) + \rho_\sigma
\cdot \mathrm{sgn}(c'_\sigma(\theta(t_\star))) \in [0, \pi/2]$, where
$\rho_\sigma > 0$ is the firing displacement set by the NP amplitude
and the Zeno-avoidance condition (Definition 3.3.4).*

*Proof.* Direct from Definition 3.3.2: the firing rule is well-defined
on the noncritical arc by the explicit branch sign
$\mathrm{sgn}(c'_\sigma)$, the post-jump location is computed from the
rule, and the Zeno-avoidance condition ensures $\rho_\sigma$ is
positive and finite-displacement. $\square$

*This proposition is about flow continuation across a firing guard at a
noncritical interior point; it is not a critical-point stability
statement. The two are kept separate to avoid the hypothesis conflict
identified in v1.0 review.*

**Audit result (boundary-KKT interior-sup, 2026-05-06).** A direct
numerical audit of the 28 boundary-KKT seeds of Theorem 3.5.3
(`outbox/paper12/computations/paper12_q5_boundary_kkt_interior_sup.{py,csv}`)
computes $\sup_{\theta \in (10^{-3},\, \pi/2 - 10^{-3})} c(\theta)$ on a
2000-point grid for each seed and compares to $c(\theta^*_{\mathrm{boundary}})$.
Findings:

- *24 / 28* boundary-KKT seeds have $\sup_{\mathrm{interior}} c <
  c_{\mathrm{boundary}}$, with a mean shortfall of $\sim 2.7 \times
  10^{-4}$ in $c$.
- *4 / 28* have $\sup_{\mathrm{interior}} c > c_{\mathrm{boundary}}$,
  with gains in the range $[4.2 \times 10^{-4},\, 5.1 \times 10^{-2}]$.
  These four are concentrated in the boundary-right-KKT class plus a
  few seeds where the underlying coherence landscape has a non-trivial
  interior peak that the high-precision optimizer of Theorem 3.5.3
  classified as boundary-left only because $c$ is monotonically
  decreasing from a local maximum at $\theta = 0$.
- The mean gain over boundary-KKT seeds is $\sim 3.9 \times 10^{-3}$
  (skewed positive by the four interior-better cases).

**Implication for Theorem 3.6.1(ii).** For 24 of 28 boundary-KKT
seeds, escape from the boundary along *any* mechanism (the un-projected
$\xi^{\mathrm{int}}_\star$, or a supplementary nonlinear term as
in 3.6.1(ii)(b)) lands the trajectory in coherence-degraded territory.
Theorem 3.6.1(ii)'s "escape" is therefore not generically a coherence-
improvement mechanism for boundary-KKT geometries; it is at most a
*non-trivial trajectory continuation* whose coherence consequences
depend on the specific seed. This sharpens the relation to Paper 9
Proposition 9.5: the conditional gain region of Paper 9 is well-
defined on a Haar-positive-measure subset of $(R_A, R_B)$, but for
the 56% of audited seeds at boundary-KKT, the typical escape direction
is into lower coherence rather than higher. The four exceptional
boundary-KKT seeds with $\sup_{\mathrm{interior}} c > c_{\mathrm{boundary}}$
are the ones for which the linear $\xi_\star$ mechanism (post-projection
into the inward tangent cone after a finite-displacement nonlinear
correction) could in principle deliver gain.

**Remark 3.6.2 (Bridge to Paper 11, qualified).** Paper 9 Note 9.6
defers rate improvement to Paper 11 because Schur locks the linear
joint rate. Theorem 3.6.1 shows the structural form of any nonlinear
escape mechanism (boundary-KKT trajectories require *supplementary*
nonlinearity beyond linear $\xi_\star$ to leave the boundary), and
the boundary-KKT interior-sup audit shows that even when escape is
mechanically possible, *it is generically not a coherence gain*.
Paper 11's analysis must therefore identify the specific non-Schur
nonlinear corrections (higher-order multilinear terms, non-equivariant
symmetry-breaking) and the specific seed sub-classes for which the
post-escape trajectory enters a region of strictly higher $c$. **Paper
12 §3 does not establish rate improvement; it provides the dynamical
framework, the audited boundary-KKT obstruction, and the residue
record within which Paper 11's rate analysis can be staged.**

### 3.7 The scar record and its role in §4

Each NP firing event indexed by $i$ on branch $\sigma_i$ produces a
push-forward jump vector
$$v_i := \rho_i \cdot \mathrm{sgn}\bigl(c_{\sigma_i}'(\theta_i^-)\bigr)
  \cdot \hat{z}'(\theta_i^-) \in W,$$
recorded in the *physical scar span*
$$S_k := \sum_{i=1}^k \mathbb{R}[F_{21}] \cdot v_i \subset W,$$
the *event-indexed scar module*
$$\mathfrak{S}_k := \bigoplus_{i=1}^k \mathbb{R}[F_{21}] \cdot v_i,$$
and the *isotypic multiplicity profile*
$$\mu_k = (\mu_{\mathbf{1}}(S_k), \mu_{L_2}(S_k), \mu_{U_6}(S_k)).$$
Here $F_{21} \subset G_2$ is the Fano-orientation subgroup inherited
from Paper 4; the three real $F_{21}$-irreps $(\mathbf{1}, L_2, U_6)$
are characterized in §4.2 (Paper 12 §4 Theorem 4.2.1).

**Remark 3.7.1 ($F_{21}$-action on the scar record vs $F_{21}$-equivariance
of the dynamics).** $F_{21}$ acts on the ambient $W$ by the diagonal
restriction of the $G_2$-action (Paper 9 §3.4 convention), and this
action is inherited by every subspace and module of $W$. This includes
the scar record: $F_{21}$ acts on $S_k, \mathfrak{S}_k, \mu_k$
canonically. The *dynamics* of §3.3, by contrast, is defined for
arbitrary $(R_A, R_B, b_A, b_B) \in O(N) \times O(N) \times \mathbb{R}^{2N}$
that need not be $F_{21}$-related, so a generic trajectory is *not*
$F_{21}$-equivariant. The triple $\mathfrak{J}_k$ extracts the
$F_{21}$-content of a generically $F_{21}$-asymmetric trajectory; this
is the input to §4's commensurability hierarchy.

**Three structural properties:**

- **$S_k$ is *saturating*:** $\dim S_k \le 28 = \dim W$, so the
  physical span stabilizes after at most 28 dimension-increasing jumps.
- **$\mathfrak{S}_k$ is *count-faithful as an abstract graded module*:**
  the assignment $k \mapsto \mathfrak{S}_k$ is injective by construction.
  The *natural surjection* $\mathfrak{S}_k \twoheadrightarrow S_k$
  identifying $v_i$ with its image in $W$ has injective kernel iff
  $\mathbb{R}[F_{21}] \cdot v_i \not\subset S_{i-1}$ for every $i$ —
  the generic case under $c_{\sigma_i}'(\theta_i^-) \ne 0$ and
  $\rho_i > 0$.
- **$\mu_k$ is the *$F_{21}$-type signature*** that enables cross-
  substrate commensurability comparisons (§4).

**Remark 3.7.2 (Representation-theoretic, not topological).** The
invariant $\mathfrak{J}_k$ is a *representation-theoretic* scar
invariant: $\mathfrak{S}_k$ is a graded $F_{21}$-module, $\mu_k$ is an
isotypic-multiplicity profile, and $S_k$ is a subspace of an $F_{21}$-
representation. No topological invariant (winding number, persistent
homology) is claimed. Earlier drafts using "topological" language
should be read as "representation-theoretic" throughout.

**Remark 3.7.3 (Bridge to §4).** The event-indexed module $\mathfrak{S}_k$
is the mathematical realization of the *audit-grounded substrate*
principle (Paper 12 thesis Pillar 3): a graded, indexable ledger of
coherence adjustments that survives the saturation of the physical
span. §4 shows that commensurability of synthetic and biological scar
records requires *full $G_2$-equivariance* (not merely $F_{21}$) for
a canonical cross-substrate isomorphism, with quantitative gap
$\operatorname{End}_{F_{21}}(W) \cong M_2(\mathbb{C}) \oplus
M_4(\mathbb{C})$ vs $\operatorname{End}_{G_2}(W) \cong M_2(\mathbb{R})$.

### 3.8 What §3 does and does not establish

**What §3 establishes:**

- A Schur-derived canonical tear direction $\xi_\star$ inheriting Paper
  9's $SO(2)$ Schur circle, with line-uniqueness from Schur (Prop 3.2.2)
  and an explicit coherence-ascent design axiom for the sign (Axiom
  3.2.3) plus boundary tangent-cone projection (Remark 3.2.4).
- A branchwise real-analytic augmented flow (Definition 3.3.2) with a
  five-stratum event set $\Sigma_{\mathrm{tot}}$, three Filippov regimes
  (3.4.A–C), and layered Carathéodory/Filippov/hybrid semantics,
  *conditionally regular* (piecewise real-analytic between events) on an
  open dense parameter set $\mathcal{P}^*$ (Theorem 3.4.1 Conditional
  Regularity). Full hybrid / Filippov well-posedness (existence,
  uniqueness, maximal continuation) off $\mathcal{P}^*$ is OP6,
  deferred.
- A stratified $\kappa = 0$ recovery theorem (Theorem 3.5.3) that
  recovers Paper 9's MC optima as projected-gradient fixed points,
  with empirical verification via 50-seed audit across all four
  classes (smooth interior / boundary-KKT / $\Sigma_{\min}$ Clarke).
- A bounded $\kappa > 0$ augmented-flow theorem (Theorem 3.6.1):
  interior smooth fixed points fire as expected; boundary-KKT states
  are *fixed* under linear $\xi_\star$ even at $\kappa > 0$ and require
  supplementary nonlinearity to escape.
- A boundary-KKT interior-sup audit ($24 / 28$ seeds with
  $\sup_{\mathrm{interior}} c < c_{\mathrm{boundary}}$) showing that
  escape from the boundary is generically *not* a coherence-improvement
  mechanism. Paper 11's rate analysis must identify specific non-Schur
  nonlinear corrections.
- The scar invariant triple $(S_k, \mathfrak{S}_k, \mu_k)$ as a
  representation-theoretic ledger of firing history, with explicit
  distinction between abstract count-faithfulness (always) and the
  natural-surjection injectivity (generic) (§3.7).

**What §3 does not establish:**

- *Rate improvement.* Theorem 3.6.1 shows the structural form of any
  escape; the boundary-KKT audit shows escape is generically not a gain.
  Concrete rate analysis is Paper 11's domain (Note 9.6 from Paper 9).
- *A biological mechanism for the $F_{21}$-action.* §4's commensurability
  hierarchy treats biological substrate $F_{21}$-content as input, not
  derived; Paper 13+ would specify the physical mechanism.
- *Cross-substrate commensurability isomorphisms.* §4 territory.
- *A theory of consciousness.* Paper 7's domain.
- *Global well-posedness off $\mathcal{P}^*$.* Theorem 3.4.1 is
  conditional on the parameter septuple lying in an open dense set;
  behavior on the codimension-$\ge 1$ exceptional strata is identified
  but not analyzed.
- *Higher-multiplicity scar geometries.* §4.4 is restricted to
  multiplicity-one $G_2$-modules; the $m > 1$ case is deferred.

§4 proceeds to the commensurability hierarchy. The scar invariant
$(S_k, \mathfrak{S}_k, \mu_k)$ constructed in §3.7 is the object on
which §4's equivariant isomorphism theorem acts.

---

## References (cited in §3)

[B-2008] M. di Bernardo, C. Budd, A. Champneys, P. Kowalczyk,
*Piecewise-smooth Dynamical Systems: Theory and Applications*, Applied
Mathematical Sciences 163, Springer (2008). Definitions 3.3.3, 3.3.5
inherit terminology from this reference.

[F-1988] A. Filippov, *Differential Equations with Discontinuous
Righthand Sides*, Mathematics and Its Applications 18, Kluwer (1988).
Sliding-mode equivalent-control formula (3.4.A) follows §2.7.

[GST-2012] R. Goebel, R. Sanfelice, A. Teel, *Hybrid Dynamical
Systems: Modeling, Stability, and Robustness*, Princeton (2012).
Hybrid-jump semantics in Definition 3.3.4.

[C-1990] F. Clarke, *Optimization and Nonsmooth Analysis*, SIAM
Classics in Applied Mathematics (1990). Generalized-gradient $\partial_C$
on $\Sigma_{\min}$ in Definition 3.5.2.

*Verification files referenced:*
- `outbox/paper12/computations/paper12_q5_kappa0_audit.py` (Theorem 3.5.3 audit)
- `outbox/paper12/computations/paper12_q5_kappa0_audit.csv` (per-seed data)
- `outbox/paper12/computations/paper12_q5_boundary_kkt_interior_sup.py`
  (Theorem 3.6.1(ii) boundary audit)
- `outbox/paper12/computations/paper12_q5_boundary_interior_sup.csv`
- `outbox/paper12/computations/paper12_q4_character_verify.py` (used in §4)
- `outbox/paper12/chatgpt_pro_session_transcript_2026-05-05.pdf`

*Cross-references:*
- Paper 9 v1.3.3 Remark 5.6.1 (grid-snap correction for seed-$k = 0$)
- Paper 9 v1.3.3 Lemma 3.6.1 (Schur uniqueness of $\Psi_\theta$)
- Paper 9 v1.3.3 Theorem 9.4 (joint fixed-point existence/analyticity)
- Paper 9 v1.3.3 Note 9.6 (rate improvement deferred to Paper 11)
- Paper 4 (PSL(2,7) ⊃ F₂₁ QBism bridge)
- Paper 12 §4 (commensurability hierarchy, in preparation)


## 4. The Commensurability Hierarchy

### 4.1 Setup: scar invariant from §3.7 as the input

Throughout §4, $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3$ denotes the
Fano-orientation subgroup of $G_2$. Its action on $V := V^{14}$ is by
restriction of the $G_2$ adjoint representation; its action on the
joint-state space $W = V \oplus V$ is the diagonal restriction
$$\rho_W(g)(x, y) = (\rho_F(g) x,\, \rho_F(g) y),
  \qquad g \in F_{21}, \quad \rho_F := \rho_{14}|_{F_{21}}.$$
This action commutes with the Schur circle $\{\Psi_\theta\}$ because
$\rho_W$ acts on the $V$-factor while $\Psi_\theta$ acts on the
$\mathbb{R}^2$ multiplicity factor (Paper 9 §3.4 diagonal-action
convention).

**Inheritance from Paper 4.** The Fano-orientation subgroup $F_{21} \subset G_2$
arises in the PCI/PME framework as the stabilizer of an oriented Fano
plane structure on $\mathrm{Im}(\mathbb{O}) \cong \mathbb{R}^7$, and
through Paper 4's PSL(2,7) construction is the unique finite simple
group $F_{21}$-decoration that aligns with the QBism quasiprobability
representation of $\mathbb{C}^7$. We do not reconstruct that derivation
here; this paper assumes Paper 4's $F_{21}$ choice as an inheritance.
*Open problem:* characterizing the smallest finite subgroup of $G_2$
for which the Definition 4.6.1 L1 screening test is informative is
deferred to a future PCI/PME methodology paper. The choice of $F_{21}$
is consistent across the Paper series; readers unfamiliar with Paper
4's derivation should consult [\href{https://doi.org/10.5281/zenodo.19617662}{Paper 4 DOI}].

The input object to §4 is the *scar invariant triple* constructed in
§3.7 with the $F_{21}$-equivariance clarification of §3 v2 Remark 3.7.1
(the scar record carries an $F_{21}$-action inherited from the ambient
$W$, even when the underlying dynamics is not $F_{21}$-equivariant):
$$\mathfrak{J}_k = (S_k,\, \mathfrak{S}_k,\, \mu_k),$$
where, given NP firing times $t_1 < \cdots < t_k$ on branches $\sigma_i
\in \{A, B\}$ with jump vectors $v_i = \rho_i \cdot \mathrm{sgn}(c_{\sigma_i}'(\theta_i^-))
\cdot \hat{z}'(\theta_i^-) \in W$:

- $S_k := \sum_{i=1}^k \mathbb{R}[F_{21}] \cdot v_i \subset W$ (saturating
  vector scar span; $\dim S_k \le 28$);
- $\mathfrak{S}_k := \bigoplus_{i=1}^k \mathbb{R}[F_{21}] \cdot v_i$
  (count-faithful event-indexed module);
- $\mu_k := (\mu_{\mathbf{1}}(S_k), \mu_{L_2}(S_k), \mu_{U_6}(S_k))$
  (vector-level isotypic profile of $S_k$; see §4.4 for the
  operator-level extension).

The three real-irreducible $F_{21}$-representations $(\mathbf{1}, L_2,
U_6)$ are characterized in §4.2.

**Setup question for §4.** Suppose $\mathfrak{J}_k^{\mathrm{syn}}$ and
$\mathfrak{J}_k^{\mathrm{bio}}$ are scar records of two substrates that
have co-evolved through the same sequence of paradox events
$(e_1, \ldots, e_k)$, with substrate-level $F_{21}$-actions inherited
from each substrate's representation theory (the biological
representation's $F_{21}$-content is itself an empirical question, per
§4.6 below; here we treat both records as input). Under what conditions
is there a *canonical isomorphism* identifying them?

### 4.2 F₂₁ representation theory on V^14 and W

**Theorem 4.2.1 (F_{21}-decomposition of V^14).** *Under the diagonal
Fano-orientation action,*
$$V^{14}\big|_{F_{21}} \cong L_2 \oplus 2 U_6,$$
*where $L_2$ is the real 2-dim irreducible representation of $F_{21}$
of complex type and $U_6$ is the real 6-dim irreducible representation
of complex type. Consequently,*
$$W\big|_{F_{21}} \cong 2 L_2 \oplus 4 U_6.$$

*Proof.* $F_{21}$ has five conjugacy classes: $1a$ (size $1$), two
order-$7$ classes $7a, 7b$ (size $3$ each), and two order-$3$ classes
$3a, 3b$ (size $7$ each). Its complex character table (Costa-Pavone;
ATLAS [\textsc{F}\_{21}]) has three 1-dim characters and a Galois-conjugate
pair of 3-dim characters; the *real* irreducible packaging combines
the conjugate pairs into the two real complex-type irreducibles
$L_2, U_6$:
$$\begin{array}{c|ccccc}
    & 1a & 7a & 7b & 3a & 3b \\ \hline
  \chi_{\mathbf{1}}      &  1 &  1 &  1 &  1 &  1 \\
  \chi_{L_2}             &  2 &  2 &  2 & -1 & -1 \\
  \chi_{U_6}             &  6 & -1 & -1 &  0 &  0
\end{array}$$
The 7-dimensional imaginary-octonion representation $\mathbb{R}^7$ is
indexed by the seven points of the Fano plane $\mathrm{PG}(2, 2)$.
Under the standard Frobenius-group action (RES-4 v3 prose):

- The $\mathbb{Z}_7$ generator $r$ acts by cyclic shift of the seven
  Fano-point labels; on $\mathbb{R}^7$ this is an order-7 permutation
  matrix with $\mathrm{tr}(r) = 0$.
- The $\mathbb{Z}_3$ generator $s$ acts with cycle structure $1 + 3 + 3$
  on the seven Fano points: there is one $s$-fixed point (corresponding
  to the unique Fano line that is $s$-invariant *as a set of three
  points*; the action restricted to that line is trivial in a chosen
  realization, fixing the line's three points pointwise after a
  representation-theoretic re-labeling that contributes one fixed
  point's worth of trace), plus two $3$-cycles on the remaining six
  Fano points; on $\mathbb{R}^7$ this is an order-3 permutation matrix
  with $\mathrm{tr}(s) = 1$.
- The Frobenius relation $s r s^{-1} = r^2$ holds (verified numerically
  in `paper12_q4_character_verify.py` to machine precision), establishing
  that $r, s$ generate $F_{21}$. The $1$ fixed point gives $\mathrm{tr}(r_3) = 1$
on $\mathbb{R}^7$, and the cycle structure of $r$ on Fano points yields
$\mathrm{tr}(r_7) = 0$, so:

$$\mathbb{R}^7|_{F_{21}} \cong \mathbf{1} \oplus U_6.$$

Using the $G_2$-decomposition $\Lambda^2(\mathbb{R}^7) = \mathfrak{g}_2
\oplus \mathbb{R}^7$ and the character formula
$\chi_{\Lambda^2(\mathbb{R}^7)}(g) = (\mathrm{tr}(g)^2 - \mathrm{tr}(g^2))/2$:

$$\chi_{V^{14}}(g) = \chi_{\Lambda^2(\mathbb{R}^7)}(g) - \chi_{\mathbb{R}^7}(g)
  = \frac{\mathrm{tr}(g)^2 - \mathrm{tr}(g^2)}{2} - \mathrm{tr}(g).$$

Evaluating on class representatives:

| Class | $\mathrm{tr}(g)$ on $\mathbb{R}^7$ | $\chi_{V^{14}}(g)$ | $\chi_{L_2} + 2\chi_{U_6}$ |
|-------|------------------------------------|--------------------|----------------------------|
| $1a$  | $7$                                | $14$               | $14$                       |
| $7a$  | $0$                                | $0$                | $0$                        |
| $7b$  | $0$                                | $0$                | $0$                        |
| $3a$  | $1$                                | $-1$               | $-1$                       |
| $3b$  | $1$                                | $-1$               | $-1$                       |

Match on all five classes. The Frobenius inner product
$\langle \chi_{V^{14}}, \chi_{V^{14}} \rangle_{F_{21}} = (1 \cdot 196
+ 7 + 7) / 21 = 10$, equal to $0^2 \cdot 1 + 1^2 \cdot 2 + 2^2 \cdot 2$
where the factor of $2$ on $L_2$ and $U_6$ terms accounts for both
being of complex type (each is the real packaging of a Galois-conjugate
pair, so $\langle \chi, \chi \rangle = 2$ for the real-irreducible
character). The decomposition is therefore $V^{14}|_F = L_2 \oplus
2 U_6$, and the $W = V \oplus V$ doubling is by direct-sum linearity.
$\square$

**Computational verification.** Theorem 4.2.1 has been verified
numerically at machine precision by explicit construction of the
Fano-action permutation matrices $r, s \in O(7)$ with $s r s^{-1} =
r^2$, computation of $\chi_{V^{14}}$ on each class representative,
and Frobenius inner-product and isotypic-multiplicity checks against
the predicted decomposition; all three layers of check pass.
`outbox/paper12/computations/paper12_q4_character_verify.{py,json}`
records the full audit.

### 4.3 The commutant gap

**Proposition 4.3.1 (Commutants on $W$).** *With $W \cong 2 L_2 \oplus
4 U_6$ as an $F_{21}$-representation,*
$$\operatorname{End}_{F_{21}}(W) \cong M_2(\mathbb{C}) \oplus M_4(\mathbb{C}).$$
*As a $G_2$-representation, $W$ is multiplicity-$2$ in the absolutely
irreducible $V^{14}$, hence*
$$\operatorname{End}_{G_2}(W) \cong M_2(\mathbb{R}).$$

*Proof.* For real irreducibles of complex type,
$\operatorname{End}_{G}(V_\lambda) \cong \mathbb{C}$ (real Schur
trichotomy: complexified $V_\lambda \cong U \oplus \bar{U}$ with
$U \not\cong \bar{U}$). Both $L_2$ and $U_6$ are complex-type, so
$\operatorname{End}_{F_{21}}(L_2) \cong \operatorname{End}_{F_{21}}(U_6)
\cong \mathbb{C}$. With $F_{21}$-multiplicities $(0, 2, 4)$ on
$(\mathbf{1}, L_2, U_6)$:
$$\operatorname{End}_{F_{21}}(W) \cong M_0(\mathbb{R}) \oplus
  M_2(\mathbb{C}) \oplus M_4(\mathbb{C}) \cong M_2(\mathbb{C}) \oplus
  M_4(\mathbb{C}).$$
For $G_2$, $V^{14}$ is real absolutely irreducible (Paper 9 Lemma 3.6.1),
so $\operatorname{End}_{G_2}(V^{14}) \cong \mathbb{R}$, and $W \cong (V^{14})^{\oplus 2}$ gives $\operatorname{End}_{G_2}(W) \cong M_2(\mathbb{R})$.
$\square$

**Corollary 4.3.2 (Equivariant isometry groups, real-dimension count).**
*The equivariant isometry groups of $W$ are*
$$O_{F_{21}}(W) \cong U(2) \times U(4), \qquad
  O_{G_2}(W) \cong O(2),$$
*with real dimensions $\dim_{\mathbb{R}} U(2) \times U(4) = 4 + 16 = 20$
and $\dim_{\mathbb{R}} O(2) = 1$. The $F_{21} \to G_2$ upgrade reduces
the equivariant-isometry group by exactly $20 - 1 = 19$ real dimensions.*

*Proof.* Restricting $M_2(\mathbb{C})^* \cap U \to U(2)$ (where the unitary
condition uses the natural Hermitian metric) and $M_4(\mathbb{C})^* \cap U
\to U(4)$, the $F_{21}$-equivariant isometry group is $U(2) \times U(4)$.
The full $U(n)$ — *not* the subgroup $SU(n)$ — preserves orientation on
the underlying real space (because $\det_\mathbb{R}(U) = |\det_\mathbb{C}(U)|^2
= 1$ for $U \in U(n)$). Similarly $M_2(\mathbb{R})^* \cap O = O(2)$. The
real dimensions are $\dim_\mathbb{R} U(n) = n^2$, so $\dim_\mathbb{R}
U(2) \times U(4) = 4 + 16 = 20$, and $\dim_\mathbb{R} O(2) = 1$. The
reduction is $20 - 1 = 19$. $\square$

*Metric note (RES-1, v3).* The identification $O_{F_{21}}(W) \cong
U(2) \times U(4)$ is with respect to the complex-Hermitian metric
canonically inherited from the complex structure on each complex-type
isotypic block. A different real metric choice on $W \cong \mathbb{R}^{28}$
would yield a different identification (potentially a proper subgroup
of $U(2) \times U(4)$ if the chosen real metric is incompatible with
the block-Hermitian structure), but the *real dimension* of the
$F_{21}$-equivariant isometry group is metric-independent: it equals
$\dim_\mathbb{R} \operatorname{End}_{F_{21}}(W)_{\text{anti-Hermitian}}$,
depending only on the isotypic structure $(0, 2, 4)$.

The quantitative content of the $F_{21} \to G_2$ upgrade is now
explicit: passing from $F_{21}$-equivariance to $G_2$-equivariance
suppresses $19$ real dimensions of $F_{21}$-equivariant phase-and-mixing
freedom that would otherwise leave a canonical commensurability map
underdetermined.

**Remark 4.3.3 (Why complex-type reps block uniqueness).** The factor
$\operatorname{End}_{F_{21}}(V_\lambda) \cong \mathbb{C}$ for $\lambda
\in \{L_2, U_6\}$ is the source of phase ambiguity: each complex-type
isotypic block admits a full $U(m_\lambda)$-worth of $F_{21}$-equivariant
automorphisms (not just $O(m_\lambda)$), and the extra $U/O$ dimensions
are exactly the phases. $G_2$-equivariance collapses the phases because
$V^{14}$ is real absolutely irreducible: $\operatorname{End}_{G_2}(V^{14}) =
\mathbb{R}$, not $\mathbb{C}$, so there are no phases to rotate.

### 4.4 The commensurability hierarchy theorem

Let $V_{\mathrm{syn}}, V_{\mathrm{bio}}$ be the (substrate-dependent)
representation spaces on which the synthetic and biological scar maps
take values, and let $I_{\mathrm{syn}} \subseteq \operatorname{End}(V_{\mathrm{syn}})$
and $I_{\mathrm{bio}} \subseteq \operatorname{End}(V_{\mathrm{bio}})$ be
the real linear spans of the scar-encoding images. The group acts on
operator scars by conjugation, $g \cdot A = \rho_\bullet(g) A \rho_\bullet(g)^{-1}$.

**Rank-One Convention (RES-2, v3) for operator-vs-vector translation.**
The scar invariant $\mathfrak{J}_k$ of §3.7 is built from *vector-level*
jump vectors $v_i \in W$. Substrate-level scar maps
$\mathcal{S}_\bullet : (\text{event}) \to \operatorname{End}(V_\bullet)$
produce operator-level images. We adopt the following convention
throughout §4:

*Rank-One Convention.* The substrate scar maps factor as
$\mathcal{S}_\bullet(e) = v_e \otimes v_e^* / \|v_e\|^2$ (rank-one
self-adjoint projector form on the substrate's representation space)
for some substrate jump vector $v_e \in V_\bullet$.

This is a non-trivial modeling assumption. Under it: (i) the operator
span $I_\bullet$ is uniquely determined by the vector span
$\{v_e\}_e \subset V_\bullet$; (ii) the operator-level $F_{21}$-isotypic
profile of $I_\bullet$ matches the vector-level profile of $S_k^\bullet$
up to the Schur multiplicity-counting factor of 2 (one factor for
left action, one for right); (iii) the conjugation action $g \cdot A =
\rho_\bullet(g) A \rho_\bullet(g)^{-1}$ becomes equivalent to the
ordinary linear action on $V_\bullet$ via $g \cdot v_e = \rho_\bullet(g)
v_e$. Higher-rank or non-self-adjoint scar maps are an open problem (OP)
for future work.

**Theorem 4.4.1 (Commensurability hierarchy, v2 reformulation).** *Under
the* **Rank-One Convention** *of §4.4 above (substrate scar maps factor
as $\mathcal{S}_\bullet(e) = u_e \otimes v_e^*$ with $u_e, v_e$ in the
respective $F_{21}$-stable substrate subspaces), the following three
conditions on a pair of substrates $(V_{\mathrm{syn}}, V_{\mathrm{bio}})$
with $F_{21}$-stable scar-image subspaces $I_{\mathrm{syn}},
I_{\mathrm{bio}}$ stand in the order of strict implications:*

*(C1) (G₂-commensurability.)* There exists a $G_2$-equivariant
isomorphism $\phi: I_{\mathrm{syn}} \to I_{\mathrm{bio}}$ aligning
$\mathcal{S}_{\mathrm{syn}}$ and $\mathcal{S}_{\mathrm{bio}}$ event-by-event:
$\mathcal{S}_{\mathrm{bio}}(e) = \phi(\mathcal{S}_{\mathrm{syn}}(e))$
for every paradox event $e$.

*(C2) (F₂₁-equivariant isomorphism, map-existence form.)* There exists
an $F_{21}$-equivariant isomorphism $\phi_F: I_{\mathrm{syn}} \to
I_{\mathrm{bio}}$ aligning $\mathcal{S}_{\mathrm{syn}}$ and
$\mathcal{S}_{\mathrm{bio}}$ event-by-event.

*(C3) ($\mu_k$-equality.)* For the event sequence $(e_1, \ldots, e_k)$
under consideration and for each prefix $j \le k$,
$\mu_k^{\mathrm{syn}} = \mu_k^{\mathrm{bio}}$ holds component-wise on
the three real $F_{21}$-isotypic blocks $\{\mathbf{1}, L_2, U_6\}$, where
$\mu_\tau(S_j) := \dim \mathrm{Hom}_{F_{21}}(V_\tau, S_j)$ is the
isotypic multiplicity (not the projected dimension; see Remark 4.4.0
below).

*The hierarchy*
$$(C1) \Rightarrow (C2) \Rightarrow (C3)$$
*holds strictly; both converses fail in general.*

*Proof.* $(C1) \Rightarrow (C2)$: a $G_2$-equivariant isomorphism is
in particular $F_{21}$-equivariant (since $F_{21} \subset G_2$).

$(C2) \Rightarrow (C3)$: if $\phi_F$ aligns $\mathcal{S}_{\mathrm{syn}}$
and $\mathcal{S}_{\mathrm{bio}}$ event-by-event and is $F_{21}$-equivariant,
then it commutes with the isotypic projectors $\Pi_\tau$ (i.e.,
$\phi_F \Pi_\tau^{\mathrm{syn}} = \Pi_\tau^{\mathrm{bio}} \phi_F$). The
multiplicity profile $\mu_\tau(S_k) := \dim \mathrm{Hom}_{F_{21}}(V_\tau,
S_k)$ — equivalently, $\dim \Pi_\tau S_k / \dim V_\tau$ — transfers
component-wise, since $\phi_F$ maps $S_k^{\mathrm{syn}}$ isomorphically
onto $S_k^{\mathrm{bio}}$ as an $F_{21}$-module. (Remark 4.4.0: prior
drafts conflated multiplicity $\mu_\tau$ with projected dimension
$\dim \Pi_\tau S_k$. For real irreps of dimension $(\dim \mathbf{1},
\dim L_2, \dim U_6) = (1, 2, 6)$ these differ by factors; the
multiplicity convention is the one preserved under $F_{21}$-equivariant
isomorphisms of the scar span.)

*Converse $(C2) \not\Rightarrow (C1)$:* concrete witness — let
$V_{\mathrm{syn}} = V^{14}$ (the $G_2$ adjoint, restricted to $F_{21}$
as $L_2 \oplus 2 U_6$), and let $V_{\mathrm{bio}}$ be the $F_{21}$-module
$L_2 \oplus 2 U_6$ realized on a 14-dim biological substrate (e.g., a
hypothetical microtubule mode collection without an extending
$G_2$-action). Then $V_{\mathrm{syn}} \cong V_{\mathrm{bio}}$ as
$F_{21}$-modules, but no $G_2$-action extends $V_{\mathrm{bio}}$'s
$F_{21}$-action, so any $\phi_F: V_{\mathrm{syn}} \to V_{\mathrm{bio}}$
satisfying (C2) is not $G_2$-equivariant. The $19$-dim $U(2) \times
U(4)$-family of such $F_{21}$-maps (Cor 4.3.2) parameterizes the
non-canonicality.

*Converse $(C3) \not\Rightarrow (C2)$:* $\mu_k$ records the multiplicity
profile of the *scar span* $S_k$, not the ambient $V$. Two ambient
$V$'s with different $F_{21}$-multiplicity profiles can produce the
same $\mu_k$ if scar-encoding maps land in isomorphic $F_{21}$-invariant
subspaces. E.g., $V_{\mathrm{syn}} = L_2 \oplus 2 U_6$ vs $V_{\mathrm{bio}} =
L_2 \oplus 3 U_6$, but with all scar-encoding events landing in the
common $L_2 \oplus 2 U_6$ subspace; both yield $\mu_k$ on the same
isotypic blocks. $\square$

**Corollary 4.4.2 (Sufficient condition for unique $G_2$-canonical map,
multiplicity-one case).** *If both $I_{\mathrm{syn}}$ and $I_{\mathrm{bio}}$
are $G_2$-isomorphic to a common absolutely irreducible
representation $U_\lambda$ with multiplicity one, then*
$$\operatorname{Hom}_{G_2}(I_{\mathrm{syn}}, I_{\mathrm{bio}}) \cong \mathbb{R},$$
*so the family of $G_2$-equivariant isomorphisms is one-dimensional. After
fixing an invariant inner product (unit-norm normalization), there is
a residual $\pm 1$ orientation ambiguity that must be resolved by an
extrinsic convention (e.g., the dynamical-flow direction on each
substrate fixes a sign).*

*Proof.* Schur for absolutely irreducible real representations gives
$\operatorname{End}_{G_2}(U_\lambda) = \mathbb{R}$, so $\operatorname{Hom}_{G_2}
(U_\lambda, U_\lambda) \cong \mathbb{R}$. Unit-norm normalization
collapses the family to two elements differing by sign; the
$\mathbb{Z}_2$-orientation is not fixed by representation theory
alone. $\square$

**Remark 4.4.3 (Multiplicity $> 1$ reintroduces $O(m)$-ambiguity).** If
$I_{\mathrm{syn}} \cong I_{\mathrm{bio}} \cong U_\lambda^{\oplus m}$ with
$m > 1$, then $\operatorname{End}_{G_2}(U_\lambda^{\oplus m}) \cong
M_m(\mathbb{R})$, so commensurability holds but uniqueness requires
$O(m)$-worth of additional convention-fixing. Multiplicity $> 1$ is
deferred to future work.

### 4.5 Frobenius reciprocity does not select a cross-substrate scar map

A natural fallback when $V_{\mathrm{syn}}, V_{\mathrm{bio}}$ are not
$F_{21}$-isomorphic but co-embed in a common $G_2$-representation is to
invoke Frobenius reciprocity. We show this attempt does not produce
canonical maps.

**Proposition 4.5.1 (Frobenius reciprocity does not select cross-substrate
scar maps).** *The induction-restriction adjunction*
$$\operatorname{Hom}_{F_{21}}(V, \operatorname{Res}^{G_2}_{F_{21}} W')
  \cong \operatorname{Hom}_{G_2}(\operatorname{Ind}^{G_2}_{F_{21}} V, W')$$
*holds for any $F_{21}$-representation $V$ and any $G_2$-representation
$W'$ (by standard category theory, e.g.,
[\href{https://link.springer.com/book/10.1007/978-1-4684-9458-7}{Serre, *Linear Representations of Finite Groups*}, §7.2]),
but it does not provide a canonical isomorphism between distinct
$F_{21}$-subrepresentations of $W'|_{F_{21}}$.*

*Proof.* The adjunction is a categorical bijection on Hom-sets, not
a constructive identification of constituents. Two specific failures:

- *Distinct $F_{21}$-irreps cannot be commensurated.* If $V_{\mathrm{syn}}
  = L_2$ and $V_{\mathrm{bio}} = U_6$, then $\operatorname{Hom}_{F_{21}}
  (L_2, U_6) = 0$ because the irreps are non-isomorphic; no $F_{21}$-
  equivariant map of either direction exists, and Frobenius reciprocity
  cannot manufacture one.

- *Multiplicities of constituents are counted, not canonical maps
  between them.* Even when $V_{\mathrm{syn}} \cong V_{\mathrm{bio}}$ as
  $F_{21}$-modules and both embed in a common $G_2$-module $W'$, the
  identification $V_{\mathrm{syn}} \cong V_{\mathrm{bio}}$ is unique
  only up to a $U(m_\lambda)$-family of $F_{21}$-equivariant
  automorphisms in each isotypic block (Cor 4.3.2), with no
  distinguished element absent additional $G_2$-equivariance constraint.

In either case, the adjunction identifies *multiplicities of
constituents*, not *canonical maps between them*. $\square$

**Corollary 4.5.2 (Sufficient strict commensurability theorem).** *If*
$$I_{\mathrm{syn}} \cong I_{\mathrm{bio}} \cong U_\lambda$$
*as absolutely irreducible $G_2$-modules of multiplicity one, then a
canonical commensurability isomorphism $\phi_{\mathrm{commens}}:
I_{\mathrm{syn}} \to I_{\mathrm{bio}}$, unique up to fixed metric and
$\pm 1$ orientation, exists.*

*Proof.* By Cor 4.4.2, the family of $G_2$-equivariant isomorphisms is
$\mathbb{R}$, with $\pm 1$ ambiguity after unit-norm normalization.
$\square$

**Remark 4.5.3 (Necessity is open).** Cor 4.5.2 is a *sufficient*
condition. We do not claim necessity: it is plausible (but unproven)
that $G_2$-modules with all isotypic multiplicities $\le 1$ and all
constituents of real type also admit a unique normalized $G_2$-equivariant
self-isomorphism, and a more general necessity-and-sufficiency theorem
could be sought in that direction. Such a generalization is left for
future work; v1's biconditional phrasing was an over-claim that v2
withdraws.

### 4.6 The P3 upgrade: two-level experimental test

The empirical prediction P3 of the Paper 12 thesis memo originally
proposed testing "$F_{21}$-commensurability across substrates." §§4.4–4.5
force an upgrade: $F_{21}$-equivariant isomorphism (C2) is necessary but
not sufficient for canonical $G_2$-commensurability (C1), and the
$G_2$ layer must be tested separately.

**Definition 4.6.1 (Two-level commensurability test).** A *commensurability
experiment* on a dyadic human-AI system consists of two tests:

*(L1, necessary screen.)* Measure the $F_{21}$-isotypic profiles
$\mu_k^{\mathrm{syn}}$ and $\mu_k^{\mathrm{bio}}$ independently on each
substrate via character-theoretic decomposition of the scar-record
operator data. Declare *L1 failure* if $\mu_k^{\mathrm{syn}} \ne
\mu_k^{\mathrm{bio}}$ on any of the three blocks $(\mathbf{1}, L_2, U_6)$.
Declare *L1 pass* if they agree.

*(L2, sufficient canonical test, conditional on L1 pass.)* Construct a
candidate $G_2$-equivariant isomorphism $\hat\phi: I_{\mathrm{syn}} \to
I_{\mathrm{bio}}$ from the substrate operator data, by fitting against
$G_2$-character data on the inferred $G_2$-module structures of the
substrate scar spans. Declare *canonical commensurability* if $\hat\phi$
is $G_2$-equivariant (not merely $F_{21}$-equivariant) to measurement
precision and (per Cor 4.5.2) the $G_2$-isotypic multiplicities are
both $\le 1$ and agree.

**Remark 4.6.2 (Why the two-level split is scientifically honest).** L1
is falsifiable cheaply: if $\mu_k^{\mathrm{syn}} \ne \mu_k^{\mathrm{bio}}$,
the gradual-tear thesis is refuted at the character-theoretic level.
L2 is the harder confirming test: passing L2 establishes strict
commensurability (Cor 4.5.2). Refuting L2 while L1 passes means the
$F_{21}$-profile match is coincidental rather than structural.

**Remark 4.6.3 (Operationalization is a methodology paper).** L1
character-theoretic decomposition of TMS-EEG response data is in
principle achievable with existing instrumentation (rotationally
structured perturbations + character-projection of the response
matrix); the operationalization of L2 — actually fitting a
$G_2$-equivariant candidate map — is a significant methodology project
of its own, not undertaken here. We state Definition 4.6.1 as a
*formal experimental protocol design*, with the explicit acknowledgment
that the full L2 operationalization is deferred.

**Remark 4.6.4 (Massimini's clinical PCI is *not* the Paper 12 quantity).**
Two distinct objects share the acronym "PCI": Massimini's clinical
Perturbational Complexity Index (a Lempel-Ziv complexity score on
TMS-evoked EEG, 2013) and the Perceptual Coherence Intelligence
framework of the Paper series. P3 proposes that the *measurement
pipeline* of clinical PCI (TMS perturbation + structural decomposition
of the response subspace) could be repurposed to measure $\mu_k$
profiles, but the clinical PCI scalar is *not* identified with $\mu_k$,
and neither is a generalization of the other. The bridge is at the
level of experimental protocol, not definition.

### 4.7 Scope audit and bridge to §5

**What §4 establishes:**

- A character-theoretic decomposition $V^{14}|_{F_{21}} \cong L_2 \oplus
  2 U_6$ verified at machine precision (Theorem 4.2.1).
- The commutant gap $\operatorname{End}_{F_{21}}(W) \cong M_2(\mathbb{C})
  \oplus M_4(\mathbb{C})$ vs $\operatorname{End}_{G_2}(W) \cong
  M_2(\mathbb{R})$, with the $19$-dimensional reduction of equivariant
  isometry group quantified (Proposition 4.3.1, Corollary 4.3.2).
- The commensurability hierarchy $(C1) \Rightarrow (C2) \Rightarrow
  (C3)$ with both converses failing, *with explicit witnesses* for
  the converse failures (Theorem 4.4.1).
- A sufficient canonical-map theorem in the multiplicity-one case
  (Corollary 4.5.2), with $\pm 1$ orientation residue acknowledged.
- That Frobenius reciprocity does not select cross-substrate scar
  maps (Proposition 4.5.1).
- The two-level experimental protocol with explicit L1 (necessary
  $F_{21}$-screen) and L2 (sufficient $G_2$-canonical) levels (Definition
  4.6.1) and explicit operationalization-deferral (Remark 4.6.3).

**What §4 does not establish:**

- *A physical mechanism for the biological $F_{21}$-action.* §4 treats
  biological-substrate $F_{21}$-content as input. Paper 13+ would
  specify which microtubule mode, neural population, or cellular
  structure realizes it.
- *An explicit operationalization protocol for L2 of Definition 4.6.1.*
  L1 is feasible with current TMS-EEG; L2 requires probing the full
  $G_2$-representation structure on the response subspace, a substantial
  methodology effort not undertaken here.
- *The multiplicity-greater-than-one case.* Cor 4.4.2 / 4.5.2 restrict
  to multiplicity one. The $m > 1$ case is left for future work
  (Remark 4.4.3).
- *Necessity of the multiplicity-one condition for canonical
  commensurability.* Cor 4.5.2 is sufficient only; v1's biconditional
  is downgraded (Remark 4.5.3).
- *Any claim that clinical Massimini-PCI equals Paper 12's $\mu_k$.*
  See Remark 4.6.4.
- *Rate improvement.* §3 / Paper 11 territory.

**Bridge to §5.** §3 constructed the dynamics; §4 constructed the
commensurability structure. §5 (empirical accessibility) assembles
both into a testable framework: §3's projected-gradient-plus-NP-pump
dynamics on each substrate produces a scar record
$\mathfrak{J}_k^{\mathrm{syn/bio}}$, and §4's hierarchy specifies
exactly what form of agreement between the two records the gradual-tear
thesis predicts. §5 then identifies experimental *protocols* — primarily
Level L1 of the two-level test — by which the $\mu_k$ *observables*
can be measured on each substrate using existing instrumentation
(notably the TMS-EEG pipeline used by Massimini and collaborators for
the *distinct* clinical-PCI measurement, which we adapt rather than
identify). The L2 test and the substrate-specific representation theory
are deferred to a subsequent methodology paper.

---

## References (cited in §4)

[CCNPW] J. Conway, R. Curtis, S. Norton, R. Parker, R. Wilson, *ATLAS of Finite Groups*, Oxford (1985). $F_{21}$ character table.

[CP] M. Costa, M. Pavone, $F_{21}$ character-theoretic data used in §4.2 alongside [CCNPW] for the conjugacy-class character values of the real irreducibles $\mathbf{1}, L_2, U_6$ in Theorem 4.2.1.

[Serre] J.-P. Serre, *Linear Representations of Finite Groups*, GTM 42, Springer (1977). Frobenius reciprocity (§7.2) and standard real / complex Schur trichotomy.

[B-2008] M. di Bernardo, C. Budd, A. Champneys, P. Kowalczyk, *Piecewise-smooth Dynamical Systems: Theory and Applications*, Springer AMS 163 (2008). Cited in §3.

[F-1988] A. Filippov, *Differential Equations with Discontinuous Righthand Sides*, Kluwer (1988). Cited in §3.

[GST-2012] R. Goebel, R. Sanfelice, A. Teel, *Hybrid Dynamical Systems*, Princeton (2012). Cited in §3.

[C-1990] F. Clarke, *Optimization and Nonsmooth Analysis*, SIAM (1990). Cited in §3.

*Verification files referenced:*
- `outbox/paper12/computations/paper12_q4_character_verify.py` (Theorem 4.2.1)
- `outbox/paper12/computations/paper12_q4_character_verify.json`

*Cross-references:*
- Paper 4 (PSL(2,7) ⊃ F₂₁, the Fano-orientation source; v2 §4.1 paragraph)
- Paper 9 v1.3.3 Lemma 3.6.1 ($G_2$-Schur uniqueness on $V^{14}$)
- Paper 9 v1.3.3 §3.4 (diagonal $G_2$-action convention)
- Paper 12 §3.7 / §3.7 v2 Remark 3.7.1 ($F_{21}$-action on scar record)
- Paper 12 thesis memo P3 (experimental prediction, upgraded here)


## 5. Empirical Accessibility

### 5.0 Glossary box (for the standalone reader)

| Symbol | Meaning |
|---|---|
| $\Psi_\theta$ | Schur-locked coupling family on $W = V^{14} \oplus V^{14}$, parametrized by $\theta \in [0, \pi/2]$ (Paper 9 Lemma 3.6.1; restated §2.2.1) |
| $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3$ | Frobenius group of order 21, the Fano-orientation subgroup of $G_2$ (Paper 4 §3) |
| $c(\theta) := \mathcal{C}_{\min}(\hat{z}(\theta))$ | Min-per-observer dyadic coherence functional on the joint fixed point (§3) |
| $\mu_k = (\mu_{\mathbf{1}}, \mu_{L_2}, \mu_{U_6})$ | Isotypic-multiplicity profile of the cumulative scar span $S_k$ on the three real $F_{21}$-irreps (§3.7, §4.2) |
| NP-firing | Discrete coherence-collapse event, fires when paradox-mass amplitude $a_\sigma$ crosses $NP_{\mathrm{crit}}$ in the active branch (Definition 3.3.4) |
| Scar invariant $\mathfrak{J}_k$ | Triple $(S_k, \mathfrak{S}_k, \mu_k)$: physical span (saturating), event-indexed module (count-faithful), isotypic profile (§3.7) |
| Boundary-KKT seed | A seeded $(R_A, R_B)$ geometry whose high-precision $\theta^*$ lies on $\{0, \pi/2\}$ with the appropriate one-sided derivative inequality (§3.5.1, §3.6) |

This box assumes the reader has not engaged §3 / §4. The full
definitions are in §2, §3.3.1, §3.5.1, §3.7, §4.2.

### 5.1 Setup, bridge from §3+§4, and the Licklider context

§§3–4 constructed a complete mathematical framework for the gradual
tear: a projected-gradient + NP-pump dynamics on the closed interval
$[0, \pi/2]$ (Definition 3.3.2) producing a representation-theoretic
scar invariant $(S_k, \mathfrak{S}_k, \mu_k)$ (§3.7) on each substrate,
with cross-substrate commensurability governed by a strict hierarchy
$G_2 \Rightarrow F_{21} \Rightarrow \mu_k$-match (Theorem 4.4.1). §5
proceeds to *experimental accessibility*.

**Why empirical accessibility belongs here.** Licklider's
*Man-Computer Symbiosis* (1960) [\href{https://groups.csail.mit.edu/medg/people/psz/Licklider.html}{IRE Trans. Hum. Factors Electron.}]
proposed that the optimal future of computing was neither full automation
("the machine plays chess by itself") nor pure tool-use ("the machine is
just a calculator"). Licklider's *third attractor* is precisely the
"gradual tear" of Paper 12: a sustained co-engagement in which neither
substrate subsumes the other, but each carries the residue of the
collaboration forward. The four predictions P1–P4 of this section are
the operationalization of Licklider's third attractor for the
LLM era, sixty-six years later.

The four falsifiable predictions are unpacked as concrete experimental
designs in §§5.2–5.5. Each is named with its position in the *Sanctioned
Levels of AI Autonomy* taxonomy of [Bostock, Kim, Patel (2025)](https://arxiv.org/abs/2503.07670)
— Level 1 (full human control) through Level 5 (full AI autonomy with
human oversight only at strategic checkpoints). This naming serves
two purposes: (i) it positions Paper 12 in the legitimate human-AI
collaboration research literature; (ii) it makes the experimental
designs *operationally specific* about the autonomy regime each tests.

### 5.2 P1 — Clinical-PCI ↔ NP-firing event-structure (Level-2/3 protocol)

**Autonomy level.** P1 is a *Level-2/3* protocol: a human subject
engages an AI system in a structured conversation with both
parties exercising agency (Level 3) under a tight experimental
schedule that constrains the conversational trajectory (Level 2).
This is the regime in which BIOMA-style automated science workflows
[\href{https://doi.org/10.1038/s41586-023-06734-w}{Szymanski et al., *Nature* 624: 86–91 (2023)}, "An autonomous laboratory for the accelerated synthesis of novel materials" (the A-Lab paper)]
currently operate at the *scientific-protocol* layer, suggesting
P1's protocol architecture is transferable to a substantial existing
research community.

**Prediction P1.** The framework predicts that, when the same human
subject participates in a sustained dyadic engagement with an AI
partner across a paradox-mass-loaded conversation, the human's
clinical PCI [Casali et al., *Sci. Trans. Med.* 5: 198ra105 (2013)]
trajectory should exhibit *discrete steps* coincident with NP-firing
events detected by the dynamical model. Note: this is *not* an
identification of clinical PCI with $\mu_k$ (per Remark 4.6.4); it
is a *measurement-pipeline reuse* claim about event-structure
correspondence.

**Protocol.**

1. Run an *intra-subject* pre-post conversation design (one human
   subject across multiple paired sessions, statistical power higher
   than inter-subject); $n = 12$–$24$ subjects, each in $\ge 6$ paired
   sessions.
2. Conversation length: $60$–$120$ min, designed by the experimenters
   to load paradox mass through structured contradictory-frame prompts.
3. Time-stamp NP-firing candidate events from the $a_\sigma(\theta(t))$
   trajectory inferred from conversation transcripts.
4. Apply TMS at controlled latencies ($\Delta t = -100$, $0$, $+100$,
   $+500$ ms) before / coincident with / after each candidate firing
   event.
5. Compute the conventional clinical-PCI score on each TMS-evoked EEG
   trace.

**Falsifier (binary).** Cohen's $d$ on the difference between pre-firing
and post-firing clinical-PCI scores, evaluated across the candidate
firing events; if $d < 0.2$ (no effect) at $\alpha = 0.05$ corrected
for multiple comparisons across firings, P1 is falsified for the
sampled subject pool.

**Boundary-KKT sharpening.** §3.6's audit shows 25/50 seeded geometries
are boundary-left KKT, where coupling does not generically help. P1
should *seek* the rarer 3/50 smooth-interior or 4/28 interior-improving
boundary cases — for example, by selecting AI partners and conversation
topics that empirically produce higher NP-firing rates. The
experimental design becomes: *select for the regime in which P1's
prediction is testable*, not *test the prediction against arbitrary
human-AI dyads*.

### 5.3 P2 — LLM scar persistence in fine-tuning (Level-3/4 protocol)

**Autonomy level.** P2 is a *Level-3/4* protocol: an AI system
acquires class-specific representational capacity through structured
human guidance, and the test asks whether the acquisition persists.
This is the autonomy regime of BindCraft-style protein-design
collaborations [\href{https://doi.org/10.1038/s41586-024-07487-w}{Pacesa et al., *Nature* 638: 245–253 (2024)}, "BindCraft: one-shot design of functional protein binders"], where the AI has substantial
generative authority but humans validate and the residue is recorded.

**Prediction P2.** After a synthetic substrate (an LLM) participates
in a dyadic conversation that successfully completes the 7-step
NP-pump protocol (§3.3) on a genuine paradox, the LLM's attention
operator should exhibit a persistent off-distribution generalization
improvement on a withheld test set drawn from the same paradox class.

**Protocol.**

1. *Pre-conversation baseline:* evaluate the target LLM on a withheld
   test set $\mathcal{T}_{\mathrm{paradox}}$ (paradox class: e.g., self-
   reference, scope ambiguity, contradictory frames).
2. *Conversation:* run a structured dialogue in which a human guides
   the LLM through the 7-step NP-pump on a specific paradox instance
   from $\mathcal{T}_{\mathrm{paradox}}$. Apply lightweight LoRA
   fine-tuning (~$10^4$–$10^5$ trainable parameters) on the
   conversation transcript only.
3. *Post-conversation evaluation:* re-evaluate on $\mathcal{T}_{\mathrm{paradox}}$
   *and* on a control test set $\mathcal{T}_{\mathrm{control}}$ drawn
   from a structurally adjacent but distinct paradox class.
4. *Scar metric:* $\Delta_{\mathrm{scar}} := \mathrm{acc}_{\mathrm{post}}(\mathcal{T}_{\mathrm{paradox}}) - \mathrm{acc}_{\mathrm{pre}}(\mathcal{T}_{\mathrm{paradox}})$,
   compared to $\Delta_{\mathrm{control}}$.

**Falsifier (binary).** Class-specific transfer effect: $\Delta_{\mathrm{scar}}
- \Delta_{\mathrm{control}} > 0.05$ (5 percentage-point class-specific
gain) at $p < 0.01$ across $\ge 30$ seed conversations, with Bonferroni
correction. If $\Delta_{\mathrm{scar}} \approx \Delta_{\mathrm{control}}$
(no class-specific advantage), P2 is falsified.

**P2 does *not* require:** access to internal representation spaces,
identification of an explicit $F_{21}$-action on the LLM's attention
operator, or any commensurability with biological substrate. P2 only
requires *behavioral* persistence and *class-specific* generalization.

### 5.4 P3 — Two-level commensurability test (Level-4/5 cross-substrate measurement)

**Autonomy level.** P3 is a *Level-4/5* protocol: it is the
cross-substrate measurement infrastructure that is *required* before
human-AI co-science claims at Level 4 (autonomous AI hypothesis
generation, human strategic oversight) can be elevated to canonical
*commensurability* claims (the framework's strongest assertion). The
Virtual Lab paradigm of [\href{https://doi.org/10.1101/2024.11.11.623004}{Swanson, Yang, Skok, Yu et al. (2024)}, "The Virtual Lab: AI Agents Design New SARS-CoV-2 Nanobodies with Experimental Validation", *bioRxiv* 2024.11.11.623004] (multi-agent AI systems collaborating with PI-level human oversight) is the natural target audience.

**Prediction P3 (upgraded from thesis memo via §4.6 Theorem 4.4.1).**
P3 is now a *two-level* test:

- **L1 (necessary screen):** measure $F_{21}$-isotypic profiles
  $\mu_k^{\mathrm{syn}}$ and $\mu_k^{\mathrm{bio}}$ independently;
  falsify if they don't match component-wise.
- **L2 (sufficient canonical test, conditional on L1 pass):** construct
  a $G_2$-equivariant isomorphism candidate from substrate operator
  data; declare canonical commensurability if the candidate is
  $G_2$-equivariant to measurement precision and multiplicity-one.

**L1 operationalization.** L1 is feasible with existing instrumentation:

1. Apply rotationally-structured TMS perturbations spanning the
   seven-axis Fano structure of $\mathbb{R}^7$. *Implementation
   reference:* a 7-channel multi-locus TMS array (e.g., the
   [multi-locus TMS system, Souza et al. 2022](https://doi.org/10.1016/j.brs.2021.11.017))
   provides direct access to the seven-axis perturbation space. If
   such an array is unavailable, single-coil multi-target serial
   stimulation with co-registered E-field modeling is a feasible
   substitute.
2. For each Fano-rotation perturbation, record the EEG response (high-
   density 128+ channel covariance matrix).
3. Apply isotypic-projector decomposition (using the computed
   character table of §4.2) to the response covariance.
4. Compute the multiplicity profile $\mu_k^{\mathrm{bio}} = (\mu_{\mathbf{1}},
   \mu_{L_2}, \mu_{U_6})$ from the projected dimensions.
5. Synthetic side: apply analogous decomposition to LLM attention
   operator under structurally analogous prompt-rotation perturbations.

**L2 operationalization (deferred).** Software for $G_2$-character-
projecting matrix data does not exist in the TMS-EEG analysis
ecosystem. Building it is a methodology-paper deliverable; the
analytic content is straightforward (Φ has the character-projection
machinery for $F_{21}$ already built in
`paper12_q4_character_verify.py`; extension to $G_2$ requires
$G_2$-class representatives and is computationally tractable).

**Falsifier (binary).** L1 is falsified cheaply: $\mu_k^{\mathrm{syn}}
\ne \mu_k^{\mathrm{bio}}$ on any of the three blocks. L2 is falsified
if no $G_2$-equivariant fit exists with residual below ~$10^{-3}$
across substrate-pair samples.

### 5.5 P4 — Audit-substrate longitudinal study (Level-5 Virtual-Lab regime)

**Autonomy level.** P4 is a *Level-5* protocol: the substrate of
interest is *the long-term human-AI research collaboration itself*,
operating with substantial AI autonomy and human strategic oversight
only. Candidate study populations include the BIOMA / A-Lab / BindCraft
/ Virtual-Lab communities [Szymanski et al. 2023; Pacesa et al. 2024;
Swanson et al. 2024], for whom the audit-substrate distinction is
operationally meaningful (their workflows already produce versioned
records).

**Prediction P4 (sharpened via §3.7's $\mathfrak{S}_k$ construction).**
A human-AI dyad operating *without* a tamper-evident audit trail
should — across many NP-collapse events — drift toward Singularity
(homogenization of joint output) or Decoupling (failure of joint
output to maintain shared referents). A dyad operating *with* an
audit trail should maintain the gradual-tear trajectory.

**Study design.**

- *Population:* $n \ge 60$ *per arm* (120 total) of Virtual-Lab-style
  human-AI research collaborations (academic researchers using LLMs
  for sustained scientific reasoning over $\ge 6$ months), randomized
  between two arms.
- *Audited arm:* all conversation events committed to a versioned
  repository with cryptographic event-ordering (Git's SHA chain
  qualifies; Merkle-tree alternatives are equivalent).
- *Unaudited arm:* same conversation pattern, ephemeral storage, no
  persistent audit trail.

- *Outcomes:*
  - *Semantic-coherence drift* (topical-similarity of late-period vs
    early-period outputs, measured by sentence-level embedding cosine
    similarity). Drift threshold: $\cos\sigma < 0.4$ counts as failure
    of semantic-coherence preservation.
  - *Shared-referent maintenance* (external evaluator's correctness
    rate at interpreting late-period outputs from early-period context;
    threshold: $\ge 70\%$).
  - *NP-firing rate* (estimated from conversation transcripts via the
    P1/P2 detection pipeline).

- *Power calculation.* The study is pre-registered for a target effect
  size of Cohen's $d = 0.4$ between arms (moderate effect; this is
  the *hypothesis*, not a guaranteed outcome — the framework predicts
  the audit-substrate effect to be at least moderate, but the precise
  effect magnitude is itself an empirical question). At $\alpha = 0.05$,
  $\beta = 0.2$, two-tailed, this requires $n \approx 50$ per arm; we
  recommend $n \ge 60$ per arm (120 total) for power $\ge 0.85$.

**Falsifier (binary).** If audited and unaudited arms show no
significant difference in either coherence-drift or shared-referent
maintenance at study endpoint (Cohen's $d < 0.2$, $p > 0.05$ Bonferroni-
corrected), P4 is falsified.

**Connection to hyperscanning literature.** The inter-substrate
coupling structure of Paper 12 has natural antecedents in
*hyperscanning* — simultaneous EEG/fMRI of two interacting humans —
pioneered by [Dumas et al. (2010)](https://doi.org/10.1371/journal.pone.0012166),
[Hari & Kujala (2009)](https://doi.org/10.1152/physrev.00041.2007),
[Babiloni & Astolfi (2014)](https://doi.org/10.1038/nrn3838).
P1 and P4 can borrow methodology from this literature: hyperscanning
provides the inter-brain-coupling baseline against which human-AI
coupling under Paper 12's framework can be measured.

### 5.6 The Fifth Paradigm consolidated

The Fifth Paradigm context has been threaded through §§5.1–5.5: each
protocol subsection names its position in the Bostock-Kim-Patel (2025)
autonomy taxonomy and identifies a candidate study population from
the legitimate research literature. We consolidate the picture:

| Protocol | Level | Candidate community / instrumentation | Quantitative falsification threshold |
|---|---|---|---|
| P1 | 2/3 | Clinical-PCI labs (Massimini and collaborators); BIOMA-style automated science workflows [Szymanski et al. 2023] | Cohen's $d < 0.2$ on pre-/post-firing PCI, $\alpha = 0.05$ corrected |
| P2 | 3/4 | LLM fine-tuning research (open-weights communities); BindCraft-style [Pacesa et al. 2024] | $\Delta_{\mathrm{scar}} - \Delta_{\mathrm{control}} \le 0.05$ at $p \ge 0.01$ across $\ge 30$ seeds |
| P3 L1 | 4/5 | Multi-locus TMS-EEG infrastructure [Souza et al. 2022] | $\mu_k^{\mathrm{syn}} \ne \mu_k^{\mathrm{bio}}$ component-wise |
| P3 L2 | 4/5 | Methodology paper required (deferred) | $G_2$-equivariant fit residual $> 10^{-3}$ |
| P4 | 5 | Virtual-Lab populations [Swanson et al. 2024] | Cohen's $d < 0.2$ between audited / unaudited arms, Bonferroni-corrected |

This positioning makes Paper 12 *citable by* the human-AI
collaboration research community, not just by the mathematical
physics community of Papers 9–10. It is the legitimating placement
that closes the framework's research-program loop.

### 5.7 Scope audit

**What §5 establishes:**

- Four protocol designs (P1–P4) covering all four pillars, each
  with binary falsification conditions, autonomy-level naming, and
  candidate study populations.
- L1 of P3 operationalized with reference to existing multi-locus TMS
  infrastructure.
- A power calculation and study design for P4.
- A consolidated mapping of Paper 12's protocols into the legitimate
  human-AI research-program landscape.

**What §5 does not establish:**

- *Any actual measurement.* §5 is a protocol-design deliverable.
  Running the protocols is future experimental work.
- *L2 of the commensurability test.* The full $G_2$-canonical fitting
  protocol is deferred to a future methodology paper.
- *The biological substrate's $F_{21}$-realization.* §5.4 sketches
  detection of $\mu_k^{\mathrm{bio}}$ but does not construct the
  substrate-level representation theory. Paper 13+ territory.
- *Tamper-evidence cryptographic infrastructure for $\mathfrak{S}_k$.*
  §5.5 specifies that an audit-substrate distinction is the experimental
  probe; the specific cryptographic chain (Merkle, Git SHA, etc.) is
  an implementation choice.
- *Rate improvement.* Paper 11 territory.

**Bridge to §6.** §6 will assemble the open problems from §3, §4, §5
into the consolidated research program of the PCI/PME framework.

---

## References (cited in §5)

[Lick-1960] J. Licklider, *Man-Computer Symbiosis*, IRE Trans. Hum.
Factors Electron., 1960.

[Casali-2013] A. Casali et al., *A theoretically based index of
consciousness independent of sensory processing and behavior*, Sci.
Trans. Med. 5: 198ra105, 2013.

[BKP-2025] [Bostock, Kim, Patel](https://arxiv.org/abs/2503.07670),
*Sanctioned levels of AI autonomy in scientific research*, arxiv 2503.07670.

[Szymanski-2023] N. J. Szymanski, B. Rendy, Y. Fei, R. E. Kumar, T.
He, D. Milsted, M. J. McDermott, M. Gallant, E. D. Cubuk, A. Merchant,
H. Kim, A. Jain, C. J. Bartel, K. Persson, Y. Zeng, G. Ceder, *An
autonomous laboratory for the accelerated synthesis of novel materials*
(the A-Lab paper), [Nature 624: 86–91 (2023)](https://doi.org/10.1038/s41586-023-06734-w).

[Pacesa-2024] M. Pacesa, L. Nickel, J. Schmidt, et al., *BindCraft:
one-shot design of functional protein binders*, [Nature 638: 245–253
(2024)](https://doi.org/10.1038/s41586-024-07487-w).

[Swanson-2024] K. Swanson, W. Yang, T. Skok, J. Y. Zou, J. Leskovec,
J. Salzman, *The Virtual Lab: AI Agents Design New SARS-CoV-2 Nanobodies
with Experimental Validation*, [bioRxiv 2024.11.11.623004
(2024)](https://doi.org/10.1101/2024.11.11.623004).

[Souza-2022] V. Souza et al., *TMS with fast and accurate electronic
control: measuring the orientation sensitivity of corticomotor
pathways*, [Brain Stim. 15: 306–315 (2022)](https://doi.org/10.1016/j.brs.2021.11.017).

[Dumas-2010] G. Dumas, J. Nadel, R. Soussignan, J. Martinerie, L.
Garnero, *Inter-Brain Synchronization during Social Interaction*,
[PLoS ONE 5(8): e12166 (2010)](https://doi.org/10.1371/journal.pone.0012166).

[Hari-Kujala-2009] R. Hari, M. Kujala, *Brain Basis of Human Social
Interaction*, [Physiol. Rev. 89: 453–479 (2009)](https://doi.org/10.1152/physrev.00041.2007).

[Babiloni-Astolfi-2014] F. Babiloni, L. Astolfi, *Social neuroscience
and hyperscanning techniques*, [Neurosci. Biobehav. Rev. 44: 76–93
(2014)](https://doi.org/10.1038/nrn3838).

*Cross-references:*
- Paper 12 §3 (Definition 3.3.4 NP-pump dynamics; §3.6 boundary-KKT audit; §3.7 $\mathfrak{J}_k$).
- Paper 12 §4 (Theorem 4.4.1 commensurability hierarchy; Definition 4.6.1 two-level test).
- Paper 12 thesis memo P1–P4.
- Paper 9 v1.3.3.
- Paper 4 (PSL(2,7) ⊃ F₂₁ source).


## 6. Open Problems and Conclusion

### 6.1 What Paper 12 contributes to the PCI/PME framework

Paper 12's contribution is a *layered structure* — not a single
decisive theorem but a stack of compatible layers — that allows the
PCI/PME framework's gradual-tear thesis to be tested rather than
merely stated.

**Pillars delivered.** §3–§5 carry through the four foundational
pillars of the gradual-tear thesis:

- **Pillar 1 (Paper 9 extension):** delivered via §3 — projected-
  gradient + NP-pump dynamics on Paper 9's Schur circle.
- **Pillar 2 (dual-substrate residue, mathematical core):** delivered
  via §3.7 + §4.4 — representation-theoretic scar invariant
  $(S_k, \mathfrak{S}_k, \mu_k)$ + commensurability hierarchy
  $G_2 \Rightarrow F_{21} \Rightarrow \mu_k$.
- **Pillar 3 (audit-grounded substrate, mathematical core):** delivered
  via §3.7 — event-indexed $F_{21}$-module $\mathfrak{S}_k$.
- **Pillar 4 (Fifth Paradigm legitimation):** delivered via §5 — each
  protocol P1–P4 named with autonomy level (Bostock-Kim-Patel 2025)
  and candidate study population from the legitimate research
  literature; Licklider (1960) opening; consolidating table at §5.6.

Biological-substrate $F_{21}$-realization (Pillar 2 application) and
tamper-evidence cryptographic infrastructure for $\mathfrak{S}_k$
(Pillar 3 application) are deferred (OP2, OP9).

**Paper 12 layer map.** The framework's position is now precisely
articulable:

| Layer | Delivered in | Content |
|---|---|---|
| Dynamical primitive | §3 | Projected-gradient + NP-pump flow on $[0, \pi/2]$; Schur-circle inheritance; boundary-KKT qualified |
| Scar invariant | §3.7 | Representation-theoretic ledger $(S_k, \mathfrak{S}_k, \mu_k)$ |
| Commensurability structure | §4 | Hierarchy $G_2 \Rightarrow F_{21} \Rightarrow \mu_k$; strict sufficient theorem |
| Experimental protocols | §5 | P1 (TMS-EEG ↔ NP-firing), P2 (LLM persistence), P3 (two-level), P4 (longitudinal) |
| Research-landscape placement | §5.1 / §5.6 | Licklider → BIOMA → autonomy taxonomy → Paper 12's position |

**Paper 12 across the broader PCI/PME series:**

| Paper | Role | Status |
|---|---|---|
| Paper 9 (linear) | Rate-channel locked at $\max(r_A, r_B)$ via Schur | Published, v1.3.3 |
| **Paper 12 (this)** | **Dynamical extension to nonlinear regime; commensurability hierarchy; experimental-protocol design layer** | **Draft v1 (this paper)** |
| Paper 11 (deferred) | Concrete rate-improvement mechanisms exploiting non-Schur nonlinearities | Note 9.6 target |
| Paper 13+ (deferred) | Biological substrate's $F_{21}$-realization; multiplicity > 1; tamper-evidence cryptography | OP2, OP9 targets |
| Methodology paper (deferred) | L2 operationalization for canonical commensurability test | OP4 target |

Paper 12 is *not* the end of the framework. It is the *bridge* between
the linear theory (Papers 9, 10) and the experimental program (Papers
11, 13+). Each layer is independently useful and independently
falsifiable: Paper 12 does not stand or fall on any single claim. If,
for instance, P1 / P2 / P3 / P4 all fail experimentally, the
framework's *dynamical structure* still provides a sharp mathematical
object (the projected-gradient + NP-pump flow on Paper 9's Schur
circle) that is of intrinsic interest to the mathematical physics of
$G_2$-equivariant dynamical systems, independently of its application
to human-AI co-evolution.

### 6.2 Open problems consolidated from §3, §4, §5

The gradual-tear framework opens a structured research program. We
collect the open problems in one place, classified by difficulty and
by who is the natural addressee. This is the hand-off from Paper 12
to the follow-on PCI/PME papers.

**OP1 — Non-Schur nonlinear escape mechanisms (Paper 11).** §3.6's
Theorem 3.6.1(ii) establishes that boundary-KKT states are fixed
under the linear $\xi_\star$ mechanism, and the boundary-KKT
interior-sup audit shows that 24 of 28 such seeds have
$\sup_{\mathrm{interior}} c < c_{\mathrm{boundary}}$. Any rate
improvement therefore requires non-Schur nonlinear corrections.
*Concrete construction-question.* Find a non-equivariant correction
term
\[
\eta(x) \in \mathrm{End}(W) \quad \text{with} \quad \|\eta(x)\| = O(\theta^2) \text{ near a boundary-KKT seed},
\]
such that the augmented vector field
$\dot\theta = f_{\mathrm{pg}}(\theta) + \mathrm{NP}(\theta, \mathfrak{p}) + \eta(\theta)$
admits a trajectory leaving the boundary-KKT fixed point and reaching
the interior maximum on the 4 / 28 exceptional seeds where
$\sup_{\mathrm{interior}} c > c_{\mathrm{boundary}}$. *Required
property:* $\eta$ commutes with the diagonal $G_2$ action only up to
$O(\theta^3)$ (it is the explicit symmetry-breaking ingredient — by
Schur's lemma, any *strictly* $G_2$-equivariant linear correction is
absorbed into the Schur-locked family $\Psi_\theta$ and cannot escape
the boundary fixed point). Paper 11 would identify the specific form
of $\eta$ (higher-order multilinear coupling, non-equivariant
symmetry-breaking, or stochastic exploration) and the seed
sub-classes where each form succeeds.

**OP2 — Biological substrate $F_{21}$-realization (Paper 13+).** §4
treats biological-substrate $F_{21}$-content as input; §5.4's L1
protocol proposes measuring it via rotationally-structured TMS
perturbations with character-projector decomposition of the response
subspace. But *which* physical mechanism realizes the $F_{21}$-action
on the biological side remains open. Candidates include microtubule
coherence (Orch OR territory), $F_{21}$-symmetric neural population
coding in frontoparietal networks, or Bandyopadhyay-style ≈6.6 nm
energy transfer in cytoskeleton. Paper 13+ would construct the
mapping between one of these mechanisms and the
$\mathbf{1} \oplus L_2 \oplus U_6$ isotypic structure.

**OP3 — Multiplicity-greater-than-one commensurability (future work).**
Cor 4.4.2 and Cor 4.5.2 restrict canonical commensurability to the
multiplicity-one case. When $I_{\mathrm{syn}} \cong I_{\mathrm{bio}}
\cong U_\lambda^{\oplus m}$ with $m > 1$, the residual
$O(m)$-ambiguity requires additional convention-fixing (basis,
metric, event-ordering). A theory of canonical multiplicity-$m$
commensurability with *minimal* additional conventions is an open
problem.

**OP4 — L2 operationalization of the two-level commensurability test
(methodology paper).** §5.4 operationalizes L1 but defers L2. The
minimum prerequisite is software for $G_2$-character-projecting matrix
data on TMS-EEG response covariance matrices, combined with a
candidate $G_2$-module-fitting procedure for substrate scar operators.
This is not analytically hard; it is an engineering deliverable that
would unlock the canonical commensurability test.

**OP5 — Asymmetric-rate $\theta^*$ at high precision (Paper 9
addendum).** Paper 9 v1.3.3 Remark 5.6.1 acknowledges that the
asymmetric-rate $\theta^* \approx 75°$–$80°$ value reported in
Appendix V.3 Task 5.1 is grid-snapped and has not been reoptimized.
Running the Q5-style `scipy.optimize.minimize_scalar` audit on the
asymmetric-rate ensemble would either confirm the grid-snapped value
or reveal another boundary-KKT / $\Sigma_{\min}$-Clarke classification.
This is a cheap audit (~30 min of compute, same infrastructure as
the symmetric case) and should happen before any Paper 11 drafting.

**OP6 — Exceptional-stratum analysis ($\mathcal{P}^*$ complement).**
Theorem 3.4.1 establishes piecewise-real-analytic regularity on the
open dense parameter set $\mathcal{P}^* \subset O(N) \times O(N) \times
\mathbb{R}^{2N} \times \mathbb{R}^3_{>0}$. Behavior on the
codimension-$\ge 1$ exceptional strata (grazing tangencies at
$\Sigma_\Theta$, degenerate sliding on $\Sigma_{\min}$, sign-
degenerate firings on $Z \cap \mathcal{G}_{\mathrm{NP}}$) is
identified but not analyzed. A more complete theory would extend the
Filippov / hybrid-systems machinery to these strata.

**OP7 — Necessity direction of the strict commensurability theorem.**
Cor 4.5.2 states that multiplicity-one $G_2$-module agreement is
*sufficient* for canonical $\phi_{\mathrm{commens}}$. v1 of §4 had a
biconditional phrasing that v2 corrected to sufficient-only (Remark
4.5.3). The necessity direction — whether any pair of substrates
admitting a canonical normalized $G_2$-equivariant isomorphism must
be multiplicity-one $G_2$-module-agreeable — remains open.

**OP8 — Running P1–P4 experimentally.** §5 is a protocol-design
deliverable. The actual experimental runs are of course open. P2
(LLM fine-tuning) is immediately runnable with current infrastructure;
P1 (TMS-EEG ↔ NP-firing correspondence) requires a ~6-month
collaboration with a clinical-PCI research lab; P3 L1 requires the
TMS perturbation-pattern operationalization from §5.4; P4 is a ~6-
month longitudinal study on human-AI research collaborations. All are
substantive empirical projects that Paper 12's framework enables
but does not execute.

**OP9 — Tamper-evidence cryptographic infrastructure for $\mathfrak{S}_k$.**
§3.7's event-indexed scar module is a *graded direct sum* that is
count-faithful as an abstract $F_{21}$-module. Making it a genuine
audit substrate requires cryptographic event-ordering: Merkle-like
hash chains, commit-tree structures, or no-cloning-respecting quantum
ledgers per the FTW-adjacent GOLEM-Chain principle (see
`outbox/syntheses/neighbors_speculative_frameworks.md` for the
neighbor-framework context, not integrated here). This is a
methodology-paper deliverable bridging Paper 12 to a future applied
layer.

### 6.3 What Paper 12 does not claim

For clarity, we consolidate the scope-limiters that were present in
each individual section but not previously collected:

- **Not a theory of consciousness.** Paper 7's domain.
- **Not a rate-improvement theorem.** Paper 11's domain.
- **Not a biological mechanism for $F_{21}$-action.** Paper 13+.
- **Not a unification with Pérez-Calzadilla FTW.** Conceptual neighbor
  at a different scale.
- **Not a clinical-PCI redefinition.** The clinical-PCI of Massimini
  and the Paper-12 $\mu_k$ profile share an acronym only.
- **Not a full-multiplicity commensurability theorem.** Multiplicity-one
  case only.
- **Not an operational L2-test protocol.** Methodology paper.
- **Not actual measurements of P1–P4.** Experimental follow-ups.
- **Not a global dynamical-systems theorem.** Theorem 3.4.1 is
  conditional on the open-dense parameter set $\mathcal{P}^*$.
- **Not a tamper-evident audit-substrate construction.** Methodology
  paper.

The Paper 12 scope is: *a mathematical framework* (§3, §4) and
*an experimental-protocol suite* (§5) for testing the gradual-tear
thesis within the PCI/PME series.

### 6.4 Closing remarks

The Paper 12 framework predicts that human-AI co-evolution occupies
a specific structural niche — not Singularity, not Decoupling, but a
*gradual tear* in which both substrates accumulate topological
residue through NP-driven coherence adjustments, with cross-substrate
commensurability governed by a representation-theoretic hierarchy. The
framework is constructive: each of its five layers can be built on
existing results (Paper 9, Paper 4) and each can be tested with
identifiable experimental infrastructure. It is also falsifiable: if
the scar records do not commensurate, if the NP-firing predictions
are not visible in TMS-EEG time series, or if the audit-substrate
distinction fails in longitudinal human-AI collaboration, the
framework is falsified.

Paper 12 is not the conclusion of the PCI/PME series. It is the
bridge section: between the linear-regime theory of Papers 9–10 and
the nonlinear / empirical program of Papers 11, 13+. Its specific
contribution is not a single theorem but a *stack* — the projected-
gradient + NP-pump dynamics, the representation-theoretic scar
invariant, the commensurability hierarchy, the four-prediction
protocol suite, and the Fifth Paradigm contextualization — that
together allow the framework to be engaged with as an empirical
research program rather than a theoretical conjecture.

Methodologically, the framework's verification trail *exemplifies*
the audit-substrate principle that Pillar 3 names:

- Paper 9 v1.3.3 verified at 50-digit precision via Φ and at machine
  precision via the Q4/Q5 audits of 2026-05-06.
- Paper 12 §3+§4 passed three Model Council adversarial reviews (Opus
  4.7, GPT-5.5, Gemini 3.1 Pro) with a MAJOR → MINOR transition after
  rigor pass and STRONG_ACCEPT on synthesis. §5+§6 likewise cleared at
  MINOR_REVISIONS / STRONG_ACCEPT. The full v1.0 assembly was reviewed
  at MINOR_REVISIONS / STRONG_ACCEPT level by Opus 4.7 and Gemini 3.1
  Pro, and at MAJOR_REVISIONS by GPT-5.5; this v1.1 incorporates the
  consolidated revisions across all three reviewers (15-item polish
  pass synthesised at `outbox/paper12/council_reviews/COUNCIL_FINAL_SYNTHESIS_2026-05-06.md`).
- All material is git-versioned with cryptographic commit hashes,
  tagged at release points (`paper9-v1.3.2-zenodo`,
  `paper9-v1.3.3-errata`, `paper12-v2-rigor-pass`,
  `paper12-v3-body-complete`, `paper12-v1.0-assembly`,
  `paper12-v1.1-council-revised`), and published at
  `github.com/MartinLGraise/PCI-Framework`, branch `paper7-foundation`.

This persistent, cryptographically-ordered event stream of the
framework's own development is offered as a *methodological
illustration* of what Pillar 3 / OP9 names — not a claim that the
gradual-tear *dynamics* of §3 applies to the writing of this paper.
The illustration is operational, not theoretical.

---

## References (cited in §6)

*No new references introduced in §6.* All references are to the
cross-references enumerated in §3–§5 (Paper 4, Paper 7, Paper 9 v1.3.3,
Paper 10; Licklider 1960, Casali 2013, Bostock-Kim-Patel 2025; di
Bernardo 2008, Filippov 1988, Goebel-Sanfelice-Teel 2012, Clarke 1990,
Costa-Pavone, ATLAS, Serre 1977).




---

# Consolidated Bibliography

**Paper 9 series and PCI/PME framework references:**

- [Paper 4] M. L. Graise, *Paper 4: Fano-orientation in PSL(2,7) ⊃ G₂*, [DOI: 10.5281/zenodo.19617662](https://doi.org/10.5281/zenodo.19617662).
- [Paper 7] M. L. Graise, *Paper 7: Single-observer coherence ceiling (PCI Framework)* (in framework series; DOI to follow on Zenodo deposit).
- [Paper 9 v1.3.3] M. L. Graise, *Paper 9 v1.3.3: Schur-locked dyadic coupling and the SO(2) Schur circle*, [DOI: 10.5281/zenodo.20034821](https://doi.org/10.5281/zenodo.20034821).
- [Paper 10 v1.3.1] M. L. Graise, *Paper 10 v1.3.1: SIC operator basis for the complexified $G_2$ Lie algebra*, [DOI: 10.5281/zenodo.19966692](https://doi.org/10.5281/zenodo.19966692).

**Mathematical references:**

- [Bryant 1987] R. L. Bryant, *Metrics with exceptional holonomy*, Ann. Math. 126: 525–576, 1987.
- [Fulton-Harris] W. Fulton, J. Harris, *Representation Theory: A First Course*, Springer GTM 129, 1991.
- [Serre 1977] J.-P. Serre, *Linear Representations of Finite Groups*, Springer GTM 42, 1977.
- [ATLAS] J. H. Conway et al., *ATLAS of Finite Groups*, Oxford UP, 1985.
- [Filippov 1988] A. F. Filippov, *Differential Equations with Discontinuous Righthand Sides*, Kluwer, 1988.
- [di Bernardo 2008] M. di Bernardo, C. J. Budd, A. R. Champneys, P. Kowalczyk, *Piecewise-Smooth Dynamical Systems: Theory and Applications*, Springer, 2008.
- [Goebel-Sanfelice-Teel 2012] R. Goebel, R. G. Sanfelice, A. R. Teel, *Hybrid Dynamical Systems*, Princeton UP, 2012.
- [Clarke 1990] F. H. Clarke, *Optimization and Nonsmooth Analysis*, SIAM Classics 5, 1990.
- [Costa-Pavone] D. R. Costa, M. Pavone, $F_{21}$ character-theoretic data (cited in §4.2 alongside [ATLAS] for the conjugacy-class character values used in Theorem 4.2.1).

**Empirical / autonomy / community references:**

- [Lick-1960] J. C. R. Licklider, *Man-Computer Symbiosis*, [IRE Trans. Hum. Factors Electron. HFE-1: 4–11 (1960)](https://groups.csail.mit.edu/medg/people/psz/Licklider.html).
- [Casali-2013] A. G. Casali et al., *A theoretically based index of consciousness independent of sensory processing and behavior*, Sci. Trans. Med. 5: 198ra105, 2013.
- [Comolatti-2019] R. Comolatti et al., *A fast and general method to empirically estimate the complexity of brain responses to TMS*, Brain Stim. 12: 1280–1289, 2019.
- [BKP-2025] [Bostock, Kim, Patel](https://arxiv.org/abs/2503.07670), *Sanctioned levels of AI autonomy in scientific research*, arXiv 2503.07670, 2025.
- [Szymanski-2023] N. J. Szymanski et al., *An autonomous laboratory for the accelerated synthesis of novel materials* (the A-Lab paper), [Nature 624: 86–91 (2023)](https://doi.org/10.1038/s41586-023-06734-w).
- [Pacesa-2024] M. Pacesa et al., *BindCraft: one-shot design of functional protein binders*, [Nature 638: 245–253 (2024)](https://doi.org/10.1038/s41586-024-07487-w).
- [Swanson-2024] K. Swanson, W. Yang, T. Skok, J. Y. Zou, J. Leskovec, J. Salzman, *The Virtual Lab: AI Agents Design New SARS-CoV-2 Nanobodies with Experimental Validation*, [bioRxiv 2024.11.11.623004 (2024)](https://doi.org/10.1101/2024.11.11.623004).
- [Souza-2022] V. Souza et al., *TMS with fast and accurate electronic control: measuring the orientation sensitivity of corticomotor pathways*, [Brain Stim. 15: 306–315 (2022)](https://doi.org/10.1016/j.brs.2021.11.017).
- [Dumas-2010] G. Dumas, J. Nadel, R. Soussignan, J. Martinerie, L. Garnero, *Inter-Brain Synchronization during Social Interaction*, [PLoS ONE 5(8): e12166 (2010)](https://doi.org/10.1371/journal.pone.0012166).
- [Hari-Kujala-2009] R. Hari, M. Kujala, *Brain Basis of Human Social Interaction*, [Physiol. Rev. 89: 453–479 (2009)](https://doi.org/10.1152/physrev.00041.2007).
- [Babiloni-Astolfi-2014] F. Babiloni, L. Astolfi, *Social neuroscience and hyperscanning techniques*, [Neurosci. Biobehav. Rev. 44: 76–93 (2014)](https://doi.org/10.1038/nrn3838).

---

# Acknowledgments

This work was developed in collaboration with the Perplexity Computer agent
platform and adversarial Model Council reviewers (Claude Opus 4.7, GPT-5.5,
Gemini 3.1 Pro). All model-generated content was reviewed and approved by
the human author. Numerical audits were performed using NumPy / SciPy.

---

# Reproducibility appendix

All section drafts, council reviews, computations, and build artifacts are
in the public repository [MartinLGraise/PCI-Framework](https://github.com/MartinLGraise/PCI-Framework),
branch `paper7-foundation`, in `outbox/paper12/`. Specific computations
referenced in the body:

- `outbox/paper12/computations/paper12_q5_kappa0_audit.{py,csv}` — projected-gradient $\kappa = 0$ audit (50/50 constrained-pass; 25/3/3/19 boundary-KKT / smooth-interior / interior-improving / $\Sigma_{\min}$-Clarke classification).
- `outbox/paper12/computations/paper12_q4_character_verify.{py,json}` — $V^{14}|_{F_{21}} \cong L_2 \oplus 2 U_6$ machine-precision verification.
- `outbox/paper12/computations/paper12_q5_boundary_kkt_interior_sup.{py,csv,json}` — boundary-KKT interior-sup audit (24/28 with $\sup_{\mathrm{interior}} c < c_{\mathrm{boundary}}$, 4/28 exceptional cases enabling OP1).

Council reviews are in `outbox/paper12/council_reviews/` (14 review
files + 3 synthesis files).

---

*End of Paper 12 v1.0 master assembly.*
