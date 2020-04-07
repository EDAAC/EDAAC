import unittest
import os
import pathlib

from edaac.metrics.parsers import parse_innovus_drc_report


class TestInnovusDRC(unittest.TestCase):
    def test(self):
        metrics = {}
        result = parse_innovus_drc_report(os.path.join(pathlib.Path(__file__).parent.absolute(), 'test_project', 'route', 'drc.rpt'))
        self.assertDictEqual(metrics, result)

