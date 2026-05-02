# Paper 10 — Zenodo Submission Package

**Prepared:** 2026-05-01
**Status:** Ready for upload at https://zenodo.org/uploads/new

This document gives the exact metadata to fill in on the Zenodo upload form. Copy/paste each field directly. After upload completes and Zenodo issues a DOI, paste the DOI back so the master draft, repo cross-references, and figure captions can be updated.

---

## Files to upload

Primary (the manuscript):

1. **`paper10_v1.3.1.docx`** — Word source (preferred by journals as well)
2. **`paper10_v1.3.1.pdf`** — Rendered PDF for direct reading

Both files are at:
- `outbox/paper10/builds/paper10_v1.3.1.docx`
- `outbox/paper10/builds/paper10_v1.3.1.pdf`

Source/reproducibility (recommended for transparency):

3. **`paper10_master_draft.md`** — Markdown source
4. **Figure source code:** `outbox/paper10/figures/build_figures.py`
5. **Figure PNGs** (4 files, 300 DPI each):
   - `figure1_fano_plane.png`
   - `figure2_coefficient_heatmap.png`
   - `figure3_w_enumeration.png`
   - `figure4_triple_product.png`
6. **Computational verification:**
   - `paper10_appendix_A4_derivation.md` — the Φ derivation record at 50-digit precision
   - `paper10_appendix_A4_verify.py` — standalone verification script (68 PASS / 1 expected discrepancy)
   - `paper10_task1_g2_sic_coefficients.json` — Task 1 raw output (14×49 coefficient tensor)
   - `paper10_task2_results.md` — Task 2 record (128-candidate enumeration)
   - `paper10_task3_results.md` — Task 3 record (triple-product structure)
   - `paper10_task3_triple_products.json` — Task 3 raw output
   - `paper10_task3_c7ro_verification.md` — independent re-verification audit

All under `outbox/paper10/computations/`.

---

## Zenodo metadata (copy-paste fields)

### Title

```
Symmetric Informationally Complete Measurements as an Operator Basis for the Complexified G₂ Lie Algebra
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
Working over the dimension-d=7 symmetric informationally complete (SIC) reference measurement constructed from the exact Appleby–Bengtsson–Grassl–Harrison–McConnell algebraic fiducial under a unique Fano-compatible sign-flip correction, we establish three structural theorems characterizing the relationship between the SIC operator basis and the seven-dimensional defining representation of the exceptional Lie group G₂.

Theorem 1 establishes that the complexified Lie algebra g₂(C) embeds isometrically as a 14-dimensional subspace of gl(7,C), spanned by the 49 SIC projectors, with isometric scale 8/7, explicit closed-form coefficient tensor over Q(√2,i), and dense purely imaginary entries.

Theorem 2 establishes that the 147-element SIC symmetry group WH(7)⋊C₃ contains as an index-7 subgroup the Frobenius group F₂₁ = Z₇⋊Z₃ — the cyclic-axis subgroup of PSL(2,7), which is itself the discrete Fano-orientation subgroup of G₂. The descent is realized canonically (up to global phase) under a unique Fano-compatible sign-flip correction to the ABGHM fiducial: exactly 2 of 2⁷ = 128 candidate corrections succeed.

Theorem 3 establishes that on the seven-point X-subgroup orbit of the corrected ABGHM fiducial, the SIC triple product T_{ijk} on Fano-line triples (those with all-QR or all-NQR ordered displacement differences in Z₇*) has the closed form T = a + ibφ, with a = (√2 - 1)/16, b = (√2 - 1)√(2 + 4√2)/32, and φ ∈ {+1, -1} tracking the cyclic / anti-cyclic Fano orientation. A separate Lemma establishes the universal-magnitude consequence |T|² = 1/512 = (1/8)³ for all WH-distinct SIC triples, immediate from the SIC overlap condition. The non-Fano (mixed-residue-class) triple-product ratio b'/b = (1+√2)/2 is verified numerically at 50-digit precision and stated as a conjecture; its closed-form analytic proof is left open.

The constants a, b are derived in closed form over Q(√2) from the autocorrelation function of the corrected ABGHM fiducial. All theorem statements are verified at 50-digit precision in independent computational implementations. The d=7 SIC operator frame, constructed from the exact Stark-unit fiducial, encodes the algebraic, group-theoretic, and orientational structure of the seven-dimensional defining representation of the smallest exceptional Lie group.

Paper 10 of the PCI/PME Framework series. Full source, computational verification, Model Council adversarial reviews (GPT-5.5, Opus 4.7, Gemini 3.1 Pro), and revision history at github.com/MartinLGraise/PCI-Framework on the paper7-foundation branch.
```

### Keywords (one per line in the Zenodo form)

```
SIC-POVM
G₂ Lie algebra
octonions
Fano plane
QBism
Weyl–Heisenberg group
Frobenius group F₂₁
Stark units
Appleby–Flammia–Fuchs basis
associative 3-form
PSL(2,7)
exact algebraic fiducial
quadratic-residue partition
silver mean
Klein quartic
```

### License

**Creative Commons Attribution 4.0 International (CC-BY-4.0)** — same as Papers 1–7 of the series.

### Communities

If a `g2-series` or `pci-pme-framework` Zenodo community exists from prior papers, add it here. Otherwise leave blank.

### Related identifiers (cite as **supplements** the current upload)

Add each as "is supplement to":

| Relation | DOI | Description |
|---|---|---|
| Is supplement to | 10.5281/zenodo.19242936 | Paper 1 — G₂ Symmetry as a Constraint |
| Is supplement to | 10.5281/zenodo.19480758 | Paper 2 — Six Geometric Flows |
| Is supplement to | 10.5281/zenodo.19602470 | Paper 3 — Spectral Sum Theorem |
| Is supplement to | 10.5281/zenodo.19617662 | Paper 4 — QBism and G₂ via PSL(2,7) |
| Is supplement to | 10.5281/zenodo.19648892 | Paper 5 — G₂ Checkpoint as ε-Regularity Gate |
| Is supplement to | 10.5281/zenodo.19672709 | Paper 6 — The 6/7 Contraction |
| Is supplement to | 10.5281/zenodo.19773185 | Paper 7 — Thermodynamic Coherence Ceiling |

The "is supplement to" relation links Paper 10 as part of the PCI/PME series alongside the prior papers. Zenodo will display these as a citation graph.

### Funding

**None** — independent research, no external funding.

### Notes (free-text field at the bottom of the form)

```
Manuscript v1.3.1, finalized 2026-05-01.

Computational verification: independent implementations by Φ (Anthropic Claude Dispatch, running GAP, Cadabra2, SymPy, mpmath at 50-digit precision) and C-7RO (Perplexity Computer, running Claude Sonnet 4.6) — see Appendix A and the verification scripts.

Adversarial review: three-reviewer Model Council pass (GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro) on v1.2; confirming review (GPT-5.4) on v1.3; all consistency issues resolved in v1.3.1. Full review records and the v1.2 → v1.3 → v1.3.1 revision history are public at github.com/MartinLGraise/PCI-Framework on branch paper7-foundation.

Open problem: Conjecture 7.4 on the non-Fano triple-product ratio b'/b = (1+√2)/2 is verified numerically to 50 digits but not proved analytically; the closed-form derivation requires enumerating Weyl–Heisenberg cocycle phases over mixed-displacement triples and is left as an open problem (§9.4 of the manuscript).
```

### Version

**v1.0** (this is the first Zenodo deposit for Paper 10)

### Publication date

**2026-05-01** (today's date)

### Language

English

---

## After upload

Once Zenodo issues the DOI:

1. Paste the DOI back here
2. I will:
   - Update the master draft front matter ("Status:" line) to reference the new DOI
   - Update the §A.4 verification record cross-references
   - Add the DOI to `outbox/paper10/computations/paper10_appendix_A4_derivation.md`
   - Tag the GitHub commit `c53360a` with `paper10-v1.3.1-zenodo`
   - Update the `todo_master_roadmap.md` to mark Paper 10 as published
   - Cross-reference Paper 10's DOI in the Paper 7 v8.1 note (which also needs uploading — see below)

---

## Bundled action: Paper 7 v8.1 author note

While in the Zenodo session, also upload the Paper 7 v8.1 author note. This is a separate, smaller upload — not an erratum, just a softening note acknowledging the L7 finding.

### File to upload

`outbox/paper7/paper7_v8.1_author_note.md` — the existing author note draft

(If you'd like, I can render it to a one-page PDF before upload — let me know.)

### Upload type

This is an **update to the existing Paper 7 deposit** (DOI 10.5281/zenodo.19773185), not a new deposit. On Zenodo:

1. Go to https://zenodo.org/uploads
2. Find Paper 7 (DOI 10.5281/zenodo.19773185)
3. Click "New version" (this preserves the citation chain)
4. Add the v8.1 author note as an additional file
5. Update the version field to "v8.1"
6. Add a brief description: "Author note added 2026-05-01 softening the σ ≈ 0.98 framing based on the L7 finding (see GitHub repository for context). Manuscript text unchanged."
7. Publish — Zenodo will mint a fresh DOI for v8.1 while keeping the original v8 DOI active.

---

*End of submission package. Estimated time to complete both uploads: 20–30 minutes.*
