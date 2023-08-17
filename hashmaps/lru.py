from collections import OrderedDict

# remove the least recently used items from a cache when the cache becomes full
class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            # move the item to the end of the cache by popping it out of the hash first
            value = self.cache.pop(key)
            self.cache[key] = value
            return value

    def put(self, key, value):
        if key in self.cache:
            # remove
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # remove the least recently used item from the cache
            # last = False tells popitem() to use FIFO order (aka the item at the bottom of the stack gets popped off)
            self.cache.popitem(last=False)
        self.cache[key] = value
