'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math

def largest_prime_factor(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    # The loop starts at 3
    # and continues as long as i is less than or equal to the square root of n plus 1,
    # incrementing i by 2 each time.
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    if n > 2: factors.append(n)
    last = factors.pop()
    print(last)
    return last

# test
print("pass") if largest_prime_factor(13195) == 29 else print("fail")

#solution
largest_prime_factor(600851475143)