#!/usr/bin/python3
"""4-inherits_from"""


def inherits_from(obj, a_class):
    """ inherits_rom """
    if obj is not float or obj is not None:
        return type(obj) is not a_class
