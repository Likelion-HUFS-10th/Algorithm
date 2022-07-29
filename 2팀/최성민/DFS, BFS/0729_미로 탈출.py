from collections import deque

n, m = map(int, input().split())
graph = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
# graph = []

# for i in range(n):
# 	graph.append(list(map(int, input())))

q = deque()
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

def in_range(x, y):
	return 0 <= x < m and 0 <= y < n

def bfs():
	cnt = 0

	while q:
		x, y = q.popleft()

		for dx, dy in zip(dxs, dys):
			nx, ny = x + dx, y + dy

			if in_range(nx, ny) and graph[ny][nx] == 1:
				if graph[ny][nx] == 1:
					graph[ny][nx] = graph[y][x] + 1
					q.append((nx, ny))

	return graph[n-1][m-1]

q.append((0, 0))
result = bfs()
print(result)