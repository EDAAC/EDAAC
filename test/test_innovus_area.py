import unittest
import os
import pathlib

from edaac.metrics.parsers import parse_innovus_area_report
from edaac.log import get_logger

logger = get_logger()


class TestInnovusArea(unittest.TestCase):
    def test(self):
        log_file = os.path.join(
            pathlib.Path(__file__).parent.absolute(), 'data', 'area1.rpt')
        metrics = {
            'area_stdcell': 48191.040,
            'area_stdcell_count': 11306
        }

        if os.path.exists(log_file):
            result = parse_innovus_area_report(log_file)
            self.assertDictEqual(metrics, result)
        else:
            logger.warning('Skipping private area report file %s' % log_file)
