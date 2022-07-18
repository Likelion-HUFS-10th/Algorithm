# 스택 : 정수를 저장하는 스택을 구현한 다음 주어진 명령 처리
# push X : 정수 X를 스택에 넣기
# pop : 스택에서 가장 위에 있는 정수 빼고 출력, 없으면 -1 출력
# size : 스택에 있는 정수의 개수 출력
# empty : 스택이 비어있으면 1 아니면 0 출력
# top : 스택의 가장 위에 있는 정수 출력, 없으면 -1 출력

# --------------------------------------------시간 초과--------------------------------------------
# class Stack:
#   def __init__(self):
#     self.stack = []

#   def push(self, push_x):
#     self.stack.append(push_x)
  
#   def pop(self):
#     if self.stack:
#       return self.stack.pop()
#     else:
#       return -1
  
#   def size(self):
#     return len(self.stack)
  
#   def empty(self):
#     if self.stack:
#       return 0
#     else:
#       return 1
  
#   def top(self):
#     if self.stack:
#       return self.stack[-1]
#     else:
#       return -1

# num = int(input())
# stack_input = Stack()

# for _ in range(num):
#   order = input()
#   if order.find(" ") != -1:
#     input_x = order.split()[-1]
#     stack_result = stack_input.push(input_x)
#   elif order == "pop":
#     stack_result = stack_input.pop()
#     print(stack_result)
#   elif order == "size":
#     stack_result = stack_input.size()
#     print(stack_result)
#   elif order == "empty":
#     stack_result = stack_input.empty()
#     print(stack_result)
#   else:
#     stack_result = stack_input.top()
#     print(stack_result)

# 시간초과 나면 PyPy나 readline으로 해결 -> PyPy도 안됨
import sys

class Stack:
  def __init__(self):
    self.stack = []
  def push(self, push_x):
    self.stack.append(push_x)
  def pop(self):
    if self.stack:
      return self.stack.pop()
    else:
      return -1
  def size(self):
    return len(self.stack)
  def empty(self):
    if self.stack:
      return 0
    else:
      return 1
  def top(self):
    if self.stack:
      return self.stack[-1]
    else:
      return -1

input = sys.stdin.readline
num = int(input())
stack_input = Stack()

for _ in range(num):
  order = input().split()
  if order[0] == "push":
    stack_input.push(order[-1])
  elif order[0] == "pop":
    print(stack_input.pop())
  elif order[0] == "size":
    print(stack_input.size())
  elif order[0] == "empty":
    print(stack_input.empty())
  else:
    print(stack_input.top())