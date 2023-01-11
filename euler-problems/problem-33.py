"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct,
is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
# find the four fractions where the numerator and denominator are
# - two digits and
# - the numerator < the denominator
# - the first digit of the numerator is the same as the second digit of the denominator OR
# - the second digit of the numerator is the same as the first digit of the numerator
# - when you remove the matching digits it results in the same value
# largest values possible are 98/99
# smallest values possible are 10/11
# find the 4 fractions, find their product, reduce, return the denominator

from helpers import get_digits
from numpy import prod
from fractions import Fraction

def is_curious(numerator, denominator):
    if numerator == denominator:
        return False
    decimal = numerator/denominator
    nums = get_digits(numerator)
    dens = get_digits(denominator)
    a, b = nums[0], nums[1]
    c, d = dens[0], dens[1]
    if a == d and c != 0:
        return b/c == decimal
    if b == c and d != 0:
        return a/d == decimal

def resulting_denominator():
    numerators = []
    denominators = []
    for numerator in range(10, 99):
        for denominator in range(numerator+1, 100):
            if is_curious(numerator, denominator):
                numerators.append(numerator)
                denominators.append(denominator)
    n = prod(numerators)
    d = prod(denominators)
    f = Fraction(n, d)
    return f.denominator

# test
print(is_curious(49, 98))

# solution
print(resulting_denominator())
