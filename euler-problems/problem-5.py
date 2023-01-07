"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def smallest_divisible(n):
    candidate = n
    solution_found = False
    while not solution_found:
        if all(candidate % i == 0 for i in range(1, n+1)):
            return candidate
        else:
            candidate += n

# test
print("pass") if smallest_divisible(10) == 2520 else print("fail")

# solution
print(smallest_divisible(20))