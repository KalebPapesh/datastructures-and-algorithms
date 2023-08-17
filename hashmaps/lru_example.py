#!/bin/env python3

from lru import LRU

cache = LRU(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1
cache.put(3, 3)       # Removes key 2 as it was least recently used
print(cache.get(2))  # Output: -1 (not found)
