"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
from math import factorial

def paths_count(n):
    return factorial(2 * n) // factorial(n) // factorial(n)

# test
print(paths_count(2)==6)

# solution
print(paths_count(20))