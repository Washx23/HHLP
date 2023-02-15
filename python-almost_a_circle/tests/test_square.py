#!/usr/bin/python3
"""Test Square"""
import unittest

from models.square import Square

class testing(unittest.TestCase):
    def test_square(self):
        data = Square(1)
        self.assertEqual(data.width, 1)
        self.assertEqual(data.height, 1)
        data = Square(1, 2, 3, 4)
        self.assertEqual(data.area(), 1)
        self.assertEqual(data.x, 2)
        self.assertEqual(data.y, 3)
        self.assertEqual(data.id, 4)
        self.assertEqual(data.__str__(), '[Square] (4) 2/3 - 1')
        data = Square(1, 2)
        self.assertEqual(data.x, 2)
        self.assertEqual(data.y, 0)
    
    def test_square_edgecases(self):
        self.assertRaises(TypeError, Square, "1")
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 1, 2, -3)
        self.assertRaises(ValueError, Square, 0)

    def test_to_dictionary(self):
        data = Square(2, 3, 4, 5)
        self.assertEqual(data.to_dictionary(), {'x': 3, 'y': 4, 'id': 5, 'size': 2})
    
    def test_update(self):
        data = Square(2, 3, 4, 5)
        data.update()
        self.assertEqual(data.__str__(), '[Square] (5) 3/4 - 2')
        
    def test_create(self):
        data = Square(2, 3, 4, 5)
        data.create(**{ 'id': 89 })
        self.assertEqual(data.__str__(), '[Square] (5) 3/4 - 2')

    def test_save1(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[]')
    
    def test_save2(self):
        Square.save_to_file([Square(2)])
        with open("Square.json", "r") as f:
            self.assertEqual('[{"id": 13, "size": 2, "x": 0, "y": 0}]',
            f.read())
    
    def test_save3(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[]')
    
    def test_load(self):
        Square.load_from_file()
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[]')

if __name__ == '__main__':
    unittest.main()