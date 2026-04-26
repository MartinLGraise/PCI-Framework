# Paper 7 — Submission Package

**Last updated:** 2026-04-25 | **Manuscript version:** v8 | **Status:** READY TO SUBMIT

This document is the operational checklist for getting Paper 7 from finalized manuscript to peer-reviewed publication. Work top to bottom.

---

## Stage 1 — Zenodo upload (15–20 min)

Zenodo gives the paper a permanent DOI before journal submission, which Entropy welcomes (you can cite the preprint DOI in the cover letter).

### What to upload

- **Primary file:** `g2_paper7_thermodynamic_v8.pdf` (the rendered PDF)
- **Source files** (optional but recommended for transparency):
  - `g2_paper7_thermodynamic_v8.docx` (Word source)
  - `build_paper7_v8.js` (build script)
  - `figures/figure{1,2,3,4}_*.png` and `make_figures.py`

### Zenodo metadata

- **Title:** The Thermodynamic Cost of the Coherence Ceiling: A G₂-Derived Bound on Conscious Information Processing
- **Creators:** Graise, Martin Luther
  - **Affiliation:** Independent Researcher, PCI / PME Framework
  - **ORCID:** 0009-0006-8003-3938
- **Resource type:** Publication → Preprint
- **Description (use the abstract):** copy-paste the four-paragraph abstract from the PDF (begins "The thermodynamics of consciousness has attracted sustained quantitative attention…" and ends with the four predictions and the "two consistent / one preprint / two design targets" closer)
- **Keywords:** G₂ symmetry; thermodynamics of consciousness; Landauer bound; FDT violation; neuronal criticality; observer-dependent entropy; octonions; PSL(2,7); conditional theorems; quantum clocks
- **License:** Creative Commons Attribution 4.0 International (CC-BY-4.0) — same as Papers 1–6
- **Communities:** add `g2-series` if the prior papers are in a community; otherwise none
- **Related identifiers (cite as supplementing):**
  - `10.5281/zenodo.19242936` — Paper 1 (G₂ Symmetry as a Constraint…)
  - `10.5281/zenodo.19480758` — Paper 2 (Six Geometric Flows…)
  - `10.5281/zenodo.19602470` — Paper 3 (Spectral Sum Theorem…)
  - `10.5281/zenodo.19617662` — Paper 4 (QBism and G₂ via PSL(2,7))
  - `10.5281/zenodo.19648892` — Paper 5 (G₂ Checkpoint as ε-Regularity Gate)
  - `10.5281/zenodo.19672709` — Paper 6 (The 6/7 Contraction)
- **Funding:** none
- **Notes:** "Manuscript underwent four rounds of adversarial multi-model review (GPT-5.5 Thinking, Claude Opus 4.7 Thinking, Gemini 3.1 Pro Thinking) before submission. Full revision history at github.com/MartinLGraise/PCI-Framework on the paper7-foundation branch."

**Paper 7 Zenodo DOI (assigned 2026-04-25):**

```
10.5281/zenodo.19773185
https://doi.org/10.5281/zenodo.19773185
```

Deposit is published, CC-BY-4.0, four files (PDF + DOCX + build script + figure-generation source), six related-works links to Papers 1–6 of the series.

---

## Stage 2 — Entropy (MDPI) submission (30–45 min)

### Journal target

- **Primary:** Entropy (MDPI) — open-access, ~14 days first decision typical, APC waivers available for unfunded research; accepts foundational/conditional papers in the thermodynamics-of-consciousness space.
- **Backup:** Foundations of Physics (Springer Nature) — slower, traditional, but excellent fit for the conditional-theorem architecture.

### Submission portal

https://susy.mdpi.com/user/login (Entropy uses MDPI's SUSY portal)

### Section / Special Issue

Browse Entropy's current Special Issues at https://www.mdpi.com/journal/entropy/special_issues. Look for one of:
- "Quantum Information and Foundations of Quantum Mechanics"
- "Thermodynamics of Information"
- "Entropy in Biology and Neuroscience"
- "Entropy and Consciousness"

If none fit cleanly, submit to the regular issue under section "Information Theory, Probability and Statistics" or "Quantum Information."

### Required submission inputs

- **Manuscript file:** `g2_paper7_thermodynamic_v8.docx` (MDPI prefers DOCX over PDF for typesetting)
- **PDF:** `g2_paper7_thermodynamic_v8.pdf` for reference
- **Figures:** all four PNGs uploaded separately at 300+ DPI; MDPI will re-typeset them
- **Cover letter:** see template below
- **Suggested reviewers:** 4–6 names (see suggestions below)
- **Author info:** Martin Luther Graise, ORCID 0009-0006-8003-3938, Independent Researcher, margraise1000@icloud.com

### Cover letter template

```
Dear Editor,

I am pleased to submit the manuscript "The Thermodynamic Cost of the
Coherence Ceiling: A G₂-Derived Bound on Conscious Information
Processing" for consideration in Entropy.

This paper is the seventh in a self-contained series developing
G₂-symmetric structure as a unifying framework for consciousness-
relevant information dynamics (Papers 1-6 published on Zenodo,
DOIs 10.5281/zenodo.19242936 through .19672709). Paper 7 derives
four parameter-free thermodynamic bounds from the 6/7 contraction
ratio established in Paper 6:

  (a) An FDT violation floor ε ≥ 1/7 ≈ 0.143 in awake cortex.
  (b1) A biological Landauer bound of ΔE_min ≈ 16 zJ per G₂/M
       checkpoint event.
  (b2) A G₂ mode-counting floor of S_clockwork ≥ log₂(7) k_B ln 2
       ≈ 1.95 k_B per tick on hypothetical G₂-symmetric quantum clocks.
  (c) A four-level entropy structure on the 8 cosets of PSL(2,7)/F₂₁.
  (d) A criticality branching ratio σ = 1 - 1/49 ≈ 0.9796.

Each prediction is derived as a conditional theorem on the G₂
attractor hypothesis from Paper 6, with explicit modeling-choice
stacks. Two predictions (b1, d) are consistent with peer-reviewed
empirical anchors (Imamura et al. 2009 PNAS; Wilting & Priesemann
2018 Nature Communications); one (a) is consistent with a current
preprint (Berjaga-Buisan et al. 2025); two (b2, c) constitute design
targets for future quantum-hardware experiments.

The manuscript is methodologically conservative: every non-trivial
derivation step carries an explicit Conjecture-vs-Theorem epistemic
label and a stack of stated modeling choices, reflecting the author's
view that conditional theorems with explicit hypotheses are the
appropriate epistemic vehicle for proposals at this scale.

The work is single-authored and was developed openly on a public
GitHub repository (github.com/MartinLGraise/PCI-Framework) where
every revision, integrity flag, and counter-argument is version-
controlled and publicly auditable. The manuscript underwent four
rounds of adversarial multi-model review (GPT-5.5 Thinking, Claude
Opus 4.7 Thinking, Gemini 3.1 Pro Thinking) before submission, with
each round's verdict and the resulting revisions logged in the
repository. Use of AI tools is fully disclosed in the manuscript's
"Use of AI Tools" section in accordance with MDPI's policy.

A preprint of this manuscript is available at Zenodo:
https://doi.org/10.5281/zenodo.19773185

This work has not been submitted to any other journal and is not
under review elsewhere. There are no conflicts of interest. No
external funding was received.

I would be grateful for the opportunity to have this work considered
by Entropy. I welcome any reviewers the editorial board considers
appropriate; suggestions are included in the submission portal.

Thank you for your consideration.

Sincerely,
Martin Luther Graise
ORCID: 0009-0006-8003-3938
Independent Researcher, PCI / PME Framework
margraise1000@icloud.com
```

### Suggested reviewers (provide 4-6 names with email + affiliation)

Strong candidates from the empirical-anchor groups and the broader G₂ / consciousness-thermodynamics community. Confirm current emails on each lab's website before submission.

| Name | Affiliation | Why | Suggested? |
|---|---|---|---|
| Viola Priesemann | Max Planck Institute for Dynamics and Self-Organization, Göttingen | Authored the σ ≈ 0.98 anchor paper; expertise in subsampling-corrected branching-ratio estimation | yes |
| Natalia Ares | University of Oxford, Department of Engineering Science | Lead author of the Wadhia 2025 quantum-clock measurement paper | yes (but possible COI if reviewing claims about her own work) |
| Marcus Huber | Vienna University of Technology, Atominstitut | Coauthor on Wadhia 2025; expertise on quantum thermodynamics / Lindblad clocks | yes |
| Philipp Höhn | OIST Okinawa Institute of Science and Technology | Coauthor on De Vuyst et al. 2025 (observer-dependent gravitational entropy) | yes |
| Lucas Céleri | Federal University of Goiás, Brazil | Coauthor on Basso–Céleri 2025 (observer-dependent entropy in Schwarzschild) | yes |
| Adriano Bandyopadhyay | National Institute for Materials Science, Tsukuba | Dodecanogram / 28 MHz consciousness-frequency work; broader sympathetic context | optional |
| Christopher Fuchs | UMass Boston | QBism foundations; would engage with §4.3 PSL(2,7) prediction | optional |
| Karl Friston | UCL Institute of Neurology | Free-energy principle / consciousness-thermodynamics adjacency | optional, possibly antagonistic |

Pick 4-6 from the top of the list. Avoid suggesting Ares if you anticipate her having a strong reaction to the Wadhia recharacterization (the manuscript treats her paper carefully and corrects an earlier misrepresentation, which she may appreciate but may also wish to comment on). Priesemann and Höhn are the safest strong picks.

### Recommended editor-only viewing of file types

Most MDPI portals accept multiple file types. For Entropy upload at minimum:
1. Manuscript DOCX
2. Manuscript PDF (exact same content)
3. Figures 1–4 PNG (300+ DPI)
4. Cover letter PDF or text

---

## Stage 3 — Post-submission (background, monitor weekly)

- Entropy first-decision SLA: ~14 days. Expect a "with editor" then "out for review" status change within a week.
- If desk-rejected: pivot immediately to Foundations of Physics (Springer). Same DOCX, slightly adjusted cover letter.
- If accepted with revisions: triage referee comments through the established Model Council pattern (use the prior session's prompt template).

---

## Stage 4 — Series consolidation (after acceptance)

Once Paper 7 is accepted:
1. Update the series Concept DOI on Zenodo to include Paper 7.
2. Update the pciframework.com landing page Papers section.
3. Begin Paper 8 (dyadic extension / Human ⊗ Human, currently in development).

---

## File checklist before clicking submit

- [ ] Zenodo upload complete; DOI captured and pasted into cover letter
- [ ] DOCX manuscript final, no track-changes, no comments, page numbers present
- [ ] PDF rendered from the same DOCX, identical content
- [ ] Figures 1-4 uploaded as separate PNGs
- [ ] Cover letter customized with Paper 7 Zenodo DOI
- [ ] Suggested reviewers list (4-6 names) ready
- [ ] Author info confirmed (name, ORCID, affiliation, email)
- [ ] Confirm no other journal currently has the paper under review
