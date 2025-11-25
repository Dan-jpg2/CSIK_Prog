def avg_of(v):
    if len(v) == 0:
        raise ValueError ("Empty vector string")
    total = 0

    i = 0
    n = len(v)
    while i < n:
        total = total + v[i]
        i = i + 1
    return total / n

print(avg_of([-2, -4, 2, -3]))