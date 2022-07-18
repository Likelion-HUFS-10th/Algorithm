# 제로
# 0이 입력될 경우 : 가장 최근에 쓴 수 지우기
# 0이 아닌 수가 입력될 경우 : 해당 수 쓰기

import sys

num = int(sys.stdin.readline())
stack = []

for _ in range(num):
  input = int(sys.stdin.readline())
  if input != 0:
    stack.append(input)
  else:
    stack.pop()

print(sum(stack))