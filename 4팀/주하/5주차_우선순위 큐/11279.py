'''
최대 힙 구하기
heapq 모듈 사용 -> 최소 힙 원리 / heappush() - 힙 원소 추가, heappop() - 가장 작은 원소 삭제 후 값 리턴 
최소 힙 내림차순 -> key에만 - 붙여서 heap에 넣고 vaule를 출력

'''
import sys
import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        
        else:
            print(heapq.heappop(heap)[1])    # 내림차순 -> 가장 앞에 있는 값이 가장 큰 값
    else:
        heapq.heappush(heap,(-num, num))
      
