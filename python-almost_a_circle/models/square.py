#!/usr/bin/python3
"""class Square"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = size
        self.y = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def update(self, *args, **kwargs):
        """ update Square """
        if args:
            new_list = ["id", "size", "x", "y"]
            for k, v in zip(new_list, args):
                setattr(self, k, v)
        else:
            for c, p in kwargs.items():
                setattr(self, c, p)

    def to_dictionary(self):
        """dictionary"""
        new_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
        return new_dict
