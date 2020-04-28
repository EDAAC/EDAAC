===================
Collecting Metrics
===================

*Metrics* are characteristics of design artifacts, processes, 
and inter-process communications during the an SoC design flow.
The main idea behind pervasively collecting metrics is to 
measure the design process and quantify its Quality of Results (QoR).
This has always been a prerequisite to optimizing it and continuously
achieving maximum productivity.

**EDAAC** implements *Metrics* collection functionality in :code:`edaac.metrics`
sub-package. Below, we document its functionality.

Design Rule Check
==================

Design rules are geometric constraints imposed on an SoC to ensure that 
the design functions properly, reliably and can be manufactured by fabs.

A Design Rule Violation (DRV) is a record that represents a violation
to the design rules defined by the technology library used.

Supported Tools
----------------
- Cadence Innovus

Usage
------
1. Generate a report from Innovus using the `instructions here <http://www.ispd.cc/contests/19/Instruction_to_generate_violation_report_by_Innovus_2019.pdf>`_.
2. Use :code:`edaac.metrics.parsers` to parse the report.

    .. code:: python

        from edaac.metrics.parsers import parse_innovus_drc_report
        metrics = parse_innovus_drc_report('/path/to/report')

3. :code:`metrics` is a Python dictionary of :code:`key: value` pairs.

    .. code:: python

        print(metrics)

Dictionary
----------

+-------------------------------------------------+-----------------------------------------------------------------+
|    Key                                          | Meaning                                                         |
+=================================================+=================================================================+
| :code:`drv_total`                               | The total number of DRVs                                        |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`drv_short_metal_total`                   | Total numner of short metal violations                          |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`drv_short_metal_area`                    | Total area of short metal violations                            |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`drv_short_cut_total`                     | Total number of cut spacing violations                          | 
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`drv_short_cut_area`                      | Total area of cut spacing violations                            |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`drv_out_of_die_total`                    | Total number of components placed/routed out of die             |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`drv_out_of_die_area`                     | Total area of components placed/routed out of die               |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`drv_spacing_total`                       | Total number of spacing violations                              |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`drv_spacing_parallel_run_length_total`   | Total number of parallel run length violations                  |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`drv_spacing_eol_total`                   | Total number of end-of-line spacing violations                  |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`drv_spacing_cut_total`                   | Total number of cut spacing violations                          |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`drv_min_area_total`                      | Total number of min-area violations                             |
+-------------------------------------------------+-----------------------------------------------------------------+


Example
-------

.. code:: python

    metrics = {
        'drv_total': 101,
        'drv_short_metal_total': 2,
        'drv_short_metal_area': 0.02382500,
        'drv_short_cut_total': 1,
        'drv_short_cut_area': 0.0012500,
        'drv_out_of_die_total': 0,
        'drv_out_of_die_area': 0.0,
        'drv_spacing_total': 41,
        'drv_spacing_parallel_run_length_total': 7,
        'drv_spacing_eol_total': 9,
        'drv_spacing_cut_total': 25,
        'drv_min_area_total': 57
    }

Connectivity
=============

This ensures that the circuit components are connected as in the schematic.

Supported Tools
-----------------
- Cadence Innovus

Usage
------
1. Generate a report from Innovus using the `instructions here <http://www.ispd.cc/contests/19/Instruction_to_generate_violation_report_by_Innovus_2019.pdf>`_.
2. Use :code:`edaac.metrics.parsers` to parse the report.

    .. code:: python

        from edaac.metrics.parsers import parse_innovus_conn_report
        metrics = parse_innovus_conn_report('/path/to/report')

3. :code:`metrics` is a Python dictionary of :code:`key: value` pairs.

    .. code:: python

        print(metrics)

Dictionary
----------

+------------------------+-------------------------------+
|    Key                 | Meaning                       |
+========================+===============================+
| :code:`conn_open_nets` | Total number of open  nets    |
+------------------------+-------------------------------+

Example
--------

.. code:: python

    metrics = {
        'conn_open_nets': 22
    }

Static Timing Analysis (STA)
============================

Static Timing Analysis validates the timing performance of a design by 
checking all possible paths for timing violations under worst-case conditions.

The *arrival time* of a signal is the time elapsed for a signal to arrive at a certain point.

The  *required time* is the latest time at which a signal can arrive without making 
the clock cycle longer than desired.

The *slack* associated with each connection is the difference between the required time
and the arrival time. 
A positive slack `s` at some node implies that the arrival time at that node may be increased by s,
without affecting the overall delay of the circuit. 
Conversely, negative slack implies that a path is too slow, 
and the path must be sped up (or the reference signal delayed) 
if the whole circuit is to work at the desired speed.

The critical path is defined as the path between an input and an output with the maximum delay. 
The critical path is sometimes referred to as the worst path.
If this path has a negative slack, the circuit won't work as expected at the desired speed.


Supported Tools
-----------------
- Cadence Innovus

Usage
------
1. Generate a report from Innovus using the `instructions here <http://www.ispd.cc/contests/19/Instruction_to_generate_violation_report_by_Innovus_2019.pdf>`_.
2. Use :code:`edaac.metrics.parsers` to parse the report.

    .. code:: python

        from edaac.metrics.parsers import parse_innovus_timing_report
        metrics = parse_innovus_timing_report('/path/to/report')

3. :code:`metrics` is a Python dictionary of :code:`key: value` pairs.

    .. code:: python

        print(metrics)

Dictionary
----------

+--------------------+-----------------------------------------------------------------+
|    Key             | Meaning                                                         |
+====================+=================================================================+
| :code:`timing_wns` | Worst negative slack                                            |
+--------------------+-----------------------------------------------------------------+

Example
-------

.. code:: python

    metrics = {
        'timing_wns': -65.967
    }

Power
======

This reports the power consumption of the circuit.

Supported Tools
----------------
- Cadence Innovus

Usage
------
1. Generate a report from Innovus using the `instructions here <http://www.ispd.cc/contests/19/Instruction_to_generate_violation_report_by_Innovus_2019.pdf>`_.
2. Use :code:`edaac.metrics.parsers` to parse the report.

    .. code:: python

        from edaac.metrics.parsers import parse_innovus_power_report
        metrics = parse_innovus_power_report('/path/to/report')

3. :code:`metrics` is a Python dictionary of :code:`key: value` pairs.

    .. code:: python

        print(metrics)

Dictionary
----------

+------------------------------------+-----------------------------------------+
|    Key                             | Meaning                                 |
+====================================+=========================================+
| :code:`power_internal_total`       | Total internal power                    |
+------------------------------------+-----------------------------------------+
| :code:`power_switching_total`      | Total switching power                   |
+------------------------------------+-----------------------------------------+
| :code:`power_leakage_total`        | Total leakage power                     |
+------------------------------------+-----------------------------------------+
| :code:`power_total`                | Total power (sumof the above)           |
+------------------------------------+-----------------------------------------+
| :code:`power_internal_percentage`  | Internal power / Total * 100.0          |
+------------------------------------+-----------------------------------------+
| :code:`power_switching_percentage` | Swithing power / Total * 100.0          |
+------------------------------------+-----------------------------------------+
| :code:`power_leakage_percentage`   | Leakage power / Total * 100.0           |
+------------------------------------+-----------------------------------------+

Example
---------

.. code:: python

    metrics = {
        'power_internal_total': 26.31116662,
        'power_switching_total': 21.61735782,
        'power_leakage_total': 13.58182182,
        'power_total': 61.51034631,
        'power_internal_percentage': 42.7752,
        'power_switching_percentage': 35.1443,
        'power_leakage_percentage': 22.0805
    }


Compute Resources
==================

This reports the compute resources (cpu, memory) used by a flow process.

Supported Tools
----------------
- Cadence Innovus

Usage
------
1. Dump Innovus logs (that are shown on stdout) to a file.
2. Use :code:`edaac.metrics.parsers` to parse the report.

    .. code:: python

        from edaac.metrics.parsers import parse_innovus_log
        metrics = parse_innovus_log('/path/to/report')

3. :code:`metrics` is a Python dictionary of :code:`key: value` pairs.

    .. code:: python

        print(metrics)

Dictionary
----------

+------------------------------------+-----------------------------------------+
|    Key                             | Meaning                                 |
+====================================+=========================================+
| :code:`compute_cpu_time_total`     | Total time from all CPU cores (seconds) |
+------------------------------------+-----------------------------------------+
| :code:`compute_real_time_total`    | Total wall clock time (seconds)         |
+------------------------------------+-----------------------------------------+
| :code:`compute_mem_total`          | Total memory Usage                      |
+------------------------------------+-----------------------------------------+

Example
---------

.. code:: python

    metrics = {
        'compute_cpu_time_total': 540,
        'compute_real_time_total':184,
        'compute_mem_total': 2287.4
    }