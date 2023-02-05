#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif int(width) < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif int(height) < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, var):
        if type(var) is not int:
            raise TypeError("width must be an integer")
        if var < 0:
            raise ValueError("widht must be >= 0")
        self.__width = var

    @height.setter
    def height(self, var):
        if type(var) is not int:
            raise TypeError("height must be an integer")
        if var < 0:
            raise ValueError("height must be >= 0")
        self.__height = var

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        count = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            return 0
        return count

    def __str__(self):
        new_str = ""
        if self.__width == 0 or self.__height == 0:
            return new_str
        for i in range(1, self.__height + 1):
            for j in range(1, self.__width + 1):
                new_str += str((self).print_symbol)
            if i is not (self.__height):
                new_str += "\n"
        return new_str

    def __repr__(self):
        return (type(self).__name__ + "(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if type(rect_1).area(rect_1) == type(rect_2).area(rect_2):
            return rect_1
        if type(rect_1).area(rect_1) < type(rect_2).area(rect_2):
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
