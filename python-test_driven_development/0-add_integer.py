#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The example module supplies one function, add_integer().  For example,
>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):

    """Return the sum of two numbers.
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> try:
    ...    print(add_integer(4, "School"))
    ... except Exception as e:
    ...    print(e)
    b must be an integer
    """

    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, float) or isinstance(b, float):
        return int(a) + int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    else:
        raise TypeError("b must be an integer")
