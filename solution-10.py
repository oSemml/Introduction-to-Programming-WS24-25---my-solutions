def decimal(frac):
    # Convert a fraction to its decimal (floating point) representation
    return frac.numerator / frac.denominator 

def reciprocal(fr):
    # Returns the reciprocal of a fraction
    return Fraction(fr.denominator, fr.numerator) 

def euclidean_algorithm(a, b):
    '''
    The Euclidean algorithm to compute the greatest common divisor (GCD) of two integers.
    '''
    if b == 0:
        return a
    return euclidean_algorithm(b, a % b)

def equal(frac1, frac2):
    '''
    Check if two fractions are equal, by reducing them to their simplest form
    using the Euclidean algorithm.
    '''
    # Simplify frac1
    gcd1 = euclidean_algorithm(frac1.denominator, frac1.numerator)
    frac1.denominator = frac1.denominator / gcd1
    frac1.numerator = frac1.numerator / gcd1
    
    # Simplify frac2
    gcd2 = euclidean_algorithm(frac2.denominator, frac2.numerator)
    frac2.denominator = frac2.denominator / gcd2
    frac2.numerator = frac2.numerator / gcd2

    # Check if simplified fractions are equal
    return frac1.denominator == frac2.denominator and frac1.numerator == frac2.numerator

def bigger(frac1, frac2):
    '''
    Check if frac1 is larger than frac2 by comparing their decimal values.
    '''
    return frac1.numerator / frac1.denominator > frac2.numerator / frac2.denominator

def average(frac1, frac2):
    '''
    Calculate the average of two fractions and return it as a new fraction.
    '''
    numerator = frac1.numerator * frac2.denominator + frac1.denominator * frac2.numerator
    denominator = 2 * frac1.denominator * frac2.denominator
    return Fraction(numerator, denominator)