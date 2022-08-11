from collections import deque
from copy import deepcopy

N, L, R = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

unit = [[0] * N for _ in range(N)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y, graph):
    queue = deque([(x, y)])
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            X, Y = nx+d[i][0], ny+d[i][1]
            if X > -1 and Y > -1 and X < N and Y < N:
                if L <= abs(graph[nx][ny] - graph[X][Y]) <= R:
                    if unit[nx][ny] == 0:
                        unit[nx][ny] = 'u'
                        unit[X][Y] = 'u'
                        queue.append((X, Y))

graph2 = deepcopy(graph)

for i in range(N):
    for j in range(N):
        bfs(i, j, graph2)

cnt = 0
people = 0
for i in range(N):
    for j in range(N):
        if unit[i][j] == 'u':
            cnt += 1
            people += graph[i][j]
print(cnt)

if cnt != 0:
    final = people // cnt

for i in range(N):
    for j in range(N):
        if unit[i][j] == 'u':
            graph2[i][j] = final

print(graph2)
print(unit)

