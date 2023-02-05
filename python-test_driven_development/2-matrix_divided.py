#!/usr/bin/python3
"""Matrix_divided"""


def matrix_divided(matrix, div):
    """matrix_divided"""
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    new_matrix = []
    for elements in matrix:
        if type(elements) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of " +
                            "integers/floats")
        new_list = []
        for i in elements:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of " +
                                "integers/floats")
            x = i / div
            new_list.append(round(x, 2))
        new_matrix.append(new_list)
    listt = len(matrix[0])
    for r in matrix:
        if len(r) != listt:
            raise TypeError("Each row of the matrix must have the same size")
    return new_matrix
