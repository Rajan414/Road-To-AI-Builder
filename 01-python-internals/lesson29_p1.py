class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def merge_sorted(self,list1,list2):
    dummy = Node(0)
    current = dummy
    a = list1.head
    b = list2.head
    while a is not None and b is not None:
        if a.data <b.data:
            current.next = a
            current = current.next
            a = a.next
        else :
            current.next = b
            current = current.next
            b = b.next
    if a is not None:
        current.next = a
    else:
        current.next = b
    return dummy.next
    