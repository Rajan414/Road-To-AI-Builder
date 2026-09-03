# Check if it is empty.
# Insert 10
# Insert 20
# Insert 30
# Display the list.
# Search for 20
# Search for 99
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
    
    def insert_list(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def display(self):
        current = self.head
        while current is not None:
            print (current.data)
            current= current.next
    
    def empty (self):
        if self.head is None:
            return True
        return False
    
    def search(self,target):
        current = self.head
        while current is not None:
            if current.data ==target:
                return True
            current = current.next
        return False
    def count(self):
         current = self.head
         count = 0
         while current is not None:
            count = count + 1 
            current = current.next
         return count
 
my_linked_list = linked_list()

print(my_linked_list.empty())

my_linked_list.insert_list(10)
my_linked_list.insert_list(20)
my_linked_list.insert_list(30)

my_linked_list.display()
my_linked_list.count()
print(my_linked_list.search(20))
print(my_linked_list.search(99))