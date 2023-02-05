#!/usr/bin/python3
"""Square"""


class Square:
    """Square"""
    def __init__(self, size=0):
        """__init__"""
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size
