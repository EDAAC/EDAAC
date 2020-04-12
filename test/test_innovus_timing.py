import unittest
import os
import pathlib

from edaac.metrics.parsers import parse_innovus_timing_report


class TestInnovusTiming(unittest.TestCase):
    def test(self):
        metrics = {
            'timing_wns': -65.967
        }
        result = parse_innovus_timing_report(os.path.join(
            pathlib.Path(__file__).parent.absolute(), 'data', 'timing1.rpt'))
        self.assertDictEqual(metrics, result)
