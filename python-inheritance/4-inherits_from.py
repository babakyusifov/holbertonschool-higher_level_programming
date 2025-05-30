#!/usr/bin/python3
"""
This module defines a function that checks whether an object is an instance
of a class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    Parameters:
    obj (any): The object to check.
    a_class (type): The class to compare against.
    Returns:
    bool: True if obj is an instance of a subclass of a_class,
          but not an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
