"""
배열에 정수를 넣음 => 절댓값이 가장 작은 값 출력 / 해당 배열에서 제거
절댓값이 가장 작은 값이 여러개인 경우에는 가장 작은 수 출력, 배열에서 제거

1.숫자를 넣어야 하는 경우에 더 작은수가 앞으로 가도록 해야 함.
"""

import heapq
import sys

n = int(input())
heap = []
input = sys.stdin.readline

for _ in range(n):
    order = int(input())
    if order == 0:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
    else:
        heapq.heappush(heap,(abs(order),order))

# for _ in range(n):
#     order = int(input())
#     if order==0:
#         if len(dq)==0:
#             print(0)
#         else:print("출력값",dq.popleft())
#     else:
#         dq.append(order)
#         list_dq = list(dq)
#         list(list_dq).sort()
#         print(list_dq)
#         list(list_dq).sort(key=abs)
#         print(list_dq)
#         dq = deque(list_dq)
