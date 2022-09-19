from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
height = [list(map(int, input().split())) for _ in range(n)]

def bfs(i, j, h, visited):
  q = deque()
  q.append((i, j))
  visited[i][j] = True
  cnt = 0
  while(q):
    cnt += 1
    v1, v2 = q.popleft()
    for dx, dy in (0, 1), (0, -1), (-1, 0), (1, 0):
      x, y = v1 + dx, v2 + dy
      if 0 <= x < n and 0 <= y < n and not visited[x][y] and height[x][y] > h:
        q.append((x, y))
        visited[x][y] = True

max_area = 0
for h in range(101):
  area = 0
  visited = [[False for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if height[i][j] > h and not visited[i][j]:
        bfs(i, j, h, visited)
        area += 1
  max_area = max(max_area, area)
  
print(max_area)