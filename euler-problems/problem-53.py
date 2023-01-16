"""
n choose r = n! / r! * (n - r)! where r <= n
How many, not necessarily distinct, values of n choose r for 1 <= n <= 100, are greater than one-million?
"""

from math import factorial as fact

def n_choose_r(n, r):
    return fact(n) / (fact(r) * fact(n - r))

def total_n_r(limit):
    total = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            if n_choose_r(n, r) > limit:
                total += 1
    return total

# test
print(n_choose_r(5, 3)==10)
print(n_choose_r(23, 10)==1144066)

# solution
print(total_n_r(1000000))