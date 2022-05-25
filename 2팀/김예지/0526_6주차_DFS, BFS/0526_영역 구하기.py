import sys
sys.setrecursionlimit(10000)

def dfs(y, x, cnt):
    graph[y][x] = 1
    for dy, dx in d:
        Y = y+dy
        X = x+dx
        if (0 <= Y < m) and (0 <= X < n) and graph[Y][X] == 0:
            cnt = dfs(Y, X, cnt+1)
    return cnt

m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            answer.append(dfs(i, j, 1))
            
print(len(answer))
print(*sorted(answer))

# Asterisk(*) :  컨테이너 타입의 데이터를 Unpacking할 때 사용