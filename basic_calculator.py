# calculator.py

def add(x, y):
    """
    Add two numbers.

    :param x: The first number.
    :param y: The second number.
    :return: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Subtract two numbers.

    :param x: The first number.
    :param y: The second number.
    :return: The result of x - y.
    """
    return x - y

def multiply(x, y):
    """
    Multiply two numbers.

    :param x: The first number.
    :param y: The second number.
    :return: The product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Divide two numbers.

    :param x: The numerator.
    :param y: The denominator.
    :return: The result of x / y.
    """
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y

# test_calculator.py
import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(4, 6), 24)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(0, 5), 0)

        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
