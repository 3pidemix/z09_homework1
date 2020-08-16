import unittest
from code.multiplication import multiplication
class TestMultiplication(unittest.Testcase):
    def test_multiplication(self):
        self.assertEqual(multiplication(2,4),8)
    def test_multiplication_neg(self):
        self.asserEqual(multiplication(5,4), 18)