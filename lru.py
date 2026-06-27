from cache import Cache


class LRUCache(Cache):
    """
    Cache with LRU policy.
    """
    def __init__(self, size):
        super().__init__(size) 
        self.cache = {}
        self.used_index = [size]
        self.counter = 0

    def contains(self, index):
        if index in self.cache:
            return True
        return False

    def lookup(self, index):
        return self.cache[index]

    def cache_is_full(self):
        if self.counter == self. size:
            return True
        return False
        
    def evict(self):
        del self.cache[self.used_index[0]]

    def insert(self, index, value):
        self.counter += 1
        self.used_index[self.counter-1] = index
        self.cache[index]=value