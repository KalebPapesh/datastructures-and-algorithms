import heapq
from collections import defaultdict

# Least Frequently Used (LFU) cache involves removing the least frequently used items
# from the cache when the cache becomes full.
# this implementation uses a priority/heap queue algorithm through heapq
# the frequency count is stored in a defaultdict which allows us to return 0 for any value not stored in the dict
class LFU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq_count = defaultdict(int)
        self.heap = []

    def get(self, key):
        if key in self.cache:
            value, freq = self.cache[key]

            # Increment the frequency count and update heap
            # store the frequency count as the heap value, when returned the priority queue will
            # provide the smallest value first unless negated as heapq uses a min-heap invariant
            # because the frequency count is the priority value a priority queue allows us to dequeue the smallest value first
            self.freq_count[key] += 1
            heapq.heappush(self.heap, (self.freq_count[key], key))
            return value
        else:
            return -1

    def put(self, key, value):
        if self.capacity <= 0:
            return

        if key in self.cache:
            # Update the cache[key] value and frequency
            self.cache[key] = (value, self.cache[key][1] + 1)
            # increment the frequency count
            self.freq_count[key] += 1
            # update the heap by pushing the frequency count and the key onto the queue
            heapq.heappush(self.heap, (self.freq_count[key], key))
        else:
            if len(self.cache) >= self.capacity:

                # Remove the least frequently used item
                # heap example:
                # [[0,1],[1,1],[2,2]]
                # heap[0][1] output = 1
                while self.heap and self.heap[0][1] != key:
                    heapq.heappop(self.heap)
                if self.heap:
                    _, removed_key = heapq.heappop(self.heap)
                    del self.cache[removed_key]
                    del self.freq_count[removed_key]

                    self.__set_values(value, key, 1)

    def __set_values(self, value, key, count):
        # add the new item to the cache, set the frequency count, and update the heap
        self.cache[key] = (value, count)
        self.freq_count[key] = count
        heapq.heappush(self.heap, (count, key))
