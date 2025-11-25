# Quick sort in place bruger partial sort rekurssivt

from random import randrange
from v7_4 import partial_sort

def quick_sort(values, start = 0, end=None):
    if end is None:
        end = len(values)
    if end - start <= 1:
        return # Allerede sorteret 
    
    pivot_index = randrange(start, end)
    pivot = values[pivot_index]
    w, b = partial_sort(pivot, values, start, end)
    quick_sort(values, start, w)
    quick_sort(values, b, end)


v = [4, 2, 5, 8, 9, 9, 11, 3, 1]
print(v)
quick_sort(v)
print(v)
print(sorted(v))