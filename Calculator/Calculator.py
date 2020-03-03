from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Exponentiation import exponentiation
from Calculator.Division import division
from Calculator.Logarithim import logarithm
from Calculator.SquareRoot import squareRoot


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def exponentiation(self, a, b):
        self.result = exponentiation(a, b)
        return self.result

    def logarithm(self, a, b):
        self.result = logarithm(a, b)
        return self.result

    def squareRoot(self, a):
        self.result = squareRoot(a)
        return self.result
