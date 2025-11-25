class Dictionary:
    def __init__(self):
        self._size = 0
        self._v = [[] for _ in range(7)]

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

    def put(self, key, value):
        index = self._bucket_index(key)
        bucket = self._v[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1
        self._maybe_grow()

    def get(self, key):
        index = self._bucket_index(key)
        for k, v in self._v[index]:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        index = self._bucket_index(key)
        bucket = self._v[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                self._maybe_shrink()
                return
        raise KeyError(key)

    def __len__(self):
        return self._size
