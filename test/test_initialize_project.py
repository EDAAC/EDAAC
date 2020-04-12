import unittest
import os
import pathlib

import mongoengine as mongo
from edaac.models import Project


class TestInitializeProject(unittest.TestCase):
    def test(self):
        project_name = 'test'
        initialize_result = True

        # assumes a localhost:27017 mongo instance
        mongo.connect('edaac_test')
        
        # create project
        project = Project(
            name='test-project',
            description='test project description'
        )
        result = project.save()

        self.assertIsNotNone(result)
