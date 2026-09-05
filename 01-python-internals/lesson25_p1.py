def reverse(self):
    previous = None
    current = self.head
    while current is not None:
        new_node = current.next
        current.next = previous
        previous = current
        current = new_node
    self.head = previous