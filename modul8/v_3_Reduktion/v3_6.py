# Kan vi undgå at løbe hele listen igennem i opgave 4 og 5?
# Ja det kan vi godt


# Opgave 4 kode som er redigeret her:

def all_of(v):
    # Fjerner denne del: result = True
    n = len(v)
    i = 0
    while i < n:
        # Fjernet denne del "result = result and v[i]""
        if not v[i]: #Hvis ét element er False kan vi stoppe
            return False
        i = i + 1
    return True # Ændret til True da vi kun er interesseret i hvis der ingen False er

# Opgave 5 kode som er redigeret her:

def any_of(v):
    # result = False -- Fjernet
    n = len(v)
    i = 0
    while i < n:
        if v[i]:
            return True
        # result = result or v[i] -- Overflødigt som før
        i = i + 1
    return False # Hvis ingen var true