"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_palindromic(n):
    s = str(n)
    if s == s[::-1]:
        b10 = bin(n)
        b = str(b10)[2:]
        return b == b[::-1]
    return False

def sum_pal(limit):
    sum = 0
    for n in range(limit):
        if is_palindromic(n):
            sum += n
    return sum

# test
print(is_palindromic(585))

# solution
print(sum_pal(1000000))