import tempfile
import unittest
from pathlib import Path

from px_loop.sweep import SweepCase, run_sweep


class PXSweepTests(unittest.TestCase):
    def test_small_sweep_writes_index_and_case_artifacts(self):
        cases = (
            SweepCase(
                name="quiet_loop__test",
                base_preset="quiet_loop",
                description="test case",
                parameter_updates={"fracture_gain": 0.05},
            ),
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            results, index_paths = run_sweep(output_dir=tmpdir, steps=2, cases=cases)

            self.assertEqual(len(results), 1)
            self.assertTrue(Path(index_paths["json"]).exists())
            self.assertTrue(Path(index_paths["csv"]).exists())
            self.assertTrue((Path(tmpdir) / "quiet_loop__test" / "trajectory.csv").exists())
            self.assertTrue((Path(tmpdir) / "quiet_loop__test" / "summary.json").exists())
            self.assertTrue((Path(tmpdir) / "quiet_loop__test" / "trajectory.png").exists())

    def test_sweep_writes_quiet_vs_paradox_comparison_when_baselines_exist(self):
        cases = (
            SweepCase(
                name="quiet_loop__baseline",
                base_preset="quiet_loop",
                description="quiet baseline",
                parameter_updates={},
            ),
            SweepCase(
                name="paradox_amplification__baseline",
                base_preset="paradox_amplification",
                description="paradox baseline",
                parameter_updates={},
            ),
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            _, index_paths = run_sweep(output_dir=tmpdir, steps=2, cases=cases)

            comparison = Path(index_paths["comparison"])
            self.assertTrue(comparison.exists())
            self.assertGreater(comparison.stat().st_size, 1000)


if __name__ == "__main__":
    unittest.main()
