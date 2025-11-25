def add_danish_vat(v):
    n = len(v)
    i = 0
    while i < n:
        v[i] = v[i] * 1.25
        i = i + 1

