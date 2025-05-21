#!/usr/bin/python3
'''
This module defines the Square class (6-square.py).
'''


class Square:
    '''
    square class has private attr size returns the current square area
    '''
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(position[0], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(position[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        '''
        Calculate and return the area of the square.
        Returns:
            int: The area of the square.
        '''
        return self.__size ** 2

    @property
    def size(self):
        '''
        it is getter for size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        this is setter for size
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        '''
        method that prints square based on self.__size
        '''
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print('#', end='')
            print()

    @property
    def position(self):
        '''
        it is getter for position
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        this is setter for position
        '''
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
