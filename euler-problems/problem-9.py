"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def pythagoreanTriplets(limit):
    c, m = 0, 2

    while c < limit:
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > limit:
                break
            if a+b+c == limit: return a*b*c
        m = m + 1

print(pythagoreanTriplets(1000))