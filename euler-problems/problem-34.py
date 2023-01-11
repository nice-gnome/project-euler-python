"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
# lower bound is 3
# upper bound is 1499999

from math import factorial
from helpers import get_digits

def is_curious(n):
    return sum(factorial(x) for x in get_digits(n)) == n

def sum_curious():
    sum = 0
    for n in range(3, 1500000):
        if is_curious(n):
            sum += n
    return sum

# test
print(is_curious(145))

# solution
print(sum_curious())