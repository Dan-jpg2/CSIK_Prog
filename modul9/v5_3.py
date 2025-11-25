from itertools import accumulate

def cum_union_of(v):
    if not v:
        return []
    result = [set(v[0])]
    for s in v[1:]:
        result.append(result[-1] | s)
    return result

def cum_union_of_1L(v):
    return list(accumulate(v, lambda a, b: a | b))

