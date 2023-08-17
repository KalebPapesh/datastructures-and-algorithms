# Heaps
These are a specialized binary tree-based data structure and satisfy the heap property (aka heap invariant). There are 2 types of heap invariants. These are commonly used to implement priority queues and perform efficient operations like inserting, deleting, and finding the highest or lowest element.

## Min-Heap Invariant
For every node `i`, the value of node `i` is <= the values of it's children (if they exist)

## Max-Heap Invariant
For every node `i`, the value of node `i` is >= the values of it's children (if they exist)

## Use Cases
1. Priority Queues - widely used to implement priority queues where elements are extracted in order of their priority.
1. Heap Sort - a sorting algorithm that uses the properties of heaps to sort elements in linearithmic time: O(n).
1. Dijkstra's Algorithm - used in Dijkstra's algorithm to select the next vertex with the smallest distance.
1. Prim's Algorithm - help select the minimum-weight edges in Prim's algorithm for finding minimum spanning trees.

# Corner Cases and Limitations
1. Duplicate values - standard heaps don't handle duplicate values well. you might have to extend the basic heap structure if you need to manage duplicates
1. Efficiency - While heaps excel at insertion and deletion of elements with the highest or lowest priority, they might not be the best choice for certain operations, like finding the kth largest or smallest element.
