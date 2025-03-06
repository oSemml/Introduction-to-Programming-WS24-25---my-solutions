class ComplexNumber():
    '''
    A class that represents complex numbers.
    Attributes: Real part (re) and imaginary part (im).
    '''
    
    def __str__(self):
        # Return a string representation of the complex number
        if self.im >= 0:
            return str(self.re) + ' + ' + str(self.im) + 'i'
        else:
            return str(self.re) + ' - ' + str(-self.im) + 'i'
    
    def __init__(self, re, im):
        # Initialize the complex number with real and imaginary parts
        self.re = re
        self.im = im

    def __add__(self, cn):
        # Add two complex numbers
        return ComplexNumber(self.re + cn.re, self.im + cn.im)

    def __sub__(self, cn):
        # Subtract one complex number from another
        return ComplexNumber(self.re - cn.re, self.im - cn.im)
    
    def __mul__(self, cn):
        # Multiply two complex numbers
        return ComplexNumber(self.re * cn.re - self.im * cn.im, self.re * cn.im + self.im * cn.re)
    
    def __truediv__(self, cn):
        # Divide one complex number by another
        denominator = cn.re ** 2 + cn.im ** 2
        return ComplexNumber((self.re * cn.re + self.im * cn.im) / denominator, 
                             (-self.re * cn.im + self.im * cn.re) / denominator)
