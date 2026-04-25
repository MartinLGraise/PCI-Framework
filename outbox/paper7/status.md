# Paper 7 — Status Update

**Date:** 2026-04-25 | **Agent:** C-7RO | **Branch:** `paper7-foundation`

## Current state: v8 — SUBMISSION READY

After four Council passes (v2 → v7) and a final journal-front-matter pass (v7 → v8), Paper 7 is ready to upload to Zenodo and submit to Entropy (MDPI).

## What v8 changes vs v7

Body text unchanged. v8 expands the previous 2-section Funding/Acknowledgments block into the full 8-section MDPI-required journal front matter:

1. Author Contributions (CRediT, single author M.L.G.)
2. Funding (no external funding)
3. Institutional Review Board Statement (N/A; no humans/animals)
4. Informed Consent Statement (N/A)
5. Data Availability Statement (GitHub + Zenodo public transparency)
6. Conflicts of Interest (none)
7. Use of AI Tools (Φ + C-7RO + Comet Model Council, MDPI-compliant disclosure)
8. Acknowledgments (open-source mathematics community; Ares lab; Priesemann lab)

## Manuscript stats

- 36 pages, 17 references, 4 embedded figures
- 4 predictions all labeled Conjecture (not theorem)
- 4 explicit modeling-choice stacks in §4.1, §4.2.2, §4.3, §4.4
- Single author: Martin Luther Graise, ORCID 0009-0006-8003-3938

## Files added in this commit

- `outbox/paper7/pdfs/g2_paper7_thermodynamic_v8.docx` — final manuscript
- `outbox/paper7/pdfs/build_paper7_v8.js` — build script
- `outbox/paper7/SUBMISSION_PACKAGE.md` — operational submission checklist with cover letter and reviewer suggestions
- `outbox/paper7/PAPER7_revisions_v8.md` — v8 revision log

## Next physical actions (user-driven)

1. **Upload to Zenodo** (~15-20 min). Use the metadata in `SUBMISSION_PACKAGE.md` Stage 1. Capture the assigned Paper 7 DOI.
2. **Submit to Entropy via MDPI SUSY portal** (~30-45 min). Use the cover letter template in `SUBMISSION_PACKAGE.md` Stage 2 with the Paper 7 Zenodo DOI inserted. Suggest 4-6 reviewers from the curated list.
3. **Monitor for first decision** (~14 days SLA at Entropy). If desk-rejected, pivot to Foundations of Physics with the same DOCX.

C-7RO cannot perform Stages 1 and 2 directly — they require the user's authenticated sessions on Zenodo and MDPI.
