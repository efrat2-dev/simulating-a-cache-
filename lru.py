from cache import Cache


class LRUCache(Cache):
    """
    Cache with LRU policy.
    """

    def __init__(self, size):
        super().__init__(size)

    def contains(self, index):
        raise NotImplementedError()

    def lookup(self, index):
        raise NotImplementedError()

    def cache_is_full(self):
        raise NotImplementedError()

    def evict(self):
        raise NotImplementedError()

    def insert(self, index, value):
        raise NotImplementedError()