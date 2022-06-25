import sys
input = sys.stdin.readline

computer = int(input())
line = int(input())
graph = [[0] * (computer + 1) for _ in range(computer + 1)]
for _ in range(line):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0] * (computer + 1)

def dfs(num):
    visited[num] = 1
    for i in range(computer + 1):
        if graph[i][num] == 1 and visited[i] == 0:
            dfs(i)

dfs(1)
print(visited.count(1) - 1)