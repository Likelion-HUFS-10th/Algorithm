import sys
sys.setrecursionlimit(300000)

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
check = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(node):
    check[node] = 1
    for i in graph[node]:
        if check[i] == 0:
            dfs(i)
dfs(1)

cnt = 0
for i in check:
  if i == 1:
    cnt += 1

print(cnt-1)