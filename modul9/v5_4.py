
# Mønstret er:
# Reduktion (x_of) producerer ét resultat.
# Kumulation (cum_x_of) producerer alle de delvise resultater.

# Dette er en MEGET GENEREL kumulations funktion som tager en binær funktion (lambda)
# og et initialt input

# Vi kan udtrykke det generelle mønster som en funktion, der tager et kombinationsudtryk (lambda) som argument.
# Denne funktion kan så udføre kumulation for enhver type operation (sum, max, union osv.).
def cumulate(v, combine):
    """ Generel kumulationsfunktion.
        combine skal være en funktion med to argumenter (akkumulator, element)."""
    result = []
    if not v:
        return result

    acc = v[0]
    result.append(acc)
    i = 1
    while i < len(v):
        acc = combine(acc, v[i])
        result.append(acc)
        i += 1
    return result

#kumuleret sum
def cum_sum_of(v):
    return cumulate(v, lambda a, b: a + b)

def cum_max_of(v):
    return cumulate(v, lambda a, b: a if a > b else b)

def cum_union_of(v):
    return cumulate(v, lambda a, b: a | b)


