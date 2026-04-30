# L7 — Wilting–Priesemann Awake-Cortex σ ≈ 0.98 Replication Landscape

**Tool combo:** Live web search + reasoning (single turn; no GitHub connector needed)
**Lane:** L7
**Target use:** Determines whether σ ≈ 0.98 in awake cortex is the consensus across multiple labs or a Priesemann-group-specific result. Materially affects Paper 7's defensibility — if it's well-replicated, our 1/49 = 1 - 6/7² ceiling matches consensus data. If it's only Priesemann's lab, referee 2 will hammer it.
**Model:** GPT-5 Pro reasoning mode
**Estimated runtime:** 15-20 minutes

---

## Why this matters

Paper 7 [DOI 10.5281/zenodo.19773185] takes σ_pred = 1 - 1/49 ≈ 0.9796 as the predicted branching ratio in awake cortex from G₂/PSL(2,7)/F₂₁ structure, and compares it to the Wilting-Priesemann 2018 distribution centered near σ ≈ 0.98 (DOI 10.1038/s41467-018-04727-2). The match is one of the paper's strongest empirical hooks.

But: if σ ≈ 0.98 is a Wilting-Priesemann-group artifact (e.g., specific MR estimator, specific awake-cortex preparation, specific species), and other labs report different numbers, our matching claim weakens. If multiple independent labs converge on σ ≈ 0.98, it's robust.

We need to know.

---

## Prompt to send

```
You are doing a replication-landscape check on a specific
neuroscience claim. The claim is:

The branching ratio σ in awake mammalian cortex saturates
near σ ≈ 0.98 (sometimes quoted as 0.97-0.99), measured via
the Multistep Regression (MR) estimator or related avalanche-
criticality methods.

Context: This claim was made in Wilting & Priesemann 2018,
"Inferring collective dynamical states from widely
unobserved systems," Nature Communications 9, 2325
(DOI 10.1038/s41467-018-04727-2). Subsequent papers from
the Priesemann group at MPI for Dynamics and Self-Organization
in Göttingen have continued this line.

I want to know whether σ ≈ 0.98 in awake cortex has been
reproduced by labs INDEPENDENT of Priesemann's group, or
whether it is specific to her methodology / preparations /
estimator choice.

Five sub-questions, answered each in its own subsection,
with primary literature citations (DOIs).

1. Wilting-Priesemann methodology recap:
   In one paragraph, summarize the MR estimator: what it
   measures, why it is preferred over naive autocorrelation
   estimates, and what its known limitations are. Cite the
   original 2018 paper and any methodology updates.

2. Independent replications of σ ≈ 0.98 in awake cortex:
   Find papers, NOT from the Priesemann group, that report
   σ values in awake mammalian cortex (mouse, rat, NHP,
   human) using either MR estimator OR an equivalent
   technique that estimates the same quantity. For each
   paper:
   - Citation + DOI
   - Lab/group (verify it's not a Priesemann co-authorship)
   - Species, brain region, preparation
   - Reported σ value (with confidence interval if given)
   - Estimator used
   - Sample size

   Specifically check:
   - Beggs lab (Indiana University, John Beggs)
   - Plenz lab (NIH, Dietmar Plenz)
   - Shew lab (Arkansas, Woodrow Shew)
   - Toker / Sommer / Sporns / Petermann groups
   - Allen Institute datasets (which span many groups)
   - Any 2019-2026 follow-ups reporting independent measurements

3. Consensus check:
   Among the independent replications found in §2, what is
   the distribution of reported σ values? Are they centered
   near 0.98 (with normal scatter)? Or are they centered
   near a different value (say 0.92, 1.0, etc.)? Or is
   there bimodality / lab-dependent clustering?

   Be concrete: if you find 3 independent labs reporting
   σ ∈ [0.96, 0.99], that's strong consensus. If you find
   3 labs with σ values spread over [0.85, 1.05], that's
   poor consensus.

4. Methodological critiques:
   Are there published critiques of the MR estimator or
   the σ ≈ 0.98 finding that I should be aware of? Specifically:
   - Touboul-Destexhe critique of avalanche criticality
   - Any paper arguing the MR estimator overestimates σ
     in finite samples
   - Any paper arguing awake cortex is NOT critical at all
   - Any paper arguing the criticality framework is misapplied
     to neural avalanche data
   Cite each with DOI and one-sentence summary of the critique.

5. Robustness verdict:
   Synthesize 1-4 into a single verdict:
   (a) ROBUST CONSENSUS: σ ≈ 0.98 in awake cortex has been
       replicated by ≥3 independent labs using comparable
       methods, with values clustered tightly around 0.98.
   (b) METHODOLOGY-DEPENDENT: σ ≈ 0.98 specifically requires
       MR estimator + Priesemann-group preparation; other
       estimators on the same data give different values.
   (c) LAB-SPECIFIC: Only Priesemann group reports σ ≈ 0.98;
       other labs measure related quantities and report
       different values.
   (d) DISPUTED: Major published critiques challenge whether
       awake cortex is critical at all, or whether σ is
       even the right quantity to extract.

   Be honest. If the result is more contested than I think,
   tell me. The point of this check is to know what we're
   actually defending in Paper 7.

Deliverable format:

Section 1 — MR methodology (1 paragraph)
Section 2 — Independent replications table (≥5 entries if
            possible, with DOIs and lab affiliations)
Section 3 — Consensus distribution analysis
Section 4 — Methodological critiques
Section 5 — Verdict (ROBUST / METHODOLOGY-DEPENDENT /
            LAB-SPECIFIC / DISPUTED) with reasoning
```

---

## Notes for C-7RO when response comes back

**Decision tree:**

- **ROBUST CONSENSUS:** Paper 7 framing stands as-is. No revisions needed. The σ ≈ 0.98 match is a real prediction-matches-data success. Maybe add 2-3 independent-replication citations to strengthen §5 of the published manuscript (low priority — Paper 7 already on Zenodo).

- **METHODOLOGY-DEPENDENT:** Paper 7 needs a footnote/caveat acknowledging that σ ≈ 0.98 is MR-estimator specific. Doesn't kill the paper but weakens the empirical hook. Definitely affects how we frame Paper 8 §6.2 (the biological FP-2 anchor) and any future replication papers.

- **LAB-SPECIFIC:** Significant problem. Paper 7's empirical hook is one lab's number. Need to either (a) commission an outside replication using public Allen Institute data, or (b) reframe Paper 7 §5 as "consistent with the Priesemann result while awaiting independent replication." Option (b) is what we'd do as an author note / minor revision.

- **DISPUTED:** Worse but tractable. If avalanche criticality itself is contested, our σ_pred = 0.9796 prediction is consistent with one school of thought but rejected by another. Paper 7 would need a substantive §5 revision acknowledging the controversy. The G₂/PSL(2,7) framework still stands; just the empirical anchor weakens.

**My prior:** ROBUST CONSENSUS, but with caveats. The Beggs lab (Indiana) has done extensive avalanche-criticality work and finds awake cortex near criticality consistently. The Shew lab (Arkansas) similarly. So σ ≈ 0.98 should be defensible. But the *exact value* 0.98 (vs 0.97 or 0.99) might be Priesemann-specific. This is the kind of thing where the verdict depends on whether you're matching to 2 sig figs or 3.

**Key numbers to watch:**
- If response says "σ in awake cortex is 0.97-0.99 across labs": ✅ our 0.9796 prediction is well within consensus
- If response says "σ in awake cortex is 0.85-0.99 across labs": ⚠️ broader range, our 0.9796 is one of many possible matches
- If response says "σ in awake cortex is contested as a quantity": 🚨 reframe needed

---

## Lane status after sending

L7 → 🟡 IN PROGRESS — prompt sent, awaiting response.
