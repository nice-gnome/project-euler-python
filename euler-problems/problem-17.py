"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
from num2words import num2words as nw

def letter_count(n):
    a = nw(n)
    a = a.replace("-","")
    a = a.replace(" ","")
    return len(a)

def total_letter_count(n):
    sum = 0
    for i in range(1,n+1):
        sum += letter_count(i)
    return sum

# test
print(total_letter_count(5)==19)
print(letter_count(342)==23)
print(letter_count(115)==20)

# solution
print(total_letter_count(1000))