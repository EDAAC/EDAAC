import os
import mongoengine as mongo
import numpy as np
import matplotlib.pyplot as plt
import edaac

mongo.connect('use_case_1')

designs = []
synthesis_delay = []
placement_delay = []
routing_delay = []

for project in edaac.Project.objects:
    designs.append(project.design.name)
    for flow in project.flows:
        for stage in flow.stages:
            if stage.name == 'Synthesis-STA':
                synthesis_delay.append(stage.metrics['arrival_time'] / 1000)
            if stage.name == 'Placement-STA':
                placement_delay.append(stage.metrics['arrival_time'] / 1000)
            if stage.name == 'Routing-STA':
                routing_delay.append(stage.metrics['arrival_time'] / 1000)

lines = list(zip(synthesis_delay, placement_delay, routing_delay))

print(designs)
for i, line in enumerate(lines):
    plt.plot(line, label=designs[i], marker='o')

plt.xticks([0, 1, 2], ['Synthesis', 'Placement', 'Routing'], rotation=45)
plt.ylabel('Delay (ns)')

plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
          ncol=3, fancybox=True, shadow=True)
plt.show()

# Calculating Spearman correlation coefficient
from numpy.random import randn
from numpy.random import seed
from scipy.stats import spearmanr


# calculate spearman's correlation
corr, _ = spearmanr(np.array(synthesis_delay), np.array(placement_delay))
print('Synthesis-Placement: delay Spearmans correlation: %.3f' % corr)

corr, _ = spearmanr(np.array(synthesis_delay), np.array(routing_delay))
print('Synthesis-Routing: delay Spearmans correlation: %.3f' % corr)

corr, _ = spearmanr(np.array(placement_delay), np.array(routing_delay))
print('Placement-Routing: delay Spearmans correlation: %.3f' % corr)