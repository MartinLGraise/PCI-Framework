# Claude Code checkpoint review: PX-Loop v0.1 draft PR #7 (head 0397ffd)

Date: 2026-07-08
Reviewer: Claude Code
Scope: v0.1 merge checkpoint per Martin's handoff via Codex. No changes made to the branch.

## Verification performed

- Fetched head 0397ffd into a clean worktree; diffed against the previously reviewed head d0b0495.
- Confirmed `operators.py`, `model.py`, and `presets.py` are byte-identical to the prior review -- PX semantics were not touched, per the guardrail.
- Ran the full test suite: 7 tests, all pass.
- Visually inspected `2026-07-07_v0.1_demo/trajectory.png` and `2026-07-07_sweeps/comparison_quiet_vs_paradox.png`.
- Independently re-ran `quiet_loop` at 140/300/500 cycles to check the horizon-dependence of the cycle-end labels.

All five items from the previous Claude Code review were addressed: `--param` CLI overlay, additive cycle-end metrics with the legacy label preserved and annotated, `pyproject.toml`, `PX_IDS` wired into run metadata, and README caveats on determinism and classifier sampling. The sweep notes and review log Entries 005/006 correctly incorporate the sampling-artifact finding rather than restating the oscillation claim.

## Q1: Is the PX operator mapping faithful enough? -- Yes, for v0.1

Each PX layer has a named operator whose coupling structure matches its documented semantic role, the loop order is explicit, and the PX-006 -> PX-007 -> PX-001 feedback path exists in the equations. Cross-couplings, such as PX-001's access decay and PX-002's temporal leak, are visible in code and named parameters. Combined with the README's standing disclaimer that these are heuristic mappings and not PCI/PME claims, this meets the v0.1 faithfulness bar. Faithfulness beyond this, such as deriving coefficients rather than choosing them, is explicitly a later-phase question and should stay that way.

## Q2: Are the visuals clear enough? -- Yes, with one caveat and one cosmetic note

The two-panel layout, per-operator sawtooth versus cycle-end-only, is exactly the right response to the sampling-artifact finding: the plot itself now teaches the distinction. Titles, dual classification subtitle, axis ticks, direct right-edge labels with final values, and the color key make each PNG self-contained.

Caveat -- horizon-dependent panel headings: the comparison image titles the left panel "QUIET LOOP | CYCLE END TRANSIENT". My re-run shows `quiet_loop` also converges to a fixed point; it just needs about 306 cycles to reach the `1e-9` tolerance, versus the 140-cycle sweep horizon:

| steps | cycle-end label | final delta |
| ---: | --- | ---: |
| 140 | cycle_end_transient | 1.8e-05 |
| 300 | cycle_end_settling | 1.4e-09 |
| 500 | cycle_end_fixed_point_like | 1.4e-14 |

So "transient" here means "not yet converged at this horizon," not a different dynamical class. Notably, the higher-gain paradox preset converges faster, implying stronger contraction. Recommendation: regenerate the canonical sweep and comparison at `--steps 400`, or add "AT 140 CYCLES" to the panel headings. This matters mainly because the comparison PNG is the portfolio-facing artifact and the prior heading invited misreading.

Cosmetic, defer: the label leader lines start at the final data point, so every series appears to hook up or down at the right edge as if the data turned. Starting leaders just outside the axis would fix it. This is not merge-blocking.

## Q3: Ready to merge after review? -- Yes

Merge-ready as v0.1. Semantics are frozen and verified, tests are green, the scope contract is met, artifacts are reproducible from committed code, and documentation is honest about limitations. Suggested sequence: fix the horizon issue from Q2, mark the draft ready, merge. If Martin prefers zero further commits, merging as-is is defensible because the sweep notes already state the 140-cycle horizon in prose; the residual risk is only that someone reads the comparison PNG in isolation.

Two non-blocking code notes for the v0.2 backlog, recorded so they are not lost:

- `cycle_end_metrics`'s insufficient-data branch omits `max_within_cycle_span`, which `sweep.py`'s index writer reads unconditionally. This is unreachable today because `steps >= 1` guarantees two cycle-end records, but it is a latent `KeyError` if a future caller feeds partial records.
- `cycles_to_tolerance` returns `None` until full convergence within the horizon; consider also reporting the first cycle where delta is below `1e-5` so sweeps can compare convergence speed without requiring full convergence.

## Q4: Defer to v0.2

Codex's out-of-scope list is right; keep all of it out: Observer Engine integration, dashboard UI, proof/category-theory layer, portfolio polish, and semantic reinterpretation. v0.2 itself should be limited to:

1. Canonical runs at a horizon where labels are asymptotic, roughly 400+ cycles, with `cycles_to_tolerance` reported as the headline convergence metric.
2. The 2D `fracture_gain` x `reset_pressure` grid from the prior review; the eight-case sweep confirmed the PX-005/PX-006/PX-007 path is the sensitivity axis, and the grid is the natural next artifact.
3. Initial-condition grids to test fixed-point uniqueness, which is cheap and high-value given determinism.
4. The two code notes above plus the leader-line cosmetic fix.

Explicitly not v0.2: richer plotting dependencies, because the stdlib PNG writer is sufficient, and any move of `classification` semantics. The legacy label should keep its documented meaning until a major version.

## Cross-links

- PR: https://github.com/MartinLGraise/PCI-Framework/pull/7
- Prior review: `outbox/ai_coordination/2026-07-07_claude_code_px_loop_v0.1_review.md`
- Sweep notes: `outbox/ai_coordination/2026-07-07_dispatch_px_loop_sweep_notes.md`
- Review log: `outbox/ai_coordination/pci_pme_review_log.md` (Entries 004-006)
