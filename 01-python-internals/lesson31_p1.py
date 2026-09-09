class Node:
    def __init__(self,data):
          self.data = data
class BST:
    def __init__(self):
        self.root = None
       

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current = self.root
        parent = None
        while current:
            parent = current
            if value < current.data:
                current = current.left
            elif value > current.data:
                current = current.right
            else :
                print("duplicate")
        
        if parent.data > value:
                parent.left = Node(value)
        elif parent.data < value:
                parent.right = Node(value)
                
    def search(self, value):
         current = self.root

         while current:
           if value == current.data:
            return True

           elif value < current.data:
            current = current.left

           else:
            current = current.right

         return False
        