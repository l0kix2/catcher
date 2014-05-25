# coding: utf-8
from __future__ import unicode_literals

import pytest

from catcher import calc

from . import functions as funcs


@pytest.mark.parametrize('func, output', [
    (funcs.yield_sequence, 2),
    (funcs.yield_pairs, 2),
    (funcs.yield_nones, 2),
    (funcs.yield_never, 0),
])
def test_count(func, output):
    assert calc.count(func)() == output


@pytest.mark.parametrize('func, output', [
    (funcs.yield_sequence, 3),
    (funcs.yield_never, 0),
])
def test_summarize(func, output):
    assert calc.summarize(func)() == output


@pytest.mark.parametrize('func, output', [
    (funcs.yield_sequence, 13),
    (funcs.yield_never, 10),
])
def test_summarize_with_initial(func, output):
    assert calc.summarize(start=10)(func)() == output


@pytest.mark.parametrize('func, output', [
    (funcs.yield_sequence, 2),
])
def test_max(func, output):
    assert calc.maximum(func)() == output
