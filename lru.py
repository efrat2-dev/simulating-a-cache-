from cache import Cache


class LRUCache(Cache):
    """
    Cache with LRU policy.
    """
    def __init__(self, size):
        super().__init__(size) 
        self.cache = {}
        self.counter = 0
        self.List_head = None
        self.List_tail = None


    def contains(self, index):
        if index in self.cache:
            return True
        return False

    def lookup(self, index):
        requested = self.cache[index]
        if self.List_tail != requested:
            self.move_to_tail(index)
        return requested.value

    def cache_is_full(self):
        if self.counter == self.size:
            return True
        return False
        
    def evict(self):
        evicted = self.List_head
        if evicted != self.List_tail:
            evicted.next.prev = None
            self.List_head = evicted.next
        else:
            self.List_head = None
            self.List_tail = None
        del self.cache[evicted.index]
        del evicted
        self.counter -=1
        

    def insert(self, index, value):
        if index in self.cache: 
            if self.List_tail != self.cache[index]:
                self.move_to_tail(index)
            self.cache[index].value = value
        else:
            if self.counter == 0:
                New = Linked_value(value,index)
                self.List_head = New
                self.List_tail = New
                self.cache[index] = New
            else:
                New = Linked_value(value,index,self.List_tail)
                self.List_tail.next = New
                self.List_tail = New
                self.cache[index] = New
            self.counter += 1

    def move_to_tail(self,index):
        replace = self.cache[index]
        if replace == self.List_head:
            self.List_head = replace.next
            self.List_head.prev = None
        else:
            replace.prev.next = replace.next
            replace.next.prev = replace.prev
        replace.prev = self.List_tail
        replace.next = None
        self.List_tail.next = replace
        self.List_tail = replace


class Linked_value():
    def __init__(self,value,index,prev = None):
        self.value = value
        self.index = index
        self.prev = prev
        self.next = None