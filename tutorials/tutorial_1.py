import edaac

# setup connection to database
connection = edaac.connect(host='', username='', password='')
if not connection:
    print('Could not connect to EDAAC database ..')
    exit()

# create project
project = edaac.Project(project_id='project-id')

# set project-wide parameters
project.set_project_name('')
project.set_description('')

# define design
design = edaac.Design()
design.configure(config={
    name='',
    rtl_files=['', ''],
    sdc_file='',
    runset_tag='',
    runset_id='',
    rtl_config='',
    rtl_tag='',
    rtl_rag='')
})

# define technology
technology = edaac.Technology()
technology.configure(config={
    foundry='',
    process='',
    beol='',
    track='',
    opv='',
    vt='',
    channel_width='',
    config='',
    version='',
    rag=''
})

# setup a flow
flow = edaac.Flow()
flow.configure(config={
    design=design,
    technology=technology,
    kits='',
    features='',
    version='',
    rag=''
})

# setup a stage in the flow
stage = edaac.Stage()
stage.configure(config={
    name='',
    tool=edaac.Tool(name='', version=''),
    machines=edaac.Machine(name=''),
    state=edaac.STAGE_FINISHED,
    log_files=['', '', ''],
    collection_mode=edaac.DATA_OFFLINE
})
flow.add_stage(stage)

# add flow to the project
project.add_flow(flow)

# extract metrics from flow stages
project.extract_metrics()

# synchronize with the database
project.sync()
