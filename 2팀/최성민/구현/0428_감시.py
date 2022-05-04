import copy
from itertools import count

r, c = tuple(map(int, input().split()))
blocks = [list(map(int, input().split())) for _ in range(r)]

copyArr = copy.deepcopy(blocks)

direction = {
	1: [[0], [1], [2], [3]],
	2: [[1, 3], [0, 2]],
	3: [[0, 1], [1, 2], [2, 3], [0, 3]],
	4: [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
	5: [[0, 1, 2, 3]]
}

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

cctv_info = []

def in_range(x, y):
	return 0 <= x < r and 0 <= y < c

for i in range(r):
	for j in range(c):
		if 1 <= blocks[i][j] <= 5:
			cctv_info.append((blocks[i][j], i, j))

def dfs(cnt, arr):
	global min_val

	if cnt == len(cctv_info):
		result = 0
		for i in range(r):
			result += arr[i].count(0)
		min_val = min(result, min_val)
		return 

	copyArr = copy.deepcopy(arr) 
	cctv, x, y = cctv_info[cnt]
	for i in direction[cctv]:
		searching(copyArr, i, x, y)
		dfs(cnt + 1, copyArr)
		copyArr = copy.deepcopy(arr)
			

def searching(arr, info, x, y):
	for i in info:
		nx, ny = x, y

		while True:
			nx += dx[i]
			ny += dy[i]

			if not in_range(nx, ny):
				break
			if arr[nx][ny] == 6:
				break
			elif arr[nx][ny] == 0:
				arr[nx][ny] = 7
	
	print(arr)

min_val = int(1e9)
dfs(0, blocks)
print(min_val)
