"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from helpers import divisors

def sum_proper_divisors(n):
    d = divisors(n)
    d.pop()
    return sum(d)

def sum_all_amicable(n):
    amicable = set()
    for i in range(2,n):
        a = sum_proper_divisors(i)
        b = sum_proper_divisors(a)
        if b == i and a != b:
            amicable.add(a)
            amicable.add(b)
    return sum(amicable)

# test
print(sum_proper_divisors(220)==284)
print(sum_proper_divisors(284)==220)

# solution
print(sum_all_amicable(10000))