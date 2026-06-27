import time

CACHE_DELAY = 0.002  # 2 ms, effective time is a bit larger than 1ms because python is not a realtime language
RAM_DELAY = 0.200  # 200 ms


class RAM:
    def __init__(self, items=None):
        self.memory = items.copy() if items else {}

    def read(self, index):
        time.sleep(RAM_DELAY)
        return self.memory.get(index)

    def put(self, index, value):
        time.sleep(RAM_DELAY)
        self.memory[index] = value


class MemorySystem:

    def __init__(self, cache, ram):

        self.cache = cache
        self.ram = ram

        self.last_access_hit = False
        self.last_access_miss = False

    def access_memory(self, index):

        time.sleep(CACHE_DELAY)

        item = self.cache.cache_get(index)

        if item is not None:

            self.last_access_hit = True
            self.last_access_miss = False

            return item

        self.last_access_hit = False
        self.last_access_miss = True

        item = self.ram.read(index)

        time.sleep(CACHE_DELAY)

        self.cache.cache_put(index, item)

        return item
