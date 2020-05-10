import unittest
import os
import pathlib

from edaac.metrics.parsers import parse_innovus_conn_report
from edaac.log import get_logger

logger = get_logger()


class TestInnovusCONN1(unittest.TestCase):
    def test(self):
        report_file = os.path.join(pathlib.Path(
            __file__).parent.absolute(), 'data', 'conn1.rpt')
        metrics = {
            'conn_open_nets': 0
        }

        if os.path.exists(report_file):
            result = parse_innovus_conn_report(report_file)
            self.assertDictEqual(metrics, result)
        else:
            logger.warning('Skipping private DRC report file %s' % report_file)


class TestInnovusCONN2(unittest.TestCase):
    def test(self):
        report_file = os.path.join(pathlib.Path(
            __file__).parent.absolute(), 'data', 'conn2.rpt')
        metrics = {
            'conn_open_nets': 22
        }

        if os.path.exists(report_file):
            result = parse_innovus_conn_report(report_file)
            self.assertDictEqual(metrics, result)
        else:
            logger.warning(
                'Skipping private Connectivity report file %s' % report_file)
