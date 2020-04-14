=================
Installing EDAAC
=================

To use EDAAC, you will need to download `MongoDB <http://mongodb.com/>`_
and ensure it is running in an accessible location. You will also need
`MongoEngine <http://mongoengine.org/>`_ to use EDAAC, but if you
install EDAAC using setuptools, then the dependencies will be handled for
you.

EDAAC is available on PyPI, so you can use :program:`pip`:

.. code-block:: console

    $ pip install edaac

Alternatively, if you don't have setuptools installed, `download it from PyPi
<https://pypi.org/project/edaac/>`_ and run

.. code-block:: console

    $ python setup.py install

To use the bleeding-edge version of EDAAC, you can get the source from
`GitHub <http://github.com/EDAAC/EDAAC/>`_ and install it as above:

.. code-block:: console

    $ git clone git://github.com/EDAAC/EDAAC
    $ cd EDAAC
    $ python setup.py install

