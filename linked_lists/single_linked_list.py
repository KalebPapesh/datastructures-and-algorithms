from single_linked_node import SingleLinkedNode

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node_to_head(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def remove_head(self):
        current_head = self.head
        new_head = self.head.next
        self.head = new_head
        return current_head.val

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.val)
            node = node.next
