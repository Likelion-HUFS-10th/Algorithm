import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())   # 화단 한 변 길이
garden = [list(map(int, input().split())) for _ in range(n)]   # 화단 지점당 가격

def check(i, j, visited):
  for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
    x, y = i + dx, j + dy
    if not ((0 <= x < n and 0 <= y < n) and visited[x][y]):
      return False
  return True

def calc(i, j):
  cost = 0
  for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
    x, y = i + dx, j + dy
    cost += garden[x][y]
  return cost

def dfs(x, cnt, visited, cost_sum):
  global min_cost
  if cnt == 3:
    min_cost = min(min_cost, cost_sum)
    return
  for i in range(x, n-1):
    for j in range(1, n-1):
      if check(i, j, visited):
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
          visited[i + dx][j + dy] = False
        dfs(i, cnt+1, visited, cost_sum + calc(i, j))
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
          visited[i + dx][j + dy] = True

min_cost = sys.maxsize
dfs(1, 0, [[True for _ in range(n)] for _ in range(n)], 0)
print(min_cost)
