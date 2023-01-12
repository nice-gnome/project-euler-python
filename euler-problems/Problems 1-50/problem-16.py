"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""
def sum_digits(n):
    return sum([int(d) for d in str(n)])

# test
print(sum_digits(2**15)==26)

# solution
print(sum_digits(2**1000))