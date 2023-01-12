"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
# find the longest sequence of primes under limit that sum to a prime

from helpers import get_primes, is_prime

def max_prime(limit):
    primes = get_primes(limit)
    prime_sums = [0]
    for prime in primes:
        last_sum = prime_sums[-1]
        if last_sum + prime <= limit:
            prime_sums.append(last_sum + prime)
    max_terms = 1
    num_sums = len(prime_sums)
    p = 0
    for i in range(num_sums):
        for j in range(num_sums - 1, max_terms + i, -1):
            n = prime_sums[j] - prime_sums[i]
            if j - i > max_terms and is_prime(n):
                max_terms = j - i
                p = n
    return p

# test
print(max_prime(100)==41)
print(max_prime(1000)==953)

# solution
print(max_prime(1000000))

