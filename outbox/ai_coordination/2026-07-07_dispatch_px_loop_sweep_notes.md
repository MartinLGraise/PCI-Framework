# PX-Loop v0.1 Sweep Notes

**Date:** 2026-07-07

**Branch:** `px-loop-v0.1`

**Prepared by:** Codex, following Perplexity implementation-phase guidance for the Claude Dispatch sweep role.

## Scope

This sweep keeps PX-loop v0.1 semantics frozen and varies only a small set of heuristic coefficients. It is an implementation/behavior check, not a proof of PCI/PME theory.

## Command

```bash
python3 -m px_loop.sweep --steps 140 --output-dir outbox/ai_coordination/px_loop_runs/2026-07-07_sweeps
```

## Artifacts

- `outbox/ai_coordination/px_loop_runs/2026-07-07_sweeps/sweep_index.csv`
- `outbox/ai_coordination/px_loop_runs/2026-07-07_sweeps/sweep_index.json`
- One case folder per run, each with:
  - `trajectory.csv`
  - `summary.json`
  - `trajectory.png`

## Sweep Cases

| Case | Per-operator label | Cycle-end label | Cycle-end delta | Within-cycle span |
| --- | --- | --- | ---: | ---: |
| `quiet_loop__baseline` | `bounded_transient` | `cycle_end_transient` | 1.78e-05 | 0.0367 |
| `quiet_loop__higher_reset` | `bounded_transient` | `cycle_end_transient` | 1.13e-05 | 0.0405 |
| `quiet_loop__higher_feedback` | `bounded_transient` | `cycle_end_transient` | 1.03e-05 | 0.0404 |
| `quiet_loop__damped_fracture` | `bounded_transient` | `cycle_end_transient` | 2.51e-05 | 0.0312 |
| `paradox_amplification__baseline` | `bounded_oscillation_or_amplification` | `cycle_end_settling` | 1.50e-09 | 0.0645 |
| `paradox_amplification__higher_reset` | `bounded_oscillation_or_amplification` | `cycle_end_fixed_point_like` | 7.75e-10 | 0.0755 |
| `paradox_amplification__higher_feedback` | `bounded_oscillation_or_amplification` | `cycle_end_fixed_point_like` | 5.75e-10 | 0.0650 |
| `paradox_amplification__damped_fracture` | `bounded_oscillation_or_amplification` | `cycle_end_settling` | 2.97e-09 | 0.0654 |

## Interpretation

The quiet preset variants remain transient at 140 complete cycles by the cycle-end criterion, with small final deltas around `1e-05` to `3e-05`. Higher reset pressure lowers final identity split and silence gain, while higher PX-005/PX-006 feedback slightly increases false signal, utterance instability, and silence gain. Damping fracture and false-signal gain lowers the final false-signal and utterance values.

The paradox-amplification variants show a per-operator sawtooth inside each seven-step cycle, but the complete seven-operator cycle is fixed-point-like or settling by cycle-end metrics. The old `classification` label should be read as a per-operator window label, not as proof of a cycle-to-cycle oscillation. Higher reset pressure reduces final identity split and silence gain relative to baseline, suggesting PX-007 reset dampens the fixed point. Higher feedback slightly raises silence and false-signal values, which supports treating PX-005/PX-006/PX-007 as the dominant sensitivity path for v0.1 experiments.

No tested run diverged numerically because the v0.1 model clamps state to `[0, 1]`. That is a design constraint, not a discovered stability theorem.

## Canonical v0.1 Candidates

- `quiet_loop__baseline`: best low-gain comparison case.
- `paradox_amplification__baseline`: best main demo case because it shows visible within-cycle PX movement while settling at complete-cycle boundaries.
- `paradox_amplification__higher_reset`: useful damping contrast.
- `paradox_amplification__higher_feedback`: useful sensitivity contrast for the PX-005/PX-006/PX-007 path.

## Follow-Up

- Keep the current branch open until a light cleanup/doc pass lands.
- Do not reinterpret PX operator semantics without an explicit README/review-log update.
- If a later agent wants stronger classification, expand the cycle-end metric suite and keep per-operator sawtooth labels separate from complete-loop behavior.
