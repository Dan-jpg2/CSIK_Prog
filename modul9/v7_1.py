
#Ny liste
def reverse_of(lst):
    return lst[::-1]

#In-place
def reverse(lst):
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n-1-i] = lst[n-1-i], lst[i]