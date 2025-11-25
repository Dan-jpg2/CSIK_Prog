def all_of(v):
    result = True
    n = len(v)
    i = 0
    while i < n:
        result = result and v[i]
        i = i + 1
    return result 

