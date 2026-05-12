# Paper 14 v1.6 — Residence Where Transits Were Design Intent — Zenodo Deposit Package

**Author:** Martin L. Graise (ORCID [0009-0006-8003-3938](https://orcid.org/0009-0006-8003-3938))
**Repository:** [github.com/MartinLGraise/PCI-Framework](https://github.com/MartinLGraise/PCI-Framework)
**Branch / tag:** `paper7-foundation` / `paper14-v1.6-preprint`
**Deposit version:** 1.6 (first deposit; new concept-DOI)
**License:** CC-BY-4.0

---

## What this deposit is

This is the **first** Zenodo deposit of Paper 14. A new concept-DOI is minted (not a new version of an earlier paper). Paper 14 builds on but is structurally independent of earlier deposits in the PCI Framework series, listed under "Related identifiers" with relation `isContinuationOf`.

v1.6 is the courtesy-preprint draft prepared for Tier A reviewer circulation two weeks before journal submission. Subsequent versions (v1.7 after Tier A revisions, v1.8 after Tier B revisions, and the journal submission version) will be deposited as Zenodo new-versions on this same concept-DOI.

## Title

**Residence Where Transits Were Design Intent: A Cross-Substrate Formalism for Coupling-Failure Pathology**

## Plain-language summary

Many biological, cognitive, and artificial systems enter transient states that are normal when briefly sampled but pathological when residence persists. This paper introduces a measurable two-axis observable for residence-pathology, demonstrates it across eight substrates from receptor pharmacology to recursive AI training loops, and proposes a thirteen-experiment falsification program.

## What's in this deposit

| File | Purpose |
|---|---|
| `paper14_v1_draft.pdf` | Main paper, v1.6 (the citable artifact) |
| `paper14_v1_draft.docx` | Same paper, Word format |
| `paper14_v1_draft.md` | Same paper, source Markdown |
| `figures/fig1_two_axis_observable.{png,pdf}` | Figure 1 — R(s,c) phase diagram with four canonical cases |
| `figures/fig2_cross_substrate_grammar.{png,pdf}` | Figure 2 — eight-substrate × six-descriptor grammar matrix |
| `figures/fig3_return_path_machinery.{png,pdf}` | Figure 3 — four-panel return-path-machinery typology |
| `figures/fig4_kinetic_strategies.{png,pdf}` | Figure 4 — symmetric kinetic-stabilization strategies (A–E) |
| `figures/fig5_experimental_agenda.{png,pdf}` | Figure 5 — thirteen experiments organized by cluster, tier, and dependency |
| `figures/*.py` | Source scripts for all five figures (reproducibility) |
| `figures/README.md` | Figure catalog with paper-section call-outs |
| `zenodo_metadata_v1.6.json` | Zenodo metadata for this deposit |
| `README_v1.6.md` | This file |

## The core claim

We introduce a two-axis residence-time observable

\[
R(s, c) = \tau_R(s) \times \pi_c
\]

combining temporal dwell τ_R in state s with compartmental occupancy probability π_c, paired with an exit-rate variable

\[
\lambda_{\mathrm{exit}}(s, c) = 1/\tau_R(s, c)
\]

that captures the return-path-machinery capacity. Pathology corresponds to R escaping substrate-specific functional residence bounds on either axis, with s and c possibly unchanged. A normalized form

\[
\Delta_R(s, c) = \log(\tau_R/\tau_0) + \log(\pi_c/\pi_0)
\]

makes the observable substrate-portable.

The one-line thesis:

> **Pathology is not visiting the wrong state; pathology is losing the way back.**

## Four canonical cases (§3)

Two pure-axis cases (FUS in stress granules — temporal only; PrP topology — spatial only) plus two both-axes cases (Huntingtin nuclear-versus-mitochondrial residence; tau multi-compartment mislocalization) establish that two axes are *empirically necessary* rather than theoretically convenient.

## Eight substrates (§8)

| § | Substrate | State / Compartment | Pathology |
|---|---|---|---|
| 8.1 | Pharmacology (Copeland) | drug-target binding / tissue compartment | long-residence toxicity |
| 8.2 | Cancer phospho-regulation | phospho-substrate state / intracellular localization | constitutive activation |
| 8.3 | Autonomic physiology | sympathetic vs parasympathetic / baseline vs perturbation regime | depression, CV disease |
| 8.4 | Exercise physiology | metabolic boundary state / cardiac etc. compartments | operator-sustained cardiomyopathy (HAARLEM) |
| 8.5 | Brain-network dynamics | metastable brain state / regional occupancy | depression, anxiety, rumination |
| 8.6.1 | Memory phenomenology | retrieval-coupled state / present-axis vs past-axis | PTSD, regret, nostalgia, grief |
| 8.6.2 | Public-epistemic ecosystems | interpretive frame / source cluster | echo chambers, misinformation |
| 8.7 | AI / data substrate | model-distribution mode / training-data regime | model collapse, epistemic degradation |

## What this contribution is

> The formal-operational composition of relation-first prior art (Rovelli, French & Ladyman, Maturana & Varela, Friston, Carhart-Harris-Chandaria-Friston, Whitehead, Simondon, Copeland) into one empirically tractable formalism with a substrate-uniform return-path-failure pathology grammar, **not** a first articulation of relation-first ontology at any single substrate.

§9 enumerates the prior-art concessions explicitly, by substrate, so reviewers see what the framework owns versus inherits.

## Experimental program (§11)

Thirteen experiments with binary falsification conditions, in two clusters:

- **Cluster A — Cross-substrate recovery-kinetics** (Experiments 1–8): cross-domain perturbation-recovery battery, multimodal HRV + fMRI in depression, proteostasis-phospho-regulation coupling, dominant-eigenvalue modeling, longitudinal early-warning, return-path composite, intervention-convergence, boundary-condition self-falsification.
- **Cluster B — Pharmacology-to-psychedelics bridge** (Experiments 9–13): matched-exposure varied-k_off 5-HT₂A panel, **antagonist-termination ketanserin-during-psilocybin (killer experiment)**, clinical occupancy-to-dynamics PK/PD model, spontaneous-vs-perturbational dissociation, baseline-rigidity-as-moderator.

Experiments 2, 5, 6, 7, 11 are designated for OSF pre-registration. Sample-size justifications and statistical-method specifications are in §11.4.

## What is deferred to a companion paper

The G₂ / octonion mathematical-physics interpretation of R(s, c) is deferred to **Paper 15** (in preparation), which has three explicit derivation burdens:

1. Derive why non-associativity should be read as irreducible relationality rather than algebraic failure of reassociation
2. Show why G₂ specifically, rather than some broader exceptional or categorical structure, is the right symmetry notion for coherent coupling
3. Define at least one concrete invariant or observable from associators or G₂-equivariant quantities that distinguishes coherent from failed coupling

**Paper 14 stands without Paper 15.** R(s, c) is empirical and operational; the mathematical-physics interpretation is a separate question.

## Citation

Graise, M. L. (2026). *Paper 14 — Residence Where Transits Were Design Intent: A Cross-Substrate Formalism for Coupling-Failure Pathology* (v1.6 preprint). Zenodo. [https://doi.org/10.5281/zenodo.20145811](https://doi.org/10.5281/zenodo.20145811)

BibTeX:

```bibtex
@misc{graise2026paper14v16,
  author       = {Graise, Martin L.},
  title        = {Paper 14 --- Residence Where Transits Were Design Intent:
                  A Cross-Substrate Formalism for Coupling-Failure Pathology
                  (v1.6 preprint)},
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v1.6},
  doi          = {10.5281/zenodo.20145811},
  url          = {https://doi.org/10.5281/zenodo.20145811},
  note         = {Tag paper14-v1.6-preprint at github.com/MartinLGraise/PCI-Framework. Cross-substrate residence-pathology formalism; PCI Framework series.}
}
```

---

## Zenodo upload steps (from your phone or laptop)

This is a **new deposit**, not a new version of an existing record:

1. Go to [zenodo.org](https://zenodo.org) and log in (use the same ORCID-linked account that deposited Paper 12 v1.4).
2. Click **"New upload."**
3. **Files:** drag in `paper14_v1_draft.pdf` (the main artifact). Optionally also add `paper14_v1_draft.docx`, `paper14_v1_draft.md`, the five figure PDFs, and `README_v1.6.md`.
4. **Resource type:** Publication → Preprint.
5. **Title:** "Paper 14 — Residence Where Transits Were Design Intent: A Cross-Substrate Formalism for Coupling-Failure Pathology"
6. **Authors:** Graise, Martin L. (ORCID `0009-0006-8003-3938`, affiliation "Independent researcher").
7. **Description:** paste from `zenodo_metadata_v1.6.json` `description` field (HTML allowed).
8. **Version:** `1.6`
9. **License:** Creative Commons Attribution 4.0 International (CC-BY-4.0).
10. **Access right:** Open.
11. **Related identifiers:** add each entry from `zenodo_metadata_v1.6.json` `related_identifiers` field. The five `isContinuationOf` DOIs are Paper 9, 11, 12 v1.0–v1.2, v1.3, and v1.4 in chronological order; the GitHub URL is the supplementary code repository.
12. **Keywords:** paste the keyword list from `zenodo_metadata_v1.6.json`.
13. **Notes:** "First deposit of Paper 14 — a new concept-DOI for the residence-pathology cross-substrate formalism. v1.6 is the draft circulated for courtesy preprint to Tier A reviewers two weeks before journal submission. Repository at github.com/MartinLGraise/PCI-Framework, branch paper7-foundation, tag paper14-v1.6-preprint."
14. **Save** → **Publish.**

Zenodo will mint a new concept-DOI plus a v1.6 version DOI. Note both for the citation block update in this README and the GitHub commit that follows.

## Post-publish GitHub steps

1. Live DOI: **[10.5281/zenodo.20145811](https://doi.org/10.5281/zenodo.20145811)** — back-filled into citation block and BibTeX above on 2026-05-12.
2. Tag the commit:

```bash
git tag -a paper14-v1.6-preprint -m "Paper 14 v1.6 first Zenodo deposit, DOI 10.5281/zenodo.20145811"
git push origin paper14-v1.6-preprint
```

3. Update `outbox/syntheses/todo_master_roadmap.md` with the v1.6 entry.

---

## Provenance

- All §1–§14 prose drafted 2026-05-12 in a single intensive session
- Five figures generated 2026-05-12 with manual inspection for text overflow, label collisions, and subscript rendering
- §8.6 restructured per Claude Opus and ChatGPT Pro reviews (missing-scientists example removed, public-epistemic substrate re-anchored to Vosoughi 2018, Cinelli 2020, Bail 2018, Mantegna-Stanley-Sornette)
- Author attribution for arXiv:2605.06347 (Wu, Kang, Xu, Xie, Mi, Wang, Liu & Chen 2026) verified directly against arxiv.org
- Sample-size justifications, OSF pre-registration commitment, and HAARLEM-anchored exercise physiology added in same session
- Abstract tightened 26% per ChatGPT Pro review

Repository commit history at [github.com/MartinLGraise/PCI-Framework/commits/paper7-foundation](https://github.com/MartinLGraise/PCI-Framework/commits/paper7-foundation) preserves the full development trail.

---

*The framework's central methodological discipline is concession of prior art at each substrate. The contribution is the explicit composition rule, not new substrate-level claims at any one row.*
