# Paper 14 — Figures

Five candidate figures for Paper 14 v1, generated from matplotlib
scripts in this directory. Each script produces both PNG (240 dpi)
and PDF outputs.

## Figure list

| # | File | Topic | Paper section call-out |
|---|---|---|---|
| 1 | `fig1_two_axis_observable` | The two-axis observable R(s,c) plotted as a phase diagram with four canonical disease cases | §3 (Four Canonical Disease Cases) — referenced immediately after Table 1 |
| 2 | `fig2_cross_substrate_grammar` | Cross-substrate residence-pathology grammar matrix — eight substrates × six descriptors | §8.8 (Synthesis across the extensions) |
| 3 | `fig3_return_path_machinery` | Four-panel return-path machinery typology with shared λ_exit observable | §6 (Return-Path Machinery as a Multiscale Class) |
| 4 | `fig4_kinetic_strategies` | Five symmetric kinetic-stabilization strategies (A–E) | §5 (Symmetric Formulation of Kinetic Stabilization) |
| 5 | `fig5_experimental_agenda` | Thirteen experiments organized by cluster, tractability tier, and dependency | §11 (Cross-Domain Experimental Agenda) |

## Regeneration

Each script is self-contained. From this directory:

```bash
python3 fig1_two_axis_observable.py
python3 fig2_cross_substrate_grammar.py
python3 fig3_return_path_machinery.py
python3 fig4_kinetic_strategies.py
python3 fig5_experimental_agenda.py
```

## Status

- v1.5 generation, 2026-05-12: all five figures generated, manually
  inspected for text overflow, label collisions, and subscript rendering.
- Caption text included on each figure; figure-list will be moved to a
  dedicated Figures section of the paper at submission packaging.
