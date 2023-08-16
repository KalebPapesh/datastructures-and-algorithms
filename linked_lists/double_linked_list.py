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
