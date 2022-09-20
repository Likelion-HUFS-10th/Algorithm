INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for cost in graph[1:]:
    for c in cost[1:]:
        if c == INF:
            print(0, end = " ")
        else:
            print(c, end = " ")
    print()