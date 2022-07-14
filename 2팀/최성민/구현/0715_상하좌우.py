import sys
input = sys.stdin.readline

n = int(input())
order = list(input().split())

dir = {
	"U": 0,
	"D": 1,
	"L": 2,
	"R": 3,
}

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
	return 0 < x < n and 0 < y < n

x, y = 1, 1

for val in order:
	idx = dir[val]

	nx, ny = x + dxs[idx], y + dys[idx]
	
	if in_range(nx, ny):
		x, y = nx, ny


print(x, y)