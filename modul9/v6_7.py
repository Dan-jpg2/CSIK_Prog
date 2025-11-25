from v6_4 import vector_prod_of

# Vi skal bruge 2 funktioner, nævnligt:
#       vector_prod_of  (produkt pr element)
#       sum_of          (sum af produkterne)

#Vi kan derfor skrive sum_of(vector_prod_of(a, b))

def sum_of(v):
    total = 0
    for x in v:
        total += x
    return total

def dot_product_of(a, b):
    return sum_of(vector_prod_of(a, b))

# Kunne også bare lave en 1 liner i stedet....

def dot_product_of_1L(a, b):
    return sum(x * y for x, y in zip(a,b))