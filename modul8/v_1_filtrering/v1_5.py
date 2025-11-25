def remove_negatives(v):
    n = len(v)
    i = 0
    j = 0
    while i < n:
        if v[i] >= 0:
            v[j] = v[i]
            j = j + 1
        i = i +1 
    del v[j:n]

