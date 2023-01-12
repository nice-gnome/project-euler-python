"""
Using names.txt a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.

Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list
to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import string
letters = [*string.ascii_uppercase]
names = open("../resources/p022_names.txt").readlines()[0].split(",")
names.sort()

def alpha_score(name):
    name = name.replace('"','')
    return sum([letters.index(char)+1 for char in [*name]])

def total_all_names():
    sum = 0
    i = 1
    for name in names:
        sum += alpha_score(name) * i
        i+=1
    return sum

# test
print(alpha_score("COLIN")==53)
# solution
print(total_all_names())