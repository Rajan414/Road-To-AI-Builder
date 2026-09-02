# Create new_node
# Handle an empty list
# Traverse to the last node
# Attach the new node
class Node:
    def __init__(self,data):
        self.new_node = data
        self.next = None
        
def insert_end(self, data):
    new_node = Node(data)
    current = self.head
    if self.head is None:
        self.head = new_node
        return 
    current = self.head
    while current.next is not None:
        self.head = current.next
    current.next = new_node
    