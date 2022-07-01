from collections import deque
import sys
input = sys.stdin.readline

n = int(input())   # 카드 수
skill = list(map(int, input().split()))   # 기술
card = deque()
num = 1

for i in range(n-1, -1, -1):
  if skill[i] == 1:
    card.insert(0, num)
  elif skill[i] == 2:
    card.insert(1, num)
  else:
    card.append(num)
  num += 1

print(*card)