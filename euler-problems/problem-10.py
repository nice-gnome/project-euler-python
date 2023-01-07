"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import helpers

def sum_primes(n):
    x = 2
    s = 0
    while x < n:
        if helpers.is_prime(x):
            s += x
        x += 1
    return s

# test
print(sum_primes(10)==17)

# solution
print(sum_primes(2000000))