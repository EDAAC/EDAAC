import mongoengine as mongo
import edaac

# setup connection to database
mongo.connect('edaac_db')

# create project
project = edaac.Project(
    name='tutorial1-flow'
)

# define design
design = edaac.Design(
    name='divisor',
    rtl_files=['/tmp/div.v']
)
project.design = design

# define technology
technology = edaac.Technology(
    foundry='TSMC',
    process='65LP'
)
project.technology = technology

# setup a stage in the flow
flow = edaac.Flow()
flow.stages = [
    edaac.Stage(
        name='LogicSynthesis',
        tool=edaac.Tool(
            name='yosys',
            version='0_8_576'
        ),
        machine='scale01.engin.brown.edu',
        collection_mode=edaac.DataCollectionMode.OFFLINE_FROM_LOGS.name,
        status=edaac.StageStatus.COMPLETED_SUCCESSFULLY.name,
        log_files=['/tmp/div.1.log']
    ),
]
project.flows.append(flow)

# extract metrics from flow stages
project.extract_metrics()

# save to the database
project.save()
