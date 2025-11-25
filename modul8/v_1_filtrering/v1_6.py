def remove_empty(v):
    n = len(v)
    i = 0
    j = 0
    while i < n:
        if v[i] != "":
            v[j] = v[i]
            j = j + 1
        i = i +1 
    del v[j:n]

