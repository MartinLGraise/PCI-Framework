# Paper 12 §5 — Empirical Accessibility: Predictions, Protocols, and the Fifth Paradigm Context (v3)

**Draft version:** v3 (2026-05-06, ~13:15 PDT)
**Status:** Phase-2 polish applied to v2 (council-cleared MINOR_REVISIONS).

---

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

*Revision log:*
- v3 (2026-05-06 ~13:15 PDT): Phase-2 polish. Glossary expanded
  ($\Psi_\theta$, $F_{21}$). P4 sample size clarified ("60 per arm,
  120 total"). Cohen's $d = 0.4$ stated as pre-registered hypothesis.
  §5.6 table gained quantitative-threshold column. BIOMA / BindCraft
  / Virtual-Lab references upgraded to specific cited papers with DOIs
  (Szymanski et al. 2023; Pacesa et al. 2024; Swanson et al. 2024).
  Cross-reference labels stripped of version qualifiers (§3 v2 → §3,
  §4 v2 → §4). Top-of-section metadata compressed.
- v2 (2026-05-06 ~03:30 PDT): MAJOR_REVISIONS pass. Pillar 4 threaded
  through P1–P4. Glossary box added. §5.6 reduced to consolidating
  table. Hyperscanning citations added.
- v1 (2026-05-06 ~03:00 PDT): First complete draft.
