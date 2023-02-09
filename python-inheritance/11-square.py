#!/usr/bin/python3
""" Base Geometry """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square func """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        """area"""
        return self.__size * self.__size

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
