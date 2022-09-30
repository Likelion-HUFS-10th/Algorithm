from collections import deque

bilgisayar = int(input())
n = int(input())
graph = [[] for _ in range(bilgisayar + 1)]
check = [0] * (bilgisayar + 1)
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(i):
    global cnt
    que = deque(graph[i])
    check[i] = 1
    while que:
        target = que.popleft()
        check[target] = 1
        for v in graph[target]:
            if check[v] != 1:
                check[v] = 1
                que.append(v)
for i in graph[1]:
    if check[i] == 0:
        bfs(i)

print(sum(check) - 1)


