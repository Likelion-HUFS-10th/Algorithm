from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
  num_lst = list(input())
  num_lst = [int(w) for w in num_lst]
  graph.append(num_lst)

# def dfs(x, y):
#   if x <= -1 or x >= n or y <= -1 or y >= m:
#     return False
#   if graph[x][y] == 0:
#     graph[x][y] = 1
#     dfs(x-1, y)
#     dfs(x, y-1)
#     dfs(x+1, y)
#     dfs(x, y+1)
#     return True
#   return False


def bfs(x, y):
  queue = deque([x, y])
  if graph[x][y] == 1:
    return False
  while queue:
    vx = queue.popleft()
    vy = queue.popleft()
    add = [[vx-1, vy], [vx, vy-1], [vx+1, vy], [vx, vy+1]]
    if graph[vx][vy] == 0:
      graph[vx][vy] = 1
    for i, j in add:
      if i > -1 and i < n and j > -1 and j < m:
        if graph[i][j] == 0:
          queue.append(i)
          queue.append(j)
          graph[i][j] = 1
  return True

result = 0
for i in range(n):
  for j in range(m):
    if bfs(i, j):
      result += 1
print(result)