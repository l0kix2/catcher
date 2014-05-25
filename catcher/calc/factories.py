# coding: utf-8
from __future__ import unicode_literals


def counter(iterable):
    _counter = lambda accumulated, next_item: accumulated + 1
    return reduce(_counter, iterable,  0)


def sum_(iterable, start=None):
    if start is not None:
        return sum(iterable, start)
    else:
        return sum(iterable)
