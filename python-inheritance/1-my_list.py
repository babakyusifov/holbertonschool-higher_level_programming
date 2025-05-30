#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.

The MyList class adds a print_sorted() method that prints the list
elements in ascending order without modifying the original list.
"""


class MyList(list):
    """
    MyList class inherits from the built-in list class.

    It adds a public instance method called print_sorted that prints
    the list elements in sorted (ascending) order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order
        without modifying the original list.

        Notes:
            - All elements are assumed to be integers.
            - The original list remains unchanged.
        """
        print(sorted(self))
