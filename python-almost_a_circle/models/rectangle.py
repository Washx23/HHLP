#!/usr/bin/python3
""" rectangle class """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ area result """
        return self.__width * self.__height

    def display(self):
        """print #"""
        new_str = ""
        if self.__width == 0 or self.__height == 0:
            return new_str
        for i in range(1, self.__height + 1):
            for j in range(1, self.__width + 1):
                new_str += "#"
            if i is not (self.__height):
                new_str += "\n"
        print(new_str)

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}'
