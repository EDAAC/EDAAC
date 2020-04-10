import unittest
import os
import pathlib

from edaac.metrics.parsers import parse_innovus_conn_report


class TestInnovusCONN1(unittest.TestCase):
    def test(self):
        metrics = {
            'conn_open_nets': 0
        }
        result = parse_innovus_conn_report(os.path.join(pathlib.Path(
            __file__).parent.absolute(), 'data', 'conn1.rpt'))
        self.assertDictEqual(metrics, result)


class TestInnovusCONN2(unittest.TestCase):
    def test(self):
        metrics = {
            'conn_open_nets': 22
        }
        result = parse_innovus_conn_report(os.path.join(pathlib.Path(
            __file__).parent.absolute(), 'data', 'conn2.rpt'))
        self.assertDictEqual(metrics, result)
