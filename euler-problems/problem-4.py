"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def largest_palindrome(n):
    palindromes = []
    for x in range(n, 1, -1):
        for y in range(n, 1, -1):
            if is_palindrome(x*y):
                palindromes.append(x*y)
    return max(palindromes)

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

# test
print("pass") if largest_palindrome(99) == 9009 else print("fail")

# solution
print(largest_palindrome(999))