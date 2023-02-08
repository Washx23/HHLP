#!/usr/bin/pyton3
"""1. My list"""


class MyList(list):
    def print_sorted(self):
        A = list.copy(self)
        A = sorted(A)
        print(A)
