def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def get_primes(limit):  # returns list of primes <= n
    primes = []
    for n in range(1, limit+1):
        if is_prime(n):
            primes.append(n)
    return primes

def divisors(n):
    divisors = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return sorted(divisors)

def sum_digits(n):
    return sum([int(d) for d in str(n)])

def get_digits(n):
    return [int(d) for d in str(n)]

def list_to_int(t): # takes list or tuple
    return int(''.join(map(str, t)))