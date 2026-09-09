class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
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
                return
        
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
    def delete(self, value):
        current = self.root
        parent = None

    # Find the node
        while current and current.data != value:
            parent = current

            if value < current.data:
                current = current.left
            else:
                current = current.right

    # Value not found
        if current is None:
            return

    # Case 1: no children
        if current.left is None and current.right is None:

            if parent is None:
                self.root = None

            elif current == parent.left:
                parent.left = None

            else:
                parent.right = None

            return

    # Case 2: one child
        if current.left is None or current.right is None:

            child = current.left or current.right

            if parent is None:
                self.root = child

            elif current == parent.left:
                parent.left = child

            else:
                parent.right = child

            return

    # Case 3: two children
        successor_parent = current
        successor = current.right

        while successor.left:
          successor_parent = successor
          successor = successor.left

        current.data = successor.data

        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right
    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)
        
tree = BST()

for value in [10, 5, 15, 2, 7, 12, 20]:
    tree.insert(value)

tree.inorder(tree.root)
print()

tree.delete(2)
tree.inorder(tree.root)
print()

tree.delete(5)
tree.inorder(tree.root)
print()

tree.delete(10)
tree.inorder(tree.root)
print()