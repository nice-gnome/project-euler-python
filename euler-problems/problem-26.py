"""
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
# set solution = 1
# set max_length = 1
# iterate n from 3 to 999 increasing by 2 (don't check evens)
# skip if divisible by 5
# set l = 1 to count length of repetend
# check if (10 ** l) % n is 1
# if it is, then l is repetend for n
# if l > max_length set max_length = l and solution = n
# if not, increase l by 1 and repeat check
# return solution

def max_rep(limit):
    solution = 1
    max_length = 1
    for n in range(3, limit, 2):
        if n % 5 == 0:
            continue
        l = 1
        while (10 ** l) % n != 1:
            l += 1
        if l > max_length:
            max_length = l
            solution = n
    return solution


# solution
print(max_rep(1000))