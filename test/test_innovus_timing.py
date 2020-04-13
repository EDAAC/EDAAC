import unittest
import os
import pathlib

from edaac.metrics.parsers import parse_innovus_timing_report


class TestInnovusTiming(unittest.TestCase):
    def test(self):
        report_file = os.path.join(
            pathlib.Path(__file__).parent.absolute(), 'data', 'timing1.rpt')
        metrics = {
            'timing_wns': -65.967
        }

        if os.path.exists(report_file):
            result = parse_innovus_timing_report(report_file)
            self.assertDictEqual(metrics, result)
        else:
            logger.warning('Skipping private DRC report file %s' % report_file)
