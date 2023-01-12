"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def last_ten(limit):
    series = 0
    for n in range(1, limit+1):
        series += n**n
    return str(series)[-10:]

# test
print(last_ten(10)=='0405071317')

# solution
print(last_ten(1000))