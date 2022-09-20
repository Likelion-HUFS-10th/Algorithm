import heapq

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
dis = [float('INF')] * (n+1)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
max_dis = 0
cnt = -1
for d in dis:
    if d == float('INF'):
        continue
    max_dis = max(max_dis, d)
    cnt += 1
print(cnt, max_dis)