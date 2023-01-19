# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e

from helpers import get_digits

def sum_100th_e():
    e = [2]
    i = 1
    while len(e) < 100:
        e.extend([1, 2 * i, 1])
        i += 1
    
    num = 1
    denom = e.pop()

    for i in e[::-1]:
        denom, num = denom * i + num, denom
    
    return sum(get_digits(denom))

# solution
print(sum_100th_e())