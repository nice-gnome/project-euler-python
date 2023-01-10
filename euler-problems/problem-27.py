"""
given quadratic formula:
n**2 + a*n + b
where |a| and |b| are integers <= 1000
Find the product of a and b,
for the quadratic expression that produces the maximum number of primes for consecutive values of n,
starting with 0.
"""
# for n = 0 to be prime b must be prime

from helpers import is_prime, get_primes

def max_prod():
    b_primes = get_primes(1000)
    max_prod = 0
    max_primes = 0
    for a in range(-999, 1001):
        for b in b_primes:
            prime_count = 0
            n = 0
            while is_prime(n ** 2 + a * n + b):
                n += 1
                prime_count += 1
            if prime_count > max_primes:
                max_primes = prime_count
                max_prod = a * b
    return max_prod

# solution
print(max_prod())