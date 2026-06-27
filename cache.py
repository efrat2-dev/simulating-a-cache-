from abc import ABC, abstractmethod


class Cache(ABC):
    """
    Abstract Cache class.
     Exposes cache_get and cache_put,
    while replacement policy is implemented
    by subclasses.
    """

    def __init__(self, size):
        self.size = size

    def cache_get(self, index):
        """
        Returns value if exists, otherwise None.
        """
        if self.contains(index):
            return self.lookup(index)

        return None

    def cache_put(self, index, value):
        """
        Inserts value into cache.
        Evicts according to replacement policy if needed.
        """

        # If index already exists, update it without eviction.
        if self.contains(index):
            self.insert(index, value)
            return

        # Evict only when inserting a new item into a full cache.
        if self.cache_is_full():
            self.evict()

        self.insert(index, value)

    # ===== Abstract inner operations =====

    @abstractmethod
    def contains(self, index):
        pass

    @abstractmethod
    def lookup(self, index):
        pass

    @abstractmethod
    def cache_is_full(self):
        pass

    @abstractmethod
    def evict(self):
        pass

    @abstractmethod
    def insert(self, index, value):
        pass
