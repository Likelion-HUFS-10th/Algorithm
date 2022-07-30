import sys
import math
input = sys.stdin.readline

n = int(input())   # 행성 수
planet = list(map(int, input().split()))   # 각 행성으로 이동하는 데 필요한 (최소) 속도
speed = planet[-1]

for i in range(n-2, -1, -1):
  if planet[i] < speed:
    if speed % planet[i] == 0:
      continue
    speed = ((speed // planet[i]) + 1) * planet[i]
  else:
    speed = planet[i]

print(speed)


