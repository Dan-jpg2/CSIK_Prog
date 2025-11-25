from functools import reduce
# Filter med seperat resultat
def Filter_sep_result(v):
    result = []
    n = len(v)
    i = 0
    while i < n:
        if v[i]:# v[i] satisfies some condition:
            result.append(v[i])
        i = i + 1
    return result

# In-Place filtrering
def filter_In_place(v):
    n = len(v)
    i = 0
    j = 0
    while i < n:
        if v[i]: # v[i] satisfies some condition:
            v[j] = v[i]
            j = j + 1
        i = i + 1
    del v[j:n]
#---------------------------------------------#
# Her fra er det opgaver fra V-1 Filtrering #
#---------------------------------------------#
##### V1_1 ----- positives_of #####
#_____Filter med seperat resultat_____#

def positives_of(v):
    result = []
    n = len(v)
    i = 0
    while i < n:
        if v[i] > 0:
            result.append(v[i])
        i = i + 1
    return result

##### V1_2 ----- non_empty_of #####
#_____Filter med seperat resultat_____#
def non_empty_of(v):
    result = []
    n = len(v)
    i = 0
    while i < n:
        if v[i] != "":
            result.append(v[i])
        i = i + 1
    return result

##### V1_3 ----- suspicious_login_attempts_of #####
#_____Filter med seperat resultat_____#
def suspicious_login_attempts_of(v):
    result = []
    n = len(v) 
    i = 0
    while i < n:
        if v[i][1] == 'root' and v[i][2] == False:
            result.append(v[i])
        i = i + 1
    return result

##### V1_4 ----- every_second_char_of #####
#_____Filter med seperat resultat_____#
def every_second_char_of(v):
    result = []
    n = len(v)
    i = 0 
    while i < n:
        if i % 2 == 0:
            result.append(v[i])
        i = i + 1
    return result

##### V1_5 ----- remove_negatives #####
def remove_negatives(v):
    n = len(v)
    i = 0
    j = 0
    while i < n:
        if v[i] >= 0:
            v[j] = v[i]
            j = j + 1
        i = i + 1
    del v[j:n]


##### V1_6 ----- remove_empty #####
def remove_empty(v):
    n = len(v)
    i = 0
    j = 0
    while i < n:
        if v[i] != "":
            v[j] = v[i]
            j = j + 1
        i = i + 1
    del v[j:n]

##### V1_7 ----- remove_every_other #####
def remove_every_other(v): # Kun lige index: 0, 2, 4...

    n = len(v)
    i = 0
    j = 0
    while i < n:
        if i % 2 != 0:
            v[j] = v[i]
            j = j + 1
        i = i + 1
    del v[j:n]

#------------------------------------------#
# Her fra er det opgaver fra V2 Afbildning
#------------------------------------------#

#Afbildning med seperat resultat
def afbildning_sep_result(v):
    n = len(v)
    result = [None] * n
    i = 0
    while i < n:
        result[i] = x # some calculation on v[i]
        i = i + 1
    return result

#Afbildning med In-Place
def afbildning_in_place(v):
    n = len(v)
    i = 0
    while i < n:
        v[i] = x # some calculation on v[i]
        i = i + 1


##### V2_1 ----- doubled ##### sep result
def doubled(v):
    n = len(v)
    i = 0
    result = [None] * n
    while i < n:
        result[i] = 2 * v[i] 
        i = i + 1
    return result

##### V2_2 ----- squared ##### sep result
def squared(v):
    n = len(v)
    i = 0
    result = [None] * n
    while i < n:
        result[i] = v[i]**2
        i = i + 1
    return result

##### V2_3 ----- lengths ##### sep result 
def lengths(v):
    n = len(v)
    i = 0
    result = [None] * n
    while i < n:
        result[i] = len(v[i])
        i = i + 1
    return result

##### V2_4 ----- decrement ##### in-place
def decrement(v):
    n = len(v)
    i = 0
    while i < n:
        v[i] = v[i] - 1
        i = i + 1

##### V2_5 ----- add_danish_vat ##### in-place
def add_danish_vat(v):
    n = len(v)
    i = 0
    while i < n:
        v[i] = v[i] * 1.25
        i = i + 1


##### V2_6 ----- negate ##### in-place
def negate(v):
    n = len(v)
    i = 0
    while i < n:
        v[i] = not v[i]
        i = i + 1
    
#------------------------------------------#
# Her fra er det opgaver fra V3 Reduktion
#------------------------------------------#
# Det giver ikke mening at lave in-place I reduktion

def reduktion_sep_(v):
    variable = []# define some variables to hold the summary of elements of v
    n = len(v)
    i = 0
    while i < n:
        v[i] = variable# update the variables using v[i]
        i = i + 1
    return variable # some combination of the variables

##### V3_1 ----- sum_of ##### sep_result
def sum_of(v):
    total = 0
    n = len(v)
    i = 0
    while i < n:
        total = v[i] + total
        i = i + 1
    return total

##### V3_2 ----- prod_of ##### sep_result
def prod_of(v):
    total = 1
    n = len(v)
    i = 0
    while i < n:
        total = v[i] * total
        i = i + 1
    return total

##### V3_3 ----- concat_of ##### sep_result
def concat_of(v):
    result = ""
    n = len(v)
    i = 0
    while i < n:
        result = result + v[i]
        i = i + 1
    return result

##### V3_4 ----- all_of ##### sep_result
def all_of(v):
    result = True
    n = len(v)
    i = 0
    while i < n:
        result = result and v[i]
        i = i + 1
    return result

##### V3_5 ----- any_of ##### sep_result
def any_of(v):
    result = False
    n = len(v)
    i = 0
    while i < n:
        result = result or v[i]
        i = i + 1
    return result

##### V3_6 ----- ændring til v3_4 og v3_5 #####

def modified_all_of(v):
    # result = True - Er ikkenødvendig
    n = len(v)
    i = 0
    while i < n:
        # result = result and v[i] - Ikke nødvendig
        if not v[i]:
            return False
        i = i + 1
    return True

def modified_any_of(v):
    # result = False - Ikke nødvendigt
    n = len(v)
    i = 0
    while i < n:
        # result = result or v[i] - Ikke nødvendigt
        if v[i]:
            return True
        i = i + 1
    return False

##### v3_7 ----- max_of ##### sep_result
def max_of(v):
    n = len(v)
    if n == 0:
        raise ValueError('Empty vector')
    max_val = v[0]
    # define some variables to hold the summary of elements of v -- initialise using v[0]
    i = 1
    while i < n:
        if v[i] >= max_val:
            max_val = v[i]
        # update the variables using v[i]
        i = i + 1
    return max_val # some combination of the variables

##### V3_8 ----- shortest_of #####
def shortest_of(v):
    n = len(v)
    if n == 0:
        raise ValueError('Empty vector')
    shortest = v[0]
    i = 1
    while i < n:
        if len(v[i]) < len(shortest):
            shortest = v[i]
        i = i + 1
    return shortest

##### V3_9 ----- avg_of #####
def avg_of(v):
    n = len(v)
    if n == 0:
        raise ValueError('Empty vector')
    total = 0
    i = 0
    while i < n:
        total = total + v[i]
        i = i + 1
    return total / n 

##### V3_10 ----- seperated_sum_of #####
def seperated_sum_of(v):
    n = len(v)
    if n == 0:
        raise ValueError('Empty vector')
    pos = 0
    neg = 0
    i = 0
    while i < n:
        if v[i] > 0:
            pos = pos + v[i]
        else:
            neg = neg + v[i]
        i = i + 1
    return pos, neg

#------------------------------------------#
# Her fra er det opgaver fra V4 Kombinationer + Indbyggede funktioner
#------------------------------------------#

##### V4_1 ----- Test sum_of(squared(positives_of())) #####
# Beregningen kører som en test

##### V4_2 ----- summary_of, timestamps_of og root_login_attempts_of #####
def summary_of(logs):
    if len(logs) == 0:
        raise ValueError('List is empty')
    first = logs[0][0]
    last = logs[0][0]
    failures = 0
    successes = 0
    i = 0
    n = len(logs)
    while i < n:
        timestamp, username, success = logs[i]
        last = timestamp
        if success: 
            successes += 1
        else:
            failures += 1
        i = i +1
    return (first, last, failures, successes)

def timestamps_of(logs):
    n = len(logs)
    result = [None] * n
    i = 0
    while i < n:
        result[i] = logs[i][0]
        i = i + 1  
    return result

def root_login_attempts_of(logs):
    result = []
    n = len(logs)
    i = 0
    while i < n:
        timestamp, username, success = logs[i]
        if username == 'root':
            result.append(logs[i])
        i = i + 1
    return result

##### V4_3 ----- Leg med indbyggede funktioner #####
# Done, tjek og videre. Brug dem evt. i 1-liners

##### V4_4 ----- omskriv 2 funktioner med 'filter' og 'map'
# Fra v1_1
def positives_of_1L(v):
    return list(filter(lambda x: x > 0, v))

# Fra v2_1
def doubled_1L(v):
    return list(map(lambda x: x *2, v))

##### V4_5 ----- omskriv 1 funktion fra v3 med 'reduce'
def sum_of_1L(v):
    return reduce(lambda acc, x: acc + x, v, 0)
