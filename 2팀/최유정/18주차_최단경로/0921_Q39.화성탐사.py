import heapq

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
t = int(input())
n = int(input())
mars = [list(map(int, input().split())) for _ in range(n)]
dis = [[float('INF')]*n for _ in range(n)]

x, y = 0, 0
q = [(mars[x][y], x, y)]
dis[x][y] = mars[x][y]

while q:
    dist, x, y = heapq.heappop(q)
    if dis[x][y] < dist:
        continue
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        cost = dis[x][y] + mars[nx][ny]
        if dis[nx][ny] > cost:
            dis[nx][ny] = cost
            heapq.heappush(q, (dis[nx][ny], nx, ny))

print(dis[n-1][n-1])