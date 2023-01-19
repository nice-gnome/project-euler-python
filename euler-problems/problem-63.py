# The 5-digit number, 16807=7^5, is also a fifth power. 
# Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

def count_nth_power():
    count = 0
    for n in range(1,10):
        for p in range(1, 23):
            if len(str(n**p))==p:
                count += 1
    return count

# solution
print(count_nth_power())