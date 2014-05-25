# coding: utf-8
from __future__ import unicode_literals


import itertools


def list_(iterable, sort=False, **kwargs):
    if not sort:
        return list(iterable)
    else:
        return sorted(iterable, **kwargs)


def reversed_list(iterable):
    return list(reversed(list(iterable)))


try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict


def dict_(iterable, ordered=False):
    if not ordered:
        return dict(iterable)
    else:
        return OrderedDict(iterable)


def set_(iterable, frozen=False):
    if not frozen:
        return set(iterable)
    else:
        return frozenset(iterable)


def chain(iterable, lazy=True):
    chained = itertools.chain.from_iterable(iterable)
    if not lazy:
        chained = list(chained)
    return chained
