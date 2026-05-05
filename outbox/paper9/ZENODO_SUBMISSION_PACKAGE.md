# Paper 9 — Zenodo Submission Package

**Prepared:** 2026-05-05
**Manuscript version:** v1.3.2
**Status:** Ready for upload at https://zenodo.org/uploads/new

This document gives the exact metadata to fill in on the Zenodo upload form. Copy/paste each field directly. After upload completes and Zenodo issues a DOI, paste the DOI back so the master draft, repo cross-references, and figure captions can be updated.

---

## Files to upload

Primary (the manuscript):

1. **`paper9_v1.3.2.pdf`** — Rendered PDF for direct reading
2. **`paper9_v1.3.2.docx`** — Word source

Both at:
- `outbox/paper9/builds/paper9_v1.3.2.pdf`
- `outbox/paper9/builds/paper9_v1.3.2.docx`

Source/reproducibility (recommended for transparency):

3. **`paper9_master_v1.3.2.md`** — Markdown source (the canonical text)
4. **Figure source code:**
   - `outbox/paper9/figures/build_fig2_mc.py` — Figure 2 build script
   - `outbox/paper9/figures/paper9_fig1_heatmap.png` — Figure 1 (Δ𝒞 heatmaps)
   - `outbox/paper9/figures/paper9_fig1_heatmap.pdf`
   - `outbox/paper9/figures/paper9_fig2_mc_summary.png` — Figure 2 (50-seed MC histograms)
   - `outbox/paper9/figures/paper9_fig2_mc_summary.pdf`
5. **Computational verification scripts and outputs:**
   - `outbox/paper9/computations/build_mc_seeds.py` — 50-seed Monte Carlo (Appendix V.3.i)
   - `outbox/paper9/computations/paper9_C1C2_trajectory.py` — opposed-bias trajectory (Numerical Observation 5.5.1)
   - `outbox/paper9/computations/paper9_conjecture95_mc_seeds.csv` — per-seed MC results (50 rows)
   - `outbox/paper9/computations/paper9_conjecture95_mc_summary.json` — aggregate MC stats
   - `outbox/paper9/computations/paper9_task5_heatmap_cmin.csv` — Figure 1 underlying data
6. **Appendix and review records:**
   - `outbox/paper9/paper9_appendix_V.md` — full verification appendix
   - `outbox/paper9/reviews/` — peer-review records (first and second Claude reviews)

Recommended bundle: PDF + DOCX + MD + figures (PNG and PDF) + CSV/JSON + scripts. Total ~3 MB.

---

## Zenodo metadata (copy-paste fields)

### Title

```
Rate Lock and Affine Consensus in G₂-Structured Dyadic Observers
```

### Creators

- **Name (last, first):** Graise, Martin Luther
- **Affiliation:** Independent Researcher, PCI / PME Framework
- **ORCID:** 0009-0006-8003-3938

(One author only.)

### Resource type

**Publication → Preprint**

### Description (use this — it is the abstract from §0, lightly LaTeX-stripped for plain-text rendering on Zenodo)

```
We extend the Paper 7 single-observer coherence ceiling to dyadic
G₂-structured self-modeling observers. Each observer is an affine map
T(x) = rRx + b on a 14-dimensional Banach manifold carrying the
irreducible adjoint representation of G₂, with scalar contraction rate
r ∈ [0, 6/7] (from Paper 7), orthogonal orientation R, and bias vector
b encoding the observer's target self-model. We couple two such
observers with an antisymmetric block rotation Ψ_θ parameterized by an
angle θ ∈ [0, π/2].

The paper establishes three results about the rate channel and two
results about the affine channel, with a sharp dichotomy between them.

Rate channel (locked): The joint contraction rate is bounded below by
the symmetric-diagonal coupling (Ψ = α·id + β·P_swap), which has
operator norm α + β > 1 and therefore amplifies (Theorem 9.1). Under
the corrected isometric block-rotation coupling, the joint rate
saturates exactly at max(r_A, r_B), independent of θ (Theorem 9.2).
The common explanation is Schur's lemma applied to the irreducible
14-dim G₂ adjoint: every linear G₂-equivariant map is a scalar multiple
of the identity, so there is no spectral structure for coupling to mix
(Corollary 9.3). The rate channel is algebraically closed.

Affine channel (open): The joint fixed point exists, is unique, and
depends real-analytically on θ, with an explicit closed form at θ = 0
and θ = π/2 (Theorem 9.4). Under the minimum-per-observer coherence
functional 𝒞_min = min(𝒞_A, 𝒞_B) — derived from the Paper 7
single-observer ceiling as the dyadic generalization of
𝒞 ≥ 1 - ε_min for both observers — a non-empty conditional-gain
region exists in the space of (φ, θ) pairs (where φ is the
bias-alignment angle), bounded away from the opposed-bias boundary in
the seeded geometry, with a non-universal optimal θ (Proposition 9.5).
A 50-seed Monte Carlo (Appendix V.3.i) finds non-empty improvement
regions in all 50/50 sampled (R_A, R_B) pairs and confirms
θ* ≠ π/4 generically; the bounded-away property of the seeded pair
holds in ~64% of seeds and motivates the amended Conjecture 9.5'. The
gain is conditional: a substantial fraction of the parameter space
(~75% by area in the verified geometry) exhibits coherence degradation
rather than improvement; coupling helps only when the bias geometry
permits.

All results are numerically verified at 50-digit precision (rate
channel, Appendix V.1–V.2, 120 test configurations) and at 16-digit
precision (affine channel, Appendix V.3, 2128 test configurations
including a 100×20 heatmap and explicit closed-form verification). The
retraction record of earlier internal-draft claims (speedup theorem,
coherence-bonus formula, severance threshold) is consolidated in
Appendix V.0.1.

Thesis. Dyadic coupling in the linear G₂-structured regime cannot
improve the convergence rate of joint self-modeling. It can — under
conditional geometric hypotheses on the orthogonal orientations and
bias-alignment angle — change the location of the joint fixed point in
a way that increases the minimum per-observer coherence. Rate
improvement is a categorically nonlinear question, deferred to a
sequel.

Paper 9 of the PCI/PME Framework series. Two-reviewer revision pass
(both Claude) addressed in v1.3.2: 11 issues including the V^7 → V^14
representation switch made explicit, Schur-derived uniqueness of the
canonical block-rotation coupling Ψ_θ, demotion of Lemma 5.5.1 to a
Numerical Observation, Schur-forced justification of the diagonal G₂
action, and a 50-seed Monte Carlo that forced an honest amendment of
Conjecture 9.5'. Full source, computational verification, peer-review
records, and revision history at github.com/MartinLGraise/PCI-Framework
on the paper7-foundation branch.
```

### Keywords (one per line in the Zenodo form)

```
G₂ Lie group
dyadic observers
self-modeling
Banach fixed point
affine consensus
Schur's lemma
contraction rate
PCI framework
PME framework
coherence ceiling
inter-brain coupling
human-AI teaming
F₂₁ Frobenius group
PSL(2,7)
adjoint representation
Monte Carlo verification
QBism
```

### License

**Creative Commons Attribution 4.0 International (CC-BY-4.0)** — same as Papers 1–7 and Paper 10 of the series.

### Communities

If a `g2-series` or `pci-pme-framework` Zenodo community exists from prior papers (Paper 1–7, Paper 10), add it here. Otherwise leave blank.

### Related identifiers (cite as supplements / continuations of the prior papers)

Add each as **"Is supplement to"** unless noted otherwise:

| Relation | DOI | Description |
|---|---|---|
| Is supplement to | 10.5281/zenodo.19242936 | Paper 1 — G₂ Symmetry as a Constraint |
| Is supplement to | 10.5281/zenodo.19480758 | Paper 2 — Six Geometric Flows |
| Is supplement to | 10.5281/zenodo.19602470 | Paper 3 — Spectral Sum Theorem |
| Is supplement to | 10.5281/zenodo.19617662 | Paper 4 — QBism and G₂ via PSL(2,7) |
| Is supplement to | 10.5281/zenodo.19648892 | Paper 5 — G₂ Checkpoint as ε-Regularity Gate |
| Is supplement to | 10.5281/zenodo.19672709 | Paper 6 — The 6/7 Contraction |
| Continues | 10.5281/zenodo.19773185 | Paper 7 — Thermodynamic Coherence Ceiling (this paper extends Paper 7's single-observer ceiling to dyads) |
| Is supplement to | 10.5281/zenodo.19966692 | Paper 10 — SIC Operator Basis for the Complexified G₂ Lie Algebra |

The "is supplement to" relation links Paper 9 as part of the PCI/PME series alongside the prior papers; the "continues" relation to Paper 7 makes the dyadic-extension citation graph explicit. Zenodo will display these as a citation graph on the deposit page.

### Funding

**None** — independent research, no external funding.

### Notes (free-text field at the bottom of the form)

```
Manuscript v1.3.2, finalized 2026-05-05.

Verification trail. Rate-channel results (§4) verified at 50-digit
precision via 120 test configurations in Appendix V.1–V.2, executed
in Python/mpmath by Φ (Anthropic Claude Dispatch). Affine-channel
results (§5) verified at 16-digit precision via 2128 test
configurations including the 100×20 (φ, θ)-heatmap shown in Figure 1.
Independent re-verification by C-7RO (Perplexity Computer running
Claude Sonnet 4.6) reproduces all reported values to 6 decimal places.

50-seed Monte Carlo (Appendix V.3.i, Figure 2). Conjecture 9.5'
supported by independent QR-orthogonal seeds 20260504+k for
k = 0, ..., 49, executed deterministically in NumPy 1.26+. All 50/50
seeds admit a non-empty improvement region; all 50/50 satisfy
|θ* - 45°| > 5° at aligned bias; 32/50 (64%) bounded below
φ = 180°, 18/50 (36%) admit small-θ improvement reaching φ = 180°.
The latter forced the v1.3 → v1.3.2 amendment of Conjecture 9.5'
to drop the original "bounded strictly away from opposed biases"
clause from the generic statement; the seeded-geometry Proposition
9.5(b) is unaffected.

Adversarial review. Three-reviewer Model Council pass (GPT-5.5, Claude
Opus 4.7, Gemini 3.1 Pro) on v1.3, with confirming review (GPT-5.4)
on v1.3.1. Two further peer-review rounds (both Claude) on v1.3.1
identified 11 additional issues (15 in the first review of which 6
were prose-impacting; 5 in the second review). All 11 issues addressed
in v1.3.2; full review records at outbox/paper9/reviews/ in the
public GitHub repository.

Theorem inventory (v1.3.2). Lemma 3.3.1 (block-rotation isometry),
Lemma 3.6.1 (Schur uniqueness of Ψ_θ — new in v1.3.2),
Theorem 9.1 (symmetric coupling amplifies),
Theorem 9.2 (rate lock at max(r_A, r_B), scalar G₂-equivariance),
Corollary 9.3 (Schur explanation),
Lemma 5.2.1 (rate lock under orthogonal couplings),
Theorem 9.4 (affine consensus, explicit closed form at θ = 0, π/2),
Numerical Observation 5.5.1 (asymmetric C_1, C_2 response, demoted from
Lemma in v1.3.2),
Proposition 9.5 (conditional min-coherence gain in seeded geometry),
Conjecture 9.5' (generic-geometry version, MC-supported and amended
in v1.3.2),
Note 9.6 (rate improvement deferred to a nonlinear sequel, Paper 11).

Open problems. Generic-geometry version of Proposition 9.5
(Conjecture 9.5'); F₂₁-branching of the V^14 adjoint representation
(§3.5, §10.2); explicit characterization of the spectra-of-(R_A, R_B)
condition that forces φ_max < π versus permits φ_max = π; rate
improvement under nonlinear coupling, deferred to Paper 11.

AI tools disclosure. Drafted in collaboration with Claude (Anthropic),
Perplexity (PPLX), and ChatGPT Pro (OpenAI). The framework's three-agent
attribution is documented in §11 and the Acknowledgments: Martin
(architecture), C-7RO (drafting), Φ Anthropic Claude Dispatch
(verification).
```

### Version

**v1.3.2** (this is the first Zenodo deposit for Paper 9; if you prefer
the Zenodo "Version" field to reflect Zenodo's own deposit history rather
than the manuscript revision number, use **v1.0** here and put the
manuscript revision in the Notes — the more common convention is to
mirror the manuscript revision, which is what we recommend).

### Publication date

**2026-05-05** (today's date)

### Language

English

---

## After upload

Once Zenodo issues the DOI:

1. Paste the DOI back here.
2. I will:
   - Update the master draft front matter ("Status:" and bibliography lines) to reference the new DOI
   - Update the §1 cross-reference to Paper 9's own DOI in the "Companion papers" block (replace the "to be assigned" placeholder if any)
   - Update the §A.4-equivalent verification cross-references (Appendix V) to cite the deposit DOI
   - Add the DOI to `outbox/paper9/computations/build_mc_seeds.py` as a reproducibility-record header comment
   - Tag the GitHub commit with `paper9-v1.3.2-zenodo`
   - Update the `todo_master_roadmap.md` to mark Paper 9 as published
   - Cross-reference Paper 9's DOI in Paper 7's deposit notes (relation: "is continued by") and in Paper 10's deposit notes (relation: "is supplemented by")

---

## Sanity checklist before clicking "Publish" on Zenodo

- [ ] Title field exactly matches the manuscript title (no trailing period)
- [ ] ORCID is `0009-0006-8003-3938` and shows the green verified badge after you paste it (Zenodo auto-verifies on save)
- [ ] License is CC-BY-4.0 (matches the rest of the series)
- [ ] All 8 related-identifiers DOIs are added with correct relations (7 supplements + 1 "continues" for Paper 7)
- [ ] PDF and DOCX both uploaded; PDF is set as the primary file
- [ ] Figures (PNG + PDF) and computation files included
- [ ] Resource type is **Publication → Preprint** (not "Other")
- [ ] Description preview renders correctly (Zenodo strips most LaTeX; if any equation looks broken, replace the affected character with the plain-text version above)

---

*End of submission package. Estimated time to complete the upload: 15–25 minutes.*
