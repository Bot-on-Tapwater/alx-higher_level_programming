#!/usr/bin/python3
"""Divides elements of a matrix"""


def matrix_divided(matrix, div):

    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(message)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(message)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by Zero")

    divided_matrix = []
    for row in matrix:
        divided_row = []
        for element in row:
            divided_row.append(round(element / div, 2))
        divided_matrix.append(divided_row)

    return divided_matrix
