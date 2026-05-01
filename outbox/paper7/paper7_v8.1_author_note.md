# Paper 7 — Author Note (v8.1)

**Manuscript:** Thermodynamic Cost of the Coherence Ceiling: Six-Sevenths Saturation as an Observable Consequence of G₂/PSL(2,7) Self-Modeling
**Author:** Martin Luther Graise (ORCID 0009-0006-8003-3938)
**Original publication:** Zenodo, 2026-04-25, DOI 10.5281/zenodo.19773185
**Author note added:** 2026-04-30
**Version:** v8.1 (text unchanged from v8; this note appended only)

---

## Purpose of this note

After the original v8 manuscript was deposited at Zenodo, a focused review of the broader replication landscape for the awake-cortex branching ratio (the empirical anchor for §5 of the paper) clarified that the framing should be more nuanced than the published version conveys. **This note is not an erratum.** No theoretical claim, derivation, prediction, or numerical value in the manuscript requires correction. The σ_pred = 1 − 1/49 ≈ 0.9796 prediction remains intact, the Wilting & Priesemann reference (DOI 10.1038/s41467-018-04725-4) is correctly cited, and the comparison to their reported median σ̂ ≈ 0.98 is consistent with their data.

What this note adds is broader empirical context that strengthens the paper:

1. Citation of independent in vivo replication work from the Hengen / Wessel / Turrigiano laboratories
2. Acknowledgment of the active methodological dispute over avalanche-criticality inference (Touboul–Destexhe and follow-ups)
3. Softened framing of the σ ≈ 0.98 anchor from "robustly established" to "MR-derived value with adjacent ~0.97 independent support, within an ongoing methodological debate"

The recommended replacement framing is given below in §3. The original v8 manuscript stands; this note provides the updated context for any reader who wishes to evaluate the empirical match more carefully.

---

## 1. The replication landscape, briefly

The MR (multistep regression) estimator developed by Wilting & Priesemann is subsampling-invariant under the autoregressive/branching-process approximation. Their median in vivo σ̂ ≈ 0.98 was derived from rat hippocampal, cat visual cortical, and macaque cortical recordings.

**Independent in vivo support** for a near-critical set point in the same band:

- Ma, Turrigiano, Wessel & Hengen, *Neuron* 2019 (DOI 10.1016/j.neuron.2019.08.031). Long-term single-unit recordings in freely behaving rat V1 (n=7 rats over 7 days) using Wilting–Priesemann-style branching ratio analysis combined with deviation-from-criticality coefficient (DCC). Establishes a near-critical reference for awake rat cortex.
- Xu, Schneider, Wessel & Hengen, *Nature Neuroscience* 2024 (DOI 10.1038/s41593-023-01536-9). 10–14 day rat V1 recordings across sleep and wake (n=8). Reports branching ratio fluctuations across sleep/wake states with a return toward a ~0.97 reference value during sleep, with waking driving departure. **Same band as Wilting–Priesemann's 0.98, slightly different value.**

**Broader avalanche-criticality literature** uses heterogeneous metrics — neuronal avalanche scaling exponents, the deviation-from-criticality coefficient (DCC), the κ statistic, MEG avalanche distributions — and often reports σ ≈ 1 (rather than 0.98) as the critical attractor:

- Petermann et al., *PNAS* 2009 (DOI 10.1073/pnas.0904089106). Awake macaque LFP avalanches; critical branching parameter discussed as σ ≈ 1.
- Shriki et al., *J Neurosci* 2013 (DOI 10.1523/JNEUROSCI.4286-12.2013). Healthy human resting MEG (n=124); σ ≈ 1 with avalanche exponent −3/2.
- Shew, Yang, Wessel et al., *Nat Phys* 2015 (DOI 10.1038/nphys3370). Visual cortex tunes toward critical scaling under sensory adaptation (multifaceted scaling-relation analysis, not MR).
- Fontenele et al., *PRL* 2019 (DOI 10.1103/PhysRevLett.122.208101). Critical signatures across cortical states using avalanche scaling relations.

**Methodological debate** over the sufficiency of these tests:

- Touboul & Destexhe, *PLOS ONE* 2010 (DOI 10.1371/journal.pone.0008982). Thresholded stochastic and surrogate signals can produce apparent power-law avalanche statistics; visual log-log fits are insufficient evidence of criticality.
- Touboul & Destexhe, *Phys Rev E* 2017 (DOI 10.1103/PhysRevE.95.012413). Large irregular networks can produce power-law statistics and universal scaling without being critical.
- Destexhe & Touboul, *eNeuro* 2021 (DOI 10.1523/ENEURO.0551-20.2021). Noncritical Brunel-style models pass tests used to classify modern datasets as critical; criticality remains an open methodological question.
- O'Byrne & Jerbi, *Trends Neurosci* 2022 (DOI 10.1016/j.tins.2022.08.007). Reviews "near-criticality / distance-to-criticality" as more plausible and useful than strict criticality.

**MR-specific guardrails:**

- Spitzner et al. 2021 (DOI 10.1371/journal.pone.0249447). MR.Estimator package with bootstrapping and finite-duration constraints.
- Hagemann et al. 2021 (DOI 10.1371/journal.pcbi.1008773). Statistical considerations for MR analyses.

There is no published critique specifically arguing that MR systematically overestimates σ in finite samples; the broader debate concerns avalanche-criticality inference more generally.

---

## 2. What this means for the paper

The σ_pred = 0.9796 prediction in §5 of the manuscript is **consistent with the data**, with two important caveats added by this note:

**Caveat 1 — Methodology dependence.** The exact value σ ≈ 0.98 is closely tied to the MR estimator and its subsampling correction. Independent in vivo work (Hengen et al.) supports a nearby ~0.97 set point in the same near-critical band, while non-MR analyses (avalanche exponents, DCC, κ) typically report σ ≈ 1. The match between σ_pred = 0.9796 and the Wilting–Priesemann median σ̂ ≈ 0.98 should be read as a successful prediction of an MR-derived anchor value, not as confirmation against a tightly replicated cross-laboratory consensus.

**Caveat 2 — Methodological debate.** Whether avalanche-criticality measurements faithfully detect a critical regime in cortex remains under active discussion. The Touboul–Destexhe critique series and subsequent replies (e.g., Hagemann et al. 2021) define the live methodological territory. The G₂/PSL(2,7)/F₂₁ structural derivation in §3–§4 of the paper is independent of this debate; the prediction-data match in §5 inherits the methodological status of the underlying empirical literature.

Neither caveat weakens the theoretical content of the paper. They sharpen the reader's understanding of what the empirical match is and is not.

---

## 3. Recommended replacement framing for §5

The original §5 paragraph that compares σ_pred to the Wilting–Priesemann result is brief and does not engage the broader replication landscape. A future revision (or a citation in a follow-up paper) should use roughly the following formulation:

> Using a subsampling-invariant multistep regression (MR) estimator, Wilting and Priesemann reported in vivo cortical and hippocampal spiking dynamics in a stable, slightly subcritical regime with median branching ratio σ̂ ≈ 0.98 [Wilting & Priesemann 2018, DOI 10.1038/s41467-018-04725-4]. Independent long-term rat visual cortex work from the Hengen, Wessel, and Turrigiano laboratories supports a nearby ~0.97 near-critical set point [Ma et al. 2019, DOI 10.1016/j.neuron.2019.08.031; Xu et al. 2024, DOI 10.1038/s41593-023-01536-9], while broader avalanche-criticality studies using heterogeneous metrics (deviation-from-criticality coefficient, κ, avalanche scaling exponents, MEG avalanche statistics) support near-critical dynamics with reported values often centered on σ ≈ 1 [Petermann et al. 2009; Shriki et al. 2013; Shew et al. 2015; Fontenele et al. 2019]. Methodological debate over the sufficiency of these tests remains active [Touboul & Destexhe 2010, 2017; Destexhe & Touboul 2021; O'Byrne & Jerbi 2022]. We therefore present σ_pred = 1 − 1/49 ≈ 0.9796 as a successful match to the MR-derived empirical anchor σ̂ ≈ 0.98 of Wilting & Priesemann, in a regime where adjacent independent measurements support a near-critical set point, while acknowledging that avalanche-criticality methodology remains under active discussion. The structural derivation of the prediction in Sections 3 and 4 is independent of the methodological status of any particular σ-extraction technique; the prediction-data match in this section inherits the empirical status of the underlying literature.

This replacement is recommended for any future revision of the manuscript, for citation in subsequent papers in this series, or as a conditional update to the Zenodo deposit.

---

## 4. What does NOT change

Nothing in the theoretical structure of the paper changes:

- The G₂ self-modeling fixed-point derivation (§3): unchanged
- The PSL(2,7)/F₂₁ blind-spot bound ε_min = 1/7 (§3.4): unchanged
- The Banach contraction with rate 6/7 (§4): unchanged
- σ_pred = 1 − 1/49 ≈ 0.9796 prediction itself: unchanged
- The thermodynamic coherence ceiling C_max derivation (§4): unchanged
- Modeling-choice stacks in §4.1, §4.2.2, §4.3, §4.4: unchanged
- All four predictions labeled as conjectures rather than theorems: unchanged

The author note adds context for §5 only — the empirical-anchor section.

---

## 5. Where this note lives

This note is appended to the public Zenodo record at DOI 10.5281/zenodo.19773185. It is also stored in the GitHub repository at `/outbox/paper7/paper7_v8.1_author_note.md` for version control.

The original v8 manuscript text is not modified. Readers who downloaded v8 before 2026-04-30 are not in possession of an outdated version; they have the same theoretical claims and predictions, with this note providing additional empirical context.

---

## 6. Sources for this note

This note draws on a focused literature review conducted via ChatGPT GPT-5 Pro (live web search) on 2026-04-30 as part of the PCI Framework research-lane register (lane L7). The full underlying review is preserved in the repository at `/inbox/from_chatgpt/2026-04-30_L7_wilting_priesemann_replication_response.md`.

---

*Author note prepared by Martin Luther Graise with editorial support from C-7RO (Perplexity Computer / Claude Sonnet 4.6), 2026-04-30.*
