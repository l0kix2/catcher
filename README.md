catcher
=======

Neat lib, which makes your code nicer.

```
from catcher import wrap

@wrap.in_dict
def function():
    yield 'a', 10
    yield 'b', 20

>>> function()
... {'a': 10, 'b': 20}


# full list
@wrap.in_list
@wrap.in_sorted_list
@wrap.in_reversed_list
@wrap.in_dict
@wrap.in_odict
@wrap.count
@wrap.summarize
@wrap.maximum
@wrap.minimum
@wrap.cat
@wrap.chain
```
