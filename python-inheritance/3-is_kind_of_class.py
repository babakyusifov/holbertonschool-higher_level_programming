#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of,
or inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if object is an instance of or inherited from the specified class.
       Args:
        obj: The object to check
        a_class: The class to compare against
        Returns:
        bool:True if obj is instance of a_class or its subclass,False otherwise
    """
    return isinstance(obj, a_class)
