import unittest
from code.multiplication import multiplication


class TestMultiplication(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(multiplication(2, 4), 8)

    def test_multiplication_neg(self):
        self.assertNotEqual(add(2, 5), 11)
