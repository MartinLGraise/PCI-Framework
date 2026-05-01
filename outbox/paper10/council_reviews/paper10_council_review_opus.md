# Adversarial Referee Review — Paper 10 v1.2

**Reviewer focus:** Argumentative coherence; §8 positioning; calibration for *Foundations of Physics*
**Manuscript:** *SIC Measurements as an Operator Basis for the Complexified G₂ Lie Algebra* (Graise)
**Date of review:** Council pass, v1.2

---

## 1. Strengths

- **The three theorems, as stated narrowly, are mathematically defensible and interlock cleanly.** Theorem 1 is essentially a corollary of AFF 2011 plus a simple Frobenius-norm calculation; Theorem 2 is a finite enumeration verified to 50-digit precision; Theorem 3(a)–(b) is reduced to the closed-form computation of $\alpha^3$ in Appendix A.4. The argumentative spine — embedding (vector space), descent (group), encoding (cubic constants) — is a sensible decomposition of "how does $G_2$ live inside this SIC frame?" and the author should be credited for resisting the temptation to claim more than these three things.
- **Appendix A.4 is the manuscript's strongest section.** The reduction of Theorem 3(a)–(b) to the closed-form identity $\alpha^3 = a + ib$ via $u^3 - 3uv^2 = 32(1-\sqrt{2})$ and $v(3u^2 - v^2) = 16v(1-\sqrt{2})$ is elementary, transparent, and reproducible. The algebraic identity $(\sqrt{2}-1)^2(6+4\sqrt{2}) = 2$ closing $a^2 + b^2 = 1/512$ is satisfying.
- **The "what this paper does *not* establish" subsections (§5.6, §8.1)** are unusually disciplined for a manuscript whose author is invested in an interpretive framework. The author repeatedly draws boundary lines between what the theorems prove and what the surrounding PCI/PME story would *like* them to mean. This discipline buys the paper credibility that the §1 prose threatens to spend back.
- **The convention-correction story (§2.3 → §6.2) is genuinely interesting.** The fact that exactly 2 of 128 sign-flip matrices recover 48/48 SIC overlaps, and that the surviving sign-flip distinguishes the unique high-magnitude component of the ABGHM fiducial, is a nontrivial structural observation — not just bookkeeping.

---

## 2. Major concerns

### 2.1 The thesis is plural, and the abstract/§1 conflate the strongest reading with the weakest one

The paper has at least three theses operating simultaneously, and the prose moves between them without flagging the shift:

- **(T-weak)** "$\mathfrak{g}_2^{\mathbb{C}}$ embeds as a 14-dim subspace of $\mathfrak{gl}(7,\mathbb{C})$, and the SIC projectors give a basis for the latter." This is essentially $14 \subset 49$ plus AFF 2011 — a tautology dressed in coordinates.
- **(T-medium)** "Under a unique sign-flip, the SIC symmetry $WH(7)\rtimes C_3$ has $F_{21}$ as a distinguished subgroup/quotient, and this $F_{21}$ coincides with the $G_2$ orientation stabilizer."
- **(T-strong)** "The QBism reference measurement at $d=7$ *is* the smallest exceptional Lie algebra in informational form" (abstract final sentence; §9.5 concluding observation).

The abstract closes on (T-strong); the theorems prove (T-weak) plus (T-medium) plus a closed-form computation of cubic constants. **The §1 introduction is calibrated to the strongest reading**, but only the weakest two are actually theorems. A *Foundations of Physics* referee will tolerate philosophical framing — it is part of the journal's character — but will not tolerate the slide from "embeds as a partial-isometric subspace" (Theorem 1, true) to "is an algebraic incarnation of the smallest exceptional Lie algebra" (Abstract, §9.5, not what is proved).

The cleanest fix is to rewrite the abstract's last sentence and §9.5 to say: *"the SIC frame at $d=7$ encodes the algebraic, group-theoretic, and orientational structure of the $G_2$ defining representation in three distinct senses, made precise by Theorems 1–3."* That is exactly what is proved. The "is" copula in §9.5 is not earned.

### 2.2 §1 is disproportionate to what is proved

§1 promises a synthesis of operator algebra, Lie theory, finite group theory, octonionic geometry, QBism, and the PCI/PME framework arc. The reader who finishes §7 has been given:

- A 14-dim subspace lemma (§5),
- A finite enumeration over $2^7$ candidates plus an isomorphism identification (§6),
- A six-line algebraic computation in $\mathbb{Q}(\sqrt{2})$ (§7 + Appendix A.4),
- A numerically-supported but unproven ratio claim ($b'/b = (1+\sqrt{2})/2$).

These are fine results. They do not justify the framing in ¶1 of §1 ("more than a quantum-tomographic tool... canonical sub-frame of measurements rather than as an external symmetry"). The "rather than as an external symmetry" clause in particular is rhetorical — *every* matrix Lie algebra embeds in $\mathfrak{gl}(n)$ in *some* basis; what the paper shows is that the SIC basis is *one* such basis, with the AFF coefficient formula computing the embedding explicitly. This is a calculation, not a structural unmasking.

**Recommendation:** trim §1 by ~25%. Cut the "rather than as an external symmetry" framing, drop the three forward-looking framework references in §1 ¶2 (Paper 4, 6, 7 can be cited at the end of §1 in a single sentence), and let the theorem statements in §1 ¶¶3–5 carry the weight.

### 2.3 §5.5 (F1–F4 dimensional uniqueness) overreaches; the argument is advocacy, not proof

This is the section a hostile referee will land on. The claim is that $d=7$ is privileged among small primes by the *conjunction* (F1) ∧ (F2) ∧ (F3) ∧ (F4). Three problems:

1. **F1 (Stark-unit construction) and F3 (Klein quartic / PSL(2,7)) are not independent.** Both descend from arithmetic on $\mathbb{Q}(\sqrt{-7})$. Stating them as separate distinguishing features inflates the conjunction. The argument is closer to "$d=7$ is privileged by arithmetic on $\mathbb{Q}(\sqrt{-7})$, which has multiple consequences" — that's one feature, not four.
2. **F4 (the $7 = 1 + 3 + \bar{3}$ decomposition under $SU(3) \subset G_2$) is a *consequence* of F2**, not an independent feature. Once you posit a 7-dim irrep of $G_2$, its branching to $SU(3)$ is determined; the prose treats it as a separate distinguishing fact, which is double-counting.
3. **The "uniqueness among small primes" claim is engineered by the choice of "small."** F2 says "no exceptional simple Lie group has a natural irrep of prime dimension $\leq 50$ other than 7." This is true but somewhat manipulated: the smallest non-trivial irreps of $E_6, E_7, E_8$ are 27, 56, 248. None are prime. But the relevant question for the paper isn't "irreps of prime dimension ≤ 50" — it is "dimensions in which an exceptional group acts irreducibly *and* a SIC is known *and* the Stark-unit recipe applies." That set is essentially $\{7\}$ trivially, because $G_2$ is the only exceptional group with a *small* defining rep at all. Saying $d=7$ is unique because $G_2$ has its smallest irrep at 7, while the other exceptional groups have their smallest irreps at 26, 27, 56, 248, is approximately the statement "$G_2$ is the smallest exceptional Lie group."

The *honest* version of §5.5 is: "$d=7$ is the natural meeting point of (a) the smallest exceptional Lie group's defining rep, (b) the simplest non-trivial Stark-unit SIC construction over a real quadratic field, and (c) the smallest finite simple group acting transitively on a projective plane (PSL(2,7) on PG(2,2)). These three facts are not independent — they all flow from the prime $7$'s position in the arithmetic of $\mathbb{Q}(\sqrt{-7})$ — but their joint structural reading at $d=7$ is what makes the present construction possible." That is defensible. The current prose, with its four-features list and explicit *non-replication* claim against $d = 11, 13, 17, 19, 23$, reads as advocacy for a coincidence the author already believes is meaningful.

### 2.4 §9.5 "concluding observation" is overreach

> "*The QBism reference measurement, when constructed from the unique exact Stark-unit fiducial, **is** the smallest exceptional Lie algebra in informational form.*"

The "is" is doing work the theorems don't do. What is proved:

- (Thm 1) $\mathfrak{g}_2^{\mathbb{C}}$ is a 14-dim subspace of the 49-dim ambient $\mathfrak{gl}(7,\mathbb{C})$ that the SIC projectors span.
- (Thm 2) The 21-element $G_2$ orientation stabilizer is a subgroup of the 147-element SIC symmetry group.
- (Thm 3) The imaginary part of the SIC triple product on Fano lines is exactly $b\cdot\varphi$, with $b$ algebraic over $\mathbb{Q}(\sqrt{2})$.

This is "the SIC frame at $d=7$ contains $G_2$ as a distinguished sub-structure in three senses." It is *not* "the SIC frame *is* $\mathfrak{g}_2$." A 14-dim subspace of a 49-dim space is not the 14-dim space; it is one of infinitely many 14-dim subspaces, distinguished here by the AFF coefficient formula.

The author should either:
- Replace "is" with "encodes" / "contains as a distinguished subspace" / "realizes" and let the reader make the philosophical leap,
- Or front-load the philosophical commitment in §1 so the reader is prepared, and acknowledge in §9.5 that the "is" is interpretive rather than theorem-content.

Right now §9.5 reads as if it's stating a result, which it isn't.

### 2.5 The b'/b open problem creates a real gap in Theorem 3

Theorem 3 as stated has three parts: (a) universal magnitude, (b) Fano-line decomposition, (c) non-Fano structure including $b'/b = (1+\sqrt{2})/2$. Parts (a) and (b) are proven analytically in Appendix A.4. Part (c) is verified numerically only — and explicitly conjectural in §9.4.

This is awkward. Either:

- **Option A:** Demote part (c) to a remark or conjecture, and state Theorem 3 as parts (a)+(b) only. The paper is not weaker for this — Theorem 3(a)+(b) is the substantive result.
- **Option B:** Provide a closed-form derivation of $b'/b = (1+\sqrt{2})/2$ from the cocycle phase analysis sketched in Appendix A.6. The author already has the apparatus (the WH cocycle $\tau^{qr-ps}$ in (A4-main)); they just haven't enumerated the mixed-displacement orbits and summed.
- **Option C (worst):** Leave Theorem 3 as currently stated, with part (c) on numerical evidence only. A *J. Math. Phys.* referee will reject this. *Foundations of Physics* may accept it with explicit conjectural framing, but a hostile referee will note that "Theorem 3" is being used to mean "Theorem 3(a)+(b) plus Conjecture 3(c)" — a labeling that overstates.

I would push hard for Option B. The closed-form non-Fano derivation should be a 2–4 page calculation in Appendix A. If it doesn't fall out of the cocycle structure, that itself is informative — it would suggest that the QR-partition organizing principle of §7.4 is incomplete and there's additional structure controlling $b'$.

### 2.6 §8 positioning is fair on Furey/Krasnov but thin on Boyle–Farnsworth, and missing several adjacent programs

I'll address §8 in detail in section 5 below. The short version: the differentiation from Furey is substantive (Furey targets SM gauge structure; this paper targets operator-frame structure), but the differentiation is described in a single closing sentence — "*The present paper does not compete with any of these programs; it adds an operator-frame and coherence/observer layer on the same exceptional-algebra foundation*" — that is too quick. It papers over questions a referee will want addressed:

- *Why* is "operator-frame and coherence/observer layer" a separate research program rather than a niche within Furey's broader division-algebraic framework? What does the SIC structure buy that Furey's ladder operators don't?
- Krasnov's continuum $G_2$ gauge theory has a discrete-frame analog (lattice $G_2$); is the present paper's discrete operator basis a candidate for that role, or is it categorically different?
- Boyle–Farnsworth's spectral-triple machinery has a SIC interpretation in dimension 4 (Coecke–Heunen, Schmid). Is this manuscript implicitly a $d=7$ analog of that program? If yes, cite the connection. If no, explain why.

Programs missing from §8:

- **Castro Perelman's $E_8$ / octonionic gravity work** — even if dismissed, should be cited as adjacent.
- **Dixon's $\mathbb{C} \otimes \mathbb{H} \otimes \mathbb{O}$ algebra** — the foundational program on which Furey builds; not citing Dixon while citing Furey is bibliographically incomplete.
- **Manogue and Dray's work on $E_6$ / 27-dim Jordan-algebra-based fermion structure** — adjacent to Todorov, often cited together.
- **The Stacey monograph (cited as [13]) on sporadic SICs** — should be discussed in body text of §8 as a closely related QBism-structural program; it is currently buried in references.
- **Khrennikov's contextual-probability / informational interpretations** — relevant to the QBism-interpretive context the paper invokes.

---

## 3. Specific line-level redlines

> **Abstract, final sentence:** "*The QBist agent's reference measurement at $d=7$, when constructed from the exact Stark-unit fiducial, is shown to be an algebraic incarnation of the smallest exceptional Lie algebra in informational form.*" — Replace "*is shown to be an algebraic incarnation of*" with "*encodes the algebraic, group-theoretic, and orientational structure of*". The "incarnation" framing is rhetorically loaded and not what the theorems establish.

> **§1 ¶1, last sentence:** "*sits as a canonical sub-frame of measurements rather than as an external symmetry*" — Cut "rather than as an external symmetry". The contrast is rhetorical. Every Lie subalgebra of $\mathfrak{gl}(n)$ "sits inside it" in some basis; the paper's contribution is *which* basis (the SIC basis) and *what coefficients* (AFF dual-frame).

> **§1 ¶5:** "*What the QBist agent's reference measurement encodes... is not merely a frame in $\mathbb{C}^7$ but the algebraic and orientational backbone of the seven-dimensional defining representation of the smallest exceptional Lie group.*" — "Backbone" is metaphor and should be replaced with a precise statement: "the 14-dim subspace, the $F_{21}$ orientation stabilizer, and the cubic structure constant $b\varphi_{ijk}$ on Fano lines."

> **§2.4:** "*The dimension $d = 7$ is privileged among small primes by a conjunction of arithmetic, Lie-algebraic, combinatorial, and representation-theoretic features whose joint occurrence does not replicate at $d = 11, 13, 17, 19$, or 23.*" — This is asserted in §2.4 and only argued in §5.5. Either move the argument forward or soften §2.4 to "as discussed in §5.5". The current placement asserts a conclusion the reader hasn't yet been shown.

> **§5.2 proof of partial isometry, displayed equation following the SIC second-frame potential identity:** "*$\sum_{p,q} |\alpha^{(a)}_{p,q}|^2 = (8/7)^2 \cdot (49/8) \cdot \operatorname{tr}(T_a^2) \cdot (-1) = 8/7$*" — The factor of $-1$ is asserted with the parenthetical explanation that follows, but the structure of the calculation has the $-1$ appearing twice (once from $T^\dagger = -T$ and once from $\operatorname{tr}(T_a^2)$ being negative). The bookkeeping should be made explicit; right now the equation looks like the $-1$ enters only once. Recommend rewriting in two steps.

> **§5.5 (F2):** "*Therefore $d=7$ is the unique small prime dimension in which an exceptional Lie group acts naturally and irreducibly.*" — The qualifier "small" is doing covert work. Reword to: "Among the exceptional simple Lie groups, only $G_2$ has a natural irreducible representation in any prime dimension. The smallest such dimension is 7, and the next exceptional irrep of any prime dimension is the 248-dim adjoint of $E_8$."

> **§5.5 (F4):** "*The structural decomposition $7 = 1 + 3 + \bar{3}$.*" — This is a consequence of (F2), not independent. Either drop it or note explicitly: "This decomposition is determined by F2 and is listed separately here because it controls the 6/7 ratio of Paper 6."

> **§5.5 closing:** "*the conjunction (F1) $\wedge$ (F2) $\wedge$ (F3) $\wedge$ (F4) at $d=7$, which to our knowledge replicates at no other small prime.*" — "to our knowledge" is weak; either remove the modal or back it up with an explicit table comparing $d \in \{7, 11, 13, 17, 19, 23\}$ across the four features. A table is more convincing than prose.

> **§6.4 Theorem 2 statement:** "*This subgroup arises as a quotient (equivalently, as a subgroup of index 7)...*" — These are not equivalent in general. They are equivalent here because the relevant subgroup of index 7 happens to be the kernel of a quotient map (the cyclic $\langle Z\rangle$ factoring out); but the prose in §6.5 Choice 2 says the framings are "equivalent for the present purpose because the relevant subgroup F₂₁ has index 7 and the relevant normal subgroup is the kernel." This needs a one-sentence statement of *why* the kernel is normal, not just that it's there. Otherwise the equivalence claim is unjustified.

> **§7.3:** "*verified to 64-bit precision and consistent with 50-digit precision in the underlying triple-product values*" — "Consistent with" is unusual phrasing. If it's verified at 50-digit precision, say so. If not, say "the underlying triple products are computed at 50-digit precision and the ratio is computed at 64-bit precision from those values." Right now the sentence is fudged.

> **§7.6 Promotion of Conjecture 3 to Theorem 3:** "*The original conjecture stated in §7 of the present paper's outline (drafted before computational verification)...*" — This sentence reveals research process in a way that hurts the paper. Reframing as "Earlier presentations of this work conjectured $T_{ijk} \propto \varphi_{ijk}$ on Fano triples; the actual structure includes a constant symmetric component $a$. We adopt the corrected statement as Theorem 3." preserves the intellectual honesty without the meta-commentary.

> **§8.2 closing sentence:** "*The present paper does not compete with any of these programs; it adds an operator-frame and coherence/observer layer on the same exceptional-algebra foundation.*" — This sentence is doing too much work. See §5 of this review for the full critique. At minimum, the "coherence/observer layer" needs to be defined; right now it's a placeholder.

> **§9.5 "Concluding observation":** Already addressed in §2.4 above. Either rewrite around "encodes" rather than "is," or clearly mark the philosophical commitment.

---

## 4. The b'/b open problem

I treat this in §2.5 above, but to summarize:

**Is this an acceptable limitation for publication?** For *Foundations of Physics*, yes — *if* Theorem 3 is restated as Theorem 3(a)+(b), with part (c) explicitly demoted to a "Conjecture 3.1" or "Numerical Observation 3.1" with the closed-form ratio $b'/b = (1+\sqrt{2})/2$ flagged as supported at 50-digit precision but unproven analytically. A referee at *J. Math. Phys.* will not accept "Theorem 3 has three parts, one of which is numerical," and even at *Foundations of Physics* the current presentation is a target for adversarial review.

**Does it undercut Theorem 3?** Partially. Theorem 3(a)+(b) is the substantive structural result — that the imaginary part of the triple product on Fano lines is exactly $b \cdot \varphi$. The non-Fano part (c) is interesting but not central to the §1 thesis. Demoting (c) costs the paper essentially nothing at the headline level.

**Minimum acceptable analytic statement:** Either (i) a closed-form derivation of $b'$ from the cocycle phase enumeration sketched in Appendix A.6 (worth attempting; the apparatus is in place), (ii) an analytic *upper and lower bound* on $b'/b$ via algebraic constraints on $\mathbb{Q}(\sqrt{2})$ that brackets $(1+\sqrt{2})/2$ as the unique value consistent with the SIC and cocycle constraints, or (iii) a precise statement of which finite enumeration over WH orbit types would close the proof, framed as a tractable open computation. Any of these three lifts the result from "we observed this numerically" to "the closed form is constrained by these structural facts and matches the observation." Option (iii) is the minimum.

---

## 5. Adjacent-programs section (§8)

### 5.1 Is the positioning fair?

Mostly yes, but the differentiation is asserted rather than argued. The author writes that this paper "*adds an operator-frame and coherence/observer layer on the same exceptional-algebra foundation*" as Furey, Krasnov, Boyle–Farnsworth, and Todorov. This is the §8 thesis, and it's the right thesis — but it's defended in a single sentence. A hostile referee will ask: what *is* the operator-frame layer that none of the four cited programs already supply?

The honest answer, which the author should write into §8.2, is:

- **Furey** supplies a division-algebraic mechanism for SM particle content via complex octonions; she does not work with finite-dim SIC frames, does not engage with QBism reference-measurement theory, and does not study the $WH(7) \rtimes C_3 \to F_{21}$ descent. The present paper is in a *strictly orthogonal* direction: it asks "what does the SIC operator basis at $d=7$ tell us about $G_2$?", which Furey's framework neither asks nor answers.
- **Krasnov** works in continuum field theory; the present paper is finite-dimensional and operator-algebraic. There is no overlap in mathematical apparatus, only in the structural object ($G_2$). A referee will accept this differentiation easily.
- **Boyle–Farnsworth** work in non-commutative spectral geometry on internal-space Dirac operators. Their machinery is closely related to SIC structure in low dimensions (cf. Coecke–Heunen on $d=4$ MUBs and SICs), but the connection is unexplored at $d=7$. The author should at minimum acknowledge that the present construction *might* admit a spectral-triple reformulation, and flag this as a direction for future work.
- **Todorov** uses the 27-dim exceptional Jordan algebra $\mathfrak{h}_3(\mathbb{O})$, which contains $G_2$ as the automorphism group of $\operatorname{Im}\mathbb{O} \subset \mathbb{O}$. The present paper does not engage $\mathfrak{h}_3(\mathbb{O})$. A natural question — does the 27-dim component $V_{27}$ of the §5.4 decomposition $\mathfrak{gl}(7,\mathbb{C}) = \mathbf{1} \oplus V_7 \oplus V_{14} \oplus V_{27}$ relate to $\mathfrak{h}_3(\mathbb{O})$? — is not addressed and is the obvious place a Todorov-program reader will press.

### 5.2 Is the differentiation substantive or papering over a competition?

It is substantive *for Furey and Krasnov*, where the mathematical apparatus is genuinely different (division-algebra ladder operators / continuum field theory vs. SIC operator basis / finite group descent). It is *less clearly substantive* for Boyle–Farnsworth and Todorov, where the structural objects overlap more directly. The author should sharpen the §8.2 prose for those two programs in particular.

The "operator-frame and coherence/observer layer" framing is currently undefined in §8 — the reader is meant to recall it from Papers 4 and 7 of the series. For *Foundations of Physics*, where philosophical context is welcome, this is acceptable; for *J. Math. Phys.*, it is not. If the paper aims at *Foundations of Physics*, define the phrase in §8 in 2–3 sentences. If it aims at *J. Math. Phys.*, drop the framing entirely and let the theorems stand on their structural merits.

### 5.3 Major programs missing

Listed in §2.6 above. To restate: Dixon (foundational for Furey), Stacey monograph (closest in QBism-structural spirit and currently buried), Manogue–Dray ($E_6$/27-dim work), Castro Perelman (octonionic-gravity, even if dismissed). The Coecke–Heunen / categorical-quantum line is also adjacent through SIC/MUB structure and deserves at least one footnote.

---

## 6. Verdict

**Major revision.**

The mathematical core (Theorems 1, 2, 3(a)+(b), Appendix A.4) is sound and represents a real contribution: an explicit and reproducible identification of $G_2$ structure inside the $d=7$ SIC operator basis, with closed-form algebraic constants over $\mathbb{Q}(\sqrt{2})$. The 50-digit numerical verification is honest and the appendix derivation is checkable in minutes.

But the manuscript is currently *over-framed*. The §1 introduction promises a structural unmasking of the QBism reference measurement as an algebraic incarnation of $G_2$; what is delivered is three precise (and useful) statements: a 14-dim subspace embedding via AFF, a finite group descent via Fano-compatible sign-flip, and a closed-form cubic-structure-constant computation. These are publishable in *Foundations of Physics*, but only after the abstract, §1, §5.5, and §9.5 are rewritten to match the proven content. The §5.5 dimensional-uniqueness argument in particular is currently advocacy and will be flagged by any referee who works in representation theory; the §8 positioning needs more substance and broader citation; and Theorem 3(c) should be demoted from theorem to conjecture (or proven). With those revisions, the paper becomes a clean structural contribution to the SIC-POVM literature with a clear philosophical home in QBism. Without them, it reads as a framework-internal document that overstates its reach — and a hostile referee will reject on those grounds rather than on mathematical ones.

---

## 7. Top three priorities for revision

1. **Recalibrate the framing.** Rewrite the abstract's final sentence, §1 (~25% trim), and §9.5 to describe what the theorems actually prove, not what the PCI/PME framework would like them to mean. Specifically: replace "*is*" with "*encodes*" / "*realizes*" everywhere a copula links the SIC frame to $\mathfrak{g}_2$. The paper's intellectual honesty in §5.6 and §8.1 should be the model for §1 and §9.5.

2. **Resolve Theorem 3(c) or demote it.** Either supply a closed-form derivation of $b'/b = (1+\sqrt{2})/2$ from the WH cocycle structure already laid out in Appendix A.4 (the apparatus is in place; the calculation is finite), or restate Theorem 3 as parts (a)+(b) only, with (c) demoted to "Conjecture 3.1" or "Numerical Observation 3.1." The current "Theorem 3 = (a) + (b) + numerical (c)" formulation is an attack surface that costs the paper nothing to remove.

3. **Tighten §5.5 and expand §8.** §5.5 (F1–F4) should be rewritten to acknowledge that F1 and F3 share an arithmetic origin and that F4 is a consequence of F2; the four-feature framing as currently written reads as advocacy. §8 should expand the "operator-frame and coherence/observer layer" framing into a defined claim, add Dixon, Stacey, Manogue–Dray, and Castro Perelman as adjacent programs, and engage the spectral-triple question (could this construction admit a Boyle–Farnsworth-style reformulation?) and the exceptional-Jordan question (does the $V_{27}$ component of §5.4 connect to Todorov's $\mathfrak{h}_3(\mathbb{O})$?). One paragraph each is sufficient; the goal is to demonstrate that the author has thought about the boundary, not to fully address every adjacent program.

---

*End of review.*
