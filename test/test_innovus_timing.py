import unittest
import os
import pathlib

from edaac.metrics.parsers import parse_innovus_timing_report


class TestInnovusTiming(unittest.TestCase):
    def test(self):
        metrics = {'arrival_time': 1625.8}
        result = parse_innovus_timing_report(os.path.join(pathlib.Path(__file__).parent.absolute(), 'test_project', 'route', 'timing.rpt'))
        self.assertDictEqual(metrics, result)

