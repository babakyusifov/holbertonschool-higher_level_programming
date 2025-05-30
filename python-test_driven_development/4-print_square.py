#!/usr/bin/python3
'''
This is the "4-print_square" module.
The example module supplies one function, def def print_square().
'''


def print_square(size):
    '''
    Write a function that prints a square with the character #.
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (size < 0 and isinstance(size, float)):
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
