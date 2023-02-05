#!/usr/bin/python3
"""Square"""


class Square:
    """Square"""
    def __init__(self, __size=0):
        """Square"""
        if __size < 0:
            raise ValueError("size must be >= 0")
        if type(__size) is not int:
            raise TypeError("size must be an integer")
        self.__size = __size

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, var):
        """size"""
        if int(var) < 0:
            raise ValueError("size must be >= 0")
        if type(var) is not int:
            raise TypeError("size must be an integer")
        self.__size = var

    def area(self):
        """area"""
        return self.__size * self.__size
