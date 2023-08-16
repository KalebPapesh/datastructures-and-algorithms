#!/usr/bin/env python3
from single_linked_node import SingleLinkedNode
from single_linked_list import SingleLinkedList

list = SingleLinkedList()
head = SingleLinkedNode("Mon")

day_2 = SingleLinkedNode("Tue")
day_3 = SingleLinkedNode("Wed")
day_4 = SingleLinkedNode("Thurs")
tail = SingleLinkedNode("Fri")

day_4.next = tail
day_3.next = day_4
day_2.next = day_3
head.next = day_2

list.head = head

print("Original List")
list.print_list()

new_head = SingleLinkedNode("Sun")
list.add_node_to_head(new_head)
print("Updated list with new Head")
list.print_list()
