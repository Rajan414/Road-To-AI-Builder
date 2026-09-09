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
    successor = current.right

    while successor.left:
        successor = successor.left

    successor_parent = current

    while successor_parent.left != successor:
        successor_parent = successor_parent.left

    current.data = successor.data

    if successor_parent.left == successor:
        successor_parent.left = successor.right
    else:
        successor_parent.right = successor.right