import unittest
from code.subtraction import subtraction

class TestSubtraction(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(subtraction(4, 2), 2)

    def test_subtraction_neg(self):
        self.assertEqual(subtraction(4, -8), 5)
