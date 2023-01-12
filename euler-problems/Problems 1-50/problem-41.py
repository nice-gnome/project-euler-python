"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from helpers import is_prime, list_to_int
from itertools import permutations as perm

def max_pan_prime():
    for d in range(9, 0, -1):
        pd = [*range(1, d+1)]
        perms = [list_to_int(p) for p in [*perm(pd)]]
        perms.sort(reverse=True)
        for p in perms:
            if is_prime(p):
                return p

# solution
print(max_pan_prime())