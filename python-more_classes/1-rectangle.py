#!/usr/bin/python3
"""Rectangle class defines a rectangle with width and height"""


class Rectangle:
    """Definition: Rectangle class"""

    def __init__(self, width=0, height=0):
        """Constructor that initializes width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method: returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method: sets the value of width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method: returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method: sets the value of height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
