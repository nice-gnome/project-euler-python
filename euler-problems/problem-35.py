"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from helpers import is_prime, get_digits, list_to_int

def is_circ_prime(n):
    if not is_prime(n):
        return False    # n is prime so get digits
    digits = get_digits(n)
    for i in range(len(digits)):    # rotate left length - 1 times
        r = list_to_int(digits[i:] + digits[:i])
        if not is_prime(r):
            return False
    return True

def circ_primes_below(limit):
    circ_primes = []
    for n in range(2, limit):
        if is_circ_prime(n):
            circ_primes.append(n)
    return len(circ_primes)

# test
print(is_circ_prime(197))
print(circ_primes_below(100)==13)

# solution
print(circ_primes_below(1000000))