# coding: utf-8
from __future__ import unicode_literals

import itertools

import six
import pytest

from catcher import wrap

from . import functions as funcs


@pytest.mark.parametrize('func, output', [
    (funcs.yield_sequence, [1, 2]),
    (funcs.yield_nones, [None, None]),
    (funcs.yield_never, []),
])
def test_in_list(func, output):
    assert wrap.in_list(func)() == output


@pytest.mark.parametrize('func, output', [
    (funcs.yield_sequence, [1, 2]),
    (funcs.yield_sequence_backwards, [1, 2]),
    (funcs.yield_never, []),
])
@pytest.mark.parametrize('tested_func', [
    wrap.in_list(sort=True),
    wrap.in_sorted_list,
])
def test_in_sorted_list(tested_func, func, output):
    assert tested_func(func)() == output


@pytest.mark.parametrize('func, output', [
    (funcs.yield_sequence, [2, 1]),
    (funcs.yield_sequence_backwards, [1, 2]),
    (funcs.yield_never, []),
])
def test_in_reversed_list(func, output):
    assert wrap.in_reversed_list(func)() == output


@pytest.mark.parametrize('func, output', [
    (funcs.yield_pairs, {'Liz': 40, 'Jack': 50}),
    (funcs.yield_never, {}),
])
def test_in_dict(func, output):
    assert wrap.in_dict(func)() == output


@pytest.mark.parametrize('func, output', [
    (funcs.yield_pairs, [('Liz', 40), ('Jack', 50)]),
    (funcs.yield_pairs_backwards, [('Jack', 50), ('Liz', 40)]),
    (funcs.yield_never, []),
])
@pytest.mark.parametrize('tested_func', [
    wrap.in_dict(ordered=True),
    wrap.in_odict,
])
def test_in_odict(tested_func, func, output):
    assert list(six.iteritems(tested_func(func)())) == output


@pytest.mark.parametrize('func, output', [
    (funcs.yield_nones, set([None])),
    (funcs.yield_sequence, set([1, 2])),
    (funcs.yield_never, set()),
])
def test_in_set(func, output):
    assert wrap.in_set(func)() == output



@pytest.mark.parametrize('func, output', [
    (funcs.yield_pairs, ['Liz', 40, 'Jack', 50]),
    (funcs.yield_never, []),
])
def test_chain_not_lazy(func, output):
    assert wrap.chain(lazy=False)(func)() == output


@pytest.mark.parametrize('func, output', [
    (funcs.yield_pairs, ['Liz', 40, 'Jack', 50]),
    (funcs.yield_never, []),
])
def test_chain_lazy(func, output):
    chained = wrap.chain(func)()
    assert isinstance(chained, itertools.chain)
    assert list(chained) == output
