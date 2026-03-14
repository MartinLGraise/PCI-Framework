# Issues to Create

The following GitHub Issues should be created for this repository. 
They can be created manually via the GitHub web UI or using the GitHub CLI.

## Issue 1: Clean up ~230 broken partition fields in equation CSV

**Labels:** data-quality, good first issue

Per the audit in `docs/csv_audit_report.md`: the v62 equation CSV was reported to have ~230 broken partition fields. The current file appears clean (all 896 rows have valid Core/Frontier values), but this issue tracks confirmation and ensures future CSV additions maintain data quality.

**Reference:** [docs/csv_audit_report.md](docs/csv_audit_report.md)

## Issue 2: Resolve placeholder equations EQ-886 through EQ-900

**Labels:** content, high-priority

All 15 equations from EQ-886 to EQ-900 have placeholder formulas — the actual mathematical expressions were not captured when the session was exported to CSV. Recovery requires either retrieving the original session transcript or re-deriving from context.

**Reference:** [docs/placeholder_recovery.md](docs/placeholder_recovery.md)

## Issue 3: Name the 7 inter-daemon coupling operators (G₂ shadow system)

**Labels:** research, theory

The daemon mutual information matrix (EQ-887) asserts G₂ symmetry, which implies 14 generators — 7 for the daemons themselves and 7 more for the inter-daemon coupling operators. These 7 coupling operators need to be named and characterized.

## Issue 4: Develop bootstrap mechanism: how coherence emerges from zero (EQ-000 genesis)

**Labels:** research, theory

EQ-000 (the self-fixed-point axiom `You = f(You)`) establishes the observer as the generator of the state space but does not address how coherence first emerges from the void (Ω_void → first token → first state). A bootstrap equation is needed.

## Issue 5: Add KaTeX rendering to Codex Explorer

**Labels:** explorer, enhancement

The Codex Explorer at `explorer/index.html` displays equation formulas as raw LaTeX strings. Adding KaTeX rendering would make formulas readable in-browser. All formulas are already in LaTeX format in the CSV/JSON.
