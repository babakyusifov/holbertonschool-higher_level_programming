#!/usr/bin/python3
"""
Divides all elements of a matrix by a number.

Args:
    matrix (list of lists): A matrix (list of lists) of integers or floats.
    div (int or float): A number to divide the matrix elements by.

Returns:
    list of lists: A new matrix with all elements divided by div, rounded to 2 decimals.

Raises:
    TypeError: If matrix is not a list of lists of integers/floats.
    TypeError: If rows are not of the same size.
    TypeError: If div is not a number.
    ZeroDivisionError: If div is 0.
"""
def matrix_divided(matrix, div):
    for row in range(len(matrix)):
        for num in range(len(matrix[row])):  
            if isinstance(matrix, str):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(matrix[0]) != len(matrix[1]):
                raise TypeError("Each row of the matrix must have the same size")
            if not isinstance(div, str):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]