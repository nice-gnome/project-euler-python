"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
# find bounds:
#   when n = 4
#   upper bound is 4 * 9**4 = 26244
#   lower bound is 2**4 = 16
# upper bound is 5 * 9**5 = 295245
# lower bound is 2**5 = 64

from helpers import get_digits

def is_sum_of_powers(n, power):
    return sum([d**power for d in get_digits(n)]) == n

def sum_powers(power):
    numbers = []
    lower = 2**power
    upper = power * 9**power
    for n in range(lower, upper+1):
        if is_sum_of_powers(n, power):
            numbers.append(n)
    return sum(numbers)

# test
print(is_sum_of_powers(1634, 4))
print(is_sum_of_powers(8208, 4))
print(is_sum_of_powers(9474, 4))
print(sum_powers(4)==19316)

# solution
print(sum_powers(5))