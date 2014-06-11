.. catcher documentation master file, created by
   sphinx-quickstart on Thu Jun  5 00:30:29 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation
=============

Contents:

.. toctree::
   :maxdepth: 2


Neat lib, which makes your code nicer.

.. code-block:: python

    from catcher import wrap, calc, string

    @wrap.in_dict
    def function():
        yield 'a', 10
        yield 'b', 20

    >>> function()
    ... {'a': 10, 'b': 20}


    # full list
    @wrap.in_list
    @wrap.in_sorted_list
    @wrap.in_reversed_list
    @wrap.in_dict
    @wrap.in_odict
    @wrap.chain
    @calc.count
    @calc.summarize
    @calc.maximum
    @calc.minimum
    @string.cat


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

