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

    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__heigth
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    
    @width.setter
    def width(self, width):
        if type(width) is not int:
            TypeError("width must be an integer")
        if width <= 0:
            ValueError("width must be > 0")
        self.__width = width
    
    @height.setter
    def height(self, height):
        if type(height) is not int:
            TypeError("width must be an integer")
        if height <= 0:
            ValueError("width must be > 0")
        self.__heigth = height
    
    @x.setter
    def width(self, x):
        if type(x) is not int:
            TypeError("width must be an integer")
        if x <= 0:
            ValueError("width must be > 0")
        self.__x = x
    
    @width.setter
    def width(self, y):
        if type(y) is not int:
            TypeError("width must be an integer")
        if y <= 0:
            ValueError("width must be > 0")
        self.__y = y
    