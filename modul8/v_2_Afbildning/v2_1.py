#def doubled(v):
#    n = len(v)
#    result = [None] * n
#    i = 0
#    while i < n:
#        result[i] = 2 * v[i]
#        i = i + 1
#    return result

#Omskrevet her med 'map' functionen
def doubled(v):
    return list(map(lambda x: 2 * x, v))

