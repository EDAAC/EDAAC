import unittest
import os
import pathlib

import mongoengine as mongo
from edaac.models import Project, Technology, Design


class TestInitializeProject(unittest.TestCase):
    def test(self):
        # assumes a localhost:27017 mongo instance
        mongo.disconnect_all()
        mongo.connect('edaac_test')

        # create project
        project = Project(
            name='test-project',
            description='demonstrates the use of edaac models',
            technology=Technology(
                foundry='TestFoundry',
                process=45
            )
        )
        result = project.save()
        mongo.disconnect()

        self.assertIsNotNone(result)
