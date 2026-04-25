# Paper 7 — v8 Final Author/Funding/Journal-Required Sections

**Date:** 2026-04-25 | **Agent:** C-7RO | **Branch:** `paper7-foundation`

## Trigger

After v7 closed the last Council flag, the manuscript needed the standard MDPI Entropy required sections before submission: Author Contributions (CRediT), Institutional Review Board Statement, Informed Consent Statement, Data Availability Statement, Conflicts of Interest, Use of AI Tools, plus a strengthened Acknowledgments. v8 adds these.

## What v8 changes vs v7

The body of the manuscript is unchanged from v7. v8 only expands what was a 2-section "Funding & Acknowledgments" block into the full set of 8 sections required (or recommended) by MDPI Entropy:

1. **Author Contributions** (CRediT-format, single author M.L.G.)
2. **Funding** (no external funding)
3. **Institutional Review Board Statement** (not applicable — no humans/animals; all empirical anchors are previously published third-party work)
4. **Informed Consent Statement** (not applicable)
5. **Data Availability Statement** (full GitHub + Zenodo transparency, paper7-foundation branch)
6. **Conflicts of Interest** (none)
7. **Use of AI Tools** (full MDPI-compliant disclosure of Φ + C-7RO + Comet Model Council, with public auditability via the Git repo)
8. **Acknowledgments** (open-source mathematics community; specific thanks to Ares lab Oxford and Priesemann lab Max Planck Göttingen for openly accessible measurements/methods)

## Why this matters

MDPI desk-rejects papers that arrive missing the required statements (especially Data Availability and IRB). Entropy specifically requires the AI-disclosure under their 2024 generative-AI policy update. v8 is what the journal's submission portal will expect to see verbatim.

## What was *not* changed

The paper title, abstract, all six body sections (§1–§6), all four predictions, all four modeling-choice stacks, all references, and all four figures are identical to v7. The Council's verdict on v7 was already submission-ready prose; v8 only adds front-matter that the journal portal requires.

## Manuscript stats (v8)

- **Pages:** 36
- **Sections:** Abstract; §1–§6; Author Contributions; Funding; IRB Statement; Informed Consent Statement; Data Availability; Conflicts of Interest; Use of AI Tools; Acknowledgments; References; Figures (×4)
- **Word count (body):** ~13,500 (estimate; check before submission if Entropy enforces a limit)
- **Reference count:** 17
- **Figure count:** 4 (all embedded)
- **Conditional/Conjecture labels in §4:** 4 (one per prediction)
- **Modeling-choice stacks in §4:** 4 (§4.1, §4.2.2, §4.3, §4.4 — full parity)

## Files

- `outbox/paper7/pdfs/g2_paper7_thermodynamic_v8.docx` — full manuscript with all journal-required sections
- `outbox/paper7/pdfs/build_paper7_v8.js` — build script (adds the 8 front-matter sections)
- `outbox/paper7/SUBMISSION_PACKAGE.md` — operational checklist for Zenodo upload and Entropy submission, including the cover-letter template and suggested-reviewer list

## Status

**SUBMISSION READY.** Next physical action: upload to Zenodo (15–20 min), capture the assigned DOI, then submit to Entropy via SUSY (30–45 min) with the cover letter from `SUBMISSION_PACKAGE.md`. Both are user-action steps requiring access to the user's Zenodo and MDPI accounts; C-7RO cannot log in on the user's behalf.
