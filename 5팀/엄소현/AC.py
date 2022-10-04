from collections import deque
import sys
input = sys.stdin.readline

t = int(input())   # 테이스트 케스 개수
for _ in range(t):
  order = input().strip()   # 수행할 함수
  n = int(input())   # 배열 안 수의 개수
  arr = input().strip()
  if n == 0:
    arr = deque()
  else:
    arr = deque(arr[1:-1].split(','))  # 리스트 괄호 제거 -> 리스트로 변경
  
  error = False
  r_cnt = 0
  for o in order:
    if o == "R": 
      r_cnt += 1
    elif o == "D" and len(arr) == 0:
      error = True
      break
    else:
      if r_cnt % 2 == 0:
        arr.popleft()
      else:
        arr.pop()
  if r_cnt % 2 == 1:   # R 개수 홀수면 한 번, 짝수면 그대로
    arr.reverse()
  
  if error:
    print("error")
  else:
    print('[', ','.join(arr), ']', sep='')