from itertools import accumulate
def cum_sum_of(v):
    n = len(v)
    if n == 0:
        return []
    result = [0] * n
    result[0] = v[0]
    i = 1
    while i < n:
        result[i] = result[i-1] + v[i]
        i = i + 1
    return result

# Alternativ one-liner 
def cum_sum_of_1L(v):
    return list(accumulate(v))

