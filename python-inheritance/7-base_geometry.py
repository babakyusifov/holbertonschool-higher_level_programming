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
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.
        Parameters:
            name (str): The name of the value (used in error messages).
            value (int): The value to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
