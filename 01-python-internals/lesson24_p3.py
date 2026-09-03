def delete(self, target):
    if self.head is None:
        return
    if self.head.data ==target:
        self.head= self.head.next
        return
    current = self.head
    while current.next is not None:
        if current.next.data == target:
             current.next = current.next.next
             return
        current = current.next