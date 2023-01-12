"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
def pandigital_prod():
    products = set()
    bounds = range(1,10000)
    pandigital = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    for a in bounds:
        for b in bounds:
            c = a*b
            digits = str(a) + str(b) + str(c)
            if len(digits) == 9:
                if sorted(digits) == pandigital:
                    products.add(c)
    return sum(products)

# solution
print(pandigital_prod())