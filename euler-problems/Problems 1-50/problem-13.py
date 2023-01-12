"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
(Numbers in resources)
"""
def first_ten():
    numbers = open("../resources/problem-13-numbers.txt", "r")
    sum = 0
    for line in numbers:
        sum += int(line)
    return str(sum)[:10]

# solution
print(first_ten())