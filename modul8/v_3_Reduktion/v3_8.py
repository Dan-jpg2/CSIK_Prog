def shortest_of(v):
    if len(v) == 0:
        raise ValueError ("Empty vector string")
    shortest_string = v[0]

    i = 1
    n = len(v)
    while i < n:
        if len(v[i]) < len(shortest_string):
            shortest_string = v[i]
        i = i + 1
    return shortest_string








