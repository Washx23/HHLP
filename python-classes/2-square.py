#!/usr/bin/python3
"""Square"""


class Square:
    """Square"""
    def __init__(self, __size=0):
        """Square"""
        if int(__size) < 0:
            raise ValueError("size must be >= 0")
        if type(__size) is not int:
            raise TypeError("size must be an integer")
        self.__size = __size
