#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix.
    Returns a new matrix
    """
    if not isinstance(div, (int, float)) or type(div) is bool:
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list or not all((type(l) is list)for l in matrix) \
        or not all((isinstance(n, (int, float))for n in l)for l in matrix) \
            or len(matrix[0]) == 0:
                raise TypeError(
                    'matrix must be a matrix (list of lists) of'
                    ' integers/floats'
                    )
    _len = len(matrix[0])
    if not all((len(l) == _len)for l in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    return [list(map(lambda x: round(x / div, 2), l))for l in matrix]
