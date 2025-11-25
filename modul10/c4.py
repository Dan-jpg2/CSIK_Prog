class Dictionary:
    """Associates a set of unique keys with values. Supports typical dictionary operations in a Pythonic way."""

    def __init__(self):
        self._size = 0
        self._v = [[] for _ in range(7)]

    # ---------------------------
    # Interne hjælpefunktioner
    # ---------------------------
    def _bucket_index(self, key):
        return hash(key) % len(self._v)

    def _resize(self, new_capacity):
        new_capacity = max(1, new_capacity)
        old_items = [item for bucket in self._v for item in bucket]
        self._v = [[] for _ in range(new_capacity)]
        for key, value in old_items:
            index = hash(key) % new_capacity
            self._v[index].append((key, value))

    def _maybe_grow(self):
        if self._size > len(self._v):
            self._resize(len(self._v) * 2)

    def _maybe_shrink(self):
        if self._size < len(self._v) // 4 and len(self._v) > 1:
            self._resize(len(self._v) // 2)

    def _find_in_bucket(self, bucket, key):
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return i
        return None

    # ---------------------------
    # Public API / Pythonic dunder methods
    # ---------------------------
    # Til d1[key] = value
    def __setitem__(self, key, value):
        idx = self._bucket_index(key)
        bucket = self._v[idx]
        i = self._find_in_bucket(bucket, key)
        if i is not None:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))
            self._size += 1
            self._maybe_grow()

    # Til value = d1[key]
    def __getitem__(self, key):
        idx = self._bucket_index(key)
        bucket = self._v[idx]
        i = self._find_in_bucket(bucket, key)
        if i is None:
            return None  # Som i testen: d0['a'] # None
        return bucket[i][1]

    # Til del d1[key]
    def __delitem__(self, key):
        idx = self._bucket_index(key)
        bucket = self._v[idx]
        i = self._find_in_bucket(bucket, key)
        if i is None:
            raise KeyError(key)
        del bucket[i]
        self._size -= 1
        self._maybe_shrink()

    # Til key in d1
    def __contains__(self, key):
        idx = self._bucket_index(key)
        bucket = self._v[idx]
        return self._find_in_bucket(bucket, key) is not None

    # Til bool(d1)
    def __bool__(self):
        return self._size > 0

    # Til len(d1)
    def __len__(self):
        return self._size

    # Til str(d1) og print(d1)
    def __str__(self):
        items = {k: v for bucket in self._v for k, v in bucket}
        return str(items)

    # Til repr(d1)
    def __repr__(self):
        items = {k: v for bucket in self._v for k, v in bucket}
        return repr(items)

    # Iteration: for key in d1
    def __iter__(self):
        for bucket in self._v:
            for k, v in bucket:
                yield k

    # Til d1 == d2
    def __eq__(self, other):
        if not isinstance(other, Dictionary):
            return False
        self_items = {k: v for bucket in self._v for k, v in bucket}
        other_items = {k: v for bucket in other._v for k, v in bucket}
        return self_items == other_items

    # Til d1 | d2
    def __or__(self, other):
        if not isinstance(other, Dictionary):
            return NotImplemented
        new_dict = Dictionary()
        # Tilføj først alle fra self
        for bucket in self._v:
            for k, v in bucket:
                new_dict[k] = v
        # Tilføj/overskriv med values fra other
        for bucket in other._v:
            for k, v in bucket:
                new_dict[k] = v
        return new_dict


d0 = Dictionary()
d1 = Dictionary()
d2 = Dictionary()
d3 = Dictionary()
d4 = Dictionary()

# Opgave 1
d1['a'] = 7
d2['dk'] = 207
d2['no'] = 208
d3['dk'] = 307
d3['se'] = 309
d3['fi'] = 310
d4['dk'] = 307
d4['se'] = 309

# Opgave 2
print("Opgave 2 ---------------")
print(d0['a']) # None
print(d1['a']) # 7


# Opgave 3
print("Opgave 3 ---------------")
print('a' in d0) # False
print('a' in d1) # True

# Opgave 4
print("Opgave 4 ---------------")
print('fi' in d3) # True
del d3['fi']
print('fi' in d3) # False

# Opgave 5
print("Opgave 5 ---------------")
if d0:
    print('The dictionary is empty')     # The dictionary is empty
else:
    print('The dictionary is non-empty')
    
# Opgave 6
print("Opgave 6 ---------------")
print(len(d0)) # 0
print(len(d1)) # 1
print(len(d2)) # 2

# Opgave 7
print("Opgave 7 ---------------")
print(d0)       # {} 
print(d1)       # {'a': 7}
print([d2, d3]) # [{'dk': 207, 'no': 208}, {'dk': 307, 'se': 309}]

# Opgave 8
print("Opgave 8 ---------------")
for key in d2:
    print(key) # dk, no
    
# Opgave 9
print("Opgave 9 ---------------")
#help(d1) # skal udskrive dokumentation for klassen Dictionary

# Opgave 10
print("Opgave 10 ---------------")
print(d4 == d3) # True
print(d4 == d2) # False

# Opgave 11
print("Opgave 11 ---------------")
all = d2 | d3 # skal beregne en ordbog med opslag fra d2 eller d3
              # sidstnævnte bestemmer værdien ved sammenfald af nøgler
print(all)    # {'dk': 307, 'no': 208, 'se': 309}]
