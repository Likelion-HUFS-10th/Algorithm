# 11286 절댓값 힙
import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    a = int(input())
    if a != 0:
        heapq.heappush(heap, (abs(a), a))
    elif a == 0 and heap:
        print(heapq.heappop(heap)[1])
    elif a == 0 and not heap:
        print(0)