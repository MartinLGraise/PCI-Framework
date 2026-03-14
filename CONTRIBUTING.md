# Contributing to PCI-Framework

Thank you for your interest in the PCI/PME framework.

## About This Project

This is an active research project by **Martin Luther Graise**. The codex is a living document — equations and symbols are continuously refined as the theoretical structure develops.

## How to Engage

**Issues and discussions are welcome.** If you find errors in the data, have questions about the framework, or want to discuss a concept, open an issue.

**Pull requests for data corrections are welcome.** If you spot a typo in an equation name, a clearly wrong partition assignment, or a broken reference, a PR is the right way to fix it. Keep data-correction PRs small and focused.

**Structural changes to the codex should be discussed first.** This includes:
- Renumbering equations or symbols
- Changing the Core/Frontier partition schema
- Adding new module families
- Modifying the daemon architecture

For anything structural, open an issue and describe the proposed change before writing code or editing CSVs.

## Codex Explorer

The live Codex Explorer is at:
**[martinlgraise.github.io/PCI-Framework/explorer/](https://martinlgraise.github.io/PCI-Framework/explorer/)**

It lets you browse and search all equations and symbols without downloading the CSVs.

## Data Files

The canonical source files are:
- `codex/pci_equation_partition_index_v62_core_frontier.csv` — equation ledger (original)
- `codex/pci_symbol_partition_index_v46_core_frontier.csv` — symbol ledger (original)

Cleaned versions (normalized metadata only, no content changes):
- `codex/pci_equations_v63_cleaned.csv`
- `codex/pci_symbols_v47_cleaned.csv`

Do not modify the original `v62` / `v46` files directly. If you are proposing data corrections, target the cleaned versions and describe the change in your PR.

## Known Issues

See [`docs/csv_audit_report.md`](docs/csv_audit_report.md) for a full audit of current data quality issues, and [`docs/placeholder_recovery.md`](docs/placeholder_recovery.md) for the list of equations needing formula recovery.
