"""
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
"""

from math import sqrt

def is_pentagonal(n):
    return sqrt(24 * n + 1) % 6 == 5

def get_pentagonal(i):
     return i * (3 * i - 1)/2

def minimal_D():
    for j in range(1, 5000):
        for k in range(j+1, 5000):
            pj = get_pentagonal(j)
            pk = get_pentagonal(k)
            if is_pentagonal(pj+pk):
                if is_pentagonal(pk-pj):
                    return pk-pj

# test
print(is_pentagonal(145))
print(get_pentagonal(4)==22)

# solution
print(minimal_D())