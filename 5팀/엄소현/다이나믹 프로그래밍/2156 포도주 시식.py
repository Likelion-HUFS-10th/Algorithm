import sys
input = sys.stdin.readline

n = int(input())   # 포도잔 개수
wine = list(int(input()) for _ in range(n))

max_wine = [0 for _ in range(n)]

for i in range(n):
  if i == 0:
    max_wine[i] = wine[i]
  elif i == 1:
    max_wine[i] = max_wine[i-1] + wine[i]
  elif i == 2:
    max_wine[i] = max(max_wine[i-1], wine[i] + wine[i-2], wine[i] + wine[i-1])
  else:
    max_wine[i] = max(max_wine[i-1], wine[i] + max_wine[i-2], wine[i] + wine[i-1] + max_wine[i-3])

print(max_wine[-1])
