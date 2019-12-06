import edaac

# setup connection to database
connection = edaac.connect(host='', username='', password='')
if not connection:
    print('Could not connect to EDAAC database ..')
    exit()

# retrieve project
project = edaac.Project(project_id='project-id')

for flow in project.flows:
    for stage in flow:
        metrics = stage.report_metrics()
        