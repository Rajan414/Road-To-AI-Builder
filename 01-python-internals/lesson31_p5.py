import heapq

heap = []

heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 3)

print(heap)

print("Minimum:", heapq.heappop(heap))
print(heap)