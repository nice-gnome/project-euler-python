"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
# largest pandigital number is 987654321
# multiplier x must be <= 4 digits long because n must be at least 2
#   (x can't be 5 digits because that would result in more than 9 concantenated)
#
# check all multiplier possibilities 2 to 9999

def is_pandigital(t):
    return sorted(t) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def largest_pandigital():
    largest = 0
    for x in range(2, 10000):
        t = ''
        for n in range(1, 10):
            t += str(x * n)
            if is_pandigital(t):
                c = int(t)
                if c > largest:
                    largest = c
    return largest

# test
print(is_pandigital('192384576'))

# solution
print(largest_pandigital())

