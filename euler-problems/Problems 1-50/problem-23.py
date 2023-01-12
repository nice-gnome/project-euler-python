"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

# if the difference of the number we're examining and every number in the set
# is in the set, then the number is the sum of two abundant numbers.
# otherwise, we must add it to our sum in question.
# if not any((n - a in abn) for a in abn):

# initiate new sum = 0
# initiate a new set called abundant
# iterate from 1 to limit (20162)
# for each n
# if n is abundant add to set
# if all solutions to n - a for all a in abundant
# then don't add n to sum
# otherwise add n to sum

from helpers import divisors

def is_abundant(n):
    d = divisors(n)
    d.pop()
    return sum(d) > n

def sum_cannot():
    sum = 0
    abundant = set()
    for n in range(1, 20162):
        if is_abundant(n):
            abundant.add(n)
        if not any((n - a in abundant) for a in abundant):
            sum += n
    return sum

# test
print(is_abundant(12))
print(is_abundant(16))

# solution
print(sum_cannot())