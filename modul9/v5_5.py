
from itertools import accumulate

#Løbende middelværdi 
def cum_avg_of(v):
    if not v:
        return []
    result = []
    total = 0
    for i, x in enumerate(v, start=1):
        total = total + x 
        result.append(total / i)
    return result

