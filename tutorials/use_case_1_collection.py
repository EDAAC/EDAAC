import os
import mongoengine as mongo
import edaac

mongo.connect('edaac_db')

data_dir = os.path.join(os.getenv('HOME'), 'Desktop', 'use_case_1')
benchmarks = [os.path.join(data_dir, o) for o in os.listdir(data_dir) \
    if os.path.isdir(os.path.join(data_dir, o))]

for benchmark in benchmarks:
    name = benchmark.split('/')[-1]

    project = edaac.Project(
        name=name
    )
    
    rtl_files = [os.path.join(benchmark, f) for f in os.listdir(benchmark) \
        if os.path.isfile(os.path.join(benchmark, f)) and f.endswith(".v")]
    design = edaac.Design(
        name=name,
        rtl_files=rtl_files
    )
    project.design = design

    technology = edaac.Technology(
        foundry='TSMC',
        process='65LP'
        )
    project.technology = technology

    # setup a stage in the flow
    flow = edaac.Flow()
    flow.stages = [
        edaac.Stage(
            name='Synthesis-STA',
            tool=edaac.Tool(
                name='Tempus',
                version='19_10_p002_1'
            ),
            machine='scale01.engin.brown.edu',
            collection_mode=edaac.DataCollectionMode.OFFLINE_FROM_LOGS.name,
            status=edaac.StageStatus.COMPLETED_SUCCESSFULLY.name,
            log_file=os.path.join(benchmark, 'stages', 'timing_synth.rpt')
        ),
        edaac.Stage(
            name='Placement-STA',
            tool=edaac.Tool(
                name='Tempus',
                version='19_10_p002_1'
            ),
            machine='scale01.engin.brown.edu',
            collection_mode=edaac.DataCollectionMode.OFFLINE_FROM_LOGS.name,
            status=edaac.StageStatus.COMPLETED_SUCCESSFULLY.name,
            log_file=os.path.join(benchmark, 'stages', 'timing_placed.rpt')
        ),
        edaac.Stage(
            name='Routing-STA',
            tool=edaac.Tool(
                name='Tempus',
                version='19_10_p002_1'
            ),
            machine='scale01.engin.brown.edu',
            collection_mode=edaac.DataCollectionMode.OFFLINE_FROM_LOGS.name,
            status=edaac.StageStatus.COMPLETED_SUCCESSFULLY.name,
            log_file=os.path.join(benchmark, 'stages', 'timing_routed.rpt')
        ),
    ]
    project.flows.append(flow)
    project.extract_metrics()
    project.save()