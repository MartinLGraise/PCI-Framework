# PX-Loop Agent v0.1

PX-Loop Agent v0.1 is a small, inspectable simulator for the Seven-Paradox Loop in the PCI-Framework repo. It treats PX-001 through PX-007 as explicit transition operators on a bounded seven-dimensional state vector.

The goal is practical, not proof-level: produce a runnable artifact with state logs, a plot, and a clear mapping from paradox semantics to code.

## State

Each state dimension is a float clamped to `[0, 1]`:

- `identity_split`
- `access_recursion`
- `contradiction_lock`
- `temporal_feedback`
- `false_signal`
- `utterance_instability`
- `silence_gain`

## Operators

The prototype applies these operators in order:

| PX step | Function | Role |
| --- | --- | --- |
| PX-001 | `px_001_amplify_identity_fracture` | amplify identity fracture |
| PX-002 | `px_002_transform_fracture_to_access_recursion` | move fracture into access recursion |
| PX-003 | `px_003_convert_negation_to_lock` | convert negation pressure into lock formation |
| PX-004 | `px_004_lagged_temporal_recursion` | feed present pressure into lagged temporal recursion |
| PX-005 | `px_005_inject_false_signal` | inject or amplify false signal |
| PX-006 | `px_006_signal_to_utterance_instability` | convert structured signal into unstable utterance and silence pressure |
| PX-007 | `px_007_silence_feedback_reset` | amplify silence and feed it back as reset pressure |

## Run

From the repo root:

```bash
python3 -m px_loop --preset paradox_amplification --steps 160 --output-dir outbox/ai_coordination/px_loop_runs/2026-07-07_v0.1_demo
```

Run with a temporary parameter overlay:

```bash
python3 -m px_loop --preset paradox_amplification --steps 160 --param reset_pressure=0.28 --output-dir outbox/ai_coordination/px_loop_runs/custom_reset_check
```

Outputs:

- `trajectory.csv` records the full state after every PX step.
- `summary.json` records the preset, replay metadata, final state, value ranges, and coarse trajectory classification.
- `trajectory.png` is a dependency-free PNG line plot of the seven state dimensions.

The plot includes a title, axis ticks, direct labels at the right edge, final values, and a color key. The direct labels point to the final PX-007 state, while the jagged paths show movement across individual PX operators inside each cycle.

`summary.json` keeps two behavior labels:

- `classification`: legacy final-window label over per-operator records, useful for spotting within-cycle sawtooth.
- `cycle_end.classification`: complete-loop behavior sampled at initial/PX-007 boundaries.

## Sweep Batch

Run the v0.1 parameter sweep batch:

```bash
python3 -m px_loop.sweep --steps 140 --output-dir outbox/ai_coordination/px_loop_runs/2026-07-07_sweeps
```

The sweep writes one folder per case, plus:

- `sweep_index.csv`
- `sweep_index.json`

Each case preserves the same PX operator semantics and varies only a small set of gains/couplings.

## Presets

- `quiet_loop`: lower gains, intended to settle or weakly oscillate.
- `paradox_amplification`: higher gains, intended to emphasize the PX-006 -> PX-007 -> PX-001 feedback path while remaining bounded.

## Tests

This v0.1 prototype uses only the Python standard library.

```bash
python3 -m unittest discover -s tests
```

## Limitations

- The operators are deliberately simple numeric approximations of the PX semantics.
- The classifiers are descriptive, not mathematical proofs of convergence or cyclicity.
- Per-operator plots can show sawtooth structure even when complete PX cycles are settling toward a fixed point.
- Markov-chain, symbolic-recursion, observer-engine integration, notebooks, dashboards, and multi-agent simulations are left for later phases.
- Parameter sweeps test sensitivity of heuristic coefficients; they do not validate the PX semantics as a theory.

## Next Steps

- Add a notebook only after the CLI and core module stay stable.
- Decide whether this remains an isolated `px_loop/` module or becomes a preset layer attached to the broader PCI Observer Engine.
