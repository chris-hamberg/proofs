from fractions import Fraction

def power(n, x):
    exponent, product = abs(n), 1
    while exponent > 0:
        product *= x
        exponent -= 1
    if n < 0:
        product = Fraction(1, product)
    return product
