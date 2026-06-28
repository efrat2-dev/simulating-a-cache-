import random
from cache import Cache


class RRCache(Cache):
    """
    Cache with Random Replacement policy.
    """

    def __init__(self, size):
        super().__init__(size) 
        self.cache = {}
        self.used_index = [None] * size
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
        randomI = random.randint(0, self.counter-1)
        key = self.used_index[randomI]
        del self.cache[key]
        self.used_index[randomI]= self.used_index[self.counter-1]
        self.counter -=1
        

    def insert(self, index, value):
        if index not in self.cache:
            self.used_index[self.counter]= index
            self.counter += 1
        self.cache[index]= value
        
