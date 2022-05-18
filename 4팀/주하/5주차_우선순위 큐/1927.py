'''
최소 힙 구하기 -> 최대 힙과 반대로

'''
import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        
        else:
            print(heapq.heappop(heap))   
    else:
        heapq.heappush(heap, num)