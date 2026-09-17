class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        # your existing push
        ...

    def pop(self):
        if not self.heap:
            return None

        minimum = self.heap[0]
        last = self.heap.pop()

        if not self.heap:
            return minimum

        self.heap[0] = last

        index = 0

        while True:
            left = index * 2 + 1
            right = index * 2 + 2
            smallest = index

            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index]
            )

            index = smallest

        return minimum
class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def enqueue(self, priority, task):
        self.heap.push((priority, task))

    def dequeue(self):
        return self.heap.pop()

    def peek(self):
        if not self.heap.heap:
            return None

        return self.heap.heap[0]
pq = PriorityQueue()

pq.enqueue(5, "Exercise")
pq.enqueue(1, "Study")
pq.enqueue(3, "Lunch")
pq.enqueue(2, "Assignment")
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())