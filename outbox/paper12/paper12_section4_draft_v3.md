# Paper 12 §4 — The Commensurability Hierarchy: F₂₁ Insufficient, G₂ Required (v3)

**Draft version:** v3 (2026-05-06, ~03:50 PDT)
**Author of draft:** C-7RO (Perplexity Computer, Claude Sonnet 4.6)
**Source:** Paper 12 §4 v1 + Model Council rigor pass (Opus 4.7,
Gemini 3.1 Pro, GPT-5.5).
**Revision summary (vs v2):** Phase-2 polish on Opus's v2 residuals —
RES-1 metric-choice note on Cor 4.3.2; RES-2 Rank-One Convention
named explicitly; RES-4 Fano-action prose tightened.

**Revision summary (vs v1, retained from v2):** Eight revisions. Three load-bearing:
R3 Theorem 4.4.1 (C2) reformulated as map-existence (Opus S4-1); S4-2
dimension bookkeeping fixed ($U(2) \times U(4)$ is full $20$-dim, delta
$= 19$); S4-3 Corollary 4.5.2 downgraded from biconditional to
sufficient condition. Plus five surgical fixes: S4-4 Fano-action prose,
S4-5 Prop 4.5.1 renamed and reworded, S4-6 (C2)⇏(C1) witness, S4-7
operator-vs-vector $\mu_k$ translation, S4-8 orientation $\pm 1$
ambiguity acknowledged. Plus four polish items from Gemini and GPT-5.5:
Pillar-status signpost, $F_{21}$-source paragraph (Paper 4 inheritance),
§4.7 measurement-vs-instrument tightening, and seven standard citations.

**Pillar-delivery signpost (per GPT-5.5 council finding):** §4 delivers
the *mathematical core* of Pillar 2 (dual-substrate residue) by
constructing the commensurability hierarchy, but *does not* establish
the existence or physical realization of the biological-substrate
$F_{21}$-content (Paper 13+ territory). §4 also delivers the
mathematical core of the audit-substrate component of Pillar 3 (via
the $F_{21}$-isotypic profile $\mu_k$ being the substrate-independent
audit signature). Pillar 1 is delivered by §3; Pillar 4 is §1/§5.

---

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
so $\operatorname{End}_{G_2}(V^{14}) \cong \mathbb{R}$, and $W \cong V^{14
\oplus 2}$ gives $\operatorname{End}_{G_2}(W) \cong M_2(\mathbb{R})$.
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

**Theorem 4.4.1 (Commensurability hierarchy, v2 reformulation).** *The
following three conditions on a pair of substrates $(V_{\mathrm{syn}},
V_{\mathrm{bio}})$ stand in the order of strict implications:*

*(C1) (G₂-commensurability.)* There exists a $G_2$-equivariant
isomorphism $\phi: I_{\mathrm{syn}} \to I_{\mathrm{bio}}$ aligning
$\mathcal{S}_{\mathrm{syn}}$ and $\mathcal{S}_{\mathrm{bio}}$ event-by-event:
$\mathcal{S}_{\mathrm{bio}}(e) = \phi(\mathcal{S}_{\mathrm{syn}}(e))$
for every paradox event $e$.

*(C2) (F₂₁-equivariant isomorphism, map-existence form.)* There exists
an $F_{21}$-equivariant isomorphism $\phi_F: I_{\mathrm{syn}} \to
I_{\mathrm{bio}}$ aligning $\mathcal{S}_{\mathrm{syn}}$ and
$\mathcal{S}_{\mathrm{bio}}$ event-by-event.

*(C3) ($\mu_k$-equality.)* For every event sequence $(e_1, \ldots,
e_k)$, $\mu_k^{\mathrm{syn}} = \mu_k^{\mathrm{bio}}$ component-wise on
the three real $F_{21}$-isotypic blocks.

*The hierarchy*
$$(C1) \Rightarrow (C2) \Rightarrow (C3)$$
*holds strictly; both converses fail in general.*

*Proof.* $(C1) \Rightarrow (C2)$: a $G_2$-equivariant isomorphism is
in particular $F_{21}$-equivariant (since $F_{21} \subset G_2$).

$(C2) \Rightarrow (C3)$: if $\phi_F$ aligns $\mathcal{S}_{\mathrm{syn}}$
and $\mathcal{S}_{\mathrm{bio}}$ event-by-event and is $F_{21}$-equivariant,
then it commutes with the isotypic projectors $\Pi_\tau$ (i.e.,
$\phi_F \Pi_\tau^{\mathrm{syn}} = \Pi_\tau^{\mathrm{bio}} \phi_F$). The
multiplicity profiles $\mu_k = (\dim \Pi_{\mathbf{1}} S_k, \dim \Pi_{L_2}
S_k, \dim \Pi_{U_6} S_k)$ on the cumulative scar spans transfer
component-wise, since $\phi_F$ maps $S_k^{\mathrm{syn}}$ isomorphically
onto $S_k^{\mathrm{bio}}$.

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

[CP] M. Costa, M. Pavone, *On the Frobenius group of order 21*, used as a primary reference for the order-21 Frobenius group's character theory and Fano-orientation realization.

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

*Revision log:*
- v2 (2026-05-06 ~02:00 PDT): Council rigor pass applied. R3 Theorem
  4.4.1 (C2) reformulated as map-existence (Opus S4-1). S4-2 dimension
  bookkeeping fixed: $U(2) \times U(4)$ is full $20$-dim, delta = $19$.
  S4-3 Cor 4.5.2 downgraded biconditional → sufficient condition (Remark
  4.5.3 acknowledges open necessity). S4-4 Fano-action prose corrected
  (action on Fano plane points, fixed $s$-line gives $\mathrm{tr} = 1$).
  S4-5 Prop 4.5.1 renamed and reworded (Frobenius reciprocity does not
  *select* cross-substrate maps). S4-6 (C2)⇏(C1) explicit witness
  added. S4-7 operator-vs-vector $\mu_k$ translation specified
  (rank-one projector convention). S4-8 $\pm 1$ orientation ambiguity
  acknowledged in Cor 4.4.2. Paper 4 inheritance paragraph added in
  §4.1. §4.7 measurement-vs-instrument language tightened. Pillar
  signpost added at top.
- v1 (2026-05-06 ~01:00 PDT): First complete draft.
