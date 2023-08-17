#!/bin/env python3
from lfu import LFU

# Usage
cache = LFU(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1
cache.put(3, 3)       # Removes key 2 as it was least frequently used
print(cache.get(2))  # Output: -1 (not found)
