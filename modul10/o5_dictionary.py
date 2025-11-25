N = 7

def create():
    '''Creates and returns an empty dictionary.'''
    d = []
    i = 0
    while i < N:
        d.append([])
        i += 1
    return d


def set_entry(d, key, value):
    '''Adds or updates an entry in the dictionary d.

    If an entry with the given key already exists,
    the old value of that entry is replaced by the
    given value and the old value is returned.

    If not, a new entry is added, and None is returned.
    '''
    index = hash(key) % N
    bucket = d[index]
    i = 0
    while i < len(bucket):
        k, v = bucket[i]
        if k == key:
            old_value = v
            bucket[i] = (key, value)
            return old_value
        i += 1
    bucket.append((key, value))
    return None


def lookup_entry(d, key):
    '''Looks up an entry in the dictionary d.
    
    Returns the value associated to the given key,
    or None, if there is no such entry.
    '''
    index = hash(key) % N
    bucket = d[index]
    i = 0
    while i < len(bucket):
        k, v = bucket[i]
        if k == key:
            return v
        i += 1
    return None


def delete_entry(d, key):
    '''Deletes an entry in the dictionary d.
    
    Returns the value associated to the given key,
    or None, if there is no such entry.
    '''
    index = hash(key) % N
    bucket = d[index]
    i = 0
    while i < len(bucket):
        k, v = bucket[i]
        if k == key:
            del bucket[i]
            return v
        i += 1
    return None


def clear(d):
    '''Deletes all entries in the dictionary d.'''
    i = 0
    while i < N:
        d[i] = []
        i += 1


def keys(d):
    '''Returns the keys of the dictionary d.

    The returned list is a detached snapshot of the current
    keys.
    '''
    result = []
    i = 0
    while i < N:
        bucket = d[i]
        j = 0
        while j < len(bucket):
            k, v = bucket[j]
            result.append(k)
            j += 1
        i += 1
    return result
