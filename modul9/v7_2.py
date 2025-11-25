from random import randrange

def shuffle(lst):
    n = len(lst)
    for i in range(n-1, 0, -1):
        j = randrange(i + 1)
        lst[i], lst[j] = lst[j], lst[i]


a = [1, 2, 3, 4, 5, 6]
shuffle(a)
print(a)
print(sorted(a))