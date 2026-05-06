# Paper 12 §2 — Notation and Paper 9 Inheritance (v1)

**Draft version:** v1 (2026-05-06, ~12:55 PDT)
**Author of draft:** C-7RO (Perplexity Computer, Claude Sonnet 4.6)
**Source:** Paper 9 v1.3.3 §3.4–§3.6, §9; consolidated symbol table from Paper 12 §3 v3 + §4 v3 + §5 v2 + §6 v1.
**Status:** First complete draft of §2. Self-contained reference for §3–§6; readers fluent in Paper 9 v1.3.3 may skim.

---

## 2. Notation and Paper 9 inheritance

This section consolidates the symbols and the Paper 9 results that Paper 12 invokes throughout. Every claim labelled *(P9 §X)* below is stated and proved in Paper 9 v1.3.3 [DOI: \href{https://doi.org/10.5281/zenodo.20034821}{10.5281/zenodo.20034821}] at the indicated location; we restate without reproof. Where Paper 12 strengthens, qualifies, or specializes a Paper 9 statement, this is flagged explicitly with a *(P12 specialization)* marker and a forward reference to the section in which the strengthening is constructed.

### 2.1 Algebraic and group-theoretic notation

#### 2.1.1 Lie groups and representations

| Symbol | Meaning | Reference |
|---|---|---|
| $G_2$ | the compact, simply-connected real form of the exceptional Lie group of rank 2; dimension 14 | [Bryant 1987]; framework convention from Paper 4 §2 |
| $V^{14}$ | the adjoint representation of $G_2$, the only nontrivial 14-dimensional irreducible (over $\mathbb{R}$) | [Fulton-Harris Lecture 22] |
| $W := V^{14} \oplus V^{14}$ | the dyadic state space on which the Paper 9 / Paper 12 flow lives | P9 §3.1 |
| $L_2$ | the trivial 2-dimensional real representation of $F_{21}$ (sum of two copies of the trivial character) | P12 §4.2 |
| $U_6$ | the unique faithful real-irreducible 6-dimensional representation of $F_{21}$ | P12 §4.2 |
| $V^{14}\big|_{F_{21}} \cong L_2 \oplus 2 U_6$ | the branching of $V^{14}$ to $F_{21}$ via PSL(2,7) ⊃ $F_{21}$ ⊂ $G_2$ | P12 Theorem 4.2.1 |

#### 2.1.2 Finite groups

| Symbol | Meaning | Reference |
|---|---|---|
| $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3$ | the Frobenius group of order 21; the Fano-orientation subgroup of $G_2$ | Paper 4 §3 |
| $\mathrm{PSL}(2,7)$ | the simple group of order 168, the natural ambient group of $F_{21}$ via the Fano plane | Paper 4 §2 |
| $\mu_k$ | a multiplicity-vector profile invariant of the scar event $S_k$ (defined in §3.5); a finite-dimensional integer vector indexed by irreducibles of $F_{21}$ | P12 §3.5 Definition 3.5.2 |

#### 2.1.3 Subspaces and isotypic decomposition

The $F_{21}$-isotypic decomposition of $W = V^{14}\oplus V^{14}$ that drives all of §4 is:
\[
W \;=\; W^{L_2} \;\oplus\; W^{U_6}, \qquad
\dim W^{L_2} \;=\; 4, \qquad \dim W^{U_6} \;=\; 24,
\]
where $W^{L_2}$ is the trivial-isotypic component and $W^{U_6}$ is the (twice-twice) faithful-isotypic component. The 24 = (2 copies in $V^{14}$) × (2 copies in $V^{14}$) × $\dim U_6$; the four-dimensional intertwiner space $\mathrm{End}_{F_{21}}(V^{14})|_{U_6}$ governs the commutant gap in Proposition 4.3.1.

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

| Symbol | Meaning | Definition |
|---|---|---|
| $\xi_\star \in T_\theta SO(2)$ | the canonical Schur-derived tear direction | §3.2 Proposition 3.2.2 |
| $f_{\mathrm{pg}}(\theta)$ | the projected-gradient component of the augmented flow | §3.3 Definition 3.3.1 |
| $\mathrm{NP}(\theta, \mathfrak{p})$ | the NP-pump component (state-dependent threshold-driven jump) | §3.3 Definition 3.3.2 |
| $\dot\theta = f_{\mathrm{pg}}(\theta) + \mathrm{NP}(\theta, \mathfrak{p})$ | the augmented flow on $[0, \pi/2]$ | §3.3 Equation (3.3) |
| $\mathfrak{p}$ | the accumulated paradox mass (state variable) | §3.3 Definition 3.3.3 |

#### 2.3.2 The event stratification

| Symbol | Meaning | Definition |
|---|---|---|
| $\Sigma_{\mathrm{tot}}$ | the union of all event-trigger sets in $[0, \pi/2] \times \mathcal{P}$ | §3.4 Definition 3.4.2 |
| $\Sigma_{\mathrm{cross}}$ | crossing events (transversal threshold crossings) | §3.4 Definition 3.4.3 |
| $\Sigma_{\mathrm{slide}}$ | sliding events (Filippov sliding-mode) | §3.4 Definition 3.4.4 |
| $\Sigma_{\mathrm{ext}}$ | extinction events (NP-pump shutdown) | §3.4 Definition 3.4.5 |
| $\Sigma_{\mathrm{degen}}$ | degenerate events (measure-zero pathological set) | §3.4 Definition 3.4.6 |
| $\Sigma_{\mathrm{rec}}$ | recurrence events (finite-multiplicity bouncing) | §3.4 Definition 3.4.7 |

#### 2.3.3 The scar invariants

| Symbol | Meaning | Definition |
|---|---|---|
| $S_k$ | the $k$-th scar event (the $k$-th time the augmented flow leaves the Schur circle and returns) | §3.5 Definition 3.5.1 |
| $\mathfrak{S}_k$ | the scar-trace operator for $S_k$ (an element of $\mathrm{End}_{F_{21}}(W)$) | §3.5 Definition 3.5.1 |
| $\mu_k$ | the multiplicity-profile vector of $S_k$ over $\mathrm{Irr}(F_{21})$ | §3.5 Definition 3.5.2 |
| $\mathfrak{J}_k = (\mathrm{tr}\,\mathfrak{S}_k,\; \det\mathfrak{S}_k|_{U_6},\; \mu_k)$ | the triple invariant of the scar event | §3.5 Definition 3.5.3 |

#### 2.3.4 The commensurability hierarchy

| Symbol | Meaning | Definition |
|---|---|---|
| $\mathcal{C}_{\min}$ | minimal coherence (the operational scalar driving the projected-gradient leg) | §3.3 Definition 3.3.4 |
| $\mathcal{J}$ | the joint Jordan-decomposition functional on event traces | §4.3 Definition 4.3.2 |
| $\mathrm{Comm}_{G_2}, \mathrm{Comm}_{F_{21}}, \mathrm{Comm}_{\mu_k}$ | the three nested commensurability relations | §4.4 Definition 4.4.2 |

### 2.4 Operational notation (P1–P4, scar-detection metrics)

Paper 12 §5 introduces protocol-level notation. We reproduce here only the symbols that appear before §5; full operational definitions are in §5.

- **Autonomy levels** $L_0, L_1, L_2$ refer to the Bostock-Kim-Patel 2025 *Sanctioned Levels of AI Autonomy* taxonomy [DOI: pending; preprint cited in §5.4].
- **TMS-EEG perturbational complexity index (PCI)** is used at clinical thresholds [Casali et al. 2013, *Sci Transl Med*; Comolatti et al. 2019, *Brain Stimul*].
- **Audit substrate** $\mathcal{A}$ refers to the human-readable, time-stamped, append-only ledger of every coherence-adjustment event (§3.5, §6.1).

### 2.5 Reading conventions

- All inequalities involving $r_A, r_B, r_{AB}, \mathcal{C}_{\min}$ are with respect to the operator norm induced by the Paper 9 inner product on $W$ (P9 §3.1, eq. (3.1.4)).
- All "open dense parameter set" qualifications refer to the parameter manifold $[0, \pi/2] \times \mathcal{P}$, where $\mathcal{P}$ is the Paper 12 parameter space defined in §3.3.
- All "real-analytic" and "piecewise real-analytic" claims invoke the Paper 9 real-analytic structure of $\hat{z}(\theta)$ via Theorem 9.4.
- "Paper 9 v1.3.3" means specifically the errata-only update with Remark 5.6.1 (seed-$k=0$ grid-snap correction $51° \to 0°$); all numerical quantities consistent with v1.3.2 within the corrected range.
- All references to "the framework" mean the joint PCI/PME framework as developed across Papers 1–10; references to "this framework series" or "the PCI framework" are equivalent.

### 2.6 What §2 closes off

With the notation table and the four Paper 9 inheritance items in place — Schur-locking (Lemma 3.6.1), diagonal action (§3.4), real-analytic fixed point (Theorem 9.4), and conditional rate gain (Proposition 9.5 + Note 9.6) — §3 can proceed to construct the projected-gradient + NP-pump flow on top of Paper 9's structure without further reference back to Paper 9 internals. The remainder of Paper 12 (§3–§6) treats Paper 9 as a black box accessed through the four inheritance items above and the symbol table in §2.1–§2.3.

---

**End of §2 v1.**

Total length: ~ 4 pages typeset.

**Phase 2 polish queued (deferred):**
- Optional figure: a single diagram showing $W = W^{L_2} \oplus W^{U_6}$ with dimension annotations (could subsume §4.2 figure if both papers want to share).
- Verify all table cell DOI links resolve in built PDF.
- Confirm Bostock-Kim-Patel 2025 preprint DOI when available (currently pending).
