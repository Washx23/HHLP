#!/usr/bin/python3
""" rectangle class """


from models.base import Base 

class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__heigth = height
        self.__x = x
        self.__y = y
        super().__init__(id)
