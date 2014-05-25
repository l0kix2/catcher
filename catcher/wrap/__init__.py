# coding: utf-8
from __future__ import unicode_literals

from functools import partial

from catcher import wrap_in
from . import factories


# TODO: set docstrings.
in_list = wrap_in(factories.list_)
in_sorted_list = wrap_in(partial(factories.list_, sort=True))
in_reversed_list = wrap_in(factories.reversed_list)

in_set = wrap_in(factories.set_)
in_frozenset = wrap_in(partial(factories.set_, frozen=True))

in_dict = wrap_in(factories.dict_)
in_odict = wrap_in(partial(factories.dict_, ordered=True))

chain = wrap_in(factories.chain)
