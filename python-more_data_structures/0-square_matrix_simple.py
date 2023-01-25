#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        aux = []
        for j in i:
            aux.append((j ** 2))
        new_matrix.append((aux))
    return(new_matrix)
