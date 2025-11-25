def any_of(v):
    result = False
    n = len(v)
    i = 0
    while i < n:
        result = result or v[i]
        i = i + 1
    return result 

