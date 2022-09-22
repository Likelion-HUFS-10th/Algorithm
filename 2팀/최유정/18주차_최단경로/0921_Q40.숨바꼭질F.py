n, m = map(int, input().split())
graph = [[float('INF')]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

h = []
max_num = 0
for i in range(1, n+1): max_num = max(max_num, graph[1][i])
cnt = 0
for j in range(1, n+1):
    if max_num == graph[1][j]:
        cnt += 1
        h.append(j)

print(min(h), max_num, len(h))