class Stack:
    def __init__(self,):
        self.stack= []

    def push(self, value):
        self.stack.append(value)
        

    def pop(self):
        top = self.stack.pop()
        return top

    def peek(self):
        y = self.stack[-1]
        return y
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.peek())  # 30
print(s.pop())   # 30
print(s.peek())  # 20
print(s.stack)   # [10, 20]