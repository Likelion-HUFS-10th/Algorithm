n, m = map(int, input().split())
graph = [[float('INF')] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
x, k = map(int, input().split())

for j in range(1, n+1):
    graph[j][j] = 0

for l in range(1, n+1):
    for m in range(1, n+1):
        for n in range(1, n+1):
            graph[m][n] = min(graph[m][n], graph[m][l]+graph[l][n])

if graph[1][k] == float('INF') or graph[k][x] == float('INF'):
    print(-1)
else:
    print(graph[1][k] + graph[k][x])
