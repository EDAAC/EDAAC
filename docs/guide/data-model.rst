===========
Data Model
===========

Managing the storage of the collected *Metrics* is a challenging task.
Collecting metrics from hundreds, or even thousands, of EDA flows introduces 
the pondering question: **How should we structure the data to make efficient use of it in predictive analytics applications?**

**EDAAC** implements a general-purpose data model in :code:`edaac.models`
sub-package. Below, we document its functionality.

Documents
==========
EDAAC's data model is an unstructured document that represents an SoC project during its different life stages (from logic synthesis to routing).
The root of the data model is a :code:`Project` document.
A :code:`Project` is a container for all related artifacts of the design lifecycle.

Below is a complete birds-eye view of the :code:`Project` document.

**Usage:** :code:`from edaac.models import Project`

Every embedded document in the project has a class representation in :code:`edaac.models`.
For example, the :code:`technology` key in the project should be an instance of :code:`edaac.models.Technology`.
Similarly, :code:`design`, :code:`flow`, :code:`stage` and :code:`tool` should be instances of 
:code:`edaac.models.Design`, :code:`edaac.models.Flow`, :code:`edaac.models.Stage` and :code:`edaac.models.Tool` respectively.

.. literalinclude:: project.json
   :language: javascript
   :linenos:

.. note::

    **rag:** red: no verification ran on the design. 
    amber: alpha or beta release with some levels of verifications. 
    green: release candidate

Database
========

The question now is where do we store this these information? Answer: `MongoDB <https://www.mongodb.com/>`_.


Starting a MongoDB Server
--------------------------

**Option 1: Docker**

This is the easiest option to get started.
Use the following command to start a local database server 

.. code:: shell

    docker run -d -p 27017:27017 -v /path/to/local/folder:/data/db --name edaac_db mongo

This will start a local MongoDB server on port :code:`27017` (the default port for MongoDB).
It will also mount a folder at :code:`/path/to/local/folder` to the container to persist data when the container is stopped.

**Option 2: Install Locally**

Follow the instructions on the `official documentation <https://docs.mongodb.com/manual/installation/>`_.

**Option 3: Cloud Instance**

Create a MongoDB instance on your cloud provider account using `MongoDB Atlas <https://www.mongodb.com/cloud/atlas>`_.

Connecting to MongoDB
----------------------

After starting the server, download `MongoDB Compass <https://www.mongodb.com/products/compass>`_ to graphically connect to 
the database and ensure that it is running correctly.

Next, create a database with a give it a name (e.g. `test_db`) using MongoDB Compass.

From Python, connect to the database using:

.. code:: python

    import mongoengine as mongo

    mongo.connect('test_db')

The above code will connect automatically to a MongoDB server running on the localhost with the default port, username and password.

If you are running a remote MongoDB instance, provide the credentials as below:

.. code:: python

    import mongoengine as mongo

    mongo.connect('test_db', host='', port='', username='', password='')

.. note::

    :code:`mongoengine` package is installed as part of :code:`edaac` dependencies.


Examples
========

Creating a Project
-------------------

The only required key of a project document is its :code:`name`.
All other keys can be updated later by retrieving the project, modifying it and then saving it back.

.. code:: python

    import mongoengine as mongo
    from edaac.models import Project, Technology, Design

    mongo.connect('test_db')

    # create project
    project = Project(
        name='test-project',
        description='demonstrates the use of edaac models',
        technology=Technology(
            foundry='TestFoundry',
            process=45
        ),
        design=Design(
            name='test-design',
            rtl_files=['/path/to/rtl1.v', '/path/to/rtl2.v'],
            netlist_file='/path/to/netlist.v',
            sdc_file='/path/to/const.sdc'
        )
    )
    project.save()
    mongo.disconnect()

Update Project Data
--------------------

The below code retrieves an existing project and updates its data.

.. code:: python

    import mongoengine as mongo
    from edaac.models import Project, Flow, Stage, Design, Tool
    from edaac.enum import StageStatus, DataCollectionMode

    mongo.connect('test_db')

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
