def nth_from_end(self, n):
    first = self.head
    second = self.head

    for _ in range(n):
        if first is None:
            return None
        first = first.next

    while first is not None:
        first = first.next
        second = second.next

    return second.data