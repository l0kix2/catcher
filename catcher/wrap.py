# coding: utf-8
from __future__ import unicode_literals

from functools import wraps
import itertools


def wrap_in(factory=None):
    """
    Fabric for decorators. Needs factory callable, that 
    can get iterable as only parameter. Decorator feeds yields from 
    decorated generator function in this factory and returns 
    resulted object.
    
    Helps in making generators shorter and simpler by splitting 
    logic and routine.
    """
    def decorator(func=None, **factory_kwargs):
        if func is not None:
            @wraps(func)
            def catcher(*args, **kwargs):
                return factory(func(*args, **kwargs))
            return catcher
        else:
            def another_wrapper(decorated_func):
                @wraps(decorated_func)
                def another_catcher(*args, **kwargs):
                    return factory(
                        decorated_func(*args, **kwargs),
                        **factory_kwargs
                    )
                return another_catcher
            return another_wrapper
    return decorator


###########
# recipes #
###########
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict


def counter(iterable):
    _counter = lambda accumulated, next_item: accumulated + 1
    return reduce(_counter, iterable,  0)


def joiner(iterable):
    return ''.join(iterable)


def chain(iterable):
    return list(itertools.chain.from_iterable(iterable))


def sum_with_start(iterable, start=None):
    if start is not None:
        return sum(iterable, start)
    else:
        return sum(iterable)


def reversed_list(iterable):
    return list(reversed(list(iterable)))


in_list = wrap_in(list)
in_sorted_list = wrap_in(sorted)
in_reversed_list = wrap_in(reversed_list)
# Takes callable, which yields or returns key-value pairs
# and makes dict of them.
# TODO: set doc arg.
in_dict = wrap_in(dict)
in_odict = wrap_in(OrderedDict)
in_set = wrap_in(set)
count = wrap_in(counter)
summarize = wrap_in(sum_with_start)
maximum = wrap_in(max)
minimum = wrap_in(min)
cat = wrap_in(joiner)
chain = wrap_in(chain)
