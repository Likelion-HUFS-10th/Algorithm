'''
절댓값 힙

-> 처음에 heapq.heappush(heap, num)으로 적어서 계속 오류 떴음..

'''
import sys
import heapq

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])       # heap[1] 안 해주면 (2, 2) 모두 출력됨
    else:
        if num < 0:
            heapq.heappush(heap,(-num, num))
        elif num > 0:
            heapq.heappush(heap, (num,num))    # heapq.heappush(heap, num) -> 작동 x

