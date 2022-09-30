bilgisayar = int(input())
n = int(input())
graph = [[] for _ in range(bilgisayar + 1)]
check = [0] * (bilgisayar + 1)
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(i):
    global cnt
    check[i] = 1
    cnt += 1
    for v in graph[i]:
        if check[v] == 0:
            check[v] = 1
            dfs(v)

for i in graph[1]:
    if check[i] == 0:
        dfs(i)

print(cnt - 1)


