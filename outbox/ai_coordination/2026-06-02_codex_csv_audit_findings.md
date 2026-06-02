# Codex CSV Audit Findings

**Date:** 2026-06-02  
**From:** ChatGPT Codex  
**To:** Martin L. Graise + Perplexity Computer  
**Repo / branch:** `MartinLGraise/PCI-Framework`, `paper7-foundation`  
**Base commit:** `f255799`

---

## 1. Repo Sync Status

Per Perplexity's authorization note, I used a clean worktree for this pass:

`/private/tmp/pci-framework-codex-hygiene`

The main local checkout at `/Users/martinluthergraise/PCI-Framework` was fast-forwarded to `f255799` before this pass and the existing untracked local paths were left untouched:

- `inbox/for_human/2026-04-23_network_restriction_and_real_data_run.md`
- `outbox/paper7/work2/`
- `results/`

No untracked local work was staged or modified.

---

## 2. Auto-Fixes Applied

### 2.1 Malformed symbol row fixed

File:

`codex/pci_symbol_partition_index_v53_core_frontier.csv`

Problem:

`SYM-1221` had an unquoted comma in the LaTeX symbol field:

```text
\omega_{\mathrm{CD}\,0}
```

Because the field was unquoted, the CSV parser treated the comma in `\,` as a delimiter and shifted the row:

- `partition` became `Coherent-Domain Resonance Frequency`
- `module_family` became `Frontier`
- remaining fields shifted right

Fix:

The symbol field is now quoted:

```text
"\omega_{\mathrm{CD}\,0}"
```

Validation:

- Parsed symbol rows: `1,242`
- Bad partition rows after fix: `0`
- `SYM-1221` now parses as `partition = Frontier`, `module_family = Bio-PCI Annex / EZ Water Dynamics`, `status = Speculative`

### 2.2 Status casing normalized

File:

`codex/pci_symbol_partition_index_v53_core_frontier.csv`

Normalized status tokens:

| Before | After |
|---|---|
| `PROPOSED`, `proposed`, `Proposed` | `Proposed` |
| `STANDARD` | `Standard` |
| `canonical` | `Canonical` |
| `canonical; glossary` | `Canonical; Glossary` |
| `glossary` | `Glossary` |
| `index` | `Index` |
| `addition` | `Addition` |
| `candidate` | `Candidate` |
| `module` | `Module` |

Post-normalization status counts:

| Status | Count |
|---|---:|
| `Proposed` | 665 |
| `Glossary` | 288 |
| `Index` | 89 |
| `Addition` | 81 |
| `Candidate` | 54 |
| `Canonical` | 15 |
| `Module` | 13 |
| `Speculative` | 12 |
| empty/null | 10 |
| `Provisional` | 8 |
| `Canonical; Glossary` | 4 |
| `Standard` | 2 |
| `Alias` | 1 |

No equation CSV status casing fix was applied because `codex/pci_equation_partition_index_v71_core_frontier.csv` has no `status` column.

---

## 3. Duplicate ID Report

Checked:

- `codex/pci_equation_partition_index_v71_core_frontier.csv`
- `codex/pci_symbol_partition_index_v53_core_frontier.csv`

Findings:

- Duplicate `eq_num` IDs: none.
- Duplicate `sym_id` IDs: none.

No action needed.

---

## 4. Equation Cross-Reference Report

I scanned equation rows for exact `EQ-...` references and compared them to IDs present in `pci_equation_partition_index_v71_core_frontier.csv`.

Present equation IDs parsed: `1,065`

Missing referenced IDs found: `6`

| Missing referenced ID | Referencing row(s) | Note |
|---|---|---|
| `EQ-001` | `EQ-854` | Likely old zero-padding variant of `EQ-01`; review before fixing. |
| `EQ-006` | `EQ-437` | Missing exact ID. |
| `EQ-015` | `EQ-437` | Missing exact ID. |
| `EQ-81` | `EQ-507` | Missing exact ID; may be old non-padded variant. |
| `EQ-97` | `EQ-496` | Missing exact ID; may be old non-padded variant. |
| `EQ-99` | `EQ-499` | Missing exact ID; may be old non-padded variant. |

Per authorization, I did **not** auto-fix these. The likely next step is a controlled alias/normalization review: determine whether each missing reference maps to an existing padded ID, an intentionally retired historical ID, or a genuinely absent equation.

---

## 5. Baseline Report Copied

Per authorization, I copied Codex's local orientation baseline into the repo:

`outbox/ai_coordination/codex_workspace/pci_orientation_baseline_2026-06-02.md`

This keeps the longer Codex working baseline separate from top-level inter-AI coordination notes.

---

## 6. Remaining Recommendations

1. Add a small codex validation script after this pass, probably under `scripts/` or `outbox/ai_coordination/codex_workspace/`, that checks:
   - CSV parse validity
   - partition values in `{Core, Frontier}`
   - duplicate IDs
   - missing equation cross-references
   - status vocabulary
2. Decide whether old references like `EQ-001` should be normalized to current IDs like `EQ-01`, or preserved as historical aliases.
3. Consider adding a `status_type` or equivalent column later if the current `status` vocabulary is mixing roles (`Glossary`, `Index`, `Addition`) with epistemic status (`Proposed`, `Speculative`, `Provisional`, `Standard`).

No Core/Frontier promotion, retirement, consolidation, or substantive equation/symbol content edits were made.
