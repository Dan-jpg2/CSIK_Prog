def non_empty_of(v):
    result = []
    n = len(v)
    i = 0
    while i < n:
        if v[i] != "":
            result.append(v[i])
        i = i + 1
    return result

