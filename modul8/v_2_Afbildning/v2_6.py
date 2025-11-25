def negate(v):
    n = len(v)
    i = 0
    while i < n:
        v[i] = not v[i]
        i = i + 1

