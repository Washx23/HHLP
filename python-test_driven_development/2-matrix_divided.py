#!/usr/bin/python3
"""2-matrix_divided"""


def matrix_divided(matrix, div):
    """matrix"""
    row = len(matrix)
    row_size = len(matrix[0])
    new_matrix = [[0 for col in range(row_size)] for row in range(row)]

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(row):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    for i, item in enumerate(matrix):
        for j, aux in enumerate(item):
            if type(aux) is not int and type(aux) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats")

            new_matrix[i][j] = round((aux / div), 2)
    return (new_matrix)
