#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix

by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists of (int or float)): The matrix to be divided.
        div (int or float): The number by which to divide all
        elements of the matrix.

    Returns:
        list of lists of (int or float): A new matrix with the result of
        the division.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   if all rows of the matrix do not have the same size,
                   or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(
            "Each row of the matrix must have the same size"
        )
    if not isinstance(div, (int, float)):
        raise TypeError(
            "div must be a number"
        )
    if div == 0:
        raise ZeroDivisionError(
            "division by zero"
        )
    return [[round(num / div, 2) for num in row] for row in matrix]
