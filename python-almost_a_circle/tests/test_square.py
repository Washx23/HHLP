#!/usr/bin/python3
"""test Square"""

import unittest

from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        self.b1 = Square(1,1)
        self.b2 = Square(5)
        self.b3 = Square(1, 2, 3)
        self.b4 = Square(1, 2, 3, 4)
        self.b5 = Square(size=7, id=89, y=1)
        self.b6 = Square(size=7, y=1)
        self.b7 = Square(x=12, size=98)

    def testBaseId(self):
        self.assertEqual(self.b1.id, 4)
        self.assertEqual(self.b2.id, 5)
        self.assertEqual(self.b3.id, 6)
        self.assertEqual(self.b4.id, 4)
        self.assertEqual(self.b5.id, 89)
        self.assertEqual(self.b6.id, 7)
        self.assertEqual(self.b7.id, 8)
    
    def test_bad_type(self):
        data = -7
        with self.assertRaises(TypeError):
            result = sum(data)
    
    def test_bad_type2(self):
        data = None
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == '__main__':
    unittest.main()