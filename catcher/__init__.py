# coding: utf-8
from __future__ import unicode_literals

from functools import wraps


def wrap_in(factory=None):
    """
    Fabric for decorators. Needs factory callable, that
    can get iterable as only parameter. Decorator feeds yields from
    decorated generator function in this factory and returns
    resulted object.

    Helps in making generators shorter and simpler by splitting
    logic and routine.

    TODO: maybe class-based decorator will be better choice for readability.
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
