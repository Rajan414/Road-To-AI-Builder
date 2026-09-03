class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            
    def search(self, target):
        current = self.head
        while current is not None:
           if current.data ==target :
               return True
           else: 
               current = current.next
        return False
    
    def is_empty(self):
           if self.head is None:
              return True
           else :
               return False
    def count(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1 
            current = current.next
        return count

my_list = LinkedList()
my_list.is_empty()
my_list.insert_first(10)
my_list.insert_first(20)
my_list.insert_first(30)
