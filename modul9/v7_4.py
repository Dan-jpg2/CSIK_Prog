

def partial_sort(x, values, start = 0, end=None):
    if end is None:
        end = len(values)
    red     = []
    white   = []
    blue    = []
    for i in range(start, end):
        v = values[i]
        if v < x:
            red.append(v)
        elif v == x:
            white.append(v)
        else:
            blue.append(v)

    values[start:end] = red + white + blue
    w = start + len(red)
    b = w + len(white)
    return(w, b)
