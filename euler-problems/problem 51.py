"""
By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""
from helpers import is_prime, get_digits, list_to_int

# n is the result of the replacement
    # so none of the replacements can be
    # a lower value than its counterpart in n
    # because if a lower prime in the family existed
    # it would have already been found
    # a combination can't be one with different values in n
    # so try each unique digit in n

def has_family(n, size):
    digits = get_digits(n)
    for d in digits:    # for each unique digit in n make 10 values with replacements 0-9
        indices = [index for index, x in enumerate(digits) if x == d]
        vals = []
        for i in range(0,10):
            val = digits.copy()
            for ind in indices:
                val[ind] = i
            v = list_to_int(val)
            if v >= n and is_prime(v):
                vals.append(v)
        if len(vals)==size:
            return True
    return False

def first_of_family(size):
    found = False
    n = 1
    while not found:
        if is_prime(n):
            if has_family(n, size):
                return n
        n += 1

# test
print(has_family(13, 6))
print(has_family(56003, 7))
print(first_of_family(6)==13)
print(first_of_family(7)==56003)

# solution
print(first_of_family(8))