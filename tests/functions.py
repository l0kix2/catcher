# coding: utf-8
from __future__ import unicode_literals


def yield_never():
    if 0:
        yield


def yield_nones():
    yield
    yield


def yield_sequence():
    yield 1
    yield 2

yield_sequence_backwards = lambda: reversed(list(yield_sequence()))


def yield_pairs():
    yield 'Liz', 40
    yield 'Jack', 50


yield_pairs_backwards = lambda: reversed(list(yield_pairs()))


def yield_strings():
    yield 'hello, '
    yield 'cruel '
    yield 'world'
