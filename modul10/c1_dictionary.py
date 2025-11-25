class Dictionary:

    def __init__(self):
        self._v = [] # Liste af (key, value)

    def _find(self, key):
        v = self._v
        n = len(v)
        i = 0
        while i < n:
            the_key, _ = v[i]
            if the_key == key:
                return i
            i = i + 1
        return -1

    def add_entry(self, key, value):
        """Adds or replaces an entry. Returns old value or None."""
        idx = self._find(key)
        if idx >= 0:
            old_value = self._v[idx][1]
            self._v[idx] = (key, value) 
            return old_value
        else:
            self._v.append((key,value))
            return None
    
    def lookup_entry(self, key):
        """Returns value for key, or None."""
        idx = self._find(key)
        if idx >= 0:
            return self._v[idx][1]
        return None
    
    def contains_key(self, key):
        """Returns True if key exists in dictionary."""
        return self._find(key) >= 0
    
    def delete_entry(self, key):
        """Deletes entry and returns its value, or None if not found."""
        idx = self._find(key)
        if idx >= 0:
            key, value = self._v[idx]
            del self._v[idx]
            return value
        return None
    
    def size(self):
        """Returns number of entries."""
        return len(self._v)
