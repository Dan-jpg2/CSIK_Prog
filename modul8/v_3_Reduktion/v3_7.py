def max_of(v):
    n = len(v)
    if n == 0:
        raise ValueError ("Empty vector")
    max_val = v[0]
    i = 0
    while i < n:
        if v[i] > max_val:
            max_val = v[i]
        i = i + 1
    return max_val


