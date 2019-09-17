from maps.map_base import MapBase

class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map"""
        self._table = []        # list of _Items

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:              #Found a match
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present"""
        for item in self._table:
            if k == item._key:          # Found a match
                item._value = v
                return
        # No match was found
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)"""
        for j in range(len(self._table)):
            if k == self._table[j]._key:        # Found a match
                self._table.pop(j)              # remove the item
                return                          # and quit
        raise KeyError('Key Error ' + repr(k))

    def __len__(self):
        """Return number of items in the map"""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map's key"""
        for item in self._table:
            yield item._key
