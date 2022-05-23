import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())

graph = [([0] * n) for _ in range(m)]

for _ in range(k):
	a, b, c, d = map(int, input().split())
	for i in range(b, d):
		for j in range(a, c):
			graph[i][j] = 1

def can_go(x, y):
	return 0 <= x < n and 0 <= y < m

def dfs(y, x, cnt):
	print(f'y = {y}, x = {x}, cnt = {cnt} ')
	graph[y][x] = 1
	dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

	for dx, dy in zip(dxs, dys):
		ny, nx = y + dy, x + dx
		if can_go(nx, ny) and not graph[ny][nx]:
			cnt = dfs(ny, nx, cnt+1)
		
	return cnt

res = []

for i in range(m):
	for j in range(n):
		if graph[i][j] == 0:
			res.append(dfs(i, j, 1))

print(len(res))
print(*sorted(res))

	
