def seperated_sum_of(v):
    pos = 0
    neg = 0
    i = 0
    n = len(v)
    while i < n:
        if v[i] > 0:
            pos = pos + v[i]
        else:
            neg = neg + v[i]
        
        i = i + 1
    return pos, neg

v = [2, 3, 2, 3]

print(seperated_sum_of(v))

