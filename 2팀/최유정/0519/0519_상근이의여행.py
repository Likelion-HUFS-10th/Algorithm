import sys
input = sys.stdin.readline
from collections import deque


def bfs(n, graph):
    q = deque([1])
    visited[1] = True
    plane = 0

    while q:
        if visited.count(True) == n:
            return plane

        next = q.popleft()

        for i in graph[next]:
            if not visited[i]:
                q.append(i)
                plane += 1
                visited[i] = True

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (n+1)
    print(bfs(n, graph))