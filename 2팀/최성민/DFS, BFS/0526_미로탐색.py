from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]
step = [([0] * m) for _ in range(n)]

for i in range(n):
	input_value = input().rstrip()

	for j in input_value:
		graph[i].append(int(j))

q = deque()

def in_range(x, y):
	return 0 <= x < m and 0 <= y < n

def bfs():
	global ans

	dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

	while q:
		x, y = q.popleft()

		for dx, dy in zip(dxs, dys):
			nx, ny = x + dx, y + dy

			if in_range(nx, ny) and graph[ny][nx] and not visited[ny][nx]:
				q.append((nx, ny))
				visited[ny][nx] = True
				step[ny][nx] = step[y][x] + 1

q.append((0, 0))
step[0][0] = 1
bfs()
print(step[-1][-1])
