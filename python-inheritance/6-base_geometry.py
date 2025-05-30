#!/usr/bin/python3
"""
BaseGeometry class module.
This serves as a base class for other geometry-related classes.
"""


class BaseGeometry:
    """Base class for geometry-related operations."""

    def area(self):
        """
        Calculates the area of a geometric shape.
        This method is not implemented in the base class and must be
        overridden by subclasses.
        Raises:
        Exception: Always with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
