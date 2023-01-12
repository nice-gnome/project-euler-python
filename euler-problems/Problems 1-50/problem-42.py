"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
"""
import string

def num_triangle_words():
    letters = [*string.ascii_uppercase]
    f = open("../resources/p042_words.txt", "r")
    all_words = f.read()
    f.close()
    raw_words = all_words.split(",")
    words = [s.replace('"','') for s in raw_words]
    scores = []
    for word in words:
        scores.append(sum([letters.index(char) + 1 for char in [*word]]))
    tri_num = [1]
    inc = 2
    while tri_num[-1] < max(scores):
        tri_num.append(tri_num[-1] + inc)
        inc += 1
    count = 0
    for score in scores:
        if score in tri_num:
            count += 1
    return count

# solution
print(num_triangle_words())