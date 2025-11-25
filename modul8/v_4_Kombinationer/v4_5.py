from functools import reduce

#denne function er til generel reduction men skal importeres som set.
# Bug den til at omskrive en opgave fra v3 til one liner

#Vi bruger her v3_1

def sum_of(v):
    return reduce(lambda acc, x: acc + x, v, 0)

# reduce(function, iterable, initializer) reducerer listen ét element ad gangen:
# acc er den akkumulerede værdi (starter ved 0 her).
# x er det næste element i listen.
# lambda acc, x: acc + x betyder, at vi lægger elementet x til summen acc.
# reduce går igennem hele listen og returnerer ét samlet resultat.

def concat_of(v):
    return reduce(lambda acc, x: acc + x, v, "")

# samme kan gøres for tekststrenge, men her er 'acc' bare vores akkumulerede tekststreng.