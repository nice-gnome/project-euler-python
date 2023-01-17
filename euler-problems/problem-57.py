def num_numerator_greater():
    count = 0
    n = 1
    d = 1
    np = 10
    dp = 10
    for i in range(1000):
        n, d = 2 * d + n, d + n
        if n >= np:
            np *= 10
        if d >= dp:
            dp *= 10
        if np > dp:
            count += 1
    return count


# solution
print(num_numerator_greater())
