"""
최단거리를 구하기 위해 bfs 알고리즘 사용
큐를 활용
처음에 graph를 만드는 과정에서 각 지점별 이어지는 지점으로 연결하는 것이 중요
"""
from collections import deque
n, m, k, x = map(int, input().split())

distance = [0] * (n+1)
visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]
#print(graph)
for _ in range(m):
    a, b = map(int, input().split()) # 각 점과 연결되는 지점을 정해주는 것이 중요
    graph[a].append(b)
    #print(graph)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[v] + 1

bfs(x)

for i,j in enumerate(distance):
    if j != 0:
        if j == k:
            print(i)

if k not in distance:
    print(-1)