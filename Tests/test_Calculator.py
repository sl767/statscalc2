import unittest

from Calculator.Calculator import Calculator
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Exponentiation import exponentiation
from Calculator.Logarithm import logarithm
from Calculator.SquareRoot import squareRoot


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_addition(self):
        self.assertEqual(6, addition(3, 3))

    def test_subtraction(self):
        self.assertEqual(10, subtraction(25, 15))

    def test_multiplication(self):
        self.assertEqual(48, multiplication(12, 4))

    def test_division(self):
        self.assertEqual(3, division(12, 4))

    def test_exponentiation(self):
        self.assertEqual(9, exponentiation(3, 2))

    def test_logarithm(self):
        self.assertEqual(6, logarithm(64, 2))

    def test_squareRoot(self):
        self.assertEqual(5, squareRoot(25))


if __name__ == '__main__':
    unittest.main()
