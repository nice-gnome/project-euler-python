"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.

If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from itertools import permutations as perm

def get_perm(limit, n):
    p = perm(range(limit+1))
    a = [*p]
    b = a[n-1]
    s = [str(d) for d in b]
    sol = int(','.join(s).replace(',', ''))
    return sol

# test
print(get_perm(2,6)==210)

# solution
print(get_perm(9,1000000))