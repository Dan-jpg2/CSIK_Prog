def decrement(v):
    n = len(v)
    i = 0
    while i < n:
        v[i] = v[i] - 1
        i = i + 1

v = [2, -3, 4, 0, 1]
decrement(v)
print(v)
