import heapq

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 1)

print(heap)
print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))
print(heap)

heap_2 = []
heapq.heappush(heap_2, (1, 'a'))
heapq.heappush(heap_2, (2, 'b'))
print(heap_2)

heapq.heappop(heap_2)
print(heap_2)