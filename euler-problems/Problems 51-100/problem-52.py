"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

from helpers import get_digits

def has_multiples(n):
    digits = get_digits(n)
    digits.sort()
    for i in range(2, 7):
        mult = n * i
        md = get_digits(mult)
        md.sort()
        if md != digits:
            return False
    return True

def perm_multiples():
    found = False
    n = 1
    while not found:
        if has_multiples(n):
            return n
        n += 1

# solution
print(perm_multiples())