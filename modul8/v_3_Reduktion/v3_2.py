def prod_of(v):
    total = 1
    n = len(v)
    i = 0
    while i < n:
        total = v[i] * total 
        i = i + 1
    return total 

