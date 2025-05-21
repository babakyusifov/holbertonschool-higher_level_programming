#!/usr/bin/python3
'''
This module defines the Square class (3-square.py).
'''


class Square:
    '''
    square class has private attr size returns the current square area
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        Calculate and return the area of the square.
        Returns:
            int: The area of the square.
        '''
        return self.__size ** 2
