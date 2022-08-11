N, K = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(input().split()))
    
S, X, Y = map(int, input().split())

v_lst = list(set([w for s in graph for w in s if w != '0']))
v_lst.sort()

def change(graph):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    change_lst = []
    for i in v_lst:
        for x in range(N):
            for y in range(N):
                if graph[x][y] == i:
                    nx, ny = x, y
                    change_lst.append((nx, ny))

        for nx, ny in change_lst:
            for j in range(4):
                X, Y = nx+d[j][0], ny+d[j][1]
                if X > -1 and Y > -1 and X < N and Y < N:
                    if graph[X][Y] == '0':
                        graph[X][Y] = i
        change_lst = []
    return graph

for i in range(S):
    change(graph)
print(graph[X-1][Y-1])
