#!/usr/bin/env python3
from double_linked_node import DoubleLinkedNode
from double_linked_list import DoubleLinkedList

list = DoubleLinkedList()

head = DoubleLinkedNode("Mon")
day_2 = DoubleLinkedNode("Tue")
day_3 = DoubleLinkedNode("Wed")
day_4 = DoubleLinkedNode("Thurs")
tail = DoubleLinkedNode("Fri")

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
