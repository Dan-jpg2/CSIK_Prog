# Definition
# def positives_of(v):
#    result = []
#    n = len(v)
#    i = 0
#    while i < n:
#        if v[i] > 0:                   
#            result.append(v[i])
#        i = i + 1
#    return result

#omskrevet version her ved brug af 'filter

def positives_of(v):
    return list(filter(lambda x: x > 0, v))

