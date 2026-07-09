import tempfile
import unittest
from pathlib import Path

from px_loop.__main__ import preset_with_overrides
from px_loop.observer import finite_records
from px_loop.simulate import run_and_save, run_simulation


class PXSimulationTests(unittest.TestCase):
    def test_simulation_logs_initial_state_and_each_px_step(self):
        result = run_simulation(preset="quiet_loop", steps=5)

        self.assertEqual(len(result.records), 1 + 5 * 7)
        self.assertEqual(result.records[0].step_id, "initial")
        self.assertEqual(result.records[-1].step_id, "PX-007")
        self.assertTrue(finite_records(result.records))
        self.assertEqual(result.summary["run_config"]["steps"], 5)
        self.assertIn("parameters", result.summary["run_config"])
        self.assertEqual(result.summary["classification_basis"], "per_operator_window")
        self.assertIn("cycle_end", result.summary)
        self.assertIn("classification", result.summary["cycle_end"])

    def test_run_and_save_writes_expected_artifacts(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            result = run_and_save(
                preset="paradox_amplification",
                steps=8,
                output_dir=tmpdir,
            )

            self.assertTrue(Path(result.output_paths["csv"]).exists())
            self.assertTrue(Path(result.output_paths["summary"]).exists())
            self.assertTrue(Path(result.output_paths["plot"]).exists())
            self.assertGreater(Path(result.output_paths["plot"]).stat().st_size, 1000)

    def test_cli_parameter_overlay_preserves_named_presets(self):
        preset = preset_with_overrides("quiet_loop", ["fracture_gain=0.123"])

        self.assertEqual(preset.name, "quiet_loop__custom")
        self.assertEqual(preset.parameters["fracture_gain"], 0.123)


if __name__ == "__main__":
    unittest.main()
