# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

# The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
# Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.

# This is the only set of 4-digit numbers with this property.

# Find the sum of the only ordered set of six cyclic 4-digit numbers 
# for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, 
# is represented by a different number in the set.

from helpers import get_digits
from itertools import permutations as perm

def get_oct():
    oct = []
    all_found = False
    n = 1
    while not all_found:
        o = n * (3 * n - 2)
        if o > 9999:
            return oct
        if o > 999:
            oct.append(o)
        n += 1

def get_hept():
    hept = []
    all_found = False
    n = 1
    while not all_found:
        h = (n * (5 * n - 3)) // 2
        if h > 9999:
            return hept
        if h > 999:
            hept.append(h)
        n += 1

def get_hex():
    hex = []
    all_found = False
    n = 1
    while not all_found:
        h = n * (2 * n - 1)
        if h > 9999:
            return hex
        if h > 999:
            hex.append(h)
        n += 1

def get_pent():
    pent = []
    all_found = False
    n = 1
    while not all_found:
        p = (n * (3 * n - 1)) // 2
        if p > 9999:
            return pent
        if p > 999:
            pent.append(p)
        n += 1

def get_sqr():
    sqr = []
    all_found = False
    n = 1
    while not all_found:
        s = n ** 2
        if s > 9999:
            return sqr
        if s > 999:
            sqr.append(s)
        n += 1

def get_tri():
    tri = []
    all_found = False
    n = 1
    while not all_found:
        t = (n * (n + 1)) // 2
        if t > 9999:
            return tri
        if t > 999:
            tri.append(t)
        n += 1

def next_possible(n, numbers):
    nd = get_digits(n)[2:]
    possible = []
    for num in numbers:
        if get_digits(num)[:2] == nd and n != num:
            possible.append(num)
    return possible

def sum_cyclic():
    polys = {
        "oct": get_oct(),
        "hept": get_hept(),
        "hex": get_hex(),
        "pent": get_pent(),
        "sqr": get_sqr(),
        "tri": get_tri()
    }
    perms = perm(list(polys.keys()))
    for p in perms:
        #('oct', 'hept', 'hex', 'pent', 'sqr', 'tri')
        for c in polys[p[0]]:
            c1s = next_possible(c, polys[p[1]])
            if len(c1s) == 0:
                continue
            for c1 in c1s:
                c2s = next_possible(c1, polys[p[2]])
                if len(c2s) == 0:
                    continue
                for c2 in c2s:
                    c3s = next_possible(c2, polys[p[3]])
                    if len(c3s) == 0:
                        continue
                    for c3 in c3s:
                        c4s = next_possible(c3, polys[p[4]])
                        if len(c4s) == 0:
                            continue
                        for c4 in c4s:
                            c5s = next_possible(c4, polys[p[5]])
                            if len(c5s) == 0:
                                continue
                            for c5 in c5s:
                                if get_digits(c5)[2:] == get_digits(c)[:2]:
                                    cycle = [c,c1,c2,c3,c4,c5]
                                    print(cycle)
                                    return sum(cycle)

# solution
print(sum_cyclic())
