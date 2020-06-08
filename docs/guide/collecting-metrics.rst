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

Synthsis Stats
===============

We can extract useful statistics about a synthesized netlist that aid in the physical design process.

Supported Tools
----------------
- Yosys

Usage
------
1. Generate a report from Yosys using the `stat` command.
2. Use :code:`edaac.metrics.parsers` to parse the report.

    .. code:: python

        from edaac.metrics.parsers import parse_yosys_log
        metrics = parse_yosys_log('/path/to/report')

3. :code:`metrics` is a Python dictionary of :code:`key: value` pairs.

    .. code:: python

        print(metrics)

Dictionary
----------

+-------------------------------------------------+-----------------------------------------------------------------+
|    Key                                          | Meaning                                                         |
+=================================================+=================================================================+
| :code:`run__synth__yosys_version`               | Version of yosys build used                                     |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`synth__inst__num__total`                 | Total numner of standard cells                                  |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`synth__inst__stdcell__area__total`       | Total area of standard cells                                    |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`synth__wire__num__total`                 | Total number of wires                                           | 
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`synth__wirebits__num__total`             | Total number of wirebits                                        |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`synth__memory__num__total`               | Total number of memories                                        |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`synth__memorybits__num__total`           | Total number of memory bits                                     |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`run__synth__warning__total`              | Total number of warnings                                        |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`run__synth__warning__unique__total`      | Total number of unique warnings                                 |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`run__synth__cpu__total`                  | CPU usage                                                       |
+-------------------------------------------------+-----------------------------------------------------------------+
| :code:`run__synth__mem__total`                  | Memory usage                                                    |
+-------------------------------------------------+-----------------------------------------------------------------+

Example
-------

.. code:: python

    metrics = {
        'run__synth__yosys_version': '0.9+1706 (git sha1 UNKNOWN, gcc 7.3.1 -fPIC -Os)',
        'synth__inst__num__total': 272,
        'synth__inst__stdcell__area__total': 407.512000,
        'synth__wire__num__total': 297,
        'synth__wirebits__num__total': 343,
        'synth__memory__num__total': 0,
        'synth__memorybits__num__total': 0,
        'run__synth__warning__total': 90,
        'run__synth__warning__unique__total': 26,
        'run__synth__cpu__total': 1.21,
        'run__synth__mem__total': 28.78
    }
    

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
- OpenSTA

Usage
-----
1. Generate a report from Innovus using the appropriate command. Or generate a report from OpenSTA using :code:`report_tns`, :code:`report_wns` and :code:`report_design_area`.
2. Use :code:`edaac.metrics.parsers` to parse the report.

    .. code:: python

        from edaac.metrics.parsers import parse_innovus_timing_report
        metrics = parse_innovus_timing_report('/path/to/report')
    
    .. code:: python

        from edaac.metrics.parsers import parse_openroad_log
        metrics = parse_openroad_log('/path/to/report', 'OpenSTA')

3. :code:`metrics` is a Python dictionary of :code:`key: value` pairs.

    .. code:: python

        print(metrics)

Dictionary from Innovus
------------------------

+--------------------------------+-----------------------------------------------------+
|    Key                         | Meaning                                             |
+================================+=====================================================+
| :code:`timing_wns`             | Worst negative slack                                |
+--------------------------------+-----------------------------------------------------+
| :code:`timing_tns`             | Total negative slack                                |
+--------------------------------+-----------------------------------------------------+
| :code:`timing_violating_paths` | Number of violating paths                           |
+--------------------------------+-----------------------------------------------------+

Example
-------

.. code:: python

    metrics = {
        'timing_tns': -27.496,
        'timing_wns': -0.851,
        'timing_violating_paths': 35
    }


Dictionary from OpenSTA
------------------------

+--------------------------------+-----------------------------------------------------+
|    Key                         | Meaning                                             |
+================================+=====================================================+
| :code:`slack__negative__total` | Total negative slack                                |
+--------------------------------+-----------------------------------------------------+
| :code:`slack__negative__worst` | Worst negative slack                                |
+--------------------------------+-----------------------------------------------------+
| :code:`std__area__total`       | Total standard cell area                            |
+--------------------------------+-----------------------------------------------------+
| :code:`util`                   | Core utilization                                    |
+--------------------------------+-----------------------------------------------------+

Example
-------

.. code:: python

    metrics = {
        'slack__negative__total': 0.00,
        'slack__negative__worst': 0.00,
        'std__area__total': 491.0,
        'util': 8.0
    }

Power
======

This reports the power consumption of the circuit.

Supported Tools
----------------
- Cadence Innovus

Usage
------
1. Generate a report from Innovus using the appropriate command.
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


Area
=====

This reports the area of the standard cells in addition to the cell count.

Supported Tools
----------------
- Cadence Innovus

Usage
------
1. Generate the area report from Innovus using the appropriate command.
2. Use :code:`edaac.metrics.parsers` to parse the report.

    .. code:: python

        from edaac.metrics.parsers import parse_innovus_area
        metrics = parse_innovus_area_report('/path/to/report')

3. :code:`metrics` is a Python dictionary of :code:`key: value` pairs.

    .. code:: python

        print(metrics)

Dictionary
----------

+------------------------------------+-----------------------------------------+
|    Key                             | Meaning                                 |
+====================================+=========================================+
| :code:`area_stdcell`               | Total area of standard cells (um^2)     |
+------------------------------------+-----------------------------------------+
| :code:`area_stdcell_count`         | Total number of standard cells          |
+------------------------------------+-----------------------------------------+

Example
---------

.. code:: python

    metrics = {
        'area_stdcell': 48191.040,
        'area_stdcell_count': 11306
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
| :code:`compute_mem_total`          | Total memory usage (MB)                 |
+------------------------------------+-----------------------------------------+

Example
---------

.. code:: python

    metrics = {
        'compute_cpu_time_total': 540,
        'compute_real_time_total':184,
        'compute_mem_total': 2287.4
    }