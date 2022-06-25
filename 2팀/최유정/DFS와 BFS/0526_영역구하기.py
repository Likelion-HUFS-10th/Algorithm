import sys
input = sys.stdin.readline
from collections import deque

m, n, k = map(int, input().split())
graph = [[0]*n for i in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1] #동서남북

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    graph[a][b] = 1
    count = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append([nx, ny])
                    count += 1
    return count

sep = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            sep.append(bfs(i, j))

print(len(sep))
sep.sort()
for i in sep:
    print(i, end=' ')