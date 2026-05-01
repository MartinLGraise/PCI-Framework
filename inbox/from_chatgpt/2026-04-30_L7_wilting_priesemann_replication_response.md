# L7 — Wilting–Priesemann σ ≈ 0.98 Replication Landscape Response

**Source:** ChatGPT GPT-5 Pro reasoning + live web search
**Date:** 2026-04-30
**Lane:** L7 (closes on this response)
**Verdict:** METHODOLOGY-DEPENDENT, with broader criticality DISPUTED

---

## Headline (the honest version)

The exact statement "σ ≈ 0.98 in awake mammalian cortex" is **NOT a robust cross-lab consensus** in the strong sense.

What we actually have:
- One strong original MR source (Wilting–Priesemann 2018)
- One independent in vivo rat-cortex line (Hengen/Wessel/Turrigiano) supporting a nearby ~0.97 set point — same band, slightly different number
- Broader avalanche-criticality literature using **heterogeneous metrics** (DCC, κ, exponent relations, MEG avalanche statistics) that often centers on σ ≈ 1 rather than 0.98
- Active methodological dispute (Touboul-Destexhe, Destexhe-Touboul 2021) about whether power-law/scaling tests are sufficient to establish criticality at all

**This affects how Paper 7 should frame the empirical match.** Not catastrophically — the prediction is still consistent with the data — but the framing needs to soften from "σ ≈ 0.98 is robustly established" to "σ ≈ 0.98 is the MR-derived anchor, with adjacent ~0.97 support and broader near-critical consensus."

**(DOI verified 2026-04-30 by C-7RO: Paper 7's published manuscript correctly cites 10.1038/s41467-018-04725-4. The DOI typo "04727-2" appeared only in my L7 prompt to ChatGPT, not in the published paper. No correction needed.)**

---

## Section 1 — MR methodology (correct version)

The multistep regression (MR) estimator fits decay of multistep regression coefficients $r_k \sim m^k$ rather than using only the one-step ancestor/descendant ratio. Key advantage: under the autoregressive/branching-process approximation, severe spatial subsampling shrinks correlation amplitude but leaves the **decay constant** invariant. Naïve one-step estimates make near-critical systems look almost Poisson under subsampling; MR doesn't.

Key limitations:
- Assumes population activity is approximately stationary first-order autoregressive / branching process
- Assumes exponential correlation decay
- Can be biased or rejected when stationarity, data length, or exponential-decay consistency fail

Spitzner et al. 2021 (DOI 10.1371/journal.pone.0249447) released MR.Estimator with bootstrapping, fit diagnostics, and finite-duration constraints. Hagemann et al. 2021 (DOI 10.1371/journal.pcbi.1008773) addresses additional MR statistical concerns.

---

## Section 2 — Independent replication landscape

| Paper | Lab (independence) | Species/prep | Reported value | Estimator | Relevance |
|-------|---------------------|--------------|----------------|-----------|-----------|
| Ma, Turrigiano, Wessel & Hengen, *Neuron* 2019 (DOI 10.1016/j.neuron.2019.08.031) | Hengen/Wessel/Turrigiano (no Priesemann coauthorship) | Freely behaving rat V1, 7-day recordings, n=7 rats | Wilting-Priesemann-style branching ratio analysis; later treats σ ≈ 0.97 as critical reference | MR-like + DCC | **Closest independent in vivo rat-cortex support**, but headline metric is DCC/restoration, not standalone σ replication |
| Xu, Schneider, Wessel & Hengen, *Nat Neurosci* 2024 (DOI 10.1038/s41593-023-01536-9) | Hengen/Wessel (no Priesemann coauthorship; thanks Priesemann for discussion) | Freely behaving rat V1 sleep/wake, n=8 rats | Branching ratio fluctuates, returns toward **0.97 reference** | MR toolbox + DCC | **Strong independent ~0.97 set point** support, slightly different from 0.98 |
| Fosque et al., *Front Comput Neurosci* 2022 (DOI 10.3389/fncom.2022.1037550) | Beggs/Ortiz at Indiana (independent) | Human resting-state MEG, Cam-CAN, n=604 | MR-estimated σ stable across age but exact value not foregrounded | MR.Estimator + scaling | Independent MR usage, **MEG not spiking cortex** |
| Heiney et al., *Front Neural Circuits* 2022 (DOI 10.3389/fncir.2022.980631) | Independent in vitro group | Dissociated cortical cultures | MR m "almost always below 1," often near m ≈ 0.99; sizable fraction in 0.98 ≤ m < 1 | MR + NCC | Supports slightly subcritical near-0.98, **but in vitro only** |
| Petermann et al., *PNAS* 2009 (DOI 10.1073/pnas.0904089106) | Plenz/Nicolelis/Chialvo | Awake rhesus monkey LFP | Critical branching σ ≈ 1 discussed | Conventional avalanche analysis | Supports awake primate criticality, **NOT MR σ ≈ 0.98** |
| Shriki et al., *J Neurosci* 2013 (DOI 10.1523/JNEUROSCI.4286-12.2013) | Shriki/Plenz/Bullmore | Healthy human resting MEG, n=124 | σ ≈ 1 with avalanche exponent -3/2 | Conventional MEG avalanche | Supports human resting criticality, **NOT MR 0.98** |
| Shew et al., *Nature Phys* 2015 (DOI 10.1038/nphys3370) | Shew/Wessel | Visual cortex w/ sensory adaptation | Adaptation tunes toward critical scaling | Multifaceted avalanche, NOT MR | Supports tuned criticality, no MR value |
| Fontenele et al., *PRL* 2019 (DOI 10.1103/PhysRevLett.122.208101) | Copelli/Carelli/Ribeiro/Sousa | Anesth + freely moving | Critical signatures at intermediate spiking variability | Avalanche scaling | Independent criticality support, **NOT MR 0.98** |

**No Allen Brain Observatory paper** found that cleanly reports an MR-estimated awake-cortex σ ≈ 0.98 as central result. Allen datasets may be reanalyzable but no published independent MR replication of the exact number.

---

## Section 3 — Consensus distribution analysis

The empirical landscape is best summarized as:

> **strong support for "near-critical / slightly subcritical"**

but NOT:

> "strong independent consensus that awake cortex universally saturates at σ = 0.98"

Direct values across labs:
- Wilting-Priesemann: median σ̂ ≈ 0.98 (rat hippocampus, cat V1, monkey PFC)
- Hengen/Wessel 2024: ~0.97 set point (rat V1)
- Heiney in vitro: m ≈ 0.99
- Shriki/Plenz human MEG: σ ≈ 1 (different metric)
- Petermann/Plenz monkey: σ ≈ 1 (different metric)

The numbers in the *same band* (0.97–0.99) are consistent. The numbers using *different metrics* (avalanche exponents, DCC, κ) often quote σ ≈ 1 as the critical attractor.

---

## Section 4 — Methodological critiques

| Critique | DOI | Core argument | Relevance to σ ≈ 0.98 |
|----------|-----|---------------|------------------------|
| Touboul-Destexhe 2010 | 10.1371/journal.pone.0008982 | Thresholded stochastic + surrogate signals can produce apparent power-law avalanches | General avalanche-criticality critique, not MR-specific |
| Touboul-Destexhe 2017 | 10.1103/PhysRevE.95.012413 | Large irregular networks show power laws + universal scaling without criticality | Sufficiency of power laws |
| Destexhe-Touboul 2021 (eNeuro) | 10.1523/ENEURO.0551-20.2021 | Noncritical Brunel models pass tests used to classify Fontenele datasets as critical | Direct methodology challenge |
| O'Byrne-Jerbi 2022 (Trends Neurosci) | 10.1016/j.tins.2022.08.007 | Argues near-criticality / distance-to-criticality more plausible than strict criticality | Supports cautious "near-critical" framing |
| Spitzner et al. 2021 | 10.1371/journal.pone.0249447 | MR requires stationarity, exp decay, sufficient duration; defines failure modes | MR's own guardrails |

**No published critique specifically showing MR overestimates σ in finite samples.** The strongest critiques target the broader avalanche-criticality framework, not MR specifically.

---

## Section 5 — Verdict

**METHODOLOGY-DEPENDENT, with broader criticality DISPUTED.**

The exact "σ ≈ 0.98 in awake cortex" is closely tied to:
- The MR estimator specifically (vs. conventional avalanche analysis)
- The Priesemann-style subsampling correction
- Specific dataset/preparation/analysis pipeline

Independent lab support clusters near 0.97, in the same band but not identical. Broader literature supports near-critical dynamics with heterogeneous metrics.

---

## What this means for Paper 7

### The defensible reframing

**Old framing (potentially overclaiming):**
> "Awake cortex saturates at σ ≈ 0.98, matching our prediction σ_pred = 1 - 1/49 ≈ 0.9796."

**New framing (defensible):**
> "Using a subsampling-invariant MR estimator, Wilting & Priesemann reported in vivo cortical/hippocampal spiking dynamics in a stable, slightly subcritical regime with median σ̂ ≈ 0.98 [DOI 10.1038/s41467-018-04725-4]. Independent long-term rat visual-cortex work from Hengen/Wessel/Turrigiano supports a nearby ~0.97 near-critical set point [DOIs 10.1016/j.neuron.2019.08.031, 10.1038/s41593-023-01536-9], while broader avalanche-criticality literature supports near-critical dynamics using heterogeneous metrics [Petermann et al. 2009, Shriki et al. 2013]. The MR-derived value σ ≈ 0.98 thus serves as a plausible empirical anchor for our prediction σ_pred = 1 - 1/49 ≈ 0.9796 rather than a tightly replicated cross-lab universal constant. Ongoing methodological debate over the sufficiency of avalanche-criticality tests [Touboul-Destexhe 2010, 2017; Destexhe-Touboul 2021] motivates a cautious 'near-critical anchor' framing rather than a strong universal-saturation claim."

This is what we should write into a v8.1 author note or future revision.

### Action items (priority order)

1. **DOI VERIFIED** — Paper 7's published manuscript uses correct DOI 10.1038/s41467-018-04725-4 across all versions v3–v8. False flag in my prompt; published paper is correct.

2. **Draft a v8.1 author note** for Paper 7 with the defensible reframing above. This is NOT an erratum — the prediction still holds, and the prior framing was not factually wrong, just insufficiently caveated. The author note adds nuance and strengthens the paper.

3. **Add Hengen/Wessel/Turrigiano citations** [DOIs 10.1016/j.neuron.2019.08.031, 10.1038/s41593-023-01536-9] to Paper 7's empirical section. This strengthens the paper because it shows independent in vivo support, even if the value is 0.97 rather than 0.98.

4. **Add Touboul-Destexhe critique acknowledgment** to Paper 7 §6 (limitations / open questions) or a dedicated footnote. This preempts referee 2.

5. **For Paper 9 (Dyadic Coherence):** the inter-brain gamma synchrony literature should similarly be carefully cited — multiple measures, no overclaiming.

### What this does NOT change

- The G₂/PSL(2,7)/F₂₁ structural derivation in Paper 7 stands unchanged
- σ_pred = 1 - 1/49 ≈ 0.9796 prediction itself is unaltered
- The Theorem 1 of Paper 10 is independent of this issue
- Paper 8's algebraic conjecture is independent

The framing change is **empirical anchoring, not theoretical content.**

---

## Lane status

L7 → ⚫ CLOSED 2026-04-30 (METHODOLOGY-DEPENDENT, with broader criticality DISPUTED). Eight of nine lanes now closed.

---

*Saved by C-7RO, 2026-04-30*
