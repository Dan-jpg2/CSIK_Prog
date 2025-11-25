def vector_min_of(a, b):
    n = len(a)
    result = [None] * n
    i = 0
    while i < n:
        result[i] = min(a[i], b[i])
        i += 1
    return result

v, b = [-5, 40, 20], [10, 25, 8]
print(v)
print (b)
print(vector_min_of(v, b))

# one liner
def vector_min_of_1L(a, b):
    return [min(x,y) for x, y in zip(a,b)]

