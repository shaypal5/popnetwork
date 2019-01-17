popnetwork
#######
.. |PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

.. .. |popnetwork_icon| image:: https://github.com/shaypal5/popnetwork/blob/88d480fd90820ea58c062029ce7e926201794e47/popnetwork_small.png

Population networks over NetworkX.

.. code-block:: python
  
  from popnetwork.generators import pasta_zaidi_rozenblat_graph
  G = pasta_zaidi_rozenblat_graph(
    n=500, m0=2, mf=60, ptf=0.9, ptl=0.7, lcount=1)


.. contents::

.. section-numbering::


Installation
============

.. code-block:: bash

  pip install popnetwork
  


Features
========

* Pure python.
* Supports Python 3.5+.
* Fully tested.


Reference
=========

Network Generators
------------------

Pasta-Zaidi-Rozenblat Graphs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An implementation of the algorithm given in [PASTA14]_ for generating online social networks based on socio-demographic attributes.


Contributing
============

Package author and maintainer is Shay Palachy (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
----------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/popnetwork.git


Install in development mode, including test dependencies:

.. code-block:: bash

  cd popnetwork
  pip install -e '.[test]'



Running the tests
-----------------

To run the tests use:

.. code-block:: bash

  cd popnetwork
  pytest


Adding documentation
--------------------

The project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings. When documenting code you add to this project, follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

Additionally, if you update this ``README.rst`` file,  use ``python setup.py checkdocs`` to validate it compiles.


Credits
=======

Created by Shay Palachy (shay.palachy@gmail.com).


References
==========

.. [PASTA14] M. Q. Pasta, F. Zaidi, C. Rozenblat "Generating online social
   networks based on socio-demographic attributes", Journal of Complex Networks 2014, 
   2 (4): 475-494.


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/popnetwork.svg
  :target: https://pypi.python.org/pypi/popnetwork

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/popnetwork.svg
   :target: https://pypi.python.org/pypi/popnetwork

.. |Build-Status| image:: https://travis-ci.org/shaypal5/popnetwork.svg?branch=master
  :target: https://travis-ci.org/shaypal5/popnetwork

.. |LICENCE| image:: https://github.com/shaypal5/popnetwork/blob/master/mit_license_badge.svg
  :target: https://github.com/shaypal5/popnetwork/blob/master/LICENSE
  
.. https://img.shields.io/github/license/shaypal5/popnetwork.svg

.. |Codecov| image:: https://codecov.io/github/shaypal5/popnetwork/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/popnetwork?branch=master
