import unittest
import os
import pathlib

from edaac.metrics.parsers import parse_innovus_timing_report
from edaac.log import get_logger

logger = get_logger()


class TestInnovusTiming(unittest.TestCase):
    def test(self):
        report_file = os.path.join(
            pathlib.Path(__file__).parent.absolute(), 'data', 'timing2.rpt')
        metrics = {
            'timing_tns': -27.496,
            'timing_wns': -0.851,
            'timing_violating_paths': 35
        }

        if os.path.exists(report_file):
            result = parse_innovus_timing_report(report_file)
            self.assertDictEqual(metrics, result)
        else:
            logger.warning(
                'Skipping private Timing report file %s' % report_file)
