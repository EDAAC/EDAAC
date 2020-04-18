import unittest
import os
import pathlib

import mongoengine as mongo
from edaac.models import Project, Flow, Stage, Design, Tool
from edaac.enum import StageStatus, DataCollectionMode
from edaac.log import get_logger

logger = get_logger()


class TestAddFlow(unittest.TestCase):
    def test_01(self):
        # assumes a localhost:27017 mongo instance
        mongo.disconnect_all()
        mongo.connect('edaac_test')

        # create project
        project = Project(
            name='test-project-flows'
        )
        result = project.save()
        mongo.disconnect()

        self.assertIsNotNone(result)

    def test_02(self):
        # assumes a localhost:27017 mongo instance
        mongo.disconnect_all()
        mongo.connect('edaac_test')

        # retrieve project
        project = Project.objects(name='test-project-flows').first()
        self.assertIsNotNone(project)

        project.design = Design(
            name='test-design',
            rtl_files=['/path/to/rtl1.v', '/path/to/rtl2.v'],
            netlist_file='/path/to/netlist.v',
            sdc_file='/path/to/const.sdc'
        )
        project.flows.append(
            Flow(
                flow_directory='/path/to/flow/directory',
                params={
                    'param1': 'value1',
                    'param2': 'value2'
                },
                stages=[
                    Stage(
                        name='synth',
                        tool=Tool(
                            name='synth_tool',
                            version='0.0.0'
                        ),
                        machine='test-machine',
                        collection_mode=DataCollectionMode.OFFLINE_FROM_LOGS.name,
                        status=StageStatus.COMPLETED_SUCCESSFULLY.name,
                        log_files=['/path/to/log1',
                                   '/path/to/drc', '/path/to/timing'],
                        metrics={}      # should be extracted using edaac.parsers
                    ),
                    Stage(
                        name='placement',
                        tool=Tool(
                            name='placement_tool',
                            version='0.0.0'
                        ),
                        machine='test-machine',
                        collection_mode=DataCollectionMode.OFFLINE_FROM_LOGS.name,
                        status=StageStatus.COMPLETED_SUCCESSFULLY.name,
                        log_files=['/path/to/log1',
                                   '/path/to/drc', '/path/to/timing'],
                        metrics={}      # should be extracted using edaac.parsers
                    ),
                    Stage(
                        name='routing',
                        tool=Tool(
                            name='routing_tool',
                            version='0.0.0'
                        ),
                        machine='test-machine',
                        collection_mode=DataCollectionMode.OFFLINE_FROM_LOGS.name,
                        status=StageStatus.COMPLETED_SUCCESSFULLY.name,
                        log_files=['/path/to/log1',
                                   '/path/to/drc', '/path/to/timing'],
                        metrics={}      # should be extracted using edaac.parsers
                    )
                ],
                log_files=['/path/to/log1', '/path/to/log2']
            )
        )

        result = project.save()
        mongo.disconnect()

        self.assertIsNotNone(result)
