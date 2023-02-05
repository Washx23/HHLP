#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """__init__"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, var):
        if not isinstance(var, int):
            raise TypeError("width must be an integer")
        elif var < 0:
            raise ValueError("width must be >= 0")
        self.__width = var

    @height.setter
    def height(self, var):
        if type(var) is not int:
            raise TypeError("height must be an integer")
        if var < 0:
            raise ValueError("height must be >= 0")
        self.__height = var
