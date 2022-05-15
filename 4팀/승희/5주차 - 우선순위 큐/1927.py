import heapq
from sys import stdin

heap = []
n = int(stdin.readline())
for _ in range(n):
    order = int(stdin.readline())
    if order==0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap,order)
