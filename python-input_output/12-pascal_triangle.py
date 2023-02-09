#!/usr/bin/python3
""" main """


def pascal_triangle(n):
    """ pascal triangle """
    new_list = []
    if n <= 0:
        return new_list
    for i in range(n):
        new_list.append([1] * (i + 1))
    for i in range(1, len(new_list)):
        for j in range(1, len(new_list[i]) - 1):
            new_list[i][j] = new_list[i - 1][j - 1] + new_list[i - 1][j]
    return new_list
