# Vi laver _v som en liste af lister – én liste per nøglelængde.
# Da nøglerne kan være vilkårligt lange, skal vi kunne udvide _v dynamisk.

class Dictionary:
    def __init__(self):
        # _v er en liste af lister
        # index = længden af key
        self._v = []

    def _ensure_bucket(self, key):
        """ Sikre at der findes en bucket (liste) for længdenaf key """
        klen = len(key)
        while len(self._v) <= klen:
            self._v.append([])
        return self._v[klen]
    
    def _find(self, key):
        """Finder indekset i bucket-listen for key — eller -1."""
        bucket = self._ensure_bucket(key)
        n = len(bucket)
        i = 0
        while i < n:
            the_key, _ = bucket[i]
            if the_key == key:
                return i
            i += 1
        return -1
    
    def add_entry(self, key, value):
        """Adds or replaces entry. Returns old value or None."""
        bucket = self._ensure_bucket(key)
        idx = self._find(key)
        if idx >= 0:
            old = bucket[idx][1]
            bucket[idx] = (key, value)
            return old
        else:
            bucket.append((key,value))
            return None
        
    def lookup_entry(self, key):
        """ Returns value for key or None """
        bucket = self._ensure_bucket(key)
        idx = self._find(key)
        if idx >= 0:
            return bucket[idx][1]
        return None
    
    def contains_key(self, key):
        """True if key exists."""
        return self._find(key) >= 0
    
    def delete_entry(self, key):
        """ Deletes entry and returns its value or None """
        bucket = self._ensure_bucket(key)
        idx = self._find(key)
        if idx >= 0:
            key, value = bucket[idx]
            del bucket[idx]
            return value
        return None
    
    def size(self):
        """ Total number of entries """
        total = 0
        for bucket in self._v:
            total += len(bucket)
        return total
    
    