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
        