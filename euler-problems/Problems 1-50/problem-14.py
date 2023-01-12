"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
# to avoid recalculating sequences
# create a dictionary where
# keys are integers and values are lists with the corresponding hailstone sequence

def longest_chain_producer():
    sequences = dict()
    # iterate for all positive integers from 1 to 999,999
    for i in range(1, 10**6):
        n = i
        sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            if n in sequences:
                sequence = sequence + sequences[n]
                n = 1
            else:
                sequence.append(int(n))
        sequences[i] = sequence
    return max(sequences, key=lambda x: len(sequences[x]))

# solution
print(longest_chain_producer())
