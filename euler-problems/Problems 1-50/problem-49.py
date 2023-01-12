"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from helpers import is_prime, get_digits, list_to_int
from itertools import permutations as perm

def has_property(n):
    if is_prime(n):
        perms = [list_to_int(x) for x in [*perm(get_digits(n))]]
        n2 = n + 3330
        if is_prime(n2) and n2 in perms:
            n3 = n2 + 3330
            return is_prime(n3) and n3 in perms
    return False

def other_answer():
    for n in range(1000, 10000):
        if has_property(n) and n != 1487:
            return str(n) + str(n+3330) + str(n+6660)

# test
print(has_property(1487))
print(has_property(1009)==False)

# solution
print(other_answer())