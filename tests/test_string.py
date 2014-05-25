# coding: utf-8
from __future__ import unicode_literals

import pytest

from catcher import string

from . import functions as funcs


@pytest.mark.parametrize('func, output', [
    (funcs.yield_strings, 'hello, cruel world'),
    (funcs.yield_never, ''),
])
def test_cat(func, output):
    assert string.cat(func)() == output
