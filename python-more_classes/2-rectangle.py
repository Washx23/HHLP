#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """__init__"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width"""
        return self.__width

    @property
    def height(self):
        """height"""
        return self.__height

    @width.setter
    def width(self, var):
        """width"""
        if type(var) is not int:
            raise TypeError("width must be an integer")
        if var < 0:
            raise ValueError("widht must be >= 0")
        self.__width = var

    @height.setter
    def height(self, var):
        """heigth"""
        if type(var) is not int:
            raise TypeError("height must be an integer")
        if var < 0:
            raise ValueError("height must be >= 0")
        self.__height = var

    def area(self):
        """area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter"""
        count = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            count = 0
            return count
        return count
