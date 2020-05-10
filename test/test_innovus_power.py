import unittest
import os
import pathlib

from edaac.metrics.parsers import parse_innovus_power_report
from edaac.log import get_logger

logger = get_logger()


class TestInnovusPower(unittest.TestCase):
    def test(self):
        report_file = os.path.join(
            pathlib.Path(__file__).parent.absolute(), 'data', 'pwr1.rpt')
        metrics = {
            'power_internal_total': 26.31116662,
            'power_switching_total': 21.61735782,
            'power_leakage_total': 13.58182182,
            'power_total': 61.51034631,
            'power_internal_percentage': 42.7752,
            'power_switching_percentage': 35.1443,
            'power_leakage_percentage': 22.0805
        }

        if os.path.exists(report_file):
            result = parse_innovus_power_report(report_file)
            self.assertDictEqual(metrics, result)
        else:
            logger.warning(
                'Skipping private Power report file %s' % report_file)
