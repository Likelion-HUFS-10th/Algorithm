import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

grid = [list(map(int, input().split())) for _ in range(5)]
num_set = set()   # 서로 다른 여섯 자리의 수들의 집합

def dfs(i, j, num):
  num += str(grid[i][j])
  if len(num) == 6:
    num_set.add(num)
    return
  for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
    x, y = i + dx, j + dy
    if 0 <= x < 5 and 0 <= y < 5:
      dfs(x, y, num)

for i in range(5):
  for j in range(5):
    dfs(i, j, '')

print(len(num_set))