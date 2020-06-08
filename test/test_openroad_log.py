import unittest
import os
import pathlib

from edaac.metrics.parsers import parse_openroad_log
from edaac.log import get_logger

logger = get_logger()


class TestOpenSTALog(unittest.TestCase):
    def test_00(self):
        log_file = os.path.join(
            pathlib.Path(__file__).parent.absolute(), 'data', '2_1_floorplan.log')

        metrics = {
            'slack__negative__total': 0.00,
            'slack__negative__worst': 0.00,
            'std__area__total': 408.0,
            'util': 6.0
        }

        if os.path.exists(log_file):
            result = parse_openroad_log(log_file, 'OpenSTA')
            self.assertDictEqual(metrics, result)
        else:
            logger.warning('Skipping private area report file %s' % log_file)
    
    def test_01(self):
        log_file = os.path.join(
            pathlib.Path(__file__).parent.absolute(), 'data', '3_2_resizer.log')

        metrics = {
            'slack__negative__total': 0.00,
            'slack__negative__worst': 0.00,
            'std__area__total': 491.0,
            'util': 8.0
        }

        if os.path.exists(log_file):
            result = parse_openroad_log(log_file, 'OpenSTA')
            self.assertDictEqual(metrics, result)
        else:
            logger.warning('Skipping private area report file %s' % log_file)
