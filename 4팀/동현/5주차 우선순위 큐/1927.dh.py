"""
최소힙 > heapq 모듈 그대로 사용
heapq 모듈은 최소힙을 기준으로 구성되어 있음
int(input()) > 시간초과 발생 > sys.stdin.readline() 사용
"""
import heapq
import sys

n = int(input())
heap = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap,(num))
    else:
        if len(heap) != 0:
            print(heapq.heappop(heap))
        else:
            print(0)