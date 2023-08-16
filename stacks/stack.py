import sys
sys.path.append('../linked_lists')
from single_linked_node import SingleLinkedNode
from single_linked_list import SingleLinkedList

class Stack:
    def __init__(self):
        self.stack = SingleLinkedList()

    def push(self, val):
        new_node = SingleLinkedNode(val)
        self.stack.add_node_to_head(new_node)
        return val

    def pop(self):
        self.stack.remove_head()

    def peek(self):
        return self.stack.head.val

    def size(self):
        pointer = self.stack.head
        count = 0
        while pointer is not None:
            count += 1
            pointer = pointer.next

        return count
