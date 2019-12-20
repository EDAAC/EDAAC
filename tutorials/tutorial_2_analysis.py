import os
import mongoengine as mongo
import numpy as np
import matplotlib.pyplot as plt
import edaac
import json

mongo.connect('use_case_1')

for project in edaac.Project.objects:
    for flow in project.flows:
        print('Design:', project.design.name)
        for stage in flow.stages:
            metrics = stage.report_metrics()
            print('\tStage:', stage.name)
            for key, value in metrics.items():
                print('\t\t', key, ':', value)