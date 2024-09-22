import unittest
from complex_number import Complex_Number
from operations import AddOperation, MultiplyOperation, DivideOperation

class TestCalculator(unittest.TestCase):
    def test_add(self):
        num1 = Complex_Number(1, 2)
        num2 = Complex_Number(3, 4)
        operation = AddOperation()
        result = operation.execute(num1, num2)
        self.assertEqual(result.real, 4)
        self.assertEqual(result.imag, 6)

    def test_multiply(self):
        num1 = Complex_Number(1, 2)
        num2 = Complex_Number(3, 4)
        operation = MultiplyOperation()
        result = operation.execute(num1, num2)
        self.assertEqual(result.real, -5)
        self.assertEqual(result.imag, 10)

    def test_divide(self):
        num1 = Complex_Number(1, 2)
        num2 = Complex_Number(3, 4)
        operation = DivideOperation()
        result = operation.execute(num1, num2)
        self.assertEqual(result.real, 11/25)
        self.assertEqual(result.imag, -2/25)

    if __name__ == '__main__':
        unittest.main()
