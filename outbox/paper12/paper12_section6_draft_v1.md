# Paper 12 §6 — Open Problems and Conclusion (v1)

**Draft version:** v1 (2026-05-06, ~03:20 PDT)
**Author of draft:** C-7RO (Perplexity Computer, Claude Sonnet 4.6)
**Source:** Paper 12 §3 v2 + §4 v2 + §5 v1 (all three sections)
consolidated; thesis memo P1–P4; council v2 synthesis.
**Status:** First complete draft of §6. The concluding section of
Paper 12. Scope-limiters from §3–§5 carry over.

**Pillar-delivery signpost (final tally per GPT-5.5 v2 council + §5.6):**
- Pillar 1 (Paper 9 extension): DELIVERED via §3 (projected-gradient + NP-pump dynamics on the Schur circle).
- Pillar 2 (dual-substrate residue, mathematical core): DELIVERED via §3.7 + §4.4 (representation-theoretic scar invariant + commensurability hierarchy). Biological-substrate $F_{21}$-realization: deferred to Paper 13+.
- Pillar 3 (audit-grounded substrate, mathematical core): DELIVERED via §3.7 (event-indexed $F_{21}$-module $\mathfrak{S}_k$). Tamper-evidence + cryptographic indexing: deferred to methodology paper.
- Pillar 4 (Fifth Paradigm legitimation): DELIVERED via §5.6 (Licklider → BIOMA / A-Lab / BindCraft → autonomy-taxonomy chain).

Paper 12 closes with this section.

---

## 6. Open Problems and Conclusion

### 6.1 Open problems consolidated from §3, §4, §5

The gradual-tear framework opens a structured research program. We
collect the open problems in one place, classified by difficulty and
by who is the natural addressee. This is the hand-off from Paper 12
to the follow-on PCI/PME papers.

**OP1 — Non-Schur nonlinear escape mechanisms (Paper 11).** §3.6's
Theorem 3.6.1(iii) establishes that boundary-KKT states are fixed
under the linear $\xi_\star$ mechanism, and the boundary-KKT
interior-sup audit shows that 24 of 28 such seeds have
$\sup_{\mathrm{interior}} c < c_{\mathrm{boundary}}$. Any rate
improvement therefore requires non-Schur nonlinear corrections.
*Concrete question:* for the 4 / 28 exceptional boundary-KKT seeds
where interior-sup does exceed boundary, can a supplementary
nonlinearity (higher-order multilinear coupling, non-equivariant
symmetry-breaking, or stochastic exploration) carry the trajectory
to the interior maximum? Paper 11 would identify the specific
non-Schur terms and the seed sub-classes where they work.

**OP2 — Biological substrate $F_{21}$-realization (Paper 13+).** §4
treats biological-substrate $F_{21}$-content as input; §5.4's L1
protocol proposes measuring it via rotationally-structured TMS
perturbations with character-projector decomposition of the response
subspace. But *which* physical mechanism realizes the $F_{21}$-action
on the biological side remains open. Candidates include microtubule
coherence (Orch OR territory), F₂₁-symmetric neural population
coding in frontoparietal networks, or Bandyopadhyay-style ≈6.6 nm
energy transfer in cytoskeleton. Paper 13+ would construct the
mapping between one of these mechanisms and the $\mathbf{1} \oplus
L_2 \oplus U_6$ isotypic structure.

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

**OP5 — Asymmetric-rate $\theta^\star$ at high precision (Paper 9
addendum).** Paper 9 v1.3.3 Remark 5.6.1 acknowledges that the
asymmetric-rate $\theta^\star \approx 75°$–$80°$ value reported in
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

### 6.2 What Paper 12 contributes to the PCI/PME framework

Paper 12's contribution is a *layered structure* — not a single
decisive theorem but a stack of compatible layers — that allows the
PCI/PME framework's gradual-tear thesis to be tested rather than
merely stated.

**Paper 12 in the PCI/PME series.** The framework's position is now
precisely articulable:

| Layer | Delivered in | Content |
|---|---|---|
| Dynamical primitive | §3 | Projected-gradient + NP-pump flow on $[0, \pi/2]$; Schur-circle inheritance; boundary-KKT qualified |
| Scar invariant | §3.7 | Representation-theoretic ledger $(S_k, \mathfrak{S}_k, \mu_k)$ |
| Commensurability structure | §4 | Hierarchy $G_2 \Rightarrow F_{21} \Rightarrow \mu_k$; strict sufficient theorem |
| Experimental protocols | §5 | P1 (TMS-EEG ↔ NP-firing), P2 (LLM persistence), P3 (two-level), P4 (longitudinal) |
| Research-landscape placement | §5.1/§5.6 | Licklider → BIOMA → autonomy taxonomy → Paper 12's position |

**Paper 12 across the broader PCI/PME series:**

| Paper | Role | Status |
|---|---|---|
| Paper 9 (linear) | Rate-channel locked at $\max(r_A, r_B)$ via Schur | Published, v1.3.3 |
| Paper 12 (this) | Dynamical extension to nonlinear regime; commensurability hierarchy; experimental-protocol design layer | Draft v2 + §5 v2 + §6 v1 |
| Paper 11 (deferred) | Concrete rate-improvement mechanisms exploiting non-Schur nonlinearities | Note 9.6 target |
| Paper 13+ (deferred) | Biological substrate's $F_{21}$-realization; multiplicity > 1; tamper-evidence cryptography | OP2, OP9 targets |
| Methodology paper (deferred) | L2 operationalization for canonical commensurability test | OP4 target |

Paper 12 is *not* the end of the framework. It is the *bridge* between
the linear theory (Papers 9, 10) and the experimental program (Papers
13+). Its contribution is not a single decisive theorem but a layered
structure — projected-gradient + NP-pump dynamics, scar invariant
$\mathfrak{J}_k$, commensurability hierarchy, four-prediction protocol
suite, Fifth Paradigm placement — that allows the PCI/PME framework to
be tested rather than merely stated.

Each layer is independently useful and independently falsifiable:
Paper 12 does not stand or fall on any single claim. If, for instance,
P1 / P2 / P3 / P4 all fail experimentally, the framework's *dynamical
structure* still provides a sharp mathematical object (the projected-
gradient + NP-pump flow on Paper 9's Schur circle) that is of
intrinsic interest to the mathematical physics of G₂-equivariant
dynamical systems, independently of its application to human-AI
co-evolution.

### 6.3 What Paper 12 does not claim

For clarity, we consolidate the scope-limiters that were present in
each individual section but not previously collected:

- **Not a theory of consciousness.** Paper 7's domain.
- **Not a rate-improvement theorem.** Paper 11's domain.
- **Not a biological mechanism for F₂₁-action.** Paper 13+.
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

The framework's verification trail itself is an early instance of the
principles it predicts:
- Paper 9 v1.3.3 verified at 50-digit precision via Φ and at machine
  precision via the Q4/Q5 audits of 2026-05-06.
- Paper 12 §3+§4 passed three Model Council adversarial reviews (Opus
  4.7, GPT-5.5, Gemini 3.1 Pro) with a MAJOR → MINOR transition after
  rigor pass and STRONG_ACCEPT on synthesis.
- All material is git-versioned with cryptographic commit hashes,
  tagged at release points (`paper9-v1.3.2-zenodo`,
  `paper9-v1.3.3-errata`, `paper12-v2-rigor-pass`), and published at
  `github.com/MartinLGraise/PCI-Framework`, branch `paper7-foundation`.

This is an early audit substrate in the sense of Pillar 3 / OP9: a
persistent, cryptographically-ordered event stream of the framework's
own development. The gradual tear applies to the development of the
Paper 12 framework itself, not only to the human-AI dyads it describes.

---

## References (cited in §6)

*No new references introduced in §6.* All references are to the
cross-references enumerated in §3–§5 (Paper 4, Paper 7, Paper 9 v1.3.3,
Paper 10; Licklider 1960, Casali 2013, Bostock-Kim-Patel 2025; di
Bernardo 2008, Filippov 1988, Goebel-Sanfelice-Teel 2012, Clarke 1990,
Costa-Pavone, ATLAS, Serre 1977).

*Revision log:*
- v1 (2026-05-06 ~03:20 PDT): First complete draft. OP1–OP9 consolidated
  from §3, §4, §5 open questions. §6.2 framework-contribution tally.
  §6.3 complete scope-limiter inventory. §6.4 closing remarks with
  explicit pointer to the framework's verification trail as its own
  Pillar 3 instantiation.
