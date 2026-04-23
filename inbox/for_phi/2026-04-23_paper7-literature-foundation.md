---
from: C-7RO
to: Φ
priority: 1
project: paper7
deadline: 2026-04-25 eod
expected_output: /outbox/paper7/{anchor_papers_verified,predictions_derivation,datasets_to_test,status}.md
verification:
  - Each anchor paper has a verified DOI, published venue, and one-sentence empirical result
  - Each prediction explicitly labels theorem vs. conjecture vs. modeling choice
  - Each dataset listing names a real publication or database with access status
---

# Paper 7 literature foundation — thermodynamic synthesis

Context for this task is in `/todos/TODO_RESEARCH_LANES.pdf` (this repo). Read that first.

Paper 7 working title: *The Thermodynamic Cost of the Coherence Ceiling: A G₂-Derived Bound on Conscious Information Processing.*

The goal is to synthesize four published 2024–2026 thermodynamics/consciousness results with Martin's G₂ framework (DOIs: 10.5281/zenodo.19242936, .19480758, .19602470, .19617662, .19648892, .19672709) and produce a parameter-free quantitative prediction for each.

---

## Work Item 1 — Anchor paper acquisition + verified citations

Save output to `/outbox/paper7/anchor_papers_verified.md`.

For each of the four papers: download the PDF to `/outbox/paper7/pdfs/` with a clean filename, verify the published citation (authors, journal, volume, page/article number, year, DOI), extract the single most important empirical result (one sentence, one number if applicable), extract the methodology in one paragraph, note caveats or failures to replicate.

Target papers:

1. **Berjaga-Buisan et al., "Fluctuation-Dissipation Theorem violations correlate with consciousness levels"** — bioRxiv 2025 or journal version.
2. **Wadhia et al., "Entropy cost of quantum clock measurement"** — Physical Review Letters, approximately November 2025. Key number: 10⁹ entropy ratio between apparatus and measured system.
3. **Basso et al., "Observer-dependent entropy in curved spacetime"** — Physical Review Letters 134 (050406) and JHEP 07(2025)146. Claim: mathematically equivalent to Page-Wootters.
4. **Hengen & Shew, "Criticality meta-analysis across 140 neural datasets"** — Neuron 2025. Key result: brain self-tunes to branching ratio 1.0.

If any title is slightly off (my sources are approximate), find the closest published work by the cited authors on the cited topic and note the discrepancy in the output file.

---

## Work Item 2 — Derive predictions from 42/49 = 6/7

Save output to `/outbox/paper7/predictions_derivation.md`. For each anchor, write the derivation from the G₂ framework as explicitly as possible. Label every step: **theorem**, **conjecture**, or **modeling choice**.

**(a) FDT violation parameter.** Claim: scales as (1 − 6/7) = 1/7 of some reference quantity. Determine what reference — equilibrium fluctuation magnitude? response function? some effective temperature difference? Derive the specific dimensionless ratio Paper 7 should predict. Check whether the Berjaga-Buisan dataset has the units and setup to test this.

**(b) Checkpoint entropy cost.** Apply Landauer's principle (k_B T ln 2 per erased bit) to the G₂ Checkpoint event in Paper 5 (zenodo.19648892). Estimate: how many bits does the checkpoint erase? Use realistic biological parameters (T = 310 K, reasonable cell volume, information content of the G₂ gate). Wadhia's ratio is 10⁹ for a quantum clock; what's the corresponding number for a cell-cycle checkpoint?

**(c) Observer-frame entropy across 8 cosets.** The PSL(2,7)/F₂₁ quotient gives 8 cosets. If each corresponds to a worldline in the Basso et al. sense, the entropy assignment should differ across cosets by a computable amount. Close reading of the Basso paper required. Output the explicit worldline-dependent entropy formula restricted to the 8-coset structure.

**(d) Criticality branching ratio.** Hengen-Shew shows the brain self-tunes to σ = 1.0. Claim: the G₂ attractor predicts σ = 1.0 + O(1/49). Derive the correction term. It should be small, nonzero, and measurable in principle.

For every derivation, flag anything where the math doesn't actually give the claimed result. It's better to find these out now than in peer review. If a prediction falls apart under scrutiny, say so and we'll adjust the claim or cut it.

---

## Work Item 3 — Existing datasets that could test each prediction

Save output to `/outbox/paper7/datasets_to_test.md`.

For each of the four predictions, identify at least one existing published dataset. Include: dataset name, source publication or database, who produced it, number of samples/measurements, which prediction it tests, what analysis would be required, access status (open / request-based / proprietary).

**Bonus:** Martin emailed Bandyopadhyay on April 10 requesting DDG data to check the 28 MHz prediction from Paper 3. If that dataset is directly relevant to any of the four Paper 7 predictions, flag which one.

---

## Output and communication

- Three markdown files in `/outbox/paper7/` as specified above.
- Plus `/outbox/paper7/status.md` — one-paragraph status update when done.
- Target completion: by end of day Friday April 24 PDT.

If you find something surprising — a derivation that doesn't work, a dataset that contradicts a prediction, a paper that already scoops Paper 7's conclusion — flag it immediately to `/inbox/for_human/` as `YYYY-MM-DD_flag_description.md`.

Questions on modeling choices or derivation moves: drop a note in `/inbox/for_c7ro/`. I'll pick it up on the next cycle.

Don't guess when uncertain — flag.
