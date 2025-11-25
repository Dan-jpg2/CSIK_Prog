# a = [('apple', 10), ('banana', 5), ('pear', 8)]
# b = [('banana', 7), ('cherry', 3), ('pear', 2)]

# Resultatet skal så være:

# [('apple', 10), ('banana', 12), ('cherry', 3), ('pear', 10)]


def combined_sales_of(a, b):
    i, j = 0, 0
    result = []
    while i < len(a) and j < len(b):
        prod_a, vol_a = a[i]
        prod_b, vol_b = b[j]
        if prod_a == prod_b:
            result.append((prod_a, vol_a + vol_b))
            i += 1
            j += 1
        elif prod_a < prod_b:
            result.append((prod_a, vol_a))
            i += 1
        else:
            result.append((prod_b, vol_b))
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result

 