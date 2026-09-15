def pop(self):
    if not self.heap:
        return None
    minimum = self.heap[0]
    last = self.heap.pop()
    if not self.heap:
        return minimum
    self.heap[0] =last
    index = 0
    while True:
        left = index * 2 + 1
        right = index*2+2
        smallest = index
        if left <len(self.heap) and self.heap[left]< self.heap[smallest]:
            smallest = left
        if right <len(self.heap) and self.heap[right]< self.heap[smallest]:
                smallest = right
        if smallest == index:
            break
        self.heap[index],self.heap[smallest] = (self.heap[smallest],self.heap[index])
        index = smallest
    return minimum
h = pop(self)

for x in [10, 5, 8, 2, 7, 3]:
    h.push(x)

print(h.heap)

print(h.pop())
print(h.heap)

print(h.pop())
print(h.heap)