# Exactly four continued fractions, for n <= 13, have an odd period.

# How many continued fractions for n <= 10000 have an odd period?

from math import sqrt

def continued_fraction_odd(n):
    mn = 0.0
    dn = 1.0
    a0 = an = int(sqrt(n))
    p = 0
    if a0 != sqrt(n):
        while an != 2 * a0:
            mn = dn * an - mn
            dn = (n - mn**2) / dn
            an = int((a0 + mn) / dn)
            p += 1
    return p % 2 != 0

def count_odd(limit):
    count = 0
    for n in range(1,limit+1):
        if continued_fraction_odd(n):
            count += 1
    return count

# test
print(count_odd(13)==4)

# solution
print(count_odd(10000))