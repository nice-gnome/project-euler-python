"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
import helpers

def prime_at(n):
    primes = []
    i = 2
    while len(primes) < n:
        if helpers.is_prime(i):
            primes.append(i)
        i += 1
    return primes.pop()

# tests
print(prime_at(6)==13)

# solution
print(prime_at(10001))