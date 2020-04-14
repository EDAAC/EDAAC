# EDA Analytics Central <img align="right" width="10%" src="https://raw.githubusercontent.com/abdelrahmanhosny/EDAAC/master/docs/img/logo.png">

## The Problem
While there is an _art_ to chip design, measuring design processes can result in precious data that help advancing the _science_ of chip design.
System-on-Chip (SoC) design flows yield a huge amount of data that can be useful in optimizing the design process and achieving maximum productivity. 
However, there currently exists no solution that makes it easy to collect, store and analyze data coming out of a SoC design flow. 

## The Solution
**EDA Analytics Central (EDAAC)** addresses this problem by building on top of a previously well-studied data collection specification, called METRICS [1, 2].
The goal of EDAAC is to make it painless to perform the following tasks:

![](https://raw.githubusercontent.com/abdelrahmanhosny/EDAAC/master/docs/img/edaac-functions.png)

1. Data Collection:
    * _Passive collection (aka: Log file mining)_: using scripts (shell tools + python) to extract metrics from log files after a flow finishes.
    * _Active Collection (i.e. Data model extraction)_: using middle-layer functions that extract from data models (i.e. OpenDB) during a flow run.
2. Data Storage: storing and indexing data in a persistent structural database that can support data analytics tasks.
3. Data Querying: 
    * _Offline usage_: the flow has run and ended, metrics are stored (either passively or actively). This supports ML around tools.
    * _Online usage_: the flow is currently running and a tool wants to take a decision based on a collected metric during the flow run. This supports ML in tools.

## Getting Started

### Install
```
$ pip install edaac
```

### Documentation
[https://edaac.readthedocs.io/en/latest/](https://edaac.readthedocs.io/en/latest/)


## License
[BSD 3-Clause License](https://github.com/abdelrahmanhosny/EDAAC/blob/master/LICENSE)

## Credits
Icon made by [mynamepong](https://www.flaticon.com/authors/mynamepong) from [www.flaticon.com](https://www.flaticon.com/)


## References
[1] Fenstermaker, Stephen, et al. "METRICS: a system architecture for design process optimization." Proceedings of the 37th Annual Design Automation Conference. ACM, 2000.

[2] Kahng, Andrew B., and Stefanus Mantik. "A system for automatic recording and prediction of design quality metrics." Proceedings of the IEEE 2001. 2nd International Symposium on Quality Electronic Design. IEEE, 2001.
