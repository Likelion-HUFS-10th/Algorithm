import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _  in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dis = [0] * (n+1)
vis = [False] * (n+1)
vis[1] = True
d = 1
q = [1]
while q:
    s = heapq.heappop(q)
    for g in graph[s]:
        if vis[g]: continue
        dis[g] += (dis[s]+1)
        vis[g] = True
        heapq.heappush(q, g)

p = []
for i in range(1, n+1): heapq.heappush(p, (-dis[i], i))

mn = heapq.heappop(p)
h = [mn[1]]
cnt = 1

while True:
    next = heapq.heappop(p)
    if mn[0] == next[0]:
        cnt += 1
        h.append(next[1])
    else: break

print(min(h), -mn[0], len(h))
