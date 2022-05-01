# 17608 막대기

# # by oneself
# stack = [0]

# def stack_push(a):
#     if stack[-1] > a:
#         stack.append(a)
#     else:
#         while stack[-1] < a:
#             stack.pop()
#             stack.append(a)

# n = int(input())       
        
# for i in range(n):
#     a = int(input())
#     stack_push(a)

# print(len(set(stack))) 

# reference
import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
  stack.append(int(input()))

highest = 0
visible = 0

for i in range(len(stack)-1, -1, -1):
  if stack[i] > highest:
    visible += 1
    highest = stack[i]

print(visible)