import sys
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n+1)
dis = [0] * (n+1)

def bfs(start):
    result = []
    queue = deque([start])
    visited[start] = True
    
    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                dis[i] = dis[n] + 1
                if dis[i] == k:
                    result.append(i)
    return result

result = bfs(x)
if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)