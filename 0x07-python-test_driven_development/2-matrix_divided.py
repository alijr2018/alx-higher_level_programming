#!/usr/bin/python3
"""Write a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """def of matrix_divided"""
    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errorMessage)
    if not isinstance(matrix, list):
        raise TypeError(errorMessage)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errorMessage)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(errorMessage)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(errorMessage)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div == float('inf'):
        n_m = [[0.0 for element in row] for row in matrix]
    else:
        n_m = [[round(item / div, 2) for item in lists] for lists in matrix]
    return (n_m)
