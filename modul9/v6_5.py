def merge_of(a, b):
    i, j = 0, 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # Tilføj evt. rester fra den ene liste
    result.extend(a[i:])
    result.extend(b[j:])
    return result


