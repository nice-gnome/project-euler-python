"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from helpers import is_prime, get_primes

# p + 2 * i^2
# p has to be a prime < n
# i is < n

def has_property(n):
    primes = get_primes(n)
    for p in primes:
        for i in range(1, n):
            if n == p + 2 * i**2:
                return True
    return False

def odd_comp():
    found = False
    n = 35
    while not found:
        if not is_prime(n):
            if not has_property(n):
                return n
        n += 2

# test
print(has_property(33))

# solution
print(odd_comp())