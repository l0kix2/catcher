# coding: utf-8
from __future__ import unicode_literals

from catcher import wrap_in
from . import factories

count = wrap_in(factories.counter)
summarize = wrap_in(factories.sum_)
maximum = wrap_in(max)
minimum = wrap_in(min)

