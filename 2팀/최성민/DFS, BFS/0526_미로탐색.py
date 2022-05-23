from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
	graph.append(list(input().rstrip()))

step = [([0] * m) for _ in range(n)]
visited = [([0] * m) for _ in range(n)]
q = deque()

def bfs():
	dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

	while q:
		x, y = q.popleft()

		for dx, dy in zip(dxs, dys):
			nx, ny = x + dx, y + dy

			if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == "1" and not visited[ny][nx]:
				visited[ny][nx] = 1
				q.append((nx, ny))
				step[ny][nx] = step[y][x] + 1

q.append((0, 0))
step[0][0] = 1
bfs()
print(step[-1][-1])
