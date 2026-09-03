from lesson23_p4 import my_linked_list
def count(self):
    current = self.head
    count = 0
    while current is not None:
        count = count + 1 
        current = current.next
    return count
my_linked_list.count()