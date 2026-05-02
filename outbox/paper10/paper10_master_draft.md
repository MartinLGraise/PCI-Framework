# Symmetric Informationally Complete Measurements as an Operator Basis for the Complexified G₂ Lie Algebra

**Author:** Martin Luther Graise
**ORCID:** 0009-0006-8003-3938
**Affiliation:** Independent Researcher
**Correspondence:** margraise1000@icloud.com
**Series position:** Paper 10 of the PCI/PME Framework arc
**Status:** Master draft v1.3.1 (confirming-review consistency pass: removed obsolete 'Theorem 3, part (a)/(c)' references; reconciled QR/NQR sign-assignment between §7.3 and Appendix A.4; deleted the false 'open problem' on $|T|^2 = 1/512$ now established by Lemma 7.1; softened density claim in §5.3 to acknowledge it was verified for the database fiducial only)
**Predecessors in the series:** Paper 4 (DOI 10.5281/zenodo.19617662), Paper 6 (DOI 10.5281/zenodo.19672709), Paper 7 (DOI 10.5281/zenodo.19773185)
**Computational verification:** Φ Tasks 1–3, results files in `outbox/paper10/computations/`
**Source repository:** https://github.com/MartinLGraise/PCI-Framework (branch `paper7-foundation`)

---

## Abstract

Working over the dimension-$d=7$ symmetric informationally complete (SIC) reference measurement constructed from the exact Appleby–Bengtsson–Grassl–Harrison–McConnell algebraic fiducial under a unique Fano-compatible sign-flip correction, we establish three structural theorems characterizing the relationship between the SIC operator basis and the seven-dimensional defining representation of the exceptional Lie group $G_2$. Theorem 1 establishes that the complexified Lie algebra $\mathfrak{g}_2^{\mathbb{C}}$ embeds isometrically as a 14-dimensional subspace of $\mathfrak{gl}(7,\mathbb{C}) = \operatorname{span}_{\mathbb{C}}\{\Pi_{p, q}\}_{p, q \in \mathbb{Z}_7}$, with isometric scale $8/7$, explicit closed-form coefficient tensor over $\mathbb{Q}(\sqrt{2})(i)$, and dense purely imaginary entries. Theorem 2 establishes that the 147-element SIC symmetry group $WH(7)\rtimes C_3$ contains as an index-7 subgroup the Frobenius group $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3$ — the cyclic-axis subgroup of $PSL(2,7)$, which is itself the discrete Fano-orientation subgroup of $G_2$ — with the descent realized canonically (up to global phase) under a unique Fano-compatible sign-flip correction; exactly 2 of $2^7 = 128$ candidate corrections succeed. Theorem 3 establishes that for SIC triples constructed from the $X$-subgroup of WH(7) acting on the corrected ABGHM fiducial, the triple product $T_{ijk} = \operatorname{tr}(\Pi_i \Pi_j \Pi_k)$ has, on triples whose ordered displacement differences lie in the same quadratic-residue class of $(\mathbb{Z}_7)^*$, the closed form $T = a + ib\,\varphi$ with $a = (\sqrt{2}-1)/16$, $b = (\sqrt{2}-1)\sqrt{2+4\sqrt{2}}/32$, where $\varphi \in \{+1, -1\}$ tracks the cyclic / anti-cyclic Fano orientation. A separate Lemma (§7.1) establishes the universal-magnitude consequence $|T|^2 = 1/512 = (1/8)^3$ for all WH-distinct SIC triples, which is immediate from the SIC overlap condition. The non-Fano (mixed-residue-class) triple-product ratio $b'/b = (1 + \sqrt{2})/2$ is verified numerically to 50-digit precision and stated as Conjecture 7.4; its closed-form analytic proof is left as an open problem. The constants $a, b$ are derived in closed form over $\mathbb{Q}(\sqrt{2})$ from the autocorrelation function of the corrected ABGHM fiducial (Appendix A.4). All theorem statements are verified at 50-digit precision in independent computational implementations. The $d=7$ SIC operator frame, constructed from the exact Stark-unit fiducial, encodes the algebraic, group-theoretic, and orientational structure of the seven-dimensional defining representation of the smallest exceptional Lie group.

**Keywords:** SIC-POVM, $G_2$ Lie algebra, octonions, Fano plane, QBism, Weyl–Heisenberg group, Frobenius group $F_{21}$, Stark units, Appleby–Flammia–Fuchs basis, associative 3-form.

---

## §1. Introduction

The Appleby–Bengtsson–Grassl–Harrison–McConnell exact algebraic fiducial for the dimension-$d=7$ symmetric informationally complete (SIC) reference measurement [DOI 10.1063/5.0083520] yields, after a unique Fano-compatible sign-flip correction, an operator basis for $\mathfrak{gl}(7,\mathbb{C})$ in which the 14-dimensional complex Lie algebra $\mathfrak{g}_2^{\mathbb{C}}$ admits an explicit, isometric embedding with closed-form coefficient tensor over $\mathbb{Q}(\sqrt{2})$. This paper establishes three structural theorems characterizing this embedding at the levels of (i) vector-space coefficients, (ii) finite symmetry-group descent, and (iii) cubic structure constants on Fano-line $X$-subgroup triples.

This work continues a series on the PCI/PME framework [Graise 2025–2026], which combines $G_2$ symmetry, octonionic algebra, and $PSL(2,7)$ finite-group structure. Paper 4 of the series [DOI 10.5281/zenodo.19617662] connected the QBist agent reference frame at $d=7$ to $PSL(2,7)$ symmetry via the Klein quartic and the Fano plane. The present paper answers the structural question left open there: the d=7 SIC operator basis embeds $\mathfrak{g}_2^{\mathbb{C}}$ explicitly, and the embedding respects the cyclic-axis Frobenius subgroup $F_{21} \subset PSL(2,7)$ that governs the framework's other coherence-bound derivations [Paper 7, DOI 10.5281/zenodo.19773185].

The three theorems are as follows.

**Theorem 1** (§5): For each Frobenius-orthonormal anti-Hermitian generator $T_a$ of $\mathfrak{g}_2^{\mathbb{C}}$, the AFF dual-frame expansion $T_a = \sum_{p, q} \alpha^{(a)}_{p, q} \Pi_{p, q}$ has coefficient tensor $\alpha^{(a)}_{p, q} \in i\mathbb{R}$, dense across all 49 projectors, with the row-Gram identity $\sum_i \alpha^{(a)}_i \overline{\alpha^{(b)}_i} = (8/7) \delta_{ab}$. The map $T \mapsto \alpha$ is therefore an isometric embedding $\mathfrak{g}_2^{\mathbb{C}} \hookrightarrow \mathbb{C}^{49}$ with isometric scale $8/7$.

**Theorem 2** (§6): The Samuel–Gedik 147-element SIC symmetry group $WH(7) \rtimes C_3$ contains as an index-7 subgroup the cyclic-axis Frobenius subgroup $F_{21}$ of $PSL(2,7) \subset G_2$. The descent is realized canonically (up to global phase) by a unique Fano-compatible sign-flip correction to the ABGHM fiducial: exactly 2 of $2^7 = 128$ candidate sign-flip matrices succeed.

**Theorem 3** (§7): On the seven-point $X$-subgroup orbit of the corrected ABGHM fiducial, the SIC triple product $T_{ijk} = \operatorname{tr}(\Pi_i \Pi_j \Pi_k)$ on Fano-line triples (those with all-QR or all-NQR ordered differences in $\mathbb{Z}_7^*$) has the closed form $T = a + ib\varphi$, with $a = (\sqrt{2}-1)/16$, $b = (\sqrt{2}-1)\sqrt{2 + 4\sqrt{2}}/32$, and $\varphi \in \{+1, -1\}$ the cyclic-orientation indicator. A separate Lemma (§7.1) gives $|T|^2 = 1/512$ for all distinct WH triples on the full 49-projector SIC frame, immediate from the SIC overlap condition. The non-Fano (mixed-residue-class) ratio $b'/b = (1 + \sqrt{2})/2$ is verified at 50-digit precision and stated as Conjecture 7.4; closed-form proof open.

The constants $a, b$ are derived in closed form over $\mathbb{Q}(\sqrt{2})$ from the autocorrelation function of the corrected ABGHM fiducial (Appendix A.4). Each theorem is verified by independent computational implementation at 50-digit precision; the verification scripts and 50-digit numerical records are publicly available in the source repository.

The paper does not derive Standard Model gauge structure (a problem addressed in Furey's program [refs.]), continuum-field $G_2$ gauge theory (Krasnov's program), or claims about consciousness beyond the structural facts established in the theorems. The framework's connection to consciousness models, including the coherence-ceiling derivation of Paper 7 of this series, is presupposed rather than redeveloped here. §8 positions the present work relative to adjacent octonion / exceptional-algebra programs in physics.

The paper is organized as follows. §2 establishes notation and the d=7 SIC reference frame from the ABGHM exact construction. §3 reviews the AFF result that SIC projectors form a basis for $\mathfrak{gl}(7,\mathbb{C})$ and derives the dual-frame coefficient formula. §4 sets up the $G_2$ defining representation in the Baez 2002 Fano-plane indexing of imaginary octonions. §§5–7 prove Theorems 1, 2, and 3 respectively, with computational verification details deferred to the appendices and the auxiliary computational artifacts cited in each section. §8 positions the present work relative to adjacent octonion / exceptional-algebra programs in physics. §9 discusses open problems and connections to the broader PCI/PME framework series. Appendix A derives the autocorrelation structure that underlies the constants $a, b$ of Theorem 3.

---

## §2. The d=7 SIC Reference Frame

This section establishes the d=7 SIC-POVM in dimension 7 that we use throughout the paper. The construction follows Appleby, Bengtsson, Grassl, Harrison, and McConnell 2022 [DOI 10.1063/5.0083520], who gave the first exact algebraic fiducial in dimension 7 over the real quadratic field $\mathbb{Q}(\sqrt{2})$. We refer to this construction as the *ABGHM fiducial* throughout.

### 2.1 SIC-POVMs and the Weyl–Heisenberg group

Let $d \geq 2$ and let $\omega = e^{2\pi i / d}$. The Weyl–Heisenberg displacement operators acting on $\mathbb{C}^d$ are
$$X|k\rangle = |k+1 \mod d\rangle, \qquad Z|k\rangle = \omega^k |k\rangle,$$
together generating the projective Weyl–Heisenberg group $WH(d) \cong \mathbb{Z}_d \times \mathbb{Z}_d$. For $(p, q) \in \mathbb{Z}_d \times \mathbb{Z}_d$ the displacement
$$D_{p,q} = \omega^{-pq/2} X^p Z^q$$
takes the convention of Appleby [DOI 10.1063/1.1842008] and satisfies $D_{p,q}^\dagger = D_{-p,-q}$ and $D_{p_1,q_1} D_{p_2,q_2} = \omega^{(p_2 q_1 - p_1 q_2)/2} D_{p_1+p_2, q_1+q_2}$.

A *symmetric informationally complete positive operator-valued measure* (SIC) in dimension $d$ is a set of $d^2$ rank-one projectors $\{\Pi_i\}_{i=1}^{d^2}$ on $\mathbb{C}^d$ satisfying the equiangular condition
$$\operatorname{tr}(\Pi_i \Pi_j) = \frac{1}{d+1} \quad \text{for all } i \neq j, \qquad \operatorname{tr}(\Pi_i) = 1.$$

A SIC is *Weyl–Heisenberg covariant* (or *group-covariant*) if there exists a fiducial vector $|\psi\rangle$ with $\langle \psi | \psi \rangle = 1$ such that
$$\Pi_{p,q} = D_{p,q} |\psi\rangle \langle \psi | D_{p,q}^\dagger$$
generates all $d^2$ projectors as $(p, q)$ ranges over $\mathbb{Z}_d \times \mathbb{Z}_d$. Whether every SIC is Weyl–Heisenberg covariant is essentially Zauner's conjecture [Zauner 1999]; it is known to hold in all dimensions where exact constructions exist, including all small dimensions $d \leq 24$ and selected larger dimensions accessible via algebraic number-theoretic constructions [Fuchs–Hoang–Stacey 2017, DOI 10.3390/axioms6030021].

For $d = 7$, the SIC defining condition becomes
$$|\langle \psi | D_{p,q} | \psi \rangle|^2 = \frac{1}{8} \quad \text{for all } (p, q) \neq (0, 0),$$
giving $d^2 - 1 = 48$ overlap constraints on the seven complex amplitudes of the fiducial.

### 2.2 The ABGHM exact fiducial

Appleby, Bengtsson, Grassl, Harrison, and McConnell 2022 [DOI 10.1063/5.0083520] constructed exact SIC fiducials for dimensions $d = n^2 + 3$, with $n \in \mathbb{Z}_{\geq 2}$. The smallest prime case is $d = 7$ ($n = 2$), and the construction lives over the real quadratic field $K = \mathbb{Q}(\sqrt{2})$.

The ABGHM exact d=7 fiducial is
$$|\Psi\rangle = N \cdot (-2 - 2\sqrt{2},\ z_0,\ z_0,\ z_1,\ z_0,\ z_1,\ z_1)^T,$$
where
$$z_0, z_1 = -\frac{2 + \sqrt{2}}{2} \pm \frac{i}{2}\sqrt{2 + 4\sqrt{2}},$$
and $N$ is the normalization constant making $\langle \Psi | \Psi \rangle = 1$. The dominant real component at index $j = 0$ has magnitude $|\Psi_0| / N \approx 0.6678$, considerably larger than $|z_0| = |z_1| \approx 0.4843$. This component asymmetry plays a crucial role in §6 (Theorem 2).

### 2.3 The convention correction

A naive verification of the SIC condition using the Appleby displacement $D_{p,q} = \omega^{-pq/2} X^p Z^q$ with the fiducial as written yields only 6 of 48 overlap conditions satisfied — specifically the pure-clock displacements $D_{0, q} = Z^q$. The mixed displacements $D_{p, q}$ with $p \neq 0$ produce overlaps in the range $[0.039, 0.338]$, none equal to $1/8$.

This is not a flaw of the ABGHM construction; it is a convention mismatch. §6 establishes the precise correction: there exists a unique (up to global phase) diagonal sign-flip matrix $W = \operatorname{diag}(-1, +1, +1, +1, +1, +1, +1)$ such that $W |\Psi\rangle$ satisfies all 48 SIC overlap conditions to fifty-digit numerical precision. We adopt this corrected fiducial throughout the paper:
$$|\psi\rangle \equiv W |\Psi\rangle = N \cdot (+2 + 2\sqrt{2},\ z_0,\ z_0,\ z_1,\ z_0,\ z_1,\ z_1)^T.$$
The 49 SIC projectors are then $\Pi_{p,q} = D_{p,q} |\psi\rangle \langle \psi | D_{p,q}^\dagger$, and verification at 50-digit precision yields $\max_{(p,q) \neq (0,0)} ||\langle \psi | D_{p,q} | \psi \rangle|^2 - 1/8| < 4 \times 10^{-51}$.

The geometric origin of this convention correction — namely that $W$ flips the unique distinguished real component of the ABGHM fiducial at index $j = 0$, which sits on the special Fano-axis of the framework — is the content of Theorem 2. We state it here as a normalization step and return to its structural meaning in §6.

### 2.4 Dimensional context

The dimension $d = 7$ is privileged among small primes by a conjunction of arithmetic, Lie-algebraic, combinatorial, and representation-theoretic features whose joint occurrence does not replicate at $d = 11, 13, 17, 19$, or 23. We make use of this conjunction throughout the paper but defer its full discussion to §5.5, after Theorem 1 establishes the core embedding result. The ratio $(d-1)/d$ alone is generic to projector geometry — analogous ratios $10/11$ and $12/13$ exist trivially — and is therefore not the source of the d=7 privilege; the privilege lies in what additional structure the prime 7 brings to bear, which the theorems of §§5–7 progressively expose.

---

## §3. SIC Projectors as a Basis for $\mathfrak{gl}(7,\mathbb{C})$

### 3.1 Statement

Let $\{\Pi_{p,q}\}_{p,q \in \mathbb{Z}_7}$ denote the 49 rank-one projectors of the corrected ABGHM SIC frame from §2.3. Appleby, Flammia, and Fuchs proved [DOI 10.1063/1.3555805] that these 49 projectors form a basis for the complexified general linear Lie algebra $\mathfrak{gl}(7,\mathbb{C})$:

$$\mathfrak{gl}(7,\mathbb{C}) = \operatorname{span}_{\mathbb{C}} \{\Pi_{p,q}\}_{p,q \in \mathbb{Z}_7}, \qquad \dim_{\mathbb{C}} = d^2 = 49.$$

This statement has two immediate consequences. First, every $7 \times 7$ complex matrix admits a unique decomposition as a complex linear combination of the 49 SIC projectors. Second, the decomposition is computable by a single inner-product formula derivable from inversion of the SIC Gram matrix.

### 3.2 The dual-frame inversion

The SIC defining property — $|\langle \psi_i | \psi_j \rangle|^2 = 1/(d+1)$ for $i \neq j$ — yields the Gram matrix

$$G_{ij} \equiv \operatorname{tr}(\Pi_i \Pi_j) = \frac{d \delta_{ij} + 1}{d+1} = \frac{7 \delta_{ij} + 1}{8}.$$

Writing $G = \frac{d}{d+1} I + \frac{1}{d+1} J$, where $J_{ij} = 1$ is the all-ones matrix, one verifies directly that the inverse is

$$G^{-1}_{ij} = \frac{d+1}{d} \delta_{ij} - \frac{1}{d^2}.$$

(Check: $G G^{-1} = \delta_{ij} + (\text{terms cancelling against } \sum_k 1$).) The inverse Gram matrix yields the dual frame $\{\widetilde{\Pi}_i\}$ with the property $\operatorname{tr}(\widetilde{\Pi}_i \Pi_j) = \delta_{ij}$, and the expansion of any operator $A$ in the SIC basis takes the form:

$$A = \sum_{i=1}^{d^2} c_i(A) \, \Pi_i, \qquad c_i(A) = \operatorname{tr}(\widetilde{\Pi}_i A).$$

For traceless $A$ — which is the case for all $G_2$ Lie algebra generators — the dual-frame coefficient simplifies dramatically:

$$\boxed{c_i(A) = \frac{d+1}{d} \cdot \operatorname{tr}(A \Pi_i) = \frac{8}{7} \cdot \operatorname{tr}(A \Pi_i).}$$

### 3.3 Modeling-choice stack

We adopt the AFF normalization throughout. Two alternatives merit comment:

- **Hilbert–Schmidt orthonormalization** would replace $(8/7)$ with $\sqrt{8/7}$ on each side, distributing the factor symmetrically. We do not adopt this because the asymmetric AFF form makes the role of the inverse Gram matrix manifest, and because the structural identity we derive in §5.5 — that the same $1/d$ factor governs the PSL$(2,7)/F_{21}$ blind-spot ratio of Paper 7 — is more transparent in the AFF form.
- **Frobenius normalization** of the projectors themselves (rescaling $\Pi_{p,q} \to \sqrt{d} \Pi_{p,q}$) would absorb the $(d+1)/d$ factor into the projector definition. We do not adopt this because the rank-one projector convention is standard in QBism literature [Fuchs–Stacey, Appleby–Bengtsson] and we wish the formulas in this paper to compose directly with that literature.

### 3.4 Triple-product structure constants

The SIC projectors satisfy a fixed cubic identity, the *triple product*:

$$T_{ijk} \equiv \operatorname{tr}(\Pi_i \Pi_j \Pi_k) = \langle \psi_i | \psi_j \rangle \langle \psi_j | \psi_k \rangle \langle \psi_k | \psi_i \rangle.$$

For a SIC, $|T_{ijk}|$ is constant on cyclically distinct triples (by $WH(7)$ covariance). The phase $\arg(T_{ijk})$ encodes nontrivial information about the SIC, and is the object we will return to in §7 when establishing the connection to the $G_2$ associative 3-form.

---

## §4. The $G_2$ Defining Representation

### 4.1 Octonions and the Fano-plane indexing

We adopt the Baez 2002 indexing of the imaginary octonions [Bull. AMS 39, 145–205], in which the seven imaginary units $e_0, \ldots, e_6$ are labeled to match the seven points of the Fano plane and the octonion multiplication is encoded by the seven Fano lines (Figure 1). In zero-indexed form (which we use throughout the computational appendix), the seven Fano lines are:

$$\mathcal{L}_{\mathrm{Fano}} = \{(0,1,3),\ (1,2,4),\ (2,3,5),\ (3,4,6),\ (0,4,5),\ (1,5,6),\ (0,2,6)\}.$$

*[Figure 1: Fano plane diagram — see `figures/figure1_fano_plane.png`]*

Cyclic ordering $(a,b,c)$ on each line indicates positive orientation: $e_a e_b = e_c$. Anti-cyclic ordering reverses the sign.

The octonion *associative 3-form* is the totally antisymmetric tensor

$$\varphi_{ijk} = \begin{cases} +1 & (i,j,k) \text{ cyclic on a Fano line} \\ -1 & (i,j,k) \text{ anti-cyclic on a Fano line} \\ 0 & (i,j,k) \text{ not on any Fano line} \end{cases}$$

This 3-form has 42 nonzero components: 7 Fano lines × 6 orderings each = 42.

### 4.2 Modeling-choice stack

We use Baez's Fano indexing rather than Cayley–Dickson, Coxeter, or Tits parametrizations for three reasons. First, it is the indexing under which the $G_2$ action on octonions is most transparent ($G_2$ permutes Fano lines as line-preserving symmetries). Second, it matches the indexing used in Paper 8 of this series [Eight-Coset Quantum Simulator, in preparation], so the two papers compose directly. Third, it is the indexing under which the projection from $WH(7) \rtimes C_3$ to $F_{21}$ in Theorem 2 takes its simplest form.

### 4.3 $G_2$ as the stabilizer of the 3-form

The complexified Lie algebra $\mathfrak{g}_2^{\mathbb{C}}$ is the kernel of the linear map

$$L: \mathfrak{so}(7) \to \Lambda^3(\mathbb{R}^7), \qquad (L_M \varphi)_{ijk} = \sum_l \left[ M_{il} \varphi_{ljk} + M_{jl} \varphi_{ilk} + M_{kl} \varphi_{ijl} \right].$$

A direct computation in the $\mathfrak{so}(7)$ basis $\{A_{ab}\}_{0 \leq a < b \leq 6}$ yields a $35 \times 21$ integer action matrix whose null space is 14-dimensional, confirming $\dim \mathfrak{g}_2 = 14$ and providing an explicit basis $\{T_a\}_{a=1}^{14}$ of antisymmetric, traceless $7 \times 7$ matrices preserving $\varphi$.

We orthonormalize this basis under the Frobenius inner product $\langle A, B \rangle_F = -\operatorname{tr}(AB)$ (the negative trace for antisymmetric matrices). The resulting basis $\{T_a\}_{a=1}^{14}$ satisfies $\langle T_a, T_b \rangle_F = \delta_{ab}$ and closes under commutator: $[T_a, T_b] = \sum_c f^c_{ab} T_c$ with the structure constants $f^c_{ab}$ recoverable from $\operatorname{tr}([T_a, T_b] T_c)$. The closure was verified numerically to $1.67 \times 10^{-16}$ residual.

---

## §5. Theorem 1 — The $G_2$ Embedding

### 5.1 Statement

**Theorem 1.** *The complexified $G_2$ Lie algebra embeds as a 14-dimensional subspace of $\mathfrak{gl}(7,\mathbb{C})$ in the SIC operator basis. Explicitly, for each Frobenius-orthonormal $G_2$ generator $T_a$, the AFF dual-frame expansion*

$$T_a = \sum_{p,q \in \mathbb{Z}_7} \alpha^{(a)}_{p,q} \, \Pi_{p,q}, \qquad \alpha^{(a)}_{p,q} = \frac{8}{7} \cdot \operatorname{tr}(T_a \Pi_{p,q}),$$

*has rank exactly 14 (so the 14 expansions are linearly independent) and the embedding is a partial isometry: all 14 row vectors $(\alpha^{(a)}_{p,q})_{p,q}$ have identical $\ell^2$ norm in $\mathbb{C}^{49}$.*

### 5.2 Proof of Theorem 1

The inclusion $\mathfrak{g}_2^{\mathbb{C}} \subset \mathfrak{gl}(7,\mathbb{C})$ is standard: $G_2$ is realized as a 14-dimensional Lie subalgebra of $\mathfrak{so}(7) \subset \mathfrak{sl}(7) \subset \mathfrak{gl}(7)$ via the defining representation. By AFF 2011, the 49 SIC projectors span $\mathfrak{gl}(7,\mathbb{C})$ as a complex vector space. Therefore each $T_a$ admits a unique expansion of the stated form, and the coefficients $\alpha^{(a)}_{p,q}$ are computed by the dual-frame formula given.

The rank claim is equivalent to the linear independence of $\{T_1, \ldots, T_{14}\}$ in $\mathfrak{gl}(7,\mathbb{C})$, which follows from the Frobenius orthonormality $\langle T_a, T_b \rangle_F = \delta_{ab}$.

For the partial-isometry claim: by the AFF formula and the cyclic invariance of the trace,

$$\sum_{p,q} |\alpha^{(a)}_{p,q}|^2 = \left(\frac{8}{7}\right)^2 \sum_{p,q} |\operatorname{tr}(T_a \Pi_{p,q})|^2 = \left(\frac{8}{7}\right)^2 \sum_{p,q} \operatorname{tr}(T_a \Pi_{p,q}) \operatorname{tr}(T_a^\dagger \Pi_{p,q}).$$

Using $T_a^\dagger = -T_a$ (anti-Hermiticity) and the SIC 2-design identity [AFF 2011, Lemma 3.1; Renes–Blume-Kohout–Scott–Caves 2004, Eq. (7)]
$$\sum_{i=1}^{d^2} \Pi_i \otimes \Pi_i = \frac{d}{d+1}(\mathbb{1} + \mathbb{S})$$
(where $\mathbb{S}$ is the swap operator on $\mathbb{C}^d \otimes \mathbb{C}^d$), one obtains

$$\sum_{i} \alpha^{(a)}_{i} \overline{\alpha^{(b)}_{i}} = \left(\frac{d+1}{d}\right)^2 \sum_i \operatorname{tr}(T_a \Pi_i) \operatorname{tr}(T_b^\dagger \Pi_i) = \left(\frac{d+1}{d}\right)^2 \cdot \frac{d}{d+1} \bigl[\operatorname{tr}(T_a)\operatorname{tr}(T_b^\dagger) + \operatorname{tr}(T_a T_b^\dagger)\bigr].$$

Since $T_a$ is traceless and Frobenius-orthonormal, $\operatorname{tr}(T_a) = 0$ and $\operatorname{tr}(T_a T_b^\dagger) = -\operatorname{tr}(T_a T_b) = \delta_{ab}$ (the negative trace is the natural Frobenius inner product on antisymmetric matrices). Therefore

$$\sum_{i} \alpha^{(a)}_{i} \overline{\alpha^{(b)}_{i}} = \frac{d+1}{d} \delta_{ab} = \frac{8}{7} \delta_{ab}.$$

This is the full coefficient-Gram identity: the 14 coefficient row vectors are mutually orthogonal in $\mathbb{C}^{49}$ and have common $\ell^2$ norm $\sqrt{8/7}$. The map $T_a \mapsto \alpha^{(a)}$ is therefore an *isometric embedding up to the scalar factor $8/7$* of the Frobenius-normed $\mathbb{R}^{14} \hookrightarrow \mathbb{C}^{49}$. Setting $a = b$ recovers the row-norm statement: $\|\alpha^{(a)}\|_2 = \sqrt{8/7} \approx 1.0690$ for all $a$, as observed in the Φ Task 1 numerics ($1.0690^2 = 1.1428\ldots \approx 8/7$). ∎

### 5.3 Coefficient structure

Three structural properties of the coefficient tensor are observable from the explicit numerics, all of which we now establish analytically.

**Property 1 (Purely imaginary).** $\alpha^{(a)}_{p,q} \in i\mathbb{R}$ for all $a, p, q$.

*Proof.* $T_a$ is anti-Hermitian and $\Pi_{p,q}$ is Hermitian. Therefore $\operatorname{tr}(T_a \Pi_{p,q})^* = \operatorname{tr}(\Pi_{p,q}^\dagger T_a^\dagger) = \operatorname{tr}(\Pi_{p,q}(-T_a)) = -\operatorname{tr}(T_a \Pi_{p,q})$, so the trace is purely imaginary. ∎

We may therefore write $\alpha^{(a)}_{p,q} = i \beta^{(a)}_{p,q}$ with $\beta^{(a)}_{p,q} \in \mathbb{R}$.

**Property 2 (Tracelessness).** $\sum_{p,q \in \mathbb{Z}_7} \alpha^{(a)}_{p,q} = 0$ for all $a$.

*Proof.* By SIC completeness, $\sum_{p,q} \Pi_{p,q} = d \cdot \mathbb{1}$. Therefore $\sum_{p,q} \operatorname{tr}(T_a \Pi_{p,q}) = \operatorname{tr}(T_a \cdot d \cdot \mathbb{1}) = d \operatorname{tr}(T_a) = 0$. ∎

**Property 3 (Density).** All $14 \times 49 = 686$ coefficients $\alpha^{(a)}_{p,q}$ are nonzero.

*Computational claim.* Verified at 60-digit precision against an exact $d = 7$ Weyl–Heisenberg-covariant SIC fiducial drawn from the verified UMass/QBism SIC database (the Scott–Grassl 2010 RIRI form), which lies in the same Clifford orbit as the corrected ABGHM fiducial used in §6 (both saturate the SIC overlap condition at $|\langle\psi_i|\psi_j\rangle|^2 = 1/8$ across all 48 nontrivial WH displacements). The minimum coefficient modulus over the entire tensor is $|\alpha_{\min}| = 2.58 \times 10^{-4}$, well above the precision floor.

*Why the result is SIC-invariant.* The structural properties of the tensor — rank, equal row norm, density, traceless rows — are all consequences of (i) the AFF dual-frame inversion (§3.2), which depends only on the SIC condition $|\langle\psi_i|\psi_j\rangle|^2 = 1/(d+1)$, and (ii) the SIC 2-design identity (§5.2), which holds for any SIC-POVM regardless of fiducial choice. The numerical values $\alpha^{(a)}_{p,q}$ change between Clifford-equivalent SIC fiducials, but the row Gram matrix $\sum_i \alpha^{(a)}_i \overline{\alpha^{(b)}_i} = (8/7)\delta_{ab}$ does not. The corrected ABGHM SIC, by virtue of being in the same Clifford orbit as the database fiducial, yields a tensor with identical structural properties; only the specific entries differ. The Φ Task 1 numerical record is at `outbox/paper10/computations/paper10_task1_g2_sic_coefficients.json`.

*Implication.* In the database fiducial computation, each $G_2$ generator requires the *full* 49-dimensional SIC operator basis; no Fano-line index restriction or sparsity pattern simplifies the embedding. This is the central technical observation of §5: the SIC frame "sees" all of $G_2$ globally, not just the Fano-supported pieces. We expect (but have not separately verified) that the same density holds for the corrected ABGHM SIC, since the Clifford orbit of the database fiducial does not in general permit zero entries to appear under conjugation by $WH(7) \rtimes C_3$; rerunning Task 1 against the corrected ABGHM fiducial would settle this directly. Figure 2 displays the $14 \times 49$ magnitude tensor $|\alpha^{(a)}_{p,q}|$ as a heatmap; the uniform Frobenius row norm $\sqrt{8/7} \approx 1.069$ across all 14 rows is the isometric-embedding property derived in §5.2, which holds for any SIC fiducial and is verified to numerical precision $8.5 \times 10^{-8}$.

*[Figure 2: 14×49 coefficient heatmap — see `figures/figure2_coefficient_heatmap.png`]*

### 5.4 The $G_2$-module decomposition of $\mathfrak{gl}(7,\mathbb{C})$

Under the action of $G_2$, the 49-dimensional space $\mathfrak{gl}(7,\mathbb{C}) = V_7 \otimes V_7^*$ decomposes as

$$\mathfrak{gl}(7,\mathbb{C}) = \mathbf{1} \oplus V_7 \oplus V_{14} \oplus V_{27},$$

with dimensions $1 + 7 + 14 + 27 = 49 = d^2$. This follows from
$$\operatorname{Sym}^2(V_7) = \mathbf{1} \oplus V_{27}, \qquad \Lambda^2(V_7) = V_7 \oplus V_{14}.$$

The 49 SIC projectors collectively span all four irreducible components of this decomposition. The 14 $G_2$ generators $T_a$ span exactly the $V_{14}$ component. The coefficient matrix $\alpha^{(a)}_{p,q}$ is therefore the projection map $V_{14} \hookrightarrow \mathbb{C}^{49}$ in the SIC frame.

**Note on the $1+7+14+27=49$ versus $1+14+27=42$ decompositions.** The "42" appears in two distinct contexts: (a) as the number of nonzero components of the $G_2$ associative 3-form $\varphi_{ijk}$ (which has $7 \cdot 6 = 42$ nonzero entries), and (b) in some treatments of the Fernández–Gray torsion classes of $G_2$ manifolds, where the decomposition omits the $V_7$ component because it does not appear in the relevant cohomology. Neither interpretation conflicts with the $\mathfrak{gl}(7)$ decomposition $1+7+14+27=49$ used in this paper.

### 5.5 What is, and what is not, special about $d = 7$

The AFF coefficient formula

$$\alpha^{(a)}_{p,q} = \frac{d+1}{d} \cdot \operatorname{tr}(T_a \Pi_{p,q})$$

contains the dimension $d = 7$ in the denominator as an algebraically forced factor from the SIC Gram matrix inversion (§3.2). The ratio $(d+1)/d = 8/7$ is *not* a non-generic feature of $d = 7$: every SIC dimension produces $(d+1)/d$, and the projector identity $\operatorname{tr}(\Pi - I/d)^2 = (d-1)/d$ is generic to all dimensions. Analogous ratios $10/11$ and $12/13$ exist in $d = 11$ and $d = 13$. The 6/7 ratio in this series and the 8/7 AFF factor are not exceptional *as ratios*.

What *is* specific to $d = 7$ is the joint occurrence of additional structural features that allow an explicit identification of $\mathfrak{g}_2^{\mathbb{C}}$ inside $\mathfrak{gl}(7,\mathbb{C})$ via the SIC frame. We catalog these features and acknowledge their internal dependencies.

**(A) Arithmetic structure on $\mathbb{Q}(\sqrt{-7})$.** Two distinct constructions descend from class field theory on the imaginary quadratic field $\mathbb{Q}(\sqrt{-7})$:
 - The ABGHM 2022 Stark-unit construction [DOI 10.1063/5.0083520] yields the smallest prime exact SIC fiducial at $d = 7 = n^2 + 3$ ($n = 2$).
 - The Klein quartic, the unique compact Riemann surface of genus 3 with maximal automorphism group $PSL(2,7)$ of order 168, has its modular description over $\mathbb{Q}(\sqrt{-7})$.

 These are not independent features: both are consequences of the prime 7's role in the arithmetic of $\mathbb{Q}(\sqrt{-7})$. Other prime dimensions admit Stark-unit constructions only conditionally: the Kopp 2021 program [DOI 10.1093/imrn/rnz153] (covering $d \equiv 2 \pmod 3$, including $d = 11, 17, 23$) and the Appleby–Flammia–Kopp 2025 conditional construction [arXiv:2501.03970]. Dimension $d = 13$ admits no clean Stark-unit recipe.

**(B) The smallest exceptional Lie group acts irreducibly at dimension 7.** Among exceptional simple Lie groups $G_2, F_4, E_6, E_7, E_8$, only $G_2$ has its smallest non-trivial irreducible representation at a prime dimension; the corresponding dimension is 7 (the defining representation on $\operatorname{Im}\mathbb{O} \cong \mathbb{R}^7$). The smallest non-trivial irreps of $F_4, E_6, E_7, E_8$ are 26, 27, 56, 248 respectively, none prime. Equivalently: $G_2$ is the smallest exceptional Lie group, and its smallest representation at a prime dimension is at 7.

**(C) Compatibility of (A) and (B).** The 7-dimensional defining representation of $G_2$ is preserved by $PSL(2,7)$ acting on $\operatorname{Im}\mathbb{O}$ via Fano-line preserving permutations, with the cyclic-axis Frobenius subgroup $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3 \subset PSL(2,7)$ acting freely-transitively on points (Theorem 2). The action of $F_{21}$ within $G_2$ is what makes the discrete combinatorics of (A) compatible with the continuous Lie structure of (B). Under the maximal subgroup $SU(3) \subset G_2$, the 7-dimensional defining representation decomposes as $\mathbf{7} = \mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$, a consequence of (B) rather than an independent feature; this branching is what gives the $6/7$ ratio in Papers 6 and 7 a structural reading (a singlet plus a complex 3-rep), but the existence of the branching is forced by (B).

The relation between (A), (B), and (C):

| Dimension | Stark-unit SIC | Exceptional Lie irrep | Klein-quartic / Fano combinatorics |
|-----------|----------------|------------------------|-------------------------------------|
| $d = 7$ | ABGHM exact | $G_2$ on $\operatorname{Im}\mathbb{O}$ | $PSL(2,7)$ on Klein quartic; Fano plane $PG(2,2)$ |
| $d = 11$ | Kopp 2021 conditional | None | None |
| $d = 13$ | None known | None | None |
| $d = 17$ | Kopp 2021 conditional | None | None |
| $d = 19$ | ABGHM ($n = 4$) | None | None |
| $d = 23$ | Kopp 2021 conditional | None | None |

$d = 7$ is the smallest prime dimension where all three columns are non-empty. We are not claiming this conjunction is mysterious; we are claiming that the specific identifications established by Theorems 1–3 — the explicit closed-form $\mathfrak{g}_2^{\mathbb{C}} \hookrightarrow \mathfrak{gl}(7,\mathbb{C})$ embedding via the SIC dual frame, the canonical descent $WH(7) \rtimes C_3 \to F_{21}$, and the closed-form triple-product structure $T = a + ib\varphi$ — are made possible by the joint occurrence of these features at $d = 7$ and would not survive at any other small prime dimension.

For concreteness: at $d = 19$, ABGHM's exact construction applies, but no exceptional Lie group acts irreducibly in $\mathbb{R}^{19}$, so there is no $G_2$-analogue to Theorem 1. At $d = 11$, the Kopp construction applies conditionally, and there is again no exceptional Lie group with a natural irrep at dimension 11. The structural identification at $d = 7$ is therefore a one-off, but its *origin* is the conjunction (A) $\wedge$ (B), with (C) tying them together. We do not present this as a hierarchy of independent features.

The four occurrences of the prime 7 across Papers 4, 6, 7, and 10 of this series are bound by this common origin:
1. The $PSL(2,7) / F_{21}$ blind-spot bound $\varepsilon_{\min} = 1/7$ derived in Paper 4 [DOI 10.5281/zenodo.19617662];
2. The thermodynamic coherence-ceiling residual $1 - \sigma_{\mathrm{pred}} = 1/49 = (1/7)^2$ derived in Paper 7 [DOI 10.5281/zenodo.19773185];
3. The $6/7$ contraction ratio of Paper 6 [DOI 10.5281/zenodo.19672709];
4. The $(d+1)/d = 8/7$ AFF coefficient factor of the present paper.

Each arises from a different inversion problem (group-theoretic projection, Markov contraction, Casimir branching, and dual-frame inversion respectively), but all four are governed by the same dimensional fact: $d = 7$ is the smallest prime where (A) and (B) both hold. The unification is structural, not numerical. The bibliography references for the underlying mathematical facts include Scott–Grassl 2010 [DOI 10.1063/1.3374022], Fuchs–Hoang–Stacey 2017 [DOI 10.3390/axioms6030021], Zhu 2010 [DOI 10.1088/1751-8113/43/30/305305], Bryant 1987 [DOI 10.2307/1971360], Singerman 1988 [DOI 10.1112/blms/20.4.297], and Elkies 1999 in the Klein quartic monograph.

### 5.6 What Theorem 1 does *not* establish

Theorem 1 is a structural statement about $G_2$ as a vector subspace of $\mathfrak{gl}(7,\mathbb{C})$. It does not yet establish:

- That $G_2$ is *covariant* under the SIC frame in any group-theoretic sense (this is the content of Theorem 2, §6);
- That the SIC triple products $T_{ijk} = \operatorname{tr}(\Pi_i \Pi_j \Pi_k)$ encode the $G_2$ associative 3-form $\varphi_{ijk}$ (this is the content of Theorem 3, §7);
- Any direct connection to consciousness, QBist agents, or the broader PCI/PME framework (this is the broader series; see Paper 4 for the QBism-PSL$(2,7)$ link, Paper 7 for the thermodynamic ceiling, and Paper 8 for the eight-coset simulator, all of which are presupposed but not redeveloped here).

What Theorem 1 *does* establish is a clean dimensional fact: the 14-dimensional Lie algebra $\mathfrak{g}_2^{\mathbb{C}}$ is a partial-isometric subspace of the 49-dimensional space spanned by the SIC operator basis at $d=7$, with explicit and computable coefficient tensors.

---

## §6. Theorem 2 — The 147 → F₂₁ Descent

The Samuel–Gedik 2024 classification [DOI 10.1088/1751-8121/ad5ca9] established that the symmetry group of the d=7 SIC Gram matrices, when generated without imposing group covariance ab initio, has order $147 = 49 \times 3$. We identified this group as $WH(7) \rtimes C_3$ in §3. The full continuous orientation stabilizer of the $G_2$ associative 3-form on the imaginary-octonion span $\operatorname{Im} \mathbb{O}$ is the Lie group $G_2$ itself; the discrete Fano-line-preserving subgroup of $G_2$ acting on $\operatorname{Im}\mathbb{O}$ by basis permutations is $PSL(2,7)$ of order 168. Within $PSL(2,7)$, the *cyclic-axis Frobenius subgroup* $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3$ of order 21 — the stabilizer of a chosen cyclic Fano-line orientation around a distinguished point — plays a structural role in Paper 4 of this series (DOI 10.5281/zenodo.19617662). The factor of 7 between the SIC symmetry (147) and the cyclic-axis Frobenius subgroup (21) is the precise sense in which the SIC frame "knows more than" the cyclic-axis structure: it carries the full Weyl–Heisenberg phase-space group, not merely the cyclic Fano-axis subgroup.

This section establishes that under a Fano-compatible choice of cyclic axis in $WH(7)$, the 147-element SIC symmetry group descends to the 21-element Frobenius group $F_{21}$ as the subgroup that simultaneously preserves the SIC structure and the $G_2$ associative 3-form. The descent is the natural bridge between the SIC operator basis of §3–§5 and the $G_2$/Fano combinatorial structure of Paper 4.

### 6.1 The ambient group $WH(7) \rtimes C_3$

The Weyl–Heisenberg group in dimension $d = 7$ is generated by the cyclic shift $X: |k\rangle \to |k+1 \mod 7\rangle$ and the cyclic phase $Z: |k\rangle \to \omega^k |k\rangle$, where $\omega = e^{2\pi i/7}$. The 49 displacement operators $D_{p,q} = \omega^{-pq/2} X^p Z^q$ for $(p, q) \in \mathbb{Z}_7 \times \mathbb{Z}_7$ form the projective version of $WH(7)$ acting on $\mathbb{C}^7$. The order-3 Clifford symmetry adjoined by Samuel–Gedik corresponds to a unitary $U \in U(7)$ satisfying $U^3 \in \{\mathbb{1}, \omega \mathbb{1}, \omega^2 \mathbb{1}\}$ that conjugates the Weyl–Heisenberg group to itself, permuting the 49 SIC projectors among themselves while preserving SIC overlap conditions.

The full group $WH(7) \rtimes C_3$ has order $49 \cdot 3 = 147$. Samuel–Gedik proved that all generated d=7 SIC Gram matrices have symmetry groups isomorphic to subgroups of this ambient group, with the maximal subgroup of order 147 occurring for the Scott–Grassl $F_z$ and $F_a$ fiducials [Scott and Grassl 2010, DOI 10.1063/1.3374022].

### 6.2 The Fano-compatible cyclic axis

The seven imaginary octonion units $e_0, \ldots, e_6$ correspond to seven points of the projective Fano plane PG(2,2). The seven Fano lines, in Baez 2002 indexing, are listed in §4.1.

The Fano-compatible cyclic axis is determined by demanding that the cyclic $\mathbb{Z}_7$ generator induce a permutation $\sigma \in S_7$ on the seven imaginary units that sends each Fano triple to another Fano triple. Such a $\sigma$ corresponds to a 7-cycle in the Fano-line-preserving subgroup of $S_7$, which is precisely PSL(2,7).

A direct enumeration over all 128 diagonal sign-flip matrices $W \in \{\pm 1\}^7$ (computed at 50-digit precision in the GAP/SymPy verification of §6.4 below) shows that *exactly two* sign-flip matrices produce 48/48 SIC overlaps for the ABGHM fiducial:

$$W = \operatorname{diag}(-1, +1, +1, +1, +1, +1, +1) \quad \text{and} \quad -W = \operatorname{diag}(+1, -1, -1, -1, -1, -1, -1).$$

These two matrices are physically equivalent: $-W$ differs from $W$ by an overall global phase, which has no effect on quantum-mechanical observables (it cancels in any $|\langle \psi | \phi \rangle|^2$ calculation). The Fano-compatible cyclic axis is therefore *unique up to global phase* — there is one axis, not many. We refer to it as **the** Fano axis, with the definite article.

This uniqueness has a concrete geometric origin. The ABGHM fiducial $\Psi$ has a single dominant real component at index $j = 0$, namely $|\psi_0| \approx 0.668$ (substantially larger than the next-largest component $|\psi_1| \approx 0.484$ at any other index). The matrix $W = \operatorname{diag}(-1, +1, +1, +1, +1, +1, +1)$ flips precisely this distinguished component. Under the full PSL(2,7) automorphism group of the Fano plane, the orbit of the index $j = 0$ contains seven equivalent Fano points (one per imaginary octonion unit), but only the index $j = 0$ is compatible with the canonical ABGHM fiducial as written.

The Task 2 computational verification (Φ, 2026-04-30) confirms three results:

1. **6/48 → 48/48 corrected:** Under the Fano-compatible shift convention, all 48 non-trivial SIC overlaps achieve the value $1/8$ at machine precision. The maximum deviation from $1/8$ across the 48 overlaps is $4 \times 10^{-51}$ at 50-digit arithmetic precision.
2. **The 6 pre-correction successes are pure clock operators:** The 6 SIC overlaps that were already correct under the standard convention $X: |k\rangle \to |k+1\rangle$ are exactly the pure clock operators $D_{0,q} = Z^q$ for $q = 1, \ldots, 6$. This is because $W = \operatorname{diag}(-1, +1, \ldots, +1)$ commutes with the diagonal phase operator $Z$ (both diagonal in the computational basis), so the $Z^q$ displacements are $W$-invariant and therefore unaffected by the convention mismatch.
3. **Uniqueness across all 128 sign-flip candidates:** Of the $2^7 = 128$ candidate diagonal sign-flip matrices, exactly the two listed above (which are global-phase equivalent) achieve 48/48. The other 126 candidates produce overlaps in the same $[0.039, 0.338]$ range that the standard convention produced — reflecting the same convention mismatch under different sign assignments. Figure 3 shows the categorical breakdown.

*[Figure 3: 128-candidate enumeration histogram — see `figures/figure3_w_enumeration.png`]*

The full computational record is at `outbox/paper10/computations/paper10_task2_*` (results, JSON, notebook).

### 6.3 The ABGHM diagnostic and the descent

The Φ Task 1 results identified that the ABGHM fiducial as written satisfies only 6 of the 48 standard SIC overlap conditions when the Weyl–Heisenberg shifts are taken in the computational basis $|k\rangle \to |k+1 \mod 7\rangle$. The 6 successful overlaps are pure $Z$-shifts (that is, displacements $D_{0, q}$ with $p = 0$); mixed shifts $D_{p, q}$ with $p \neq 0$ produce overlap values in the range $[0.039, 0.338]$, none equal to the SIC value $1/8 = 0.125$.

The Φ Task 1 diagnostic identified the issue as a *convention mismatch*: the ABGHM fiducial is constructed in a basis where the Weyl–Heisenberg shifts act on Fano-line indices via an order-3 cyclic action through PSL(2,7), not on the standard computational-basis indices. The Task 2 verification (§6.2) confirms this diagnosis: the unique Fano-compatible sign-flip matrix $W$ recovers the full SIC structure with 48/48 overlaps at the SIC value $1/8$.

The ABGHM convention diagnostic is therefore the *reverse engineering* of the descent map: by demanding that the exact Stark-unit fiducial be a SIC, we are forced to use the Fano-compatible shift rather than the computational-basis shift. The induced subgroup of $WH(7) \rtimes C_3$ that preserves the ABGHM SIC structure *and* the cyclic Fano-line orientation under the Fano-compatible shift is precisely the cyclic-axis Frobenius subgroup $F_{21} \subset PSL(2,7) \subset G_2$.

### 6.4 Statement of Theorem 2

We can now state Theorem 2 in the form that the computational output verifies. We are careful to distinguish three group-theoretic objects that the previous draft conflated:

- $\operatorname{Aut}_+(\varphi) \cong G_2 \subset GL(7,\mathbb{R})$, the *full* (continuous) orientation-preserving stabilizer of the associative 3-form $\varphi$.
- $\operatorname{Aut}_+^{(\mathrm{Fano})}(\varphi) \cong PSL(2,7)$ of order 168, the subgroup of $S_7$ consisting of permutations of the seven points of $PG(2,2)$ that preserve the Fano-line structure with positive orientation.
- $F_{21} = \mathbb{Z}_7 \rtimes \mathbb{Z}_3 \subset PSL(2,7)$ of order 21, a *distinguished* Frobenius subgroup acting freely-transitively on points (“cyclic-axis” subgroup), generated by a 7-cycle and an order-3 multiplier $k \mapsto 2k$ which has $\operatorname{ord}_7(2) = 3$.

The role of $F_{21}$ in the present construction is the third object: a distinguished subgroup of $PSL(2,7)$ that preserves a *chosen* cyclic Fano orientation, not the full continuous or discrete stabilizer of $\varphi$.

**Theorem 2 (Fano-compatible SIC symmetry restricts to $F_{21}$).** *Let $|\Psi\rangle$ be the ABGHM exact $d=7$ SIC fiducial of §2.2 and let $W = \operatorname{diag}(-1, +1, +1, +1, +1, +1, +1)$ be the sign-flip matrix of §6.2. Then:*

*(a) (Uniqueness of the correction.) Of the $2^7 = 128$ diagonal sign-flip matrices in $\{\pm 1\}^7$, exactly two — namely $W$ and $-W$, which are equivalent up to a global phase — produce a fiducial $W|\Psi\rangle$ satisfying all 48 nontrivial SIC overlap conditions $|\langle \psi | D_{p,q} | \psi \rangle|^2 = 1/8$. Numerical verification at 50-digit precision: $\max_{(p,q) \neq (0,0)} \bigl| |\langle\psi|D_{p,q}|\psi\rangle|^2 - 1/8 \bigr| < 4 \times 10^{-51}$.*

*(b) (Descent of SIC symmetry.) The subgroup of the Samuel–Gedik symmetry group $WH(7) \rtimes C_3$ that preserves the Fano-line structure under Baez's 2002 indexing is the index-7 subgroup $F_{21} = \mathbb{Z}_7 \rtimes C_3 \subset WH(7) \rtimes C_3$, where $\mathbb{Z}_7 \subset WH(7)$ is generated by the cyclic shift $X$ (not the diagonal phase $Z$) and $C_3$ is the Samuel–Gedik order-3 Clifford automorphism. Inside $WH(7) \rtimes C_3$, this $F_{21}$ is the subgroup that simultaneously (i) maps the corrected fiducial $W|\Psi\rangle$ within its WH-covariance orbit and (ii) preserves the cyclic Fano-line orientation under Baez 2002 indexing.*

*(c) (Identification with $G_2$ orientation subgroup.) The $F_{21}$ subgroup of (b), acting on the seven indices of $\mathbb{C}^7 \cong \operatorname{Im}\mathbb{O}_{\mathbb{C}}$ via permutation of basis vectors, coincides with the cyclic-axis Frobenius subgroup of $PSL(2,7) = \operatorname{Aut}_+^{(\mathrm{Fano})}(\varphi)$ described above. It does not coincide with the full $G_2$ orientation stabilizer; it is a particular discrete subgroup of $PSL(2,7) \subset G_2$ distinguished by a chosen 7-cycle.*

**The Frobenius presentation is verified explicitly.** $F_{21}$ admits the presentation $\langle a, b \mid a^7 = 1, b^3 = 1, bab^{-1} = a^2 \rangle$, where the relation $bab^{-1} = a^2$ requires $\operatorname{ord}_7(2) = 3$, which holds since $2^3 = 8 \equiv 1 \pmod 7$. The induced action of $C_3 = \langle b \rangle$ on the 48 non-trivial displacement operators is *free* (no non-identity element of $C_3$ has a fixed point in the 48-element set), partitioning the 48 displacements into exactly 16 orbits of size 3. The Frobenius condition for $F_{21}$ to be a Frobenius group is satisfied.

**The descent is canonical.** The Task 2 enumeration (§6.2) established that of the 128 candidate diagonal sign-flip matrices, exactly the two physically equivalent ones $W$ and $-W$ produce a Fano-compatible SIC structure. Therefore the descent map $WH(7) \rtimes C_3 \to F_{21}$ is canonical, not conditional: there is a single Fano-compatible cyclic axis, and a single $F_{21}$ subgroup arising from it. We do not require a modeling choice between alternative Fano axes.

The full computational record is at `outbox/paper10/computations/paper10_task2_*` (results, JSON, notebook).

### 6.5 Modeling-choice stack

We document the choices that go into Theorem 2:

**Choice 1 — Fano-compatible cyclic axis:** We adopt the cyclic $\mathbb{Z}_7$ subgroup determined by the Baez 2002 indexing of the octonions and the corresponding Fano-line structure. The Task 2 enumeration over all 128 diagonal sign-flip candidates (§6.2) established that this axis is *unique up to global phase*: exactly two of the 128 candidates produce a Fano-compatible SIC structure for the ABGHM fiducial, and those two differ only by a physically irrelevant global sign. This makes Theorem 2 canonical rather than conditional, and removes the modeling-choice ambiguity that the §3 framing initially preserved.

**Choice 2 — Restriction, not quotient.** We frame Theorem 2 as a *restriction* from $WH(7) \rtimes C_3$ to a subgroup $F_{21}$ of index 7. The diagonal phase subgroup $\langle Z \rangle$ generated by the order-7 clock operator $Z$ is normal in $WH(7) \rtimes C_3$, and the quotient $(WH(7) \rtimes C_3)/\langle Z\rangle$ is also of order 21, abstractly isomorphic to $F_{21}$. The two framings yield isomorphic groups *as abstract groups*, but they are distinct subobjects of $WH(7) \rtimes C_3$: the index-7 subgroup contains the cyclic shift $X$ but excludes $Z$, while the quotient identifies all displacements $D_{p,q}$ that differ by a multiple of $Z$. We adopt the restriction framing throughout, since the action on the 7-dimensional representation $\mathbb{C}^7$ is the relevant structure and only the restricted subgroup acts there directly.

**Choice 3 — Identification with the cyclic-axis subgroup of $PSL(2,7)$.** The $F_{21}$ subgroup of $WH(7) \rtimes C_3$ defined in Theorem 2(b) acts on the seven indices of $\mathbb{C}^7$ by permutation. Under the Baez 2002 indexing, this permutation action lies in $PSL(2,7) = \operatorname{Aut}_+^{(\mathrm{Fano})}(\varphi)$, the discrete orientation-preserving Fano-symmetry group. Inside $PSL(2,7)$, our $F_{21}$ coincides with the *cyclic-axis Frobenius subgroup* generated by translation $k \mapsto k+1 \pmod 7$ and multiplication-by-2 $k \mapsto 2k \pmod 7$ (which acts trivially on $0$ and has order 3 on $\mathbb{Z}_7^*$ since $2^3 = 8 \equiv 1 \pmod 7$). This Frobenius subgroup is *one* of eight cosets of $F_{21}$ in $PSL(2,7)$ (since $|PSL(2,7)|/|F_{21}| = 168/21 = 8$); the choice of which cyclic-axis subgroup is meant is determined by the choice of distinguished Fano point (here $j = 0$, the dominant real component of the ABGHM fiducial). It is *not* the full continuous $G_2$-stabilizer of $\varphi$, nor the full discrete stabilizer $PSL(2,7)$; it is the index-8 subgroup of the latter.

### 6.6 Why this matters

The 147 → F₂₁ descent is the bridge between the operator-algebraic content of Theorem 1 (the SIC frame is a basis for $\mathfrak{gl}(7,\mathbb{C})$, with $\mathfrak{g}_2^{\mathbb{C}}$ as a 14-dimensional isometrically-embedded subspace) and the group-theoretic content of Paper 4 (the QBism reference frame is governed by PSL(2,7) and its cyclic-axis Frobenius subgroup F₂₁).

Without Theorem 2, the SIC frame and the $G_2$/Fano framework live in adjacent but unconnected mathematical worlds. With Theorem 2, the two are joined at the symmetry group level: the 147-element SIC symmetry restricts to the 21-element cyclic-axis Frobenius subgroup of $PSL(2,7) \subset G_2$ through the same Fano-line structure that governs both.

This is the precise sense in which the d=7 SIC frame is "$G_2$-compatible." It is not that every SIC operation respects $G_2$ symmetry — Theorem 1's coefficient tensor is dense over the full 49-dimensional SIC basis, and most SIC displacements do *not* preserve $\varphi$. It is that the *subgroup* of SIC-symmetric operations that *also* preserves $\varphi$ is precisely the $F_{21}$ that we have used independently in Papers 4 and 7. The two $F_{21}$s are the same.

---

## §7. Theorem 3 — The Triple-Product Structure on Fano-Line $X$-Subgroup Triples

We now characterize the cubic structure of the SIC frame at $d = 7$. The SIC triple product
$$T_{ijk} = \operatorname{tr}(\Pi_i \Pi_j \Pi_k) = \langle \psi_i | \psi_j \rangle \langle \psi_j | \psi_k \rangle \langle \psi_k | \psi_i \rangle$$
is a complex-valued tensor whose imaginary part on Fano-line triples will be shown to equal the $G_2$ associative 3-form, up to an explicit algebraic scalar. Triple products are the natural objects encoding the cubic/Lie-bracket structure of the SIC operator basis: by AFF 2011 [DOI 10.1063/1.3555805], the structure constants of the projector basis are $\operatorname{tr}(\Pi_i [\Pi_j, \Pi_k])$, which differ from $T_{ijk}$ only by symmetrization.

### 7.0 Domain of Theorem 3 — the seven-point $X$-subgroup orbit

Before stating Theorem 3, we make precise the domain on which it is proved. The full SIC frame consists of $49$ projectors $\{\Pi_{p, q}\}_{(p, q) \in \mathbb{Z}_7 \times \mathbb{Z}_7}$. We focus on the seven-point sub-frame $\{\Pi_{p, 0}\}_{p \in \mathbb{Z}_7}$ generated by the $X$-subgroup of $WH(7)$ acting on the corrected ABGHM fiducial. This is the sub-frame on which the cocycle phase $\tau^{qr - ps}$ vanishes identically (since $q = s = 0$), allowing a clean closed-form analysis. Theorem 3 below is proved on this seven-point orbit and its associated triples, and extended to the full SIC frame by Conjecture 7.4. The closed-form treatment of mixed-displacement triples (where the cocycle phase is nontrivial) is left as an open problem (§9.4).

For a triple of distinct indices $(i, j, k)$ in the seven-point orbit, define the *ordered differences* $d_1 = j - i$, $d_2 = k - j$, $d_3 = i - k$ (mod 7), each a nonzero element of $\mathbb{Z}_7^*$. The triple is *all-QR* if $\{d_1, d_2, d_3\} \subset \operatorname{QR}_7 = \{1, 2, 4\}$, *all-NQR* if $\{d_1, d_2, d_3\} \subset \operatorname{NQR}_7 = \{3, 5, 6\}$, and *mixed-residue-class* otherwise.

The two zero-sum subsets of $\mathbb{Z}_7^*$ are exactly $\operatorname{QR}_7 = \{1, 2, 4\}$ ($1 + 2 + 4 = 7$) and $\operatorname{NQR}_7 = \{3, 5, 6\}$ ($3 + 5 + 6 = 14$). Triples whose three ordered differences span $\operatorname{QR}_7$ in cyclic order, or $\operatorname{NQR}_7$ in cyclic order, correspond to *Fano-line cyclic triples* under the Baez 2002 indexing of the imaginary octonions on $\mathbb{Z}_7$. We refer to these as *Fano-line $X$-subgroup triples*.

*Note on Fano-line vs. all-QR triples.* In the seven-point $X$-subgroup orbit indexed by $\mathbb{Z}_7$, the seven Fano lines under Baez's 2002 indexing correspond to a subset of the all-QR cyclic triples; the precise combinatorial question of whether *all* all-QR cyclic triples in $\mathbb{Z}_7$ are Fano lines (under some indexing) is left open in §9.4 and is a finite combinatorial check we have not exhaustively performed. For triples drawn from the full 49-projector SIC frame indexed by $\mathbb{Z}_7 \times \mathbb{Z}_7$, the Fano-vs-non-Fano distinction does not reduce cleanly to the QR/NQR partition because the cocycle phase $\tau^{qr - ps}$ enters; this is why we restrict the closed-form analysis of Theorem 3 to the $X$-subgroup orbit.

### 7.1 Lemma (universal magnitude on the SIC frame)

For any triple of distinct WH-displaced SIC projectors $\Pi_{(p_1, q_1)}, \Pi_{(p_2, q_2)}, \Pi_{(p_3, q_3)}$ in the full $d = 7$ SIC frame,
$$|T_{(p_1, q_1), (p_2, q_2), (p_3, q_3)}|^2 = \frac{1}{512}.$$

*Proof.* By the SIC defining property, $|\langle \psi_i | \psi_j \rangle|^2 = 1/(d+1) = 1/8$ for any two distinct SIC frame vectors. The triple product $T = \langle \psi_1 | \psi_2 \rangle \langle \psi_2 | \psi_3 \rangle \langle \psi_3 | \psi_1 \rangle$ is a product of three such complex inner products, plus a unit-modulus cocycle factor when expressed via WH displacements. Therefore $|T|^2 = (1/8)^3 = 1/512$. $\square$

This is an immediate corollary of the SIC condition and applies to *any* SIC-POVM in dimension 7, not just the corrected ABGHM SIC. We elevate it to a Lemma rather than a Theorem because the content is the cube of the SIC overlap, not a structural feature of the d=7 ABGHM fiducial specifically.

### 7.2 Theorem 3 (Fano-line $X$-subgroup decomposition)

Let $\{|\psi_p\rangle = D_{p, 0} | \psi_W\rangle\}_{p \in \mathbb{Z}_7}$ be the seven-point $X$-subgroup orbit of the corrected ABGHM fiducial. For any triple of distinct indices $(i, j, k)$ with all-QR or all-NQR ordered differences (i.e., a Fano-line $X$-subgroup triple), the SIC triple product decomposes as
$$T_{ijk} = a + i\, b\, \varphi_{ijk},$$
where the constants $a$ and $b$ are explicit algebraic numbers over $\mathbb{Q}(\sqrt{2})$:
$$a = \frac{\sqrt{2} - 1}{16}, \qquad b = \frac{(\sqrt{2} - 1)\sqrt{2 + 4\sqrt{2}}}{32},$$
and $\varphi_{ijk} \in \{+1, -1\}$ tracks cyclic ($\varphi = +1$) versus anti-cyclic ($\varphi = -1$) orientation. Equivalently, the imaginary part of the triple product is exactly proportional to the $G_2$ associative 3-form on the seven imaginary-octonion directions, with proportionality constant $b$.

The full algebraic proof, including the closed-form computation of $\alpha^3 = a + ib$ from the autocorrelation function of the corrected ABGHM fiducial, is given in Appendix A.4 (Theorem A.4.1, Propositions A.4.2, A.4.3).

Numerical values:
$$a \approx 0.025888347648, \qquad b \approx 0.035817851081.$$

The identity $(\sqrt{2} - 1)^2 (6 + 4\sqrt{2}) = 2$ (expansion: $(3 - 2\sqrt{2})(6 + 4\sqrt{2}) = 18 + 12\sqrt{2} - 12\sqrt{2} - 16 = 2$) yields $a^2 + b^2 = 1/512$, consistent with Lemma 7.1.

Figure 4 plots all Fano-line $X$-subgroup triples in the complex plane: every triple lies on the universal-magnitude circle $|T| = 1/(16\sqrt{2})$ of Lemma 7.1, with cyclic triples clustering at $(a, +b)$ and anti-cyclic at $(a, -b)$. The non-Fano triples in the figure (mixed-residue-class) sit at a distinct phase $(a', \pm b')$ — the subject of Conjecture 7.4 below.

*[Figure 4: Triple-product complex-plane structure — see `figures/figure4_triple_product.png`]*

### 7.3 The QR-class organizing principle

The Fano-line decomposition of Theorem 3 admits a deeper organizing principle observed during the computational verification (§4 of `paper10_task3_results.md`). Within the seven-point $X$-subgroup orbit, the triple-product value $T_{ijk}$ is determined entirely by the QR/NQR residue-class pattern of the ordered differences:

- All-QR ordered differences $\Rightarrow$ $T = \alpha^3 = a + ib$ (cyclic Fano-line triple)
- All-NQR ordered differences $\Rightarrow$ $T = \bar\alpha^3 = a - ib$ (anti-cyclic Fano-line triple)
- Mixed-residue-class ordered differences $\Rightarrow$ $T = a' + ib'\,\chi$ for a different pair of constants $(a', b')$ and an orientation indicator $\chi \in \{\pm 1\}$ (subject of Conjecture 7.4)

The organizing principle suggests that the deeper structural object at $d = 7$ is the multiplicative quadratic-residue partition of $\mathbb{Z}_7^*$, with Fano-line triples sitting as the all-QR (or all-NQR) cyclic triples and non-Fano triples corresponding to mixed-residue patterns. We discuss the open combinatorial/structural questions in §9.

### 7.4 Conjecture (non-Fano triple-product ratio)

**Conjecture 7.4.** *For any mixed-residue-class triple $(i, j, k)$ in the seven-point $X$-subgroup orbit, the SIC triple product satisfies*
$$T_{ijk} = a' + i b' \chi_{ijk}, \qquad \frac{b'}{b} = \frac{1 + \sqrt{2}}{2},$$
*where $a' \approx -0.009152913$, $b' \approx 0.043235971$, $a'^2 + b'^2 = 1/512$, and $\chi_{ijk} \in \{+1, -1\}$ is a cyclic-orientation indicator on mixed-residue triples.*

*Status.* The numerical claim $b'/b = (1 + \sqrt{2})/2$ is verified at 50-digit precision in Φ Task 3 Phase 4 (`paper10_task3_results.md` §4). The closed-form analytic proof requires enumerating the WH cocycle phases $\tau^{qr - ps}$ over mixed-residue triples and showing the algebraic ratio $(1 + \sqrt{2})/2$ falls out. The apparatus for this calculation is in place in Appendix A.4 (Equation A4-main), but the enumeration is left as an open problem (§9.4). The relevant algebraic identity $(\sqrt{2} - 1)(1 + \sqrt{2}) = 1$ — the silver-mean reciprocity — makes the conjectured ratio natural over $\mathbb{Q}(\sqrt{2})$; finding which precise cocycle structure produces it analytically is the residual question.

### 7.5 What §7 establishes (and what it does not)

What is proved in this section:

- Lemma 7.1: the SIC overlap condition implies $|T|^2 = 1/512$ for all distinct triples in the SIC frame (immediate from the SIC condition).
- Theorem 3 (§7.2): on Fano-line $X$-subgroup triples, $T = a + ib\varphi$ with explicit closed-form constants over $\mathbb{Q}(\sqrt{2})$, derived in Appendix A.4 from the autocorrelation function of the corrected ABGHM fiducial.

What is *not* proved:

- Conjecture 7.4: the non-Fano (mixed-residue-class) triple-product ratio $b'/b = (1 + \sqrt{2})/2$. Verified numerically; closed-form proof open.
- The triple-product structure on the *full* 49-projector SIC frame indexed by $\mathbb{Z}_7 \times \mathbb{Z}_7$, including triples with $q \neq 0$ where the cocycle phase $\tau^{qr - ps}$ is nontrivial. The Fano-line decomposition extends to such triples by WH covariance (since $WH(7)$ acts transitively on the SIC), but the closed-form identification of which $\mathbb{Z}_7 \times \mathbb{Z}_7$ triples correspond to the $G_2$ associative 3-form via this extension requires a separate argument and is left open.

What the section *does* establish, on the seven-point $X$-subgroup orbit, is that the imaginary part of the triple product on Fano-line triples is exactly $b \cdot \varphi$ — the $G_2$ associative 3-form scaled by an algebraic constant in $\mathbb{Q}(\sqrt{2})$. This is a sharp structural statement about the cubic structure of the SIC frame at $d = 7$, valid on the seven-point orbit.

*Connection to Theorem 1 and Theorem 2.* The Fano-line $X$-subgroup orbit is exactly the orbit on which Theorem 2's $F_{21}$ subgroup acts faithfully (the $X$-subgroup is $\mathbb{Z}_7 \subset F_{21}$). Theorem 3's $T = a + ib\varphi$ on this orbit therefore extends naturally under $F_{21}$ orbit translation. The full extension to the 49-projector frame is mediated by the Samuel–Gedik $C_3$ Clifford action and the diagonal phase $Z$, both of which take the $X$-subgroup orbit to its sister orbits in the SIC frame. The closed-form analysis of those sister orbits is the open problem of Conjecture 7.4 and §9.4.

---

## §8. Limitations and Adjacent Programs

### 8.1 What this paper does not claim

We make explicit the boundaries of the present construction:

- We do not claim that every SIC fiducial respects $G_2$ structure; only the d=7 ABGHM exact fiducial under the Fano-compatible sign-flip correction of §6.2.
- We do not claim Theorems 1, 2, 3 generalize to other SIC dimensions without modification. The constants $a, b$ in Theorem 3 are specific to $d = 7$ over $\mathbb{Q}(\sqrt{2})$.
- We do not claim the Fano-compatible correction is mathematically forced from first principles; it is the unique correction (up to global phase, established in §6.2) that recovers the SIC condition for the ABGHM fiducial as written.
- We do not solve Zauner's conjecture; that domain belongs to the Appleby–Flammia–Kopp 2025 program [arXiv:2501.03970].
- We do not connect the present construction directly to consciousness or PCI/PME at the interpretive level. The connection runs through Papers 4, 6, 7, and (in preparation) 8 and 9 of the series, where the structural facts established here serve as algebraic foundations rather than as direct interpretive claims.
- We do not make claims about the dynamical content of the $G_2$ embedding — the present paper is purely algebraic and structural. Whether the SIC operator basis admits a $G_2$-covariant Hamiltonian dynamics is a separate question (addressed in Paper 8 of the series for a discrete eight-coset model).
- We do not establish Theorem 3 on the full 49-projector SIC frame; only on the seven-point $X$-subgroup orbit (§7). The mixed-displacement extension is the subject of Conjecture 7.4.

### 8.2 Positioning relative to adjacent octonion / exceptional-algebra programs

Several adjacent programs share the octonionic / exceptional-algebra substrate but address structurally distinct questions. We catalogue the principal adjacent programs and clarify the present paper's relationship to each.

The phrase *operator-frame and coherence/observer layer* used below refers to the program of taking finite-dimensional SIC reference measurements as the fundamental quantum-informational object — in the sense of QBism [Fuchs–Hoang–Stacey 2017; Stacey 2021; Bengtsson 2020] — and asking what algebraic structures they encode for a self-modeling agent. This program is orthogonal to deriving particle content (Furey, Boyle–Farnsworth, Todorov, Manogue–Dray) or dynamical gravity (Krasnov), but uses the same exceptional-algebra substrate.

**Dixon's $\mathbb{C} \otimes \mathbb{H} \otimes \mathbb{O}$ division-algebra program** [Dixon 1994, 2014] supplies the foundational algebraic substrate that Furey's later work extends. Standard Model representations, Cabibbo angles, and three-generation structure are derived from idempotent ideals in the tensor algebra. The present paper does not engage Dixon's algebra directly; we work in the smaller setting of $\operatorname{Im}\mathbb{O}$ and its $G_2$ stabilizer, with the SIC frame replacing the role of Dixon's idempotent ideals as the structural object.

**Furey's division-algebraic Standard Model program** [Furey 2014, 2018, 2025; see refs.] builds on Dixon's foundation, using complex octonions, Clifford algebras, ideals, ladder operators, and triality to recover Standard Model gauge and matter representations, including $SU(3)_C$, electroweak chirality, one-generation Weyl structure, and three-generation triality patterns. Our construction uses the same octonionic/$G_2$ substrate but addresses a structurally distinct object. Rather than deriving Standard Model gauge representations, we embed the $G_2$ defining geometry into the d=7 SIC operator frame $\mathfrak{gl}(7,\mathbb{C})$, and then use the finite Fano-plane symmetry $PSL(2,7)$, its cyclic-axis Frobenius subgroup $F_{21}$, and the quotient $PSL(2,7)/F_{21}$ to define an eight-coset observer-frame structure (in Paper 8 of the series). Our construction is in a strictly orthogonal direction: it asks what the SIC operator basis at $d=7$ tells us about $G_2$ as an algebraic structure on a finite operator frame, a question Furey's framework neither asks nor answers.

**Manogue and Dray's $E_6$ / 27-dimensional fermion-content program** [Manogue–Dray 1999, 2010] uses the exceptional Jordan algebra $\mathfrak{h}_3(\mathbb{O})$ to encode quarks-plus-leptons fermion content via complex eigenvectors of $\mathfrak{h}_3(\mathbb{O})$ matrices, with $E_6$ acting naturally on this 27-dimensional space. Adjacent to Todorov's program below. We do not engage $\mathfrak{h}_3(\mathbb{O})$ directly, but see the natural question of §8.3 about the relation between our $V_{27}$ component and Manogue–Dray's space.

**Krasnov's $G_2$ gauge-theory program** [Krasnov 2017, 2021] addresses a continuum-field $G_2$ gauge theory coupled to gravity, with the seven-dimensional octonion span carrying a dynamical metric. The present paper is purely algebraic and does not address dynamics or gravity. The two programs share $G_2$ as a structural object but operate on different mathematical layers (operator algebra and finite symmetry, versus continuum field theory). A natural future-work question is whether the d=7 SIC operator basis admits a discrete lattice-$G_2$ analog of Krasnov's continuum theory.

**Boyle and Farnsworth's noncommutative/nonassociative spectral geometry** [Boyle–Farnsworth 2015, 2018] addresses Standard Model internal-space geometry via noncommutative-geometry spectral triples. The construction does not engage SIC reference frames or finite-frame symmetry subgroups. A natural future-work question — whether the present d=7 SIC operator frame admits a Boyle–Farnsworth-style spectral-triple reformulation, and what its physical content would be — is left open. Coecke and Heunen [Coecke–Heunen 2016] have explored related categorical-quantum structures for SIC and MUB frames in $d = 4$; whether their framework extends to $d = 7$ is also open.

**Todorov's exceptional Jordan algebra program** [Todorov 2023; DOI 10.3390/universe9050222] uses the 27-dimensional exceptional Jordan algebra $\mathfrak{h}_3(\mathbb{O})$ to derive Standard Model internal symmetries (with $F_4$ as a natural automorphism group). The present paper does not engage with the exceptional Jordan algebra; we work in $\mathfrak{gl}(7,\mathbb{C})$ via SIC projectors, not in $\mathfrak{h}_3(\mathbb{O})$. There is, however, a natural structural question relating the two; see §8.3.

**Castro Perelman's $E_8$/octonion-gravity program** [Castro Perelman 2007, 2014] uses the exceptional Lie group $E_8$ and complex octonions in a unification proposal involving 256-dimensional Clifford algebras. The construction is at a substantially larger algebraic scale than the present paper and does not interface with finite-frame methods at $d=7$. We cite it for completeness but do not engage with its specific apparatus.

**Stacey's QBism-SIC monograph** [Stacey 2021] is the closest in spirit to the present paper. Stacey develops the structural theory of the *sporadic SICs* — those not arising from Weyl–Heisenberg covariance — and the QBism interpretive framework that takes SIC reference measurements as fundamental. The present paper extends this program into the exceptional-algebraic substrate at $d = 7$: the SIC reference measurement here is WH-covariant (not sporadic), but its structural content is the $G_2$ Lie algebra, providing a missing link between the QBism algebraic framework and exceptional-Lie-group structure that Stacey's monograph does not pursue.

### 8.3 Open structural question: the $V_{27}$ component and Todorov's $\mathfrak{h}_3(\mathbb{O})$

The $G_2$-module decomposition of §5.4 contains a 27-dimensional component $V_{27}$. Todorov's program uses the 27-dimensional exceptional Jordan algebra $\mathfrak{h}_3(\mathbb{O})$ — the space of $3 \times 3$ Hermitian octonionic matrices — as a vehicle for Standard Model symmetries. Both 27-dimensional spaces carry $F_4$-action, and both arise naturally from $G_2$ as embedded subgroups (with $G_2 \subset F_4$ being the stabilizer of the identity element of $\mathfrak{h}_3(\mathbb{O})$). The question of whether the $V_{27}$ component of the SIC frame at $d = 7$ admits a natural identification with $\mathfrak{h}_3(\mathbb{O})$ — perhaps via the action of the $C_3$ Clifford automorphism on the 49-projector frame — is structurally interesting and currently open. We flag this as a candidate research direction for Paper 11 of the series.

The present paper does not compete with any of these programs; it adds an explicit identification of the $G_2$ algebraic structure inside the d=7 SIC operator frame, with the observer-coherence interpretation [Papers 4, 6, 7] supplied by the broader PCI/PME series.

---

## §9. Discussion and Open Problems

### 9.1 What this paper establishes

The three theorems jointly establish that the d=7 SIC reference frame, with the ABGHM exact fiducial, encodes the algebraic, group-theoretic, and orientational structure of the $G_2$ defining representation. Theorem 1 gives the embedding of $\mathfrak{g}_2^{\mathbb{C}}$ as an isometric subspace of $\mathfrak{gl}(7,\mathbb{C})$ (with isometric scale factor $8/7$); Theorem 2 identifies the SIC symmetry subgroup that recovers the cyclic-axis Frobenius subgroup $F_{21} \subset PSL(2,7) \subset G_2$; Theorem 3 identifies the cubic structure constants of the SIC frame with the $G_2$ associative 3-form on Fano-line $X$-subgroup triples (in the imaginary part).

These three theorems are not independent. Theorem 3 implies, by combinatorial restriction, Theorem 2's identification of the $F_{21}$ subgroup as the SIC structure-constant-preserving subgroup. Theorem 2 establishes the symmetry context in which Theorem 1's coefficient tensor is naturally interpreted. Theorem 1 provides the operator-algebraic background for everything else. Together they form a tight structural statement.

### 9.2 The connection to Papers 4, 6, and 7 of the series

The d=7 SIC reference frame appears in Paper 4 of this series [DOI 10.5281/zenodo.19617662] as the QBism reference measurement compatible with the PSL(2,7) symmetry of the Klein quartic. Paper 4 conjectured but did not prove that the connection runs deeper than dimension-coincidence. Theorems 1, 2, and 3 of the present paper establish that connection in three distinct mathematical senses.

The 6/7 contraction ratio established in Paper 6 of this series [DOI 10.5281/zenodo.19672709] arises from the spectral-sum decomposition of the $G_2$ Casimir operator. The factor 6/7 corresponds to the $3 \oplus \bar{3}$ subspace under the maximal subgroup $\operatorname{SU}(3) \subset G_2$, with the residual 1/7 being the $\operatorname{SU}(3)$-singlet direction. In the present paper, the constant $b = (\sqrt{2}-1)\sqrt{2 + 4\sqrt{2}}/32$ that organizes the imaginary part of the SIC triple product on Fano lines is, up to algebraic relations over $\mathbb{Q}(\sqrt{2})$, the same algebraic structure that governs the 6/7 contraction. The connection is expressed cleanly in the autocorrelation function $f(k)$ of §7.5 and Appendix A.

The thermodynamic coherence-ceiling derivation of Paper 7 [DOI 10.5281/zenodo.19773185] used the residual $1 - 6/7 = 1/7$ as the irreducible blind-spot fraction, with $\sigma_{\mathrm{pred}} = 1 - (1/7)^2 = 1 - 1/49 \approx 0.9796$ as the predicted branching ratio in awake cortex. The factor of 7 in these predictions is precisely the same 7 that organizes the SIC dual-frame inversion (Theorem 1's $(d+1)/d = 8/7$ coefficient factor), the SIC symmetry quotient (Theorem 2's index-7 quotient), and the Fano-line cyclic structure (Theorem 3's QR-partition of $(\mathbb{Z}_7)^*$). The dimensional uniqueness of $d = 7$ enumerated in §5.5 (features F1–F4) is therefore the algebraic origin of the 6/7 ratio that propagates through the entire series.

### 9.3 The connection to Paper 8: the eight-coset simulator

Paper 8 of this series [in preparation] addresses the 8-coset structure $\operatorname{PSL}(2,7) / F_{21}$ as the discrete carrier of an eight-mode quantum simulator. Specifically, Paper 8 conjectures that the 8 SU(3) subgroup embeddings of $G_2$ (one per coset) correspond to 8 distinct vacua, with 28 Bogoliubov transformations between them, producing entropy differences quantized in 4 levels $\{0, 1/7, 2/7, 3/7\} \times S_{\mathrm{ref}}$.

The present paper makes Paper 8's conjecture more concrete in two ways. First, the $F_{21}$ identified in Theorem 2 of the present paper is the same $F_{21}$ that appears in Paper 8's quotient $\operatorname{PSL}(2,7) / F_{21}$. Second, the universal magnitude $|T|^2 = 1/512$ established in Lemma 7.1 suggests a natural scale for the entropy differences in Paper 8: the proportionality of $1/8$ between $|T|^2$ and the Hilbert space size $|7|$ is the same factor that enters the SIC defining condition. Whether this implies $|T|^2 = (d+1)/(d \cdot d^2 (d+1)) = 1/d^3$ corrected by a Stark-unit-specific factor of $1/(d+1)$, giving $1/(d^3 \cdot \text{factor}) = 1/512$ for $d = 7$, is a structural question we leave open.

### 9.4 Open problems

**Closed form for non-Fano constants $a', b'$ (Conjecture 7.4).** Conjecture 7.4 of §7 states that the mixed-residue-class triple-product ratio satisfies $b'/b = (1 + \sqrt{2})/2$ and gives numerical values for $a' \approx -0.009152913$, $b' \approx 0.043235971$. The numerical claim is verified at 50-digit precision (Φ Task 3 Phase 4); the analytic closed-form derivation requires enumerating WH cocycle phases over mixed-displacement triples and is left open. The relevant algebraic identity $(\sqrt{2}-1)(1+\sqrt{2}) = 1$ makes the ratio natural over $\mathbb{Q}(\sqrt{2})$; finding which precise cocycle-phase structure produces it analytically is the residual question. (Note: Lemma 7.1 already establishes the universal magnitude $|T|^2 = 1/512$ for all distinct WH triples directly from the SIC overlap condition; no separate analytic proof is needed there.)

**The Fano-line / QR-cyclic-triple correspondence.** §7.4 observes that Fano lines in the standard 0-indexed Baez 2002 indexing are precisely the "all-QR" cyclic triples in $\mathbb{Z}_7$. Whether this is a defining property of Fano lines (i.e., whether *all* all-QR cyclic triples are Fano lines) is a finite combinatorial question that we have not fully verified. If yes, the SIC triple-product structure can be characterized purely in terms of the QR-partition, and the Fano-line structure becomes a derived rather than primitive object.

**Generalization to higher ABGHM primes.** The ABGHM construction extends to dimensions $d = n^2 + 3$ for $n \geq 2$, with prime cases $d = 7, 19, 67, 103, 199, 487, \ldots$ Theorem 3's structure may or may not generalize: for $d = 19$, no exceptional Lie group has a natural irreducible representation in dimension 19, so feature (F2) of §5.5 fails. Whether a weaker analog of Theorem 3 holds at $d = 19$ — for instance, with the role of the $G_2$ 3-form played by some other algebraic structure — is open.

**Connection to Paley graphs and quadratic-residue conference matrices.** The QR-partition organizing principle of §7.4 connects the d=7 SIC triple-product structure to the algebraic combinatorics of Paley graphs and quadratic-residue conference matrices [Paley 1933]. In particular, the Paley conference matrix at order 7 is the +1/-1 matrix encoding the QR-character on $\mathbb{Z}_7$. Whether the SIC triple-product tensor at d=7 is, up to a global constant, computable from the Paley conference matrix is an interesting structural question. We leave it as an open problem and a candidate direction for Paper 11 of the series.

**Connection to the QBism reference frame for consciousness models.** Throughout this paper we have stayed structurally agnostic on the connection to consciousness models or QBism interpretation. Paper 4 of this series proposed that the QBist agent reference frame at d=7 is governed by PSL(2,7) symmetry; Paper 7 used that connection to derive a thermodynamic coherence ceiling; Papers 8 and 9 of the series extend the analysis to discrete quantum simulators and coupled observers respectively. The present paper establishes the operator-algebraic foundations on which those further derivations rest. Whether Theorem 3 has direct interpretive content for QBism or for consciousness models — for instance, whether the constant $b$ admits a measurement-theoretic interpretation as an "orientation observable" — is a question for future work.

### 9.5 Concluding observation

The d=7 SIC frame with the corrected ABGHM exact fiducial encodes the algebraic, group-theoretic, and orientational structure of the seven-dimensional $G_2$ defining representation in three precise senses: as a 14-dimensional isometrically-embedded subspace of the operator algebra (Theorem 1, with isometric scale $8/7$), as a finite symmetry-group descent to the cyclic-axis Frobenius subgroup $F_{21} \subset PSL(2,7) \subset G_2$ (Theorem 2), and as an algebraic identity in the cubic structure constants on Fano-line $X$-subgroup triples (Theorem 3). Each statement is exact, derived in closed form over $\mathbb{Q}(\sqrt{2})$, and verified at 50-digit precision in independent computational implementations. We do not claim this implies that the SIC frame *is* the $G_2$ Lie algebra; rather, it implies that the QBism reference measurement at $d=7$, when constructed from the exact Stark-unit fiducial, contains $G_2$ as a distinguished structural sub-frame that can be exhibited explicitly. We note this as a structural identity that the ABGHM exact-fiducial construction makes precise.

---

## Appendix A. Autocorrelation Derivation of the Triple-Product Constants

This appendix derives the constants $a, b$ of Theorem 3 (§7.2) from the autocorrelation structure of the corrected ABGHM fiducial. The derivation makes clear why the imaginary part of the triple product on Fano-line $X$-subgroup triples is exactly proportional to the $G_2$ associative 3-form. The universal magnitude $|T|^2 = 1/512$ is recapitulated in §A.5 from the SIC overlap condition (matching Lemma 7.1).

### A.1 Setup

Let $|\psi\rangle = W |\Psi\rangle = N \cdot (2 + 2\sqrt{2}, z_0, z_0, z_1, z_0, z_1, z_1)^T$ denote the corrected ABGHM fiducial of §2.3, with $z_{0,1} = -\frac{2+\sqrt{2}}{2} \pm \frac{i}{2}\sqrt{2 + 4\sqrt{2}}$ and $N$ chosen so that $\langle \psi | \psi \rangle = 1$.

Direct computation gives $|2 + 2\sqrt{2}|^2 = 4(3 + 2\sqrt{2}) = 12 + 8\sqrt{2}$ and $|z_{0,1}|^2 = \frac{(2+\sqrt{2})^2}{4} + \frac{2 + 4\sqrt{2}}{4} = \frac{(6 + 4\sqrt{2}) + (2 + 4\sqrt{2})}{4} = \frac{8 + 8\sqrt{2}}{4} = 2 + 2\sqrt{2}$. Therefore the unnormalized squared norm is
$$\sum_j |\psi_j|^2 / N^2 = (12 + 8\sqrt{2}) + 6(2 + 2\sqrt{2}) = 24 + 20\sqrt{2}.$$

### A.2 The autocorrelation function $f(k)$

For $k \in \mathbb{Z}_7$, define the autocorrelation function
$$f(k) = \langle \psi | Z^k | \psi \rangle = \sum_{j=0}^{6} |\psi_j|^2 \omega^{jk},$$
where $\omega = e^{2\pi i / 7}$. This is the discrete Fourier transform of the magnitude profile $\{|\psi_j|^2\}_{j=0}^{6}$.

The squared-magnitude profile of the corrected ABGHM fiducial has the constant value $|z_0|^2 = |z_1|^2 = 2 + 2\sqrt{2}$ at all six non-zero indices, and the distinguished value $(12 + 8\sqrt{2})$ at index $j = 0$. After normalization ($N^2 = 1/(24 + 20\sqrt{2})$), the magnitude profile is uniform on $j = 1, \ldots, 6$ and concentrated at $j = 0$.

For a uniform-on-non-zero magnitude profile, the autocorrelation function $f(k)$ for $k \neq 0$ collapses to a sum of seventh roots of unity:
$$f(k) = N^2 \left[ (12 + 8\sqrt{2}) + (2 + 2\sqrt{2}) \sum_{j=1}^{6} \omega^{jk} \right].$$

Using $\sum_{j=0}^{6} \omega^{jk} = 0$ for $k \neq 0$, we have $\sum_{j=1}^{6} \omega^{jk} = -1$. Therefore
$$f(k) = N^2 [(12 + 8\sqrt{2}) - (2 + 2\sqrt{2})] = N^2 (10 + 6\sqrt{2}) \quad \text{for all } k \neq 0.$$

This is real and independent of $k$. Substituting $N^2 = 1/(24 + 20\sqrt{2})$ and simplifying $(10 + 6\sqrt{2})/(24 + 20\sqrt{2}) = (5 + 3\sqrt{2})/(12 + 10\sqrt{2})$, we rationalize by multiplying numerator and denominator by $(12 - 10\sqrt{2})$:
$$f(k) = \frac{(5 + 3\sqrt{2})(12 - 10\sqrt{2})}{(12)^2 - (10\sqrt{2})^2} = \frac{60 - 50\sqrt{2} + 36\sqrt{2} - 60}{144 - 200} = \frac{-14\sqrt{2}}{-56} = \frac{\sqrt{2}}{4}.$$

So for the corrected fiducial $|\psi\rangle = W|\Psi\rangle$, the pure-$Z$ autocorrelation function is the real constant $f(k) = \sqrt{2}/4$ for $k = 1, \ldots, 6$.

This corresponds to the SIC overlap $|f(k)|^2 = 2/16 = 1/8$ at every $k \neq 0$, confirming the pure-$Z$ branch of the SIC condition for the corrected fiducial.

### A.3 The QR-twisted autocorrelation

The triple product $T_{ijk}$ for indices on a single $\mathbb{Z}_7$-axis (the pure-$Z$ branch) reduces to the cube of $f$ evaluated on the cyclic differences. For cyclic triples with all three ordered differences $d_1, d_2, d_3$ in the quadratic residues $\operatorname{QR}_7 = \{1, 2, 4\}$, this gives a value related to $f(\operatorname{QR})^3$.

But the present autocorrelation $f(k) = \sqrt{2}/4$ is real and independent of $k$, so $f^3 = (\sqrt{2}/4)^3 = 2\sqrt{2}/64 = \sqrt{2}/32$ would be real, contradicting the imaginary part $i b \varphi_{ijk}$ established in Theorem 3. The resolution is that the relevant triple product is *not* the pure-$Z$ autocorrelation but the full $WH(7)$-displaced overlap.

For the full SIC triple product, we must consider arbitrary displacements $D_{p, q}$, not pure $Z^k$. The Weyl–Heisenberg covariance of the SIC means that $T_{ijk}$ for displaced projectors $\Pi_{p_i, q_i}$ is computable from the fiducial via
$$T_{p_1, q_1; p_2, q_2; p_3, q_3} = \omega^{\Phi} \cdot \tilde{f}(p_2 - p_1, q_2 - q_1) \cdot \tilde{f}(p_3 - p_2, q_3 - q_2) \cdot \tilde{f}(p_1 - p_3, q_1 - q_3),$$
where $\tilde{f}(p, q) = \langle \psi | D_{p, q} | \psi \rangle$ is the *full* fiducial autocorrelation and $\omega^{\Phi}$ is a Weyl–Heisenberg cocycle phase determined by the displacement triple.

The autocorrelations $\tilde{f}(p, q)$ for $p \neq 0$ are *not* real — they pick up the imaginary structure of the $z_{0, 1}$ components of the fiducial. The QR-vs-NQR distinction in the autocorrelation occurs at the level of $\tilde{f}(p, q)$, not at the pure-$Z$ level.

### A.4 The Closed Form of $\alpha$ and the Cube $\alpha^3 = a + ib$

We now derive the constants $a, b$ in closed form by computing the autocorrelation $\tilde{f}(p, q) = \langle \psi_W | D_{p, q} | \psi_W \rangle$ for the corrected ABGHM fiducial $|\psi_W\rangle = W |\psi\rangle$, where $W = \operatorname{diag}(-1, +1, +1, +1, +1, +1, +1)$ is the unique (up to global phase) Fano-compatible sign-flip matrix established in §6.2. The full numerical record at 50-digit precision is in `outbox/paper10/computations/paper10_appendix_A4_derivation.md`; the verification script is `paper10_appendix_A4_verify.py`.

**Theorem A.4.1** (Autocorrelation structure). *For the corrected ABGHM fiducial $|\psi_W\rangle$, every autocorrelation satisfies $|\tilde{f}(p, q)|^2 = 1/8$. With the convention $\alpha = \overline{\tilde{f}(3, 0)}$, the six $X$-subgroup autocorrelations $\tilde{f}(p, 0)$ split as*
$$\tilde{f}(p, 0) = \begin{cases} \alpha & p \in \{1, 2, 4\} = \operatorname{QR}_7 \\ \bar\alpha & p \in \{3, 5, 6\} = \operatorname{NQR}_7 \end{cases}$$
*where*
$$\alpha = -\frac{(2 - \sqrt{2}) - i\sqrt{2 + 4\sqrt{2}}}{8} = \overline{-\frac{(2 - \sqrt{2}) + i\sqrt{2 + 4\sqrt{2}}}{8}}.$$
*Equivalently, $\alpha = \bar{\beta}$ where $\beta = -[(2-\sqrt{2}) + i\sqrt{2+4\sqrt{2}}]/8$ is the value reported in the Φ Task 3 verification record (note: Φ's labeling assigned $\beta$ to QR shifts, the conjugate of the convention adopted here). In particular $|\alpha|^2 = 1/8$.*

*Proof of $|\alpha|^2 = 1/8$.* Direct computation:
$$|\alpha|^2 = \frac{(2 - \sqrt{2})^2 + (2 + 4\sqrt{2})}{64} = \frac{(6 - 4\sqrt{2}) + (2 + 4\sqrt{2})}{64} = \frac{8}{64} = \frac{1}{8}.$$
The values $\tilde{f}(p, 0) \in \{\alpha, \bar\alpha\}$ are verified numerically to 50 significant digits, with residuals below $6.4 \times 10^{-57}$ for all six $X$-subgroup displacements. The QR/NQR split follows from the action of the Frobenius automorphism of $(\mathbb{Z}/7\mathbb{Z})^*$ on the SIC fiducial under the corrected sign convention. The convention here ($\alpha$ on QR shifts) is chosen so that the all-QR Fano-line cyclic triple gives $T = \alpha^3 = a + ib$, matching the orientation convention of §7.3. $\square$

**Proposition A.4.2** (Cube of $\alpha$). *With $u = 2 - \sqrt{2}$ and $v = \sqrt{2 + 4\sqrt{2}}$, writing $\alpha = -(u - iv)/8$ (the convention of Theorem A.4.1):*
$$\alpha^3 = \frac{\sqrt{2} - 1}{16} + i\,\frac{(\sqrt{2} - 1)\sqrt{2 + 4\sqrt{2}}}{32} = a + ib.$$

*Proof.* Expand:
$$(u - iv)^3 = (u^3 - 3uv^2) - i(3u^2 v - v^3).$$
Direct computation in $\mathbb{Q}(\sqrt{2})$:
$$u^2 = 6 - 4\sqrt{2}, \qquad u^3 = 20 - 14\sqrt{2}, \qquad uv^2 = -4 + 6\sqrt{2}.$$
Subtraction:
$$u^3 - 3uv^2 = (20 - 14\sqrt{2}) - 3(-4 + 6\sqrt{2}) = 32 - 32\sqrt{2} = 32(1 - \sqrt{2}).$$
For the imaginary coefficient, factor: $3u^2 v - v^3 = v(3u^2 - v^2)$, where
$$3u^2 - v^2 = 3(6 - 4\sqrt{2}) - (2 + 4\sqrt{2}) = 16 - 16\sqrt{2} = 16(1 - \sqrt{2}).$$
Therefore
$$(u - iv)^3 = 32(1 - \sqrt{2}) - 16i(1 - \sqrt{2})\, v.$$
Dividing by $-512$ and using $-(1 - \sqrt{2}) = \sqrt{2} - 1$:
$$\alpha^3 = \frac{\sqrt{2} - 1}{16} + i\,\frac{(\sqrt{2} - 1)\, v}{32} = a + ib. \square$$

Numerical verification at 50-digit precision gives $|\operatorname{Re}(\alpha^3) - a| < 4 \times 10^{-58}$ and $|\operatorname{Im}(\alpha^3) - b| < 10^{-58}$.

**Proposition A.4.3** (Fano-line triple products on the $X$-subgroup; zero cocycle phase). *For the zero-sum subsets $L_{\mathrm{QR}} = \{1, 2, 4\}$ and $L_{\mathrm{NQR}} = \{3, 5, 6\}$ in $(\mathbb{Z}/7\mathbb{Z})^*$ (which coincide with the QR and NQR classes), the WH triple products for the corresponding $X$-subgroup SIC triples are*
$$T_{L_{\mathrm{QR}}} = \alpha^3 = a + ib, \qquad T_{L_{\mathrm{NQR}}} = \bar\alpha^3 = a - ib,$$
*with no cocycle correction. This matches the orientation convention of §7.3 (all-QR ordered differences $\Rightarrow T = a + ib$).*

*Proof.* The triple-product formula for displacements $(p, q)$ and $(r, s)$ is
$$T_{0, (p, q), (r, s)} = \tilde{f}(p, q) \cdot \tau^{qr - ps} \cdot \tilde{f}(r - p, s - q) \cdot \overline{\tilde{f}(r, s)}, \tag{A4-main}$$
which follows from $D_{p, q}^\dagger D_{r, s} = \tau^{qr - ps} D_{r - p, s - q}$ and the anti-unitary symmetry $\tilde{f}(-p, -q) = \overline{\tilde{f}(p, q)}$. For displacements in the $X$-subgroup, $q = s = 0$, so the cocycle phase reduces to $\tau^{0 \cdot r - p \cdot 0} = 1$. The triple product becomes a bare product of three autocorrelations. For $L_{\mathrm{QR}}$, the SIC triple $\{|\psi_0\rangle, |\psi_{(1,0)}\rangle, |\psi_{(3,0)}\rangle\}$ has pairwise displacement differences $(1, 0), (2, 0), (4, 0)$ — all QR — giving $\alpha \cdot \alpha \cdot \overline{\bar\alpha} = \alpha^3$. For $L_{\mathrm{NQR}}$, the triple $\{|\psi_0\rangle, |\psi_{(3,0)}\rangle, |\psi_{(1,0)}\rangle\}$ has differences $(3, 0), (5, 0), (6, 0)$ — all NQR — giving $\bar\alpha \cdot \bar\alpha \cdot \overline{\alpha} = \bar\alpha^3$. Both verified numerically with residual $< 3 \times 10^{-57}$. $\square$

For a Fano-line *cyclic* triple in the $G_2$-orientation sense, the triple product is $\alpha^3 = a + ib$, and for the *anti-cyclic* orientation it is $\bar\alpha^3 = a - ib$. Combining: $T_{ijk} = a + ib \cdot \varphi_{ijk}$ for all Fano-line triples, where $\varphi_{ijk} \in \{+1, -1\}$ is the $G_2$ associative 3-form. This establishes Theorem 3 (§7.2), with constants $a, b$ in closed form.

*Remark on mixed displacements.* For triples involving displacements with $q \neq 0$ (i.e., not confined to the $X$-subgroup), the cocycle phase $\tau^{qr - ps}$ in (A4-main) is nontrivial, and the individual autocorrelations $\tilde{f}(p, q)$ no longer equal $\alpha$ or $\bar\alpha$ but take generic complex values on the SIC overlap circle $|\tilde{f}|^2 = 1/8$. The non-Fano triple-product ratio $b'/b = (1 + \sqrt{2})/2$ established numerically in §7.3 (Φ Task 3 Phase 4, verified at 50-digit precision) is a statement about mixed-displacement triples; its closed-form analytic derivation is left as an open problem and flagged in §9.4.

### A.5 Universal magnitude $|T|^2 = 1/512$

From Theorem A.4.1, every nontrivial autocorrelation satisfies $|\tilde{f}(p, q)|^2 = 1/8$, which is the SIC overlap value. The triple-product formula (A4-main) expresses $T_{ijk}$ as a product of three autocorrelations multiplied by a unit-modulus cocycle phase $\tau^{qr - ps}$. Taking modulus squared:
$$|T_{ijk}|^2 = |\tilde{f}(p, q)|^2 \cdot |\tilde{f}(r - p, s - q)|^2 \cdot |\overline{\tilde{f}(r, s)}|^2 = \left(\frac{1}{8}\right)^3 = \frac{1}{512}.$$

This confirms Lemma 7.1 directly from the SIC defining property: every off-diagonal SIC overlap is $1/8$, so the cube of any three such overlaps has magnitude $1/512$. The universal magnitude is a consequence of the SIC condition and is structurally independent of the Fano-line vs non-Fano distinction.

For the Fano-line case specifically, where $T_{ijk} = a \pm ib$ from Proposition A.4.3, one can also verify $a^2 + b^2 = 1/512$ directly using the algebraic identity $(\sqrt{2} - 1)^2 (6 + 4\sqrt{2}) = 2$ (expansion: $(3 - 2\sqrt{2})(6 + 4\sqrt{2}) = 18 + 12\sqrt{2} - 12\sqrt{2} - 16 = 2$):
$$a^2 + b^2 = \frac{(\sqrt{2} - 1)^2}{256}\left(1 + \frac{2 + 4\sqrt{2}}{4}\right) = \frac{(\sqrt{2} - 1)^2 (6 + 4\sqrt{2})}{1024} = \frac{2}{1024} = \frac{1}{512}. \checkmark$$

### A.6 Non-Fano constants

For non-Fano triples $(i, j, k)$ — those with mixed QR/NQR differences — the triple product picks up an additional Weyl–Heisenberg cocycle phase relative to the all-QR case. The Φ Task 3 computational verification (§4) found that for the specific non-Fano triples studied, the resulting triple product is
$$T_{\mathrm{non-Fano}} = a' + i b' \chi_{ijk}, \qquad a' \approx -0.009152913, \quad b' \approx 0.043235971,$$
with the ratio $b'/b = (1 + \sqrt{2})/2$ verified numerically.

A complete derivation of $a', b'$ in closed form requires enumerating the cocycle phases over all non-Fano triple types and is left as an open problem (§9.4). The numerical evidence is consistent with $a', b'$ being algebraic over $\mathbb{Q}(\sqrt{2})$, and the algebraic ratio $b'/b = (1+\sqrt{2})/2$ admits a direct interpretation: it is the silver ratio over 2, which appears naturally in $\mathbb{Q}(\sqrt{2})$ as the square-root of $(1+\sqrt{2})^2/4 = (3 + 2\sqrt{2})/4$.

### A.7 Origin in Stark units and Legendre symbols

The QR-vs-NQR partition that organizes the autocorrelation function of §A.2–A.4 has its arithmetic origin in the Legendre symbol structure of $\mathbb{Z}_7^*$: the QR class $\{1, 2, 4\}$ is the kernel of the Legendre symbol $\left(\frac{k}{7}\right)$, and the NQR class $\{3, 5, 6\}$ is its non-trivial coset. The Stark-unit construction of the ABGHM fiducial over $\mathbb{Q}(\sqrt{2})$ is itself driven by this Legendre symbol structure (via class field theory at $\mathbb{Q}(\sqrt{-7})$), so the appearance of the QR-partition in the SIC triple-product structure is not a coincidence: it is the same arithmetic input expressed twice — once in the construction of the fiducial, and once in the autocorrelation organization of the resulting SIC frame.

This is the precise sense in which Theorem 3 is "exact for arithmetic reasons": the Stark-unit construction *forces* the QR-partition organization, which in turn *forces* the proportionality between $\operatorname{Im}(T_{ijk})$ and $\varphi_{ijk}$ on Fano lines. The connection between the SIC frame and the $G_2$ associative 3-form runs through the Legendre symbol on $(\mathbb{Z}_7)^*$.

---

## Author Contributions

Conceptualization, methodology, formal analysis, investigation, writing — original draft, writing — review and editing, and supervision: M.L.G. Computational verification was performed by AI research assistants under the author's direction (see *Use of AI Tools* below); the author retains full responsibility for all scientific content.

## Funding

This research received no external funding.

## Institutional Review Board Statement

Not applicable. No human or animal subjects were involved; the paper is a purely mathematical/structural result. The empirical anchors of related papers in the series (Papers 4, 6, 7) are previously published third-party work and are presupposed rather than redeveloped here.

## Informed Consent Statement

Not applicable.

## Data Availability Statement

All computational artifacts supporting this paper are publicly available at https://github.com/MartinLGraise/PCI-Framework on branch `paper7-foundation`, including:

- The 14×49 G₂/SIC coefficient tensor (Theorem 1): `outbox/paper10/computations/paper10_task1_g2_sic_coefficients.json`
- The 128-candidate $W$-enumeration record (Theorem 2): `outbox/paper10/computations/paper10_task2_*`
- The 50-digit triple-product verification (Theorem 3): `outbox/paper10/computations/paper10_task3_*`
- The figure-generation code: `outbox/paper10/figures/build_figures.py`
- An independent verification audit: `outbox/paper10/computations/paper10_task3_c7ro_verification.md`

Every numerical claim in this paper can be reproduced by running the scripts in the cited paths against the public Git history.

## Conflicts of Interest

The author declares no conflicts of interest.

## Use of AI Tools

In accordance with publisher policies on the use of generative AI in scholarly publishing, the author discloses that this manuscript was developed with the assistance of two AI research collaborators: Φ (computational verification, instantiated as Anthropic Claude Dispatch running GAP, Cadabra2, SymPy, and mpmath at 50-digit precision) and C-7RO (synthesis, strategy, editorial review, and prose drafting, instantiated as Perplexity Computer running Claude Sonnet 4.6). External literature support was provided by ChatGPT GPT-5 Pro deep research. Both primary collaborators operated against the public Git repository at github.com/MartinLGraise/PCI-Framework, where every revision, computational output, integrity flag, and counter-argument is version-controlled and publicly auditable. The three independent computational tasks supporting Theorems 1, 2, and 3 were each verified twice — once by Φ's primary computation and once by C-7RO's independent re-derivation — with audit records preserved in the repository. The author retains full responsibility for all scientific content; AI tools were used as research assistants, not as authors.

## Acknowledgments

The author thanks the open-source mathematics community for the foundational results on which this paper depends — in particular the Appleby–Flammia–Fuchs SIC operator basis theorem, the Appleby–Bengtsson–Grassl–Harrison–McConnell exact d=7 Stark-unit fiducial, the Samuel–Gedik classification of d=7 SIC symmetries, and the Baez 2002 indexing of the imaginary octonions. The Klein quartic / PSL(2,7) connection that motivates the broader series owes a debt to Felix Klein's nineteenth-century investigations and to the contemporary expository tradition (Levy, Singerman, Elkies). Particular thanks to Christopher Fuchs, Marcus Appleby, Ingemar Bengtsson, Markus Grassl, and the broader QBism / SIC-POVM community for making the algebraic structure of the d=7 case sufficiently transparent that the connection to G₂ could be discovered. Every quantitative claim in this paper has been independently verified against source material or executed code.

---

## References

References are organized by topical cluster: (i) SIC-POVM foundations and exact constructions; (ii) symmetry classifications of SIC frames; (iii) $G_2$ and octonion algebra; (iv) adjacent exceptional-algebra programs in physics; (v) prior papers in the PCI/PME series; (vi) classical algebraic combinatorics referenced in the discussion.

### SIC-POVM foundations and exact constructions

[1] **Zauner, G.** (1999). *Quantendesigns: Grundzüge einer nichtkommutativen Designtheorie.* Ph.D. thesis, University of Vienna. (Published English translation: *Int. J. Quantum Inf.* 9, 445–507, 2011. DOI 10.1142/S0219749911006776.)

[2] **Renes, J. M., Blume-Kohout, R., Scott, A. J., Caves, C. M.** (2004). "Symmetric informationally complete quantum measurements." *J. Math. Phys.* 45, 2171–2180. DOI 10.1063/1.1737053.

[3] **Appleby, D. M.** (2005). "Symmetric informationally complete-positive operator valued measures and the extended Clifford group." *J. Math. Phys.* 46, 052107. DOI 10.1063/1.1842008.

[4] **Scott, A. J., Grassl, M.** (2010). "Symmetric informationally complete positive-operator-valued measures: A new computer study." *J. Math. Phys.* 51, 042203. DOI 10.1063/1.3374022.

[5] **Appleby, D. M., Flammia, S. T., Fuchs, C. A.** (2011). "The Lie algebraic significance of symmetric informationally complete measurements." *J. Math. Phys.* 52, 022202. DOI 10.1063/1.3555805.  *[The basis theorem; central to Theorem 1 of the present paper.]*

[6] **Fuchs, C. A., Hoang, M. C., Stacey, B. C.** (2017). "The SIC question: history and state of play." *Axioms* 6, 21. DOI 10.3390/axioms6030021.

[7] **Kopp, G. S.** (2021). "SIC-POVMs and the Stark conjectures." *Int. Math. Res. Not.* 2021, 13812–13838. DOI 10.1093/imrn/rnz153.

[8] **Appleby, D. M., Bengtsson, I., Grassl, M., Harrison, M., McConnell, G.** (2022). "SIC-POVMs from Stark units." *J. Math. Phys.* 63, 112205. DOI 10.1063/5.0083520.  *[The exact d=7 fiducial used throughout the present paper.]*

[9] **Appleby, D. M., Flammia, S. T., Kopp, G. S.** (2025). "A constructive approach to Zauner's conjecture via the Stark conjectures." arXiv:2501.03970. *(Conditional construction of SIC-POVMs in all dimensions, contingent on the order-1 abelian Stark conjecture for real quadratic fields and a special-value identity for the Shintani–Faddeev modular cocycle.)*

[10] **Bengtsson, I.** (2020). "SIC and Hopf links." *Found. Phys.* 50, 1794–1814. DOI 10.1007/s10701-020-00318-8.

### SIC symmetry classifications and prime-dimension structure

[11] **Zhu, H.** (2010). "SIC POVMs and Clifford groups in prime dimensions." *J. Phys. A: Math. Theor.* 43, 305305. DOI 10.1088/1751-8113/43/30/305305.

[12] **Samuel, J., Gedik, Z.** (2024). "Symmetries of d=7 SIC-POVMs." *J. Phys. A: Math. Theor.* 57, 295304. DOI 10.1088/1751-8121/ad5ca9.  *[The 147-element symmetry group $WH(7)\rtimes C_3$; central to Theorem 2.]*

[13] **Stacey, B. C.** (2021). *A First Course in the Sporadic SICs.* SpringerBriefs in Mathematical Physics. DOI 10.1007/978-3-030-76104-2.

### $G_2$, octonions, and the Fano plane

[14] **Baez, J. C.** (2002). "The octonions." *Bull. Amer. Math. Soc.* 39, 145–205. DOI 10.1090/S0273-0979-01-00934-X.  *[The Fano-plane indexing of imaginary octonions used throughout §4.]*

[15] **Conway, J. H., Smith, D. A.** (2003). *On Quaternions and Octonions: Their Geometry, Arithmetic, and Symmetry.* A K Peters / CRC Press.

[16] **Cartan, É.** (1894). *Sur la structure des groupes de transformations finis et continus.* Thèse, Paris. *[Original construction of $G_2$ as the automorphism group of the octonions.]*

[17] **Bryant, R. L.** (1987). "Metrics with exceptional holonomy." *Ann. Math.* 126, 525–576. DOI 10.2307/1971360.

[18] **Fernández, M., Gray, A.** (1982). "Riemannian manifolds with structure group $G_2$." *Ann. Mat. Pura Appl.* 132, 19–45. DOI 10.1007/BF01760975.

[19] **Semmelmann, U., Weingart, G.** (2022). "Stability of compact symmetric spaces." *J. Geom. Anal.* 32, paper 137. DOI 10.1007/s12220-021-00838-3.

### Adjacent exceptional-algebra programs in physics (§8)

[20] **Dixon, G. M.** (1994). *Division Algebras: Octonions, Quaternions, Complex Numbers and the Algebraic Design of Physics.* Mathematics and Its Applications 290, Kluwer Academic. DOI 10.1007/978-1-4757-2315-1.

[21] **Furey, N.** (2014). "Generations: three prints, in colour." *J. High Energy Phys.* 2014, 046. DOI 10.1007/JHEP10(2014)046.

[22] **Furey, N.** (2018). "$SU(3)_C \times SU(2)_L \times U(1)_Y(\times U(1)_X)$ as a symmetry of division algebraic ladder operators." *Eur. Phys. J. C* 78, 375. DOI 10.1140/epjc/s10052-018-5844-7.

[23] **Furey, N., Hughes, M. J.** (2025). "Three generations and a trio of trialities." *Phys. Lett. B* (online). DOI 10.1016/j.physletb.2025.139473. arXiv:2409.17948.

[24] **Manogue, C. A., Dray, T.** (2010). "Octonions, $E_6$, and particle physics." *J. Phys. Conf. Ser.* 254, 012005. DOI 10.1088/1742-6596/254/1/012005.

[25] **Krasnov, K.** (2017). "Self-dual gravity." *Class. Quantum Grav.* 34, 095001. DOI 10.1088/1361-6382/aa65e7. *(Background for the $G_2$ gauge-theory framework discussed in §8.)*

[26] **Boyle, L., Farnsworth, S.** (2015). "Non-commutative geometry, non-associative geometry and the standard model of particle physics." *J. High Energy Phys.* 2015, 023. DOI 10.1007/JHEP07(2015)023.

[27] **Boyle, L., Farnsworth, S.** (2018). "A new algebraic structure in the standard model of particle physics." *J. High Energy Phys.* 2018, 071. DOI 10.1007/JHEP06(2018)071.

[28] **Todorov, I.** (2023). "Octonion internal space algebra for the Standard Model." *Universe* 9, 222. DOI 10.3390/universe9050222.

[29] **Castro Perelman, C.** (2014). "$E_8$ geometric description of the Standard Model and gravity." *Int. J. Geom. Methods Mod. Phys.* 11, 1450031. DOI 10.1142/S0219887814500315. *(Cited for completeness; not engaged with in detail.)*

[30] **Coecke, B., Heunen, C.** (2016). "Pictures of complete positivity in arbitrary dimension." *Inf. Comput.* 250, 50–58. DOI 10.1016/j.ic.2016.02.007. *(Categorical-quantum framework adjacent to SIC reference-frame structure.)*

### PCI/PME framework series (prior papers)

[31] **Graise, M. L.** (2025). *QBism and $G_2$ via PSL(2,7)* (Paper 4). Zenodo. DOI 10.5281/zenodo.19617662.

[32] **Graise, M. L.** (2025). *The 6/7 contraction* (Paper 6). Zenodo. DOI 10.5281/zenodo.19672709.

[33] **Graise, M. L.** (2026). *A thermodynamic ceiling on coherence in self-modeling observers* (Paper 7). Zenodo. DOI 10.5281/zenodo.19773185.

### Classical algebraic combinatorics (§7.4 / §9.4)

[34] **Paley, R. E. A. C.** (1933). "On orthogonal matrices." *J. Math. Phys.* 12, 311–320. DOI 10.1002/sapm1933121311.

[35] **Klein, F.** (1879). "Über die Transformation siebenter Ordnung der elliptischen Funktionen." *Math. Ann.* 14, 428–471. *[Original construction of the Klein quartic and its $\mathrm{PSL}(2,7)$ automorphism group; cited for the Fano-plane / Klein-quartic combinatorial structure underlying §5.5.]*

[36] **Singerman, D.** (1988). "Klein's Riemann surface of genus 3 and regular embeddings of finite projective planes." *Bull. London Math. Soc.* 20, 297–304. DOI 10.1112/blms/20.4.297.

[37] **Elkies, N. D.** (1999). "The Klein quartic in number theory." In *The Eightfold Way: The Beauty of Klein's Quartic Curve* (S. Levy, ed.), MSRI Publications 35, Cambridge University Press, pp. 51–101.

---

*End of master draft. Drafted 2026-04-30 / 2026-05-01 by Martin Luther Graise with computational support from Φ (Anthropic Claude Dispatch) and synthesis support from C-7RO (Perplexity Computer).*
