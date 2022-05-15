"""
파이썬의 모듈에서는 heapq 가 최소힙만 제공한다고 해서 -1을 곱해서 푸쉬하고
-1을 곱해서 출력하려고 했음..!

=> 코드 맞음.. 기계적으로 stdin 을 쓰는 연습을 해야 할듯
"""

# 최대힙의 시간을 어떻게 줄일 수 있을까?

import heapq
from sys import stdin

heap = []
n = int(stdin.readline())
for _ in range(n):
    order = int(stdin.readline())
    if order==0:
        try:
            print(heapq.heappop(heap)*-1)
        except:
            print(0)
    else:
        heapq.heappush(heap,order*-1)