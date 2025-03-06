import math

class Fraction():
    '''
    A class that represents fractions.
    Attributes: numerator (zähler), denominator (nenner)
    '''
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __add__(self, other):
        if isinstance(other, int):
            # Adding an integer to the fraction
            add_numerator = self.numerator + other * self.denominator
            add_denominator = self.denominator
            return Fraction(add_numerator, add_denominator)
        elif isinstance(other, float):
            # Adding a float to the fraction
            return self.numerator / self.denominator + other
        else:
            # Adding another fraction
            add_numerator = self.numerator * other.denominator + self.denominator * other.numerator
            add_denominator = self.denominator * other.denominator
            return Fraction(add_numerator, add_denominator)
    
    def __radd__(self, other):
        return self + other
       
    def __sub__(self, other):
        if isinstance(other, int):
            # Subtracting an integer from the fraction
            sub_numerator = self.numerator - other * self.denominator
            sub_denominator = self.denominator
            return Fraction(sub_numerator, sub_denominator)
        elif isinstance(other, float):
            # Subtracting a float from the fraction
            return self.numerator / self.denominator - other
        # Subtracting another fraction
        sub_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        sub_denominator = self.denominator * other.denominator
        return Fraction(sub_numerator, sub_denominator)
    
    def __rsub__(self, other):
        return Fraction(-self.numerator, self.denominator) + other

    def __mul__(self, other):
        if isinstance(other, int):
            # Multiplying the fraction by an integer
            mul_numerator = self.numerator * other
            mul_denominator = self.denominator
            return Fraction(mul_numerator, mul_denominator)
        if isinstance(other, float):
            # Multiplying the fraction by a float
            return (self.numerator / self.denominator) * other
        # Multiplying by another fraction
        mul_numerator = self.numerator * other.numerator
        mul_denominator = self.denominator * other.denominator
        return Fraction(mul_numerator, mul_denominator)
    
    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, int):
            # Dividing the fraction by an integer
            div_numerator = self.numerator
            div_denominator = self.denominator * other
            return Fraction(div_numerator, div_denominator)
        elif isinstance(other, float):
            # Dividing the fraction by a float
            return (self.numerator / self.denominator) / other
        # Dividing by another fraction
        div_numerator = self.numerator * other.denominator
        div_denominator = self.denominator * other.numerator
        return Fraction(div_numerator, div_denominator)
    
    def __rtruediv__(self, other):
        return Fraction(self.denominator, self.numerator) * other

    @staticmethod
    def gcd(a, b):
        # Compute the greatest common divisor of a and b
        while b != 0:
            a, b = b, a % b
        return a

    def simplify(self):
        # Simplify the fraction to its lowest terms
        common = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // common
        self.denominator = self.denominator // common

    sqrt2 = 1.41421356237  # Square root of 2 for reference

###### Inheritance #######

class Inverse(Fraction):
    '''
    A class representing reciprocals (inverse fractions)
    '''
    def __init__(self, denominator):
        self.numerator = 1
        self.denominator = denominator

    def __mul__(self, other):
        # Multiply two inverse fractions
        return Inverse(self.denominator * other.denominator)

class Vector(list):
    '''
    A class representing vectors
    '''
    def __add__(self, other):
        # Add two vectors element-wise
        sum_list = [self[i] + other[i] for i in range(len(self))]
        return Vector(sum_list)

    def __mul__(self, other):
        # Multiply two vectors element-wise
        prod_list = [self[i] * other[i] for i in range(len(self))]
        return Vector(prod_list)

    def scalar(self, other):
        # Compute the scalar (dot) product of two vectors
        return sum(self * other)
