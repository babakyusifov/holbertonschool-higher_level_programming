#!/usr/bin/python3
'''
this module 1-square right now it is empty
'''


class Square:
    '''
    square class has private attr size
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
