# 카드2
# 맨위에 있는 카드 바닥에 버림 -> 맨위에 있는 카드 맨밑으로

from collections import deque
from sys import stdin

num = int(stdin.readline())
deq = deque()

for i in range(num):
  # 우선 데크에 추가
  deq.append(i+1)

while len(deq) > 1:
  # 맨위 카드 바닥에 버리기 -> popleft
  deq.popleft()
  # 맨위 카드를 맨뒤로 append
  deq.append(deq.popleft())
print(deq.pop())

