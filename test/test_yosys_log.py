import unittest
import os
import pathlib

from edaac.metrics.parsers import parse_yosys_log
from edaac.log import get_logger

logger = get_logger()


class TestYosysLog(unittest.TestCase):
    def test(self):
        log_file = os.path.join(
            pathlib.Path(__file__).parent.absolute(), 'data', '1_1_yosys.log')

        metrics = {
            'run__synth__yosys_version': '0.9+1706 (git sha1 UNKNOWN, gcc 7.3.1 -fPIC -Os)',
            'synth__inst__num__total': 272,
            'synth__inst__stdcell__area__total': 407.512000,
            'synth__wire__num__total': 297,
            'synth__wirebits__num__total': 343,
            'synth__memory__num__total': 0,
            'synth__memorybits__num__total': 0,
            'run__synth__warning__total': 90,
            'run__synth__warning__unique__total': 26,
            'run__synth__cpu__total': 1.21,
            'run__synth__mem__total': 28.78
        }

        if os.path.exists(log_file):
            result = parse_yosys_log(log_file)
            self.assertDictEqual(metrics, result)
        else:
            logger.warning('Skipping private area report file %s' % log_file)
