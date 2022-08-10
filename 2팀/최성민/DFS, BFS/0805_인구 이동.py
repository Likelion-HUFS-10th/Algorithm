import sys
sys.setrecursionlimit(100000)

n, l, r = map(int, input().split())

countries = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

def in_range(x, y):
	return 0 <= x < n and 0 <= y < n

def 국경확인(x, y, graph):
	visited[x][y] = True

	for dx, dy in zip(dxs, dys):
		nx, ny = x + dx, y + dy

		if in_range(nx, ny) and not visited[nx][ny] :
			if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
				location.append((nx, ny))
				국경확인(nx, ny, graph)

	return location

count = 0
while True:	
	visited = [[False] * n for _ in range(n)]
	flag = False

	for i in range(n):
		for j in range(n):
			location = [(i, j)]
			if not visited[i][j]:
				location = 국경확인(i, j, countries)
			
			if len(location) > 1:
				flag = True
				sum = 0
				for x, y in location:
					sum += countries[x][y]
				
				avg = sum // len(location)

				for x, y in location:
					countries[x][y] = int(avg)

	if not flag:
		print(count)
		break

	count += 1

# print(f"result = {all_count}")