# The primes 3, 7, 109, and 673, are quite remarkable.
#  
# By taking any two and concatenating them in any order 
# the result will always be prime. 
# 
# For example, taking 7 and 109, both 7109 and 1097 are prime. 
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from helpers import is_prime, get_digits, list_to_int, get_primes

def concats_prime(n, p):
    nd = get_digits(n)
    pd = get_digits(p)
    return is_prime(list_to_int(nd+pd)) and is_prime(list_to_int(pd+nd))

def sum_five_primes():
    primes = get_primes(10000)
    for a in primes:
        for b in primes:
            if b < a:
                continue
            if concats_prime(a, b):
                for c in primes:
                    if c < b:
                        continue
                    if concats_prime(a, c) and concats_prime(b, c):
                        for d in primes:
                            if d < c:
                                continue
                            if concats_prime(a, d) and concats_prime(b, d) and concats_prime(c,d):
                                for e in primes:
                                    if e < d:
                                        continue
                                    if concats_prime(a, e) and concats_prime(b, e) and concats_prime(c, e) and concats_prime(d, e):
                                        return a+b+c+d+e


# test
# print(concats_prime(3, 673))
# print(concats_prime(5, 673)==False)

# solution
print(sum_five_primes())