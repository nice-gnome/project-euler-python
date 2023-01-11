"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from math import sqrt

def num_solutions(p):
    solutions = set()
    for a in range(1, p//2):
        for b in range(1, p//2):
            c = sqrt(a**2 + b**2)
            if a + b + c == p:
                s = [a,b,c]
                s.sort()
                solutions.add(tuple(s))
    return len(solutions)

def max_solutions(limit):
    max_sol = 0
    solution = 0
    for p in range(1, limit):
        num_sol = num_solutions(p)
        if num_sol > max_sol:
            max_sol = num_sol
            solution = p
    return solution

# test
print(num_solutions(120)==3)

# solution
print(max_solutions(1000))