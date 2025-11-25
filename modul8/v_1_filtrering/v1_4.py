def every_second_char_of(v):
    result = []
    n = len(v)
    i = 0
    while i < n:
        if i % 2 == 0:          # hvert andet tegn fra indeks 0
            result.append(v[i])
        i = i + 1
    return result
