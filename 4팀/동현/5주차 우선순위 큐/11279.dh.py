"""
최대힙 > 완전 이진트리, 루트 노드로 올라갈수록 저장된 값이 커지는 구조
우선순위 큐 라이브러리 활용 > 힙 사용
heapq 모듈은 최소힙을 가정 -> '-' 붙여 최대힙으로 사용
heqppop() -> 최솟값을 뽑아줌 > 사실상 최댓값
int(input()) > 시간초과 발생 > sys.stdin.readline() 사용
"""
import heapq
import sys

n = int(input())
heap = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap,(-num))
    else:
        if len(heap) != 0:
            print(-1 * heapq.heappop(heap))
        else:
            print(0)