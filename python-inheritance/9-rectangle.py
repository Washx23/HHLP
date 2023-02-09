#!/usr/bin/python3
""" Base Geometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle func """
    def __init__(self, width, height):
        self.__width = width
        self.__heigth = height
        self.integer_validator("height", self.__heigth)
        self.integer_validator("width", self.__width)

    def area(self):
        """area"""
        return self.__heigth * self.__width

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__heigth, self.__width))
