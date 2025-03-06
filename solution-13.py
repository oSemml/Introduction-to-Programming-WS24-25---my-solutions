import math

class Function():
    '''
    An abstract base class for mathematical functions
    '''
    def __init__(self):
        pass

    def __call__(self, x):
        # This method will be overridden by specific functions to define how they behave when called with an argument
        return None

    def __repr__(self):
        # Returns a string representation of the function (for debugging purposes)
        return 'Abstract function'

    def __add__(self, other):
        # Adding two functions (returns a new abstract function)
        return Function()

    def derivative(self):
        # Returns the derivative of the function (abstract in base class)
        return Function()


class Polynomial(Function):
    '''
    A class representing polynomial functions.
    It inherits from the base class "Function".
    '''
    def __init__(self, coefficients):
        '''
        Initialize the polynomial with a list of coefficients.
        Example: [1, 2, 3] represents 1 + 2x + 3x²
        '''
        self.coefficients = coefficients

    def __call__(self, x):
        # Evaluate the polynomial for a given x
        return sum([self.coefficients[i] * x ** i for i in range(len(self.coefficients))])

    def __repr__(self):
        # Returns a string representation of the polynomial in standard form
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef == 0:
                continue
            if i == 0 or coef not in [1, -1]:
                term = str(coef)
            elif coef == 1:
                term = ''
            elif coef == -1:
                term = '-'
            
            # Append the term with the proper exponent notation
            if i == 0:
                terms.append(str(coef))
            else:
                terms.append(term + 'x' + Polynomial.superscript(i))
        
        result = ' + '.join(terms)
        result = result.replace('x⁰', '')
        if len(self.coefficients) > 1:
            if self.coefficients[1] != 0:
                result = result.replace('x¹', 'x', 1)
        result = result.replace('+ -', '- ')
        return result

    @staticmethod
    def superscript(n):
        # Converts an integer to a superscript string
        return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c) - ord('0')] for c in str(n)])

    def __add__(self, other):
        # Adds two polynomials by adding their corresponding coefficients
        j = min(len(self.coefficients), len(other.coefficients))
        coef_sum = [self.coefficients[i] + other.coefficients[i] for i in range(j)]
        
        # If one polynomial is longer than the other, append the remaining coefficients
        if len(self.coefficients) > len(other.coefficients):
            coef_sum += self.coefficients[j:]
        else:
            coef_sum += other.coefficients[j:]
        
        return Polynomial(coef_sum)
    
    def __sub__(self, other):
        # Subtracts two polynomials by subtracting their corresponding coefficients
        j = min(len(self.coefficients), len(other.coefficients))
        coef_diff = [self.coefficients[i] - other.coefficients[i] for i in range(j)]

        # If one polynomial is longer than the other, append the remaining coefficients
        if len(self.coefficients) > len(other.coefficients):
            coef_diff += self.coefficients[j:]
        else:
            coef_diff += [-i for i in other.coefficients[j:]]
        
        return Polynomial(coef_diff)

    def derivative(self):
        # Returns the derivative of the polynomial
        coef_derivative = [i * self.coefficients[i] for i in range(1, len(self.coefficients))]
        return Polynomial(coef_derivative)

    def primitive(self):
        # Returns the primitive (integral) of the polynomial
        coef_integral = [0] + [self.coefficients[i] / (i + 1) for i in range(len(self.coefficients))]
        return Polynomial(coef_integral)
    
    def degree(self):
        # Returns the degree of the polynomial (highest exponent with non-zero coefficient)
        for i in range(len(self.coefficients) - 1, -1, -1):
            if self.coefficients[i] != 0:
                return i
        return float('-inf')  # Return negative infinity if the polynomial is zero
