#!/usr/bin/python3
"""
This module defines a Rectangle class that allows
area and perimeter calculations, with proper encapsulation,
validation, and string representation using '#'.
"""


class Rectangle:
    """
    A class that defines a rectangle by its width and height,
    and provides methods to compute area and perimeter.
    Also supports visual representation using the '#' character.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle (default is 0).
            height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width with validation.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height with validation.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle.

        Returns:
            int: The perimeter (2 * (width + height)), or 0 if
            width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the string representation of the rectangle using `#`.

        Returns:
            str: Visual rectangle using '#' characters, or an empty
            string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])
