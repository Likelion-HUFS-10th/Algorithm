from collections import deque
import sys
input = sys.stdin.readline

n = int(input())   # 학생 수
num = deque(list(map(int, input().split())))   # 번호표

now = 1   # 현재 받아야 하는 번호
q = []   # 빈 공간

while num:
  if now == num[0]:
    num.popleft()
    now += 1
  elif len(q) != 0 and now == q[-1]:
    q.pop()
    now += 1
  else:
    if len(q) == 0 or (len(q) != 0 and q[-1] > num[0]):
      q.append(num.popleft())
    else:
      print("Sad")
      exit(0)

if len(q) != 0:
  for i in range(len(q)-1, -1, -1):
    if now == q[i]:
      now += 1
    else:
      print("Sad")
      exit(0)
  
print("Nice")