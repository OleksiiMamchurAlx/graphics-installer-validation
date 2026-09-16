import math
import unittest
from frame_report import metrics, report

class FrameTests(unittest.TestCase):
    def test_constant_intervals(self):
        self.assertEqual(metrics([10]*100)['mean_fps'], 100)
    def test_slow_frame(self):
        self.assertEqual(metrics([10]*99+[20])['one_percent_low_fps'], 50)
    def test_invalid_intervals(self):
        for values in ([], [True], [0], [-1], [math.nan], [math.inf], '10'):
            with self.assertRaises(ValueError):
                metrics(values)
    def test_missing_metrics_unknown(self):
        value = report({'mode': 'SYNTHETIC', 'display_intervals_ms': [8]})
        self.assertIsNone(value['base'])
        self.assertIsNone(value['latency_ms'])
    def test_base_not_derived_from_display(self):
        value = report({'mode': 'SYNTHETIC', 'base_intervals_ms': [10], 'display_intervals_ms': [8]})
        self.assertEqual(value['base']['mean_fps'], 100)
        self.assertEqual(value['displayed']['mean_fps'], 125)
    def test_provenance_required(self):
        with self.assertRaises(ValueError):
            report({})
    def test_invalid_latency(self):
        for latency in (True, -1, math.inf, 'unknown'):
            with self.assertRaises(ValueError):
                report({'mode': 'SYNTHETIC', 'latency_ms': latency})

if __name__ == '__main__':
    unittest.main(verbosity=2)
