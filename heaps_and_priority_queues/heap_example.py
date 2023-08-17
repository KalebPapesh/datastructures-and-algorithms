#!/bin/env python3
import heapq

# min-heap
heap = []  # Create an empty heap

heapq.heappush(heap, 5)  # Insert elements into the heap
heapq.heappush(heap, 3)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

print(heap)  # Output: [1, 3, 8, 5]

min_value = heapq.heappop(heap)  # Remove and return the smallest element
print(min_value)  # Output: 1

print(heap[0])  # Peek at the smallest element


# max-heap (negation trick)
# the standard heapq module implements min-heaps.
# To work with max-heaps, you need to negate the values when inserting or extracting.
# To create max-heap custom objects you negate the priority value along with the object
max_heap = []  # Create an empty max-heap

# Insert elements into the heap by negating them
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)
heapq.heappush(max_heap, -1)

print(-max_heap[0])  # Peek at the largest element (negate the value)
