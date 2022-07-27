# 큐2
# FIFO : First In First Out

############################ 데크 사용X - 시간초과 ######################
# import sys
# num = int(sys.stdin.readline())
# queue = []

# for _ in range(num):
#   input = sys.stdin.readline().split()

#   if input[0] == "push":
#     queue.append(int(input[1]))
#   elif input[0] == "pop":
#     if queue:
#       # 'list' object has no attribute 'popleft' 리스트는 popleft 연산 없음
#       # print(queue.popleft())
#       print(queue[0])
#       # 근데 del 함수는 나머지 요소들이 앞으로 땡겨지는데 시간이 걸림
#       del queue[0]
#     else:
#       print(-1)
#   elif input[0] == "size":
#     print(len(queue))
#   elif input[0] == "empty":
#     if queue:
#       print(0)
#     else:
#       print(1)
#   elif input[0] == "front":
#     if queue:
#       print(queue[0])
#     else:
#       print(-1)
#   elif input[0] == "back":
#     if queue:
#       print(queue[-1])
#     else:
#       print(-1)

############################ 데크 사용 - 통과 ######################
from collections import deque
from sys import stdin

num = int(stdin.readline())
deq = deque([])

for _ in range(num):
  input = stdin.readline().split()
  if input[0] == "push":
    deq.append(int(input[1]))
  elif input[0] == "pop":
    if deq: print(deq.popleft())
    else: print(-1)
  elif input[0] == "size":
    print(len(deq))
  elif input[0] == "empty":
    if deq: print(0)
    else: print(1)
  elif input[0] == "front":
    if deq: print(deq[0])
    else: print(-1)
  elif input[0] == "back":
    if deq: print(deq[-1])
    else: print(-1)