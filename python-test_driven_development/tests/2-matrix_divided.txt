>>> matrix_divided = __import__('2-matrix_divided').matrix_divided
>>> matrix = [
...    [1, 2, 3],
...    [4, 5, 6]
... ]
>>> print(matrix_divided(matrix, 3))
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
>>> print(matrix)
[[1, 2, 3], [4, 5, 6]]
>>> try:
...     print(matrix_divided(matrix, 'hello'))
... except Exception as e:
...     print(e)
div must be a number
>>> try:
...     print(matrix_divided(matrix, 0))
... except Exception as e:
...     print(e)
division by zero
>>> matrix = [
...    ['a', 2, 3],
...    [4, 5, 6]
... ]
>>> try:
...     print(matrix_divided(matrix, 2))
... except Exception as e:
...     print(e)
matrix must be a matrix (list of lists) of integers/floats
>>> matrix = [
...    [2, 3],
...    [4, 5, 6]
... ]
>>> try:
...     print(matrix_divided(matrix, 2))
... except Exception as e:
...     print(e)
Each row of the matrix must have the same size
>>> matrix = [
...    [1, 2],
...    [3, 4]
... ]
>>> print(matrix_divided(matrix, float('inf')))
[[0.0, 0.0], [0.0, 0.0]]
>>> try:
...     print(matrix_divided(matrix))
... except Exception as e:
...     print(e)
matrix_divided() missing 1 required positional argument: 'div'
>>> try:
...     print(matrix_divided())
... except Exception as e:
...     print(e)
matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'
