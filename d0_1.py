# Opgave 1 - 

"""source = [42, 87, 13, 16, 36, 25]
stream = iter(source)
stream2 = iter(source)
print(next(stream))     #42
print(next(stream2))    #42
print(next(stream2))    #87
print(next(stream2))    #13
print(next(stream))     #87
print(next(stream))     #13
print(next(stream))     #16"""

# Opgave 2 - Kalde iter 2 gange på samme vektor.

# Er de uafhængige, eller påvirker de hinanden? 
# De er uafhængige og påvirker ikke hinanden. 

# Opgave 3 - Er tupler iterables i Python? Er tekststrenge? Hvad med ordbøger? Hvad med tal?
# Hvor svaret er "ja" -- hvad består datastrømmene så af?
# Det eneste der ikke er iterables er tal (int osv.)
# Datastrømmen består af de første elementer. startene fra v[0]. Men i tekststrenge kommer " tegnet ikke med. 
# Ved ordbøger er det key der bliver printet. 

"""source = [123, 234]  #Iterable
source1 = "hej, med, dig" #Iterable
source2 = (123, 234, 567) #Iterable
source3 = {1: "hej", 2:"test"} #Iterable
source4 = 125 #Ikke Iterable
stream = iter(source)
print(next(stream))
print(next(stream))
print(next(stream))
print(next(stream))"""

# Opgave 4

#While løkke til at behandle alle data-elementerne i en data strøm
"""source = []
stream = iter(source)
while True:
    try:
        x = next(stream)
        # do something with x
    except StopIteration:
        break"""

#Smartere måde at gøre det påå såfremt at source er en iterabel
"""
source = {"land": [str("dk"), ' uk '], "by": "odense", "region": "midtjylland"}
for x in source:
    print(source[x])
"""
    


# opgave 5
"""source = [42, 87, 13, 16, 36, 25]
stream = iter(source)
next(stream)
next(stream)
for x in stream:
    print(x)
"""
# Laver source som en vektor af tal.
# Stream bliver så en iterable over vores vektor
# Vi kalder next 2 gange, så vi får 42 og så 87.
# Ind i en for-løkke hvor vi kører over det der er i stream (fra 13 af) og printer værdien ud
# Derfor starter vi fra 13 af. 


#Opgave 6 - Omskriv to tidligere funktioner
# Har her bare taget en random funktion og omskrevet den i begge tilfælde
"""
    def greater_than_10(v):
    i = 0
    count = 0
    while i < len(v):
        if v[i] > 10:
            count += 1
        i += 1
    return count
"""

""" 
    def greater_than_10(v):
    count = 0
    for x in v:
        if x > 10:
            count += 1
    return count
"""

# Opgave 7 
"""
def my_generator():
    yield 42
    print("hej")
    yield 87
    yield 13
    yield 16
    yield 36
    yield 25

stream = my_generator()
print(next(stream))
print(next(stream))
print(next(stream))
print(next(stream))
print(next(stream))
print(next(stream)) """

# Opgave 8
def stream_from(v):
    i = 0
    while i < len(v):
        yield v[i]
        i += 1

source = [42, 87, 13, 16, 36, 25]
stream = stream_from(source)

print(next(stream))
print(next(stream))
print(next(stream))
print(next(stream))
print(next(stream))
print(next(stream))
print("\n")

for x in stream_from([1, 2, 3]):
    print(x)
    
