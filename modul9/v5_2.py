from itertools import accumulate

def cum_max_of(v):
    if not v:
        return[]
    result = [v[0]]
    for x in v[1:]:
        result.append(max(result[-1], x))
    return result

def cum_max_of_1L(v):
    return list(accumulate(v, lambda a, b: max(a,b)))
