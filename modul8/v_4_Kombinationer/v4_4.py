# Python har indbyggede funktioner til generel filtrering og afbildning: 'filter' og 'map'
# Omskriv nogle funktioner fra v-1 og v-2 til 'one-liners' ved brug af 'filter' og 'map'

# Fra v1_1
def positives_of(v):
    return list(filter(lambda x: x > 0, v))

# Fra v2_1
def doubled(v):
    return list(map(lambda x: 2*x , v))

