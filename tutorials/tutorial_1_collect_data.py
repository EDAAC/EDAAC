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
stage = edaac.Stage()
stage.configure(config={
    name:'',
    tool:edaac.Tool(name='', version=''),
    machines:edaac.Machine(name=''),
    state:edaac.STAGE_FINISHED,
    log_files:['', '', ''],
    collection_mode:edaac.DATA_OFFLINE
})
flow.add_stage(stage)

# add flow to the project
project.add_flow(flow)

# extract metrics from flow stages
project.extract_metrics()

# synchronize with the database
project.sync()
