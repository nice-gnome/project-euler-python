"""
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
def f_term_with_digits(digits):
    terms = [1,1]
    while len(str(terms[-1])) < digits:
        terms.append(terms[-1]+terms[-2])
    return len(terms)



# test
print(f_term_with_digits(3)==12)

# solution
print(f_term_with_digits(1000))