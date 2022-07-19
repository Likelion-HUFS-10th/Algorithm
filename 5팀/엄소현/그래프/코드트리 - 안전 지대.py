import sys
input = sys.stdin.readline


def in_range(i, j):
  return 0 <= i < n and 0 <= j < m

def bfs(i, j, visited, k):
  dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
  visited[i][j] = False
  for dx, dy in zip(dxs, dys):
    x, y = i + dx, j + dy
    if in_range(x, y) and visited[x][y] and g[x][y] > k:
      bfs(x, y, visited, k)
  return True

# 입력
n, m = map(int, input().split())   # n: 행, m: 열
g = []
max_height = 0
for _ in range(n):
  g_line = list(map(int, input().split()))
  g.append(g_line)
  if max_height < max(g_line):
    max_height = max(g_line)

max_cnt = 0   # 안전 영역의 수의 최댓값
max_k = 0   # 안전 영역의 수가 최대가 될 때 K

# 출력
for k in range(1, max_height):
  cnt = 0   # 안전 영역의 수
  visited = [[True for _ in range(m)] for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if g[i][j] > k and visited[i][j] and bfs(i, j, visited, k):
        cnt += 1
  if max_cnt < cnt:
    max_cnt = cnt
    max_k = k

print(max_k, max_cnt)