# 괄호
# VPS(올바를 괄호 문자열) 판단하기

import sys

input_t = int(sys.stdin.readline())

for _ in range(input_t):
  stack = []
  input_str = sys.stdin.readline()
  
  # 짝이 맞는 왼쪽은 남기고 오른쪽만 날림 -> 스택에 무언가 남아있다? = 짝이 안맞는 오른쪽
  for elem in input_str:
    # 왼쪽 괄호면 스택에 넣기
    if elem == "(":
      stack.append(elem)
    # 오른쪽 괄호면 1. 현재 스택 상태 확인 2. 스택에서 꺼내기
    elif elem == ")":
      # 스택에 아무것도 없거나 top이 오른쪽 괄호일 때
      if not stack or stack[-1] != "(":
        stack.append(")")
        break
      stack.pop()
  if not stack:
    print("YES")
  else:
    print("NO")

