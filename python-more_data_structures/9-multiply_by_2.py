#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    aux = {}
    for i, n in a_dictionary.keys():
        aux[i] = n * 2
    return aux 