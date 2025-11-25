def lengths(v):
    n = len(v)
    result = [None] * n
    i = 0
    while i < n:
        result[i] = len(v[i])
        i = i + 1
    return result

