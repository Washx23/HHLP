#!/usr/bin/python3
"""Test class rectangle"""


import sys
import unittest
from models.rectangle import Rectangle
from io import StringIO


class testing(unittest.TestCase):
    
    def test_rectangle(self):
        """test cases"""
        print("test simple cases approved")
        data = Rectangle(1, 2)
        self.assertEqual(data.width, 1)
        self.assertEqual(data.height, 2)
        data = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(data.width, 1)
        self.assertEqual(data.height, 2)
        self.assertEqual(data.x, 3)
        self.assertEqual(data.y, 4)
        self.assertEqual(data.id, 5)
        self.assertEqual(data.area(), 2)
        self.assertEqual(data.__str__(), '[Rectangle] (5) 3/4 - 1/2')

    def test_rectangle_edgecases(self):
        """edege cases"""
        print("test edge cases approved")
        self.assertRaises(TypeError, Rectangle,"1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3,-4)

    def test_display(self):
        data = StringIO()
        sys.stdout = data
        aux = Rectangle(2, 2)
        aux.display()
        self.assertEqual(data.getvalue(), "##\n##\n")

    def test_to_dictionary(self):
        data = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(data.to_dictionary(), {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1})

    def test_update(self):
        data = Rectangle(1, 2, 3, 4, 5)
        data.update()
        self.assertEqual(data.__str__(), '[Rectangle] (5) 3/4 - 1/2')
    
    def test_create(self):
        data = Rectangle(1, 2, 3, 4, 5)
        data.create(**{ 'id': 89 })
        self.assertEqual(data.__str__(), '[Rectangle] (5) 3/4 - 1/2')
    
    def test_save1(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), '[]')
    
    def test_save3(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), '[]')
    
    def test_load(self):
        Rectangle.load_from_file()
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), '[]')

    if __name__ == '__main__':
        unittest.main()