
class Node:
    def __init__(self, data):
        self.data = data
        self. next = None
        
def remove_nth_from_end(self, n):
    dummy = Node(0)
    dummy.next = self.head

    first = dummy
    second = dummy

    for _ in range(n):
        first = first.next

    while first.next is not None:
        first = first.next
        second = second.next

    second.next = second.next.next
    self.head = dummy.next