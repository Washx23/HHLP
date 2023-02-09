#!/usr/bin/python3
""" Base Geometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle func """
    def __init__(self, width, height):
        self.__whidth = width
        self.__heigth = height
        self.integer_validator("height", self.__heigth)
        self.integer_validator("whidth", self.__whidth)
