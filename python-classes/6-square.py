#!/usr/bin/python3
"""Square"""


class Square:
    """Square"""
    def __init__(self, size=0, position=(0, 0)):
        """def name: __init__"""
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, var):
        """size"""
        if var < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(var, int):
            raise TypeError("size must be an integer")
        self.__size = var

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, value):
        """position"""
        self.__position = value

    def area(self):
        """area"""
        return self.__size * self.__size

    def my_print(self):
        """my_print"""
        if self.__size == 0:
            print()
            return
        for x in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for p in range(self.__position[0]):
                print(end=" ")
            for j in range(self.__size):
                print("#", end="")
            print()