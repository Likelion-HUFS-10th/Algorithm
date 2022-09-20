import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[float('INF')] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

for x in range(1, n+1):
    for y in range(1, n+1):
        if graph[x][y] == float('INF'):
            print(0, end=' ')
        else:
            print(graph[x][y], end=' ')
    print()