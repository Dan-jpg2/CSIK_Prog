def positives_of(v):
    result = []
    n = len(v)
    i = 0
    while i < n:
        if v[i] > 0:                    #vi vil kun have positive tal
            result.append(v[i])
        i = i + 1
    return result

def squared(v):
    n = len(v)
    result = [None] * n
    i = 0
    while i < n:
        result[i] = v[i] * v[i]
        i = i + 1
    return result

# definition
def sum_of(v):
    total = 0
    n = len(v)
    i = 0
    while i < n:
        total = v[i] + total 
        i = i + 1
    return total 


v = [3, -2, 7, 1, -4]

print(sum_of(squared(positives_of(v))))
