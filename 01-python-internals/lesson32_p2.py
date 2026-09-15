from lesson32_p2 import MinHeap
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