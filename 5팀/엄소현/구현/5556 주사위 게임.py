import sys
input = sys.stdin.readline

n, m = map(int, input().split())   # m: 상근이가 주사위
bord = [int(input()) for _ in range(n)]   # 보드 각 칸의 지시 사항
dice = [int(input()) for _ in range(m)]   # 던져서 나온 주사위 번호

now = 0   # 현재 위치 index
cnt = 0   # 주사위 던진 횟수

for i in range(m):
  cnt += 1
  now += dice[i]
  if now >= n-1:
    break
  now += bord[now]
  if now >= n-1:
    break

print(cnt)
