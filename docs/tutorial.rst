========
Tutorial
========

This tutorial introduces **EDAAC** by means of example --- we will walk
through how to extract metrics from a log file that comes out of an EDA tool.

Metrics are essential information that we extract about a circuit (hardware design)
at a specific stage of the tape-out process. For example, after *Logic Synthesis*, 
we might be interested to know the total number of standard cells used after mapping
the design to a standard cell library. After *Routing*, we would be concerned with 
the total number of *Design Rule Violations (DRVs)*. Instead of looking at the log
files of EDA tools and searching through them for the important piece of information,
**EDAAC** makes this straightforward for you.

To make use of the extracted metrics, **EDAAC** offers data models to store the 
collected metrics into a document-based database (MongoDB). This database can be
used for further research and development of EDA tools.


Getting Started
================

If you haven't installed EDAAC,
simply use pip to install it like so::

    $ pip install edaac

To verify the installation:

.. code-block:: python

    $ python
    >>> import edaac
    >>> edaac.version()
    EDA Analytics Central (EDAAC) v0.0.11


Extracting Metrics
===================

In this example, we show how to extract *Design Rule Violations (DRVs)* 
from a log file saved by Cadence Innovus.

.. note::

    Since Cadence tools are proprietary software, we are unable to publish
    raw log files outputted by the tool. We will update this tutorial with
    example log files once we support open-source EDA tools.


Assuming you have generated a DRC report using a proper command within Innovus
to verify that the design meets the technology-defined constraints. The log file
is located at :code:`./test_design.drc.rpt`.

Now, you can use the below Python code to extract DRVs into a metrics dictionary:

.. code:: python

    from edaac.metrics.parsers import parse_innovus_drc_report
    
    log_file = './test_design.drc.rpt'
    metrics = parse_innovus_drc_report(log_file)
    print(metrics)

An example output would be:

.. code:: javascript

    {
        'drv_total': 76,
        'drv_short_metal_total': 30,
        'drv_short_metal_area': 0.06930000,
        'drv_short_cut_total': 0,
        'drv_short_cut_area': 0.0,
        'drv_out_of_die_total': 0,
        'drv_out_of_die_area': 0.0,
        'drv_spacing_total': 32,
        'drv_spacing_parallel_run_length_total': 19,
        'drv_spacing_eol_total': 13,
        'drv_spacing_cut_total': 0,
        'drv_min_area_total': 14
    }

**What just happened?** 
Underneath, the function mines the log files for a number of metrics that it registered.
In its core, it heavily uses `regular expressions <https://en.wikipedia.org/wiki/Regular_expression>`_
to look for patterns.

**Why I can't find the metric I'm looking for?**
Most probably, the metric is not yet registered in the parsing function. 
Help us improve the package by `submitting an issue <https://github.com/EDAAC/EDAAC/issues>`_
with label :code:`enhancement`

What's Next?
=============
**EDAAC** comes pre-loaded with a number of parsers ( ..and more under development).
But that's not all. Storing metrics effeciently for post-processing is as important as
-*if not more important than*- collecting the metrics themeselves. 

In the :doc:`guide/index`, we show more examples of using **EDAAC** for metrics processing and storage.

