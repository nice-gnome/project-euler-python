"""
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits
from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from helpers import is_prime, get_digits, list_to_int

def is_trunctable(n):
    if is_prime(n):
        digits = get_digits(n)
        for i in range(1, len(digits)):  # left to right
            t = list_to_int(digits[i:])
            if not is_prime(t):
                return False
        for i in range(len(digits)-1, 0, -1):   # right to left
            t = list_to_int(digits[:i])
            if not is_prime(t):
                return False
        return True
    return False

def sum_trunctable():
    primes = set()
    n = 8
    while len(primes) < 11:
        if is_trunctable(n):
            primes.add(n)
        n += 1
    return sum(primes)

# test
print(is_trunctable(3797))

# solution
print(sum_trunctable())
