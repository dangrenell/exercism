from math import sin, cos, exp


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return f'{self.real} + {self.imaginary}i'

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        new_re = self.real + other.real
        new_im = self.imaginary + other.imaginary
        return ComplexNumber(new_re, new_im)

    def __mul__(self, other):
        new_re = self.real * other.real - self.imaginary * other.imaginary
        new_im = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(new_re, new_im)

    def __sub__(self, other):
        new_re = self.real - other.real
        new_im = self.imaginary - other.imaginary
        return ComplexNumber(new_re, new_im)

    def __truediv__(self, other):
        new_re = (self.real * other.real + self.imaginary *
                  other.imaginary) / (other.real**2 + other.imaginary**2)
        new_im = (- self.real * other.imaginary +
                  self.imaginary * other.real) / (other.real**2 + other.imaginary**2)
        return ComplexNumber(new_re, new_im)

    def __abs__(self):
        return (self.real**2 + self.imaginary**2)**0.5

    def conjugate(self):
        new_re = self.real
        new_im = -self.imaginary
        return ComplexNumber(new_re, new_im)

    def exp(self):
        new_re = exp(self.real)*cos(self.imaginary)
        new_im = exp(self.real)*sin(self.imaginary)
        return ComplexNumber(new_re, new_im)
