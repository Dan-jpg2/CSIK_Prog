
def vector_sum_of(a, b):
    n = len(a)
    result = [None] * n
    i = 0
    while i < n:
        result[i] = a[i] + b[i]
        i += 1
    return result

# one liner
def vector_sum_of_1L(a, b):
    return [x + y for x, y in zip(a, b)]

