#!/usr/bin/python3
"""4-inherits_from"""


def inherits_from(obj, a_class):
    """ inherits_rom """
    if obj is None and a_class is object:
        return True
    return type(obj) is not a_class