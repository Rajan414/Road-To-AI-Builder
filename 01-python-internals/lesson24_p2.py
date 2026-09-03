def delete_last(self):
    if self.head is None:
        return
    if self.head.next is None:
        self.head = None
        return
    current = self.head
    while current.next.next is not None:
        current = current.next
    current.next = None
