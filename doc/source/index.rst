extractTaxonomy's Documentation
===============================

Indices and tables
##################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Introduction
############

.. _rpBase: https://github.com/Galaxy-SynBioCAD/rpBase

Welcome to the documentation for extractTaxonomy. This projects takes for input an SBML file and then generates a JSON file containing the taxonomy id.

Usage
#####

First build the rpBase_ docker before building the local docker:

.. code-block:: bash

   docker build -t brsynth/extracttaxonomy-standalone:v2 -f Dockerfile .

To call the docker locally you can use the following command:

.. code-block:: bash

   python run.py -input /path/to/file -output /path/to/output

API
###

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. currentmodule:: rpTool

.. autoclass:: getTaxon
    :show-inheritance:
    :members:
    :inherited-members:

.. currentmodule:: run

.. autoclass:: main
    :show-inheritance:
    :members:
    :inherited-members:
