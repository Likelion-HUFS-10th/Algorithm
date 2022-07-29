from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

visited = [0] * (n+1)
visited[0] = -1

d = 1
def bfs(start):
  global d
  queue = deque([start])
  visited[start] = 0
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if visited[i] == 0:
        visited[i] += d
        queue.append(i)
    d += 1

bfs(x)
judge = False
for i in range(n+1):
  if visited[i] == k:
    print(visited.index(k))
    visited[i] = -1
    judge = True
if not judge:
  print(-1)
