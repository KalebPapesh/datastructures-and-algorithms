#!/usr/bin/env python3

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.val)
            node = node.next

list = SingleLinkedList()
list.head = Node("Mon")
day_2 = Node("Tue")
day_3 = Node("Wed")
day_4 = Node("Thurs")
tail = Node("Fri")
day_4.next = tail
day_3.next = day_4
day_2.next = day_3
list.head.next = day_2

list.print_list()
