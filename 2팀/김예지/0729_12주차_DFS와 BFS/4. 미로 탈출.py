n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))
visited = [[0] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = 1

def dfs(x, y):
  global result
  visited[x][y] = 1
  for i in range(4):
    X, Y = x + dx[i], y + dy[i]
    if X > -1 and X < n and Y > -1 and Y < m:
      if graph[X][Y] == 1 and visited[X][Y] == 0:
        result += 1
        visited[X][Y] = 1
        return X, Y

nx, ny = dfs(0, 0)

while True:
  if nx == n-1 and ny == m-1:
    break
  else:
    nx, ny = dfs(nx, ny)

print(result)