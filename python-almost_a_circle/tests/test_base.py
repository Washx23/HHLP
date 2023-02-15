#!/usr/bin/python3
"""test base"""



import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ Test base """
    def setUp(self):
        self.b1 = Base()
        self.b89 = Base(89)
        self.b23 = Base(id=23)
        self.b4 = Base(4)
        self.b3, self.b4 = Base(), Base()
        self.b6 = Base(-7)
        self.b0 = Base(0)

    def testBaseId(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b89.id, 89)
        self.assertEqual(self.b23.id, 23)
        self.assertEqual(self.b4.id, 3)
        self.assertEqual((self.b3.id, self.b4.id), (2, 3))
        self.assertEqual(self.b6.id, -7)
        self.assertEqual(self.b0.id, 0)