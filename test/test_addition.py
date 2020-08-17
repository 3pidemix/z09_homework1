import unittest
from code.addition import add
from code.increment import inc

class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 4), 6)

    def test_addition_neg(self):
        self.assertNotEqual(add(82, -42), 16)
