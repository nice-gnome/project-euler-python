"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
from helpers import divisors, is_prime

def distinct_primes(n):
    return sum([is_prime(x) for x in set(divisors(n))])

def first_with_distinct(d):
    dps = []
    n = 0
    while dps[-d:] != [d] * d:  # check if last d elements are d
        n += 1
        dps.append(distinct_primes(n))
    return n - (d-1)

# test
print(distinct_primes(14)==2)
print(distinct_primes(644)==3)
print(first_with_distinct(2)==14)
print(first_with_distinct(3)==644)

# solution
print(first_with_distinct(4))