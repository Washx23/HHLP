#!/usr/bin/python3
"""1. My list"""


class MyList(list):
    """MyList"""
    def print_sorted(self):
        """print_sortet"""
        if self:
            A = list.copy(self)
            A = sorted(A)
            print(A)
