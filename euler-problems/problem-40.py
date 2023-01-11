"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def champ_prod():
    w = ''
    n = 1
    while len(w) < 1000000:
        print(n)
        w += str(n)
        n += 1
    return int(w[0]) * int(w[9]) * int(w[99]) * int(w[999]) * int(w[9999]) * int(w[99999]) * int(w[999999])

# solution
print(champ_prod())