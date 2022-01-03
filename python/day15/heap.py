from heapq import heappop, heappush

heap = [(1, 1, 1)]


for x in range(5):
    heappush(heap, (1, x))

for x in range(6):
    item = heappop(heap)
    print(item)