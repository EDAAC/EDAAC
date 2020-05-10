import unittest
import os
import pathlib

from edaac.metrics.parsers import parse_innovus_log
from edaac.log import get_logger

logger = get_logger()


class TestInnovusLog(unittest.TestCase):
    def test(self):
        log_file = os.path.join(
            pathlib.Path(__file__).parent.absolute(), 'data', 'compute1.log')
        metrics = {
            'compute_cpu_time_total': 540,
            'compute_real_time_total': 184,
            'compute_mem_total': 2287.4,
            'area_stdcell': 56916,
            'area_total': 78139
        }

        if os.path.exists(log_file):
            result = parse_innovus_log(log_file)
            self.assertDictEqual(metrics, result)
        else:
            logger.warning('Skipping private log report file %s' % log_file)
