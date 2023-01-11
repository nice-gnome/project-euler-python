"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
from itertools import permutations as perm
from helpers import list_to_int

def has_property(digits):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        chk = list_to_int(digits[i:i+3])
        if chk % primes[i-1] != 0:
            return False
    return True

def sum_sub_pans():
    pd = [*range(0,10)]
    perms = [[*p] for p in [*perm(pd)]]
    sum = 0
    for p in perms:
        if has_property(p):
            sum += list_to_int(p)
    return sum

# test
print(has_property([1, 4, 0, 6, 3, 5, 7, 2, 8, 9]))

# solution
print(sum_sub_pans())