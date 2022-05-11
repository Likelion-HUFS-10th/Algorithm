import sys
import heapq
input = sys.stdin.readline
N = int(input())
pq = []
for _ in range(N):
    x = int(input())
    if x != 0:
        positive = 1 if x > 0 else -1
        heapq.heappush(pq, (abs(x), positive))
    else:
        if pq:
            (y, positive) = heapq.heappop(pq)
            print(y*positive)
        else:
            print(0)
