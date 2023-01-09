"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
from math import factorial
from helpers import sum_digits

def sum_digits_factorial(n):
    return sum_digits(factorial(n))

# test
print(sum_digits_factorial(10)==27)

# solution
print(sum_digits_factorial(100))