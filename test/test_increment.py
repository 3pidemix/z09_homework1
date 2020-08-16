import unittest
from code.addition import add
from code.increment import inc

class TestAddition(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc(40), 41)

    def test_increment_neg(self):
        self.assertEqual(inc(10), 40)