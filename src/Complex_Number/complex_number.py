# complex_number.py
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        denominator = other.real2 + other.imag2
        return ComplexNumber((self.real * other.real + self.imag * other.imag) / denominator,
                             (self.imag * other.real - self.real * other.imag) / denominator)

