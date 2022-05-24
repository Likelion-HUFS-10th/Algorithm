"""
힙 > heapq 모듈 사용
절댓값 > 최솟값 알고리즘을 변형해서 사용
절댓값 > abs()함수 사용
모두 abs로 받아줌 > abs로 출력
리스트로 절댓값과 num을 그대로 받아서 접근
"""
import heapq
import sys

n = int(input())
heap = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap,[abs(num),num])
    else:
        if len(heap) != 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)