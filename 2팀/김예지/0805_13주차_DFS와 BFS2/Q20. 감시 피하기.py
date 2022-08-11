from collections import deque
from itertools import combinations
from copy import deepcopy

N = int(input())
graph = []
for i in range(N):
    graph.append(list(input().split()))

x_lst = []
s_lst = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'X':
            x_lst.append((i, j))
        elif graph[i][j] == 'S':
            s_lst.append((i, j))

judge = True
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def change(graph):
    global judge
    for sx, sy in s_lst:
        for i in range(4):
            queue = deque([(sx, sy)])
            while queue:
                print(queue)
                nx, ny = queue.popleft()
                X, Y = nx+d[i][0], ny+d[i][1]
                print(X, Y)
                if X > -1 and Y > -1 and X < N and Y < N:
                    if graph[X][Y] == 'X':
                        graph[X][Y] = 'S'
                        queue.append((X, Y))
                    elif graph[X][Y] == 'O':
                        break
                    elif graph[X][Y] == 'T':
                        judge = False
                        break
                else:
                    break
    return judge

for c in combinations(x_lst, 3):
    graph2 = deepcopy(graph)
    for x, y in c:
        graph2[x][y] = 'O'
    print("O가 든 : ", graph2)

    change(graph2)
    print("judge : ", judge)
    if judge == True:
        print("YES")
        break

print("NO")
        