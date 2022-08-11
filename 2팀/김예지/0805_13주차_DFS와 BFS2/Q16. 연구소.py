from itertools import combinations
from copy import deepcopy
from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(input().split()))

zero_lst = []
two_lst = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            zero_lst.append((i, j))
        elif graph[i][j] == '2':
            two_lst.append((i, j))

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(graph):
    queue = deque([])
    for nodes in two_lst:
        queue.append(nodes)
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            X, Y = nx+d[i][0], ny+d[i][1]
            if X > -1 and Y > -1 and X < N and Y < M:
                if graph[X][Y] == '0':
                    graph[X][Y] = '2'
                    queue.append((X, Y))
    return graph

max = 0
for c in combinations(zero_lst, 3):
    cnt = 0
    graph2 = deepcopy(graph)
    for x, y in c:
        graph2[x][y] = '3'
    
    bfs(graph2)

    for i in range(N):
        for j in range(M):
            if graph2[i][j] == '0':
                cnt += 1
    if cnt > max:
        max = cnt

print(max)
        
    

