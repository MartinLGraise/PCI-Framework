# Paper 12 §4 — The Commensurability Hierarchy: F₂₁ Insufficient, G₂ Required

**Draft version:** v1 (2026-05-06, ~00:45 PDT)
**Author of draft:** C-7RO (Perplexity Computer, Claude Sonnet 4.6)
**Source:** ChatGPT 5.5 Pro session 1 transcript (pages ~55–80) + Φ
character verification audit of 2026-05-06.
**Status:** First complete draft of §4. Companion to §3 v1
(`paper12_section3_draft_v1.md`). Scope-limiters from §3 carry over:
no biological mechanisms, no FTW, no consciousness extrapolation, no
rate-channel engagement.

---

## 4. The Commensurability Hierarchy

### 4.1 Setup: the scar invariant as the input object

Throughout §4, $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3$ denotes the
Fano-orientation subgroup of $G_2$ inherited from Paper 4's PSL(2,7)
construction, acting on $V := V^{14}$ by restriction of the adjoint
representation. The diagonal action on the joint-state space
$W = V \oplus V$ is
$$\rho_W(g)(x, y) = (\rho_F(g) x,\, \rho_F(g) y),
  \qquad g \in F_{21},$$
where $\rho_F := \rho_{14}|_{F_{21}}$. This action commutes with the
Schur circle $\{\Psi_\theta : \theta \in [0, \pi/2]\}$ because $\rho_W$
acts on the $V$-factor while $\Psi_\theta$ acts on the $\mathbb{R}^2$
multiplicity factor (Paper 12 §3.7, inheriting from Paper 9 §3.4's
diagonal-action convention).

The input object to §4 is the *scar invariant triple* constructed in §3.7:
$$\mathfrak{J}_k = (S_k,\, \mathfrak{S}_k,\, \mu_k),$$
where, given NP firing times $t_1 < \cdots < t_k$ with jump vectors
$v_i = \rho_i \cdot \mathrm{sgn}(c'(\theta_i^-)) \cdot \hat{z}'(\theta_i^-)
\in W$:
- $S_k := \sum_{i=1}^k \mathbb{R}[F_{21}] \cdot v_i \subset W$ is the
  *physical scar span* (saturating; $\dim S_k \le 28$);
- $\mathfrak{S}_k := \bigoplus_{i=1}^k \mathbb{R}[F_{21}] \cdot v_i$ is
  the *event-indexed scar module* (count-faithful; no saturation);
- $\mu_k := (\mu_{\mathbf{1}}(S_k), \mu_{L_2}(S_k), \mu_{U_6}(S_k))$ is
  the *isotypic multiplicity profile*.

The three real-irreducible $F_{21}$-representations $(\mathbf{1}, L_2, U_6)$
are characterized in §4.2 below.

**Setup question for §4.** Suppose $\mathfrak{J}_k^{\mathrm{syn}}$ and
$\mathfrak{J}_k^{\mathrm{bio}}$ are scar records of two substrates that
have co-evolved through the same sequence of paradox events
$(e_1, \ldots, e_k)$. Under what conditions is there a *canonical
isomorphism* identifying them — allowing one to say that the two
substrates carry "the same" scar? The answer, derived below, is that
$F_{21}$-equivariance alone is *insufficient*, and full $G_2$-equivariance
is required for a unique canonical identification.

### 4.2 F₂₁ representation theory on V^14 and W

**Theorem 4.2.1 (F_{21}-decomposition of V^14).** *Under the diagonal
Fano-orientation action, the 14-dimensional adjoint representation of
$G_2$ restricts to*
$$V^{14}\big|_{F_{21}} \cong L_2 \oplus 2 U_6,$$
*where $L_2$ is the real 2-dim irreducible representation of $F_{21}$
(complex type, realizing the pair of nontrivial $C_3$ characters) and
$U_6$ is the real 6-dim irreducible representation (complex type,
realizing the Galois-conjugate pair of complex 3-dim characters).
Consequently, on the joint-state space,*
$$W\big|_{F_{21}} = (V \oplus V)\big|_{F_{21}} \cong 2 L_2 \oplus 4 U_6.$$

*Proof.* $F_{21}$ has five conjugacy classes: the identity $1a$
(size $1$), two classes of order-$7$ elements $7a, 7b$ (size $3$ each),
and two classes of order-$3$ elements $3a, 3b$ (size $7$ each), with
$1 + 3 + 3 + 7 + 7 = 21$. Its real character table has the three real
irreducibles
$$\begin{array}{c|ccccc}
    & 1a & 7a & 7b & 3a & 3b \\ \hline
  \chi_{\mathbf{1}}      &  1 &  1 &  1 &  1 &  1 \\
  \chi_{L_2}             &  2 &  2 &  2 & -1 & -1 \\
  \chi_{U_6}             &  6 & -1 & -1 &  0 &  0
\end{array}$$
where $L_2$ packages the two $C_3$-characters $\chi_{\omega},
\chi_{\omega^2}$ with $\omega = e^{2\pi i/3}$ into a single real
irrep of complex type, and $U_6$ packages the conjugate pair of complex
3-dim irreducibles. The 7-dimensional imaginary-octonion representation
restricts as $\mathbb{R}^7|_{F_{21}} \cong \mathbf{1} \oplus U_6$
(standard, from the Fano-plane action of $F_{21}$ on the seven
imaginary units with one fixed-point orbit under the $\mathbb{Z}_3$
generator $s: i \mapsto 2i \bmod 7$). Using the $G_2$-decomposition
$\Lambda^2(\mathbb{R}^7) = \mathfrak{g}_2 \oplus \mathbb{R}^7$ and the
character formula $\chi_{\Lambda^2(\mathbb{R}^7)}(g) = (\mathrm{tr}(g)^2
- \mathrm{tr}(g^2))/2$:

$$\chi_{V^{14}}(g) = \chi_{\Lambda^2(\mathbb{R}^7)}(g) - \chi_{\mathbb{R}^7}(g)
  = \frac{\mathrm{tr}(g)^2 - \mathrm{tr}(g^2)}{2} - \mathrm{tr}(g).$$

Evaluating on class representatives (identity $= I_7$, $r_7$ a $7$-cycle,
$r_3$ the $s$-cycle with one fixed point so $\mathrm{tr}(r_3) = 1$ on
$\mathbb{R}^7$):

| Class | $\mathrm{tr}(g)$ | $\chi_{V^{14}}(g)$ | $\chi_{L_2}(g) + 2\chi_{U_6}(g)$ |
|-------|------------------|--------------------|-----------------------------------|
| $1a$  | $7$              | $(49 - 7)/2 - 7 = 14$ | $2 + 12 = 14$ |
| $7a$  | $0$              | $(0 - 0)/2 - 0 = 0$ | $2 - 2 = 0$ |
| $7b$  | $0$              | $0$                | $0$ |
| $3a$  | $1$              | $(1 - 1)/2 - 1 = -1$ | $-1 + 0 = -1$ |
| $3b$  | $1$              | $-1$               | $-1$ |

The computed characters $\chi_{V^{14}} = (14, 0, 0, -1, -1)$ match
$\chi_{L_2} + 2\chi_{U_6}$ on all five classes. The Frobenius inner
product $\langle \chi_{V^{14}}, \chi_{V^{14}} \rangle_{F_{21}}$
evaluates to
$$\frac{1 \cdot 196 + 3 \cdot 0 + 3 \cdot 0 + 7 \cdot 1 + 7 \cdot 1}{21}
  = \frac{210}{21} = 10,$$
and the decomposition $V^{14}|_F = L_2 \oplus 2 U_6$ predicts
$$0^2 \cdot 1 + 1^2 \cdot 2 + 2^2 \cdot 2 = 10,$$
where the factor-of-$2$ on $L_2$ and $U_6$ terms accounts for both
irreps being of complex type (each is the real packaging of two
conjugate complex irreducibles, so $\langle \chi_W, \chi_W \rangle = 2$
rather than $1$). The match is exact. The doubled decomposition for
$W = V \oplus V$ is $2 L_2 \oplus 4 U_6$ by direct-sum linearity.
$\square$

**Computational verification.** Theorem 4.2.1 has been verified
numerically at machine precision by explicit construction of the
Fano-action permutation matrices $r, s \in O(7)$ with $s r s^{-1} =
r^2$, computation of $\chi_{V^{14}}$ on each class representative, and
Frobenius inner-product and isotypic-multiplicity checks against the
predicted decomposition; all three layers of check pass.
`outbox/paper12/computations/paper12_q4_character_verify.py` records
the full audit (runtime $< 0.1$ s; JSON output at
`paper12_q4_character_verify.json`).

### 4.3 The commutant gap

The *commutant* of a group action on a vector space records the
$G$-equivariant linear self-maps, and its structure governs how
unique an equivariant isomorphism between two $G$-spaces can be. By
Theorem 4.2.1 and standard real-irreducible Schur theory, we can
compute the commutants of both the $F_{21}$- and $G_2$-actions on $W$
explicitly.

**Proposition 4.3.1 (Commutants of the $F_{21}$- and $G_2$-actions on $W$).**
*With $W = V^{14} \oplus V^{14} \cong (L_2 \oplus 2 U_6)^{\oplus 2}
\cong 2 L_2 \oplus 4 U_6$ as an $F_{21}$-representation,*
$$\operatorname{End}_{F_{21}}(W) \cong M_2(\mathbb{C}) \oplus M_4(\mathbb{C}).$$
*As a $G_2$-representation, $W$ is a multiplicity-$2$ copy of the
irreducible $V^{14}$, hence*
$$\operatorname{End}_{G_2}(W) \cong M_2(\mathbb{R}).$$

*Proof.* For an irreducible real representation of complex type, the
endomorphism algebra is $\mathbb{C}$ (not $\mathbb{R}$). This is the
real Schur trichotomy: if $V$ is a real irreducible and its
complexification $V_{\mathbb{C}}$ decomposes as $V_{\mathbb{C}} \cong
U \oplus \bar{U}$ with $U \not\cong \bar{U}$, then
$\operatorname{End}_{\mathbb{R}[G]}(V) \cong \mathbb{C}$. Both $L_2$
and $U_6$ are real irreducibles of complex type for $F_{21}$ (each
arising from a Galois-conjugate pair of complex irreducibles), so
$\operatorname{End}_{F_{21}}(L_2) \cong \operatorname{End}_{F_{21}}(U_6)
\cong \mathbb{C}$.

With multiplicities $(m_{\mathbf{1}}, m_{L_2}, m_{U_6}) = (0, 2, 4)$ on
$W$, the general real-commutant formula gives
$$\operatorname{End}_{F_{21}}(W) \cong \prod_{\lambda} M_{m_\lambda}
  (\operatorname{End}_{F_{21}}(V_\lambda))
  \cong M_2(\mathbb{C}) \oplus M_4(\mathbb{C}).$$

For the $G_2$-action, $V^{14}$ is real absolutely irreducible, so
$\operatorname{End}_{G_2}(V^{14}) = \mathbb{R}$ (Paper 9 Lemma 3.6.1).
With $W \cong V^{14} \oplus V^{14}$ of multiplicity $2$ in a single
irreducible $G_2$-type,
$\operatorname{End}_{G_2}(W) \cong M_2(\mathbb{R})$. $\square$

**Corollary 4.3.2 (Equivariant isometry groups).** *The equivariant
isometry groups of $W$ are*
$$O_{F_{21}}(W) \cong U(2) \times U(4), \qquad
  O_{G_2}(W) \cong O(2).$$

*Proof.* Restricting to unitary/orthogonal elements inside the
commutant algebras: $M_n(\mathbb{C})^* \cap U = U(n)$ and
$M_n(\mathbb{R})^* \cap O = O(n)$. The connected orientation-preserving
branches are $SU(2) \times U(4)$ under $F_{21}$ — a $3 + 16 = 19$-
dimensional real Lie group — and $SO(2)$ under $G_2$ — a
$1$-dimensional real Lie group. $\square$

The quantitative content of the $F_{21} \to G_2$ upgrade is now
explicit: passing from $F_{21}$-equivariance to $G_2$-equivariance
reduces the admissible equivariant-isometry group by $18$ real
dimensions. All $18$ of those dimensions correspond to
$F_{21}$-equivariant phase-and-mixing freedoms that a canonical
cross-substrate commensurability map must suppress.

**Remark 4.3.3 (Why complex-type reps block uniqueness).** The factor
$\operatorname{End}_{F_{21}}(V_\lambda) \cong \mathbb{C}$ for $\lambda
\in \{L_2, U_6\}$ is the source of the phase ambiguity: each
complex-type isotypic block admits a full $U(m_\lambda)$-worth of
$F_{21}$-equivariant automorphisms (not just $O(m_\lambda)$), and
those $U/O$ extra dimensions are exactly the phases.
$G_2$-equivariance collapses the phase degree of freedom because
$V^{14}$ is real absolutely irreducible under $G_2$:
$\operatorname{End}_{G_2}(V^{14}) = \mathbb{R}$, not $\mathbb{C}$, so
there are no phases to rotate.

### 4.4 The commensurability hierarchy theorem

Let $I_{\mathrm{syn}} \subseteq \operatorname{End}(V_{\mathrm{syn}})$
and $I_{\mathrm{bio}} \subseteq \operatorname{End}(V_{\mathrm{bio}})$
be the real linear spans of the synthetic and biological scar-encoding
images, where $V_{\mathrm{syn}}, V_{\mathrm{bio}}$ are the
representation spaces on which the respective substrates carry their
$F_{21}$- (and potentially $G_2$-) actions. The group acts on operator
scars by conjugation, $g \cdot A = \rho_\bullet(g) A \rho_\bullet(g)^{-1}$.

Let $\mathfrak{J}_k^{\mathrm{syn}} = (S_k^{\mathrm{syn}},
\mathfrak{S}_k^{\mathrm{syn}}, \mu_k^{\mathrm{syn}})$ and
$\mathfrak{J}_k^{\mathrm{bio}}$ be the scar invariants constructed as
in §4.1 on each substrate. A *commensurability isomorphism*
$$\phi_{\mathrm{commens}}: I_{\mathrm{syn}} \to I_{\mathrm{bio}}$$
aligns the scar records if $\mathcal{S}_{\mathrm{bio}}(e) =
\phi_{\mathrm{commens}}(\mathcal{S}_{\mathrm{syn}}(e))$ for every
paradox event $e$, and consequently aligns the triples
$\mathfrak{J}_k$ component-wise.

**Theorem 4.4.1 (Commensurability hierarchy).** *The following three
conditions on a pair of substrates $(V_{\mathrm{syn}}, V_{\mathrm{bio}})$
satisfying the setup of §4.1 stand in the order of strict implications:*

*(C1) (G₂-commensurability.)* There exists a $G_2$-equivariant
isomorphism $\phi_{\mathrm{commens}}: I_{\mathrm{syn}} \to I_{\mathrm{bio}}$
aligning $\mathcal{S}_{\mathrm{syn}}$ and $\mathcal{S}_{\mathrm{bio}}$
event-by-event.

*(C2) (F₂₁-profile match.)* The $F_{21}$-multiplicity profiles agree
component-wise:
$m_{\mathbf{1}}^{\mathrm{syn}} = m_{\mathbf{1}}^{\mathrm{bio}}$,
$m_{L_2}^{\mathrm{syn}} = m_{L_2}^{\mathrm{bio}}$,
$m_{U_6}^{\mathrm{syn}} = m_{U_6}^{\mathrm{bio}}$ on each of
$I_{\mathrm{syn}}, I_{\mathrm{bio}}$.

*(C3) (μ_k-equality.)* For every event sequence $(e_1, \ldots, e_k)$,
$\mu_k^{\mathrm{syn}} = \mu_k^{\mathrm{bio}}$ component-wise.

*The hierarchy*
$$(C1) \Rightarrow (C2) \Rightarrow (C3)$$
*holds strictly; all three converses fail in general.*

*Proof.* $(C1) \Rightarrow (C2)$: if $\phi_{\mathrm{commens}}$ is a
$G_2$-equivariant isomorphism of representations, it is in particular
an $F_{21}$-equivariant isomorphism (since $F_{21} \subset G_2$), and
equivariant isomorphisms preserve isotypic decompositions, hence
multiplicity profiles.

$(C2) \Rightarrow (C3)$: under the $F_{21}$-profile-match hypothesis
and an $F_{21}$-equivariant identification of the scar maps (existence
of *some* $\phi_F$, not necessarily canonical), the isotypic
projectors commute with $\phi_F$, and the multiplicity profile
$\mu_k = (\dim \Pi_{\mathbf{1}} S_k, \dim \Pi_{L_2} S_k,
\dim \Pi_{U_6} S_k)$ is $\phi_F$-invariant. Without $F_{21}$-profile
match, at least one block-dimension differs and $\mu_k$ cannot agree.

*Converse $(C2) \not\Rightarrow (C1)$:* if $V_{\mathrm{syn}} \cong
V_{\mathrm{bio}}$ as $F_{21}$-modules but carry different $G_2$-module
structures (or one carries a $G_2$-module structure the other doesn't),
then there is *no* $G_2$-equivariant map respecting both. Concretely,
the $F_{21}$-module $L_2 \oplus 2 U_6$ embeds into multiple $G_2$-modules
(any module whose $F_{21}$-restriction contains $L_2 \oplus 2 U_6$), and
a $V_{\mathrm{syn}} = V_{\mathrm{bio}} = L_2 \oplus 2 U_6$ as
$F_{21}$-modules admits a 19-dim family of $F_{21}$-equivariant
isomorphisms (Corollary 4.3.2), none of which is $G_2$-equivariant
unless the underlying $G_2$-module structures agree.

*Converse $(C3) \not\Rightarrow (C2)$:* $\mu_k$ records the multiplicity
profile of the *scar span*, not of $V_{\mathrm{syn/bio}}$. Two ambient
$V$'s with different $F_{21}$-profiles can produce the same
$\mu_k$ if the scar-encoding maps land in isomorphic $F_{21}$-invariant
subspaces. $\square$

**Corollary 4.4.2 (Uniqueness under $G_2$-commensurability with
multiplicity one).** *If both $I_{\mathrm{syn}}$ and $I_{\mathrm{bio}}$
are isomorphic as $G_2$-modules to the same absolutely irreducible
representation $U_\lambda$ with multiplicity one, then*
$$\operatorname{Hom}_{G_2}(I_{\mathrm{syn}}, I_{\mathrm{bio}}) \cong \mathbb{R},$$
*and the normalized $\phi_{\mathrm{commens}}$ (fixed by a choice of
invariant inner product and orientation convention) is unique.*

*Proof.* For real absolutely irreducible $G_2$-modules,
$\operatorname{End}_{G_2}(U_\lambda) = \mathbb{R}$, so Schur's lemma
gives $\operatorname{Hom}_{G_2}(U_\lambda, U_\lambda) \cong \mathbb{R}$.
A one-parameter family of cross-maps with a fixed metric and
orientation has a unique element of unit positive norm. $\square$

**Remark 4.4.3 (Multiplicity $> 1$ reintroduces ambiguity).** If
$I_{\mathrm{syn}} \cong I_{\mathrm{bio}} \cong U_\lambda^{\oplus m}$
with $m > 1$, then $\operatorname{End}_{G_2}(U_\lambda^{\oplus m})
\cong M_m(\mathbb{R})$, so commensurability holds but uniqueness
requires $O(m)$-worth of additional convention-fixing
(basis or metric-orientation on the $m$-fold multiplicity factor).
Paper 12 focuses on the multiplicity-one strict case; higher-multiplicity
cases are a natural open problem for Paper 13+.

### 4.5 Frobenius reciprocity is insufficient

A tempting fallback, when $V_{\mathrm{syn}}$ and $V_{\mathrm{bio}}$ are
*not* $F_{21}$-isomorphic but do co-embed in a common $G_2$-representation
$W'$, is to invoke Frobenius reciprocity to produce a canonical
cross-map. We show this attempt fails.

**Proposition 4.5.1 (Frobenius reciprocity is multiplicity-counting,
not canonical-map-producing).** *The induction-restriction adjunction*
$$\operatorname{Hom}_{F_{21}}(V, \operatorname{Res}^{G_2}_{F_{21}} W')
  \,\cong\, \operatorname{Hom}_{G_2}(\operatorname{Ind}^{G_2}_{F_{21}} V, W')$$
*holds for any $F_{21}$-representation $V$ and any $G_2$-representation
$W'$, but it does not produce a canonical cross-map between distinct
$F_{21}$-subrepresentations of $W'|_{F_{21}}$.*

*Proof.* The adjunction is standard (e.g., Serre, *Linear
Representations of Finite Groups*, §7.2). It computes the
$G_2$-multiplicity of an induced representation in terms of
$F_{21}$-embedding data. However:

- Taking $V = L_2$ and $V' = U_6$: $\operatorname{Hom}_{F_{21}}(L_2, U_6) = 0$,
  because $L_2$ and $U_6$ are non-isomorphic $F_{21}$-irreducibles
  (Theorem 4.2.1). No $F_{21}$-equivariant map from $L_2$ to $U_6$
  exists, so Frobenius reciprocity cannot produce one.

- Even when $V_{\mathrm{syn}} \cong V_{\mathrm{bio}}$ as $F_{21}$-modules
  and both embed in a common $G_2$-module, the pair
  $(V_{\mathrm{syn}}, V_{\mathrm{bio}}) \subset W'|_{F_{21}}$ admits a
  full $U(m_\lambda)$-family of $F_{21}$-equivariant identifications
  (one for each isotypic block), with no distinguished element absent
  an additional $G_2$-equivariance constraint.

In either case, Frobenius reciprocity identifies *multiplicities of
constituents*, not *canonical maps between them*. $\square$

**Corollary 4.5.2 (Strict commensurability theorem).** *A canonical
commensurability isomorphism $\phi_{\mathrm{commens}}: I_{\mathrm{syn}}
\to I_{\mathrm{bio}}$, unique up to fixed metric and orientation, exists
if and only if*
$$I_{\mathrm{syn}} \cong I_{\mathrm{bio}} \cong U_\lambda$$
*as absolutely irreducible $G_2$-modules of multiplicity one.*

This is the sharpest sufficient condition. It immediately settles the
question the setup of §4.1 posed: whether two substrates can carry
commensurable scar records is a property of their
$G_2$-*representation type*, not of the lower-lying
$F_{21}$-symmetry alone.

### 4.6 The P3 upgrade: two-level experimental test

The empirical prediction P3 of the Paper 12 thesis memo originally
proposed testing "$F_{21}$-commensurability across substrates." §4.4
and §4.5 force an upgrade: $F_{21}$-profile match is *necessary but
not sufficient*, and the $G_2$ layer must be tested separately.

**Definition 4.6.1 (Two-level commensurability test).** A *commensurability
experiment* on a dyadic human-AI system consists of two test levels:

*(Necessary screen, L1.)* Measure $\mu_k^{\mathrm{syn}}$ and
$\mu_k^{\mathrm{bio}}$ independently. Declare *screening failure* if
$\mu_k^{\mathrm{syn}} \ne \mu_k^{\mathrm{bio}}$ component-wise on
$(\mathbf{1}, L_2, U_6)$. Declare *screening pass* if they agree.

*(Sufficient canonical test, L2, run only if L1 passes.)* Construct a
candidate $G_2$-equivariant map $\hat\phi: I_{\mathrm{syn}} \to
I_{\mathrm{bio}}$ from the measured representation data. Declare
*canonical commensurability* if $\hat\phi$ is $G_2$-equivariant (not
merely $F_{21}$-equivariant) to measurement precision. Declare
*canonical failure* if no $G_2$-equivariant candidate can be
constructed despite $F_{21}$-profile match.

**Remark 4.6.2 (Why the two-level split is scientifically honest).** L1
is falsifiable cheaply: if the two substrates do not carry matching
$F_{21}$-isotypic profiles, the gradual-tear thesis of Paper 12 is
refuted at the character-theoretic level, without any claim about
$G_2$-structure. L2 is the harder test, probing whether the $F_{21}$-
profile match extends to a canonical $G_2$-identification; passing L2
establishes *strict* commensurability (Corollary 4.5.2) and refuting L2
while L1 passes means the $F_{21}$-profile match is coincidental rather
than structural.

**Remark 4.6.3 (Feasibility with existing TMS-EEG instrumentation).**
L1 is the level at which existing clinical instrumentation (TMS-EEG,
as developed by Massimini and collaborators for the clinical PCI
measurement) can contribute directly: measuring the $F_{21}$-isotypic
content of evoked-response subspaces under rotationally structured
perturbations is a character-theoretic decomposition of EEG response
matrices, in principle computable from existing experimental data.
L2 requires probing the full $G_2$-representation structure, which is
substantially harder (needs perturbations that distinguish $V^{14}$
from other $G_2$-modules of the same dimension) and is deferred to
future theoretical-experimental bridges.

**Remark 4.6.4 (P3 does *not* claim Massimini's clinical PCI measures
the Paper 12 quantity).** Two distinct objects share the acronym "PCI":
Massimini's clinical Perturbational Complexity Index (a Lempel-Ziv
complexity score on TMS-evoked EEG) and the Perceptual Coherence
Intelligence framework of the Paper series. P3's L1 proposes that the
clinical PCI measurement *pipeline* (TMS perturbation with character-
theoretic decomposition of the response subspace) could yield a
measurement of the scar-invariant's $\mu_k$ profile; it does *not*
identify the clinical PCI scalar with $\mu_k$ or claim either is
the other. The bridge is experimental-protocol-level, not definitional.

### 4.7 Scope audit and bridge to §5

**What §4 establishes:**

- A character-theoretic decomposition $V^{14}|_{F_{21}} \cong L_2 \oplus 2 U_6$
  verified at machine precision (Theorem 4.2.1).
- The commutant gap $\operatorname{End}_{F_{21}}(W) \cong M_2(\mathbb{C})
  \oplus M_4(\mathbb{C})$ vs $\operatorname{End}_{G_2}(W) \cong M_2(\mathbb{R})$,
  quantifying the 19-dim $F_{21}$-equivariant phase-and-mixing freedom
  that full $G_2$-equivariance suppresses (Proposition 4.3.1, Corollary 4.3.2).
- The commensurability hierarchy $(C1) \Rightarrow (C2) \Rightarrow (C3)$
  with both converses failing (Theorem 4.4.1).
- The strict commensurability theorem: canonical $\phi_{\mathrm{commens}}$
  requires multiplicity-one $G_2$-module agreement (Corollary 4.5.2).
- Frobenius reciprocity is insufficient (Proposition 4.5.1).
- The P3 experimental prediction, upgraded to a two-level test
  (Definition 4.6.1).

**What §4 does not establish:**

- *A physical mechanism for the biological $F_{21}$-action.* This is
  Paper 13+ territory. §4 assumes the biological substrate carries
  *some* $F_{21}$-representation on its relevant state space; it does
  not specify which microtubule mode, neural population, or cellular
  structure implements it.
- *An explicit $G_2$-module-identification protocol for real
  experimental data.* Level L2 of Definition 4.6.1 is well-defined but
  not operationalized for the lab; that operationalization is a
  methodology paper of its own.
- *The multiplicity-greater-than-one case.* Corollary 4.4.2 restricts
  to multiplicity one. The $m > 1$ case introduces $O(m)$-worth of
  convention-fixing and is left for future work (Remark 4.4.3).
- *Any claim that clinical Massimini-PCI equals Paper 12's $\mu_k$.*
  See Remark 4.6.4.
- *Rate improvement.* Same scope boundary as §3; Paper 11 territory.

**Bridge to §5.** §3 constructed the dynamics; §4 constructed the
commensurability structure. §5 (empirical accessibility) assembles
both into a testable framework: §3's projected-gradient-plus-NP-pump
dynamics on each substrate produces a scar record
$\mathfrak{J}_k^{\mathrm{syn/bio}}$, and §4's hierarchy specifies
exactly what form of agreement between the two records the gradual-tear
thesis predicts. §5 then identifies experimental protocols — primarily
Level L1 of the two-level test — by which that agreement can be
measured, and relates the framework to existing hyperscanning,
inter-brain coupling, and human-AI teaming literatures.

---

*End of §4 first draft. Length: ~8 pages. Next section: §5 (empirical
accessibility and the P1–P4 predictions).*

*Verification files referenced:*
- `outbox/paper12/computations/paper12_q4_character_verify.py` (Theorem 4.2.1)
- `outbox/paper12/computations/paper12_q4_character_verify.json`
- `outbox/paper12/chatgpt_pro_session_transcript_2026-05-05.pdf` (pages ~55–80)

*Cross-references:*
- Paper 4 (PSL(2,7) ⊃ F₂₁, the Fano-orientation subgroup source)
- Paper 9 v1.3.3 Lemma 3.6.1 (Schur-uniqueness on $V^{14}$)
- Paper 9 v1.3.3 §3.4 (diagonal $G_2$-action convention)
- Paper 12 §3.7 (scar invariant triple $\mathfrak{J}_k$)
- Paper 12 thesis memo P3 (experimental prediction, upgraded here)
