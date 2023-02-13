#!/usr/bin/python3
""" Square class """


from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = size
        self.y = size
        super().__init__(size, size, y, x, id)

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.size}'