#!/usr/bin/python3
class Square:
    def __init__(self, __size= 0):
        """"Square"""
        if __size < 0:
            raise ValueError("size must be >= 0")
        if type(__size) != int:
            raise TypeError("size must be an integer") 
        self.__size = __size
    def area(self):
        """area"""
        return self.__size * self.__size