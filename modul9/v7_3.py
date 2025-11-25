# Merge sort som returnere en ny liste
from v6_5 import merge_of

def merge_sort_of(lst):
    if len(lst) <= 1:
        return lst[:]
    mid = len(lst) // 2
    left = merge_sort_of(lst[:mid])
    right = merge_sort_of(lst[mid:])
    return merge_of(left, right) # Bruger merget of fra opgave 6.5


