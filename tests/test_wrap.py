# coding: utf-8
from __future__ import unicode_literals

import pytest

from catcher import wrap


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


@pytest.mark.parametrize('func, output', [
    (yield_sequence, [1, 2]),
    (yield_nones, [None, None]),
    (yield_never, []),
])
def test_in_list(func, output):
    assert wrap.in_list(func)() == output


@pytest.mark.parametrize('func, output', [
    (yield_sequence, [1, 2]),
    (yield_sequence_backwards, [1, 2]),
    (yield_nones, [None, None]),
    (yield_never, []),
])
def test_in_sorted_list(func, output):
    assert wrap.in_sorted_list(func)() == output


@pytest.mark.parametrize('func, output', [
    (yield_sequence, [2, 1]),
    (yield_sequence_backwards, [1, 2]),
    (yield_never, []),
])
def test_in_reversed_list(func, output):
    assert wrap.in_reversed_list(func)() == output


@pytest.mark.parametrize('func, output', [
    (yield_pairs, {'Liz': 40, 'Jack': 50}),
    (yield_never, {}),
])
def test_in_dict(func, output):
    assert wrap.in_dict(func)() == output


@pytest.mark.parametrize('func, output', [
    (yield_pairs, [('Liz', 40), ('Jack', 50)]),
    (yield_pairs_backwards, [('Jack', 50), ('Liz', 40)]),
    (yield_never, []),
])
def test_in_odict(func, output):
    assert wrap.in_odict(func)().items() == output


@pytest.mark.parametrize('func, output', [
    (yield_nones, set([None])),
    (yield_sequence, set([1, 2])),
    (yield_never, set()),
])
def test_in_set(func, output):
    assert wrap.in_set(func)() == output


@pytest.mark.parametrize('func, output', [
    (yield_sequence, 2),
    (yield_pairs, 2),
    (yield_nones, 2),
    (yield_never, 0),
])
def test_count(func, output):
    assert wrap.count(func)() == output


@pytest.mark.parametrize('func, output', [
    (yield_sequence, 3),
    (yield_never, 0),
])
def test_summarize(func, output):
    assert wrap.summarize(func)() == output


@pytest.mark.parametrize('func, output', [
    (yield_sequence, 13),
    (yield_never, 10),
])
def test_summarize_with_initial(func, output):
    assert wrap.summarize(start=10)(func)() == output


@pytest.mark.parametrize('func, output', [
    (yield_strings, 'hello, cruel world'),
    (yield_never, ''),
])
def test_cat(func, output):
    assert wrap.cat(func)() == output


@pytest.mark.parametrize('func, output', [
    (yield_pairs, ['Liz', 40, 'Jack', 50]),
    (yield_never, []),
])
def test_chain(func, output):
    assert wrap.chain(func)() == output


@pytest.mark.parametrize('func, output', [
    (yield_sequence, 2),
])
def test_max(func, output):
    assert wrap.maximum(func)() == output
