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

def divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
    divisors.sort()
    return divisors

def sum_digits(n):
    return sum([int(d) for d in str(n)])
