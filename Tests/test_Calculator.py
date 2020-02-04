import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
            calculator = Calculator()
            result = calculator.addition(1, 2)
            self.assertEqual(3, result)

    def test_subtraction(self):
        calculator = Calculator()
        result = calculator.subtraction(1, 2)
        self.assertEqual(-1, result)

    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(1, 2)
        self.assertEqual(2, result)

    def test_divide(self):
        calculator = Calculator()
        result = calculator.divide(1, 2)
        self.assertEqual(0.5, result)

    def test_squareRoot(self):
        calculator = Calculator()
        result = calculator.squareRoot(9)
        self.assertEqual(3, result)

    def test_square(self):
        calculator = Calculator()
        result = calculator.square(4)
        self.assertEqual(2, result)

if __name__ == '__main__':
    unittest.main()