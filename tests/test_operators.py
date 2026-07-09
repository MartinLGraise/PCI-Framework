import unittest

from px_loop.model import DIMENSIONS
from px_loop.operators import OPERATORS, apply_operator
from px_loop.presets import get_preset


class PXOperatorTests(unittest.TestCase):
    def test_all_operators_preserve_dimensions_and_bounds(self):
        preset = get_preset("paradox_amplification")
        state = preset.initial_state

        for operator in OPERATORS:
            state = apply_operator(state, operator, preset.parameters, cycle=1)
            self.assertEqual(tuple(state.values), DIMENSIONS)
            for value in state.values.values():
                self.assertGreaterEqual(value, 0.0)
                self.assertLessEqual(value, 1.0)

    def test_operator_sequence_names_all_px_layers(self):
        self.assertEqual([operator.step_id for operator in OPERATORS], [f"PX-00{i}" for i in range(1, 8)])
        self.assertEqual([operator.phase_index for operator in OPERATORS], list(range(1, 8)))


if __name__ == "__main__":
    unittest.main()
