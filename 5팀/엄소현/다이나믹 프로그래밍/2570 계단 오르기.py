import sys
input = sys.stdin.readline

n = int(input())   # 계단 개수
stair = list(int(input()) for _ in range(n))

point = [0 for _ in range(n)]   # 점수 저장
cnt = 0   # 연속해서 계단 오르는 횟수

for i in range(n):
  if i == 0:
    point[i] = stair[i]
  elif i == 1:
    point[i] = point[i-1] + stair[i]
  else:
    point[i] = max(stair[i-1] + point[i-3], point[i-2]) + stair[i]    # 바로 이전 계단에서 올라온 경우, 두 계단 전에서 올라온 경우

print(point[-1])
