#!/usr/bin/env python3

class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        node = self.head
        while node is not None:
            print("Val: " + node.val)
            if node.prev is not None: print("Prev val: " + node.prev.val)
            if node.next is not None: print("Next val: " + node.next.val)
            node = node.next

list = DoubleLinkedList()

head = Node("Mon")
day_2 = Node("Tue")
day_3 = Node("Wed")
day_4 = Node("Thurs")
tail = Node("Fri")

day_2.prev = head
day_3.prev = day_2
day_4.prev = day_3
tail.prev = day_4

day_4.next = tail
day_3.next = day_4
day_2.next = day_3
head.next = day_2

list.head = head
list.tail = tail

list.print_list()
