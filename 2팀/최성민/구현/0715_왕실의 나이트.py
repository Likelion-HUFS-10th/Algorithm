val = input()

dir = {
	"a" : 1,
	"b" : 2,
	"c" : 3,
	"d" : 4,
	"e" : 5,
	"f" : 6,
	"g" : 7,
	"h" : 8,
}

x, y = int(val[1]), int(ord(val[0])) - int(ord('a')) + 1
cnt = 0

def in_range(x, y):
	return 1 <= x < 9 and 1 <= y < 9

dxs, dys = [2, 2, -2, -2, 1, -1, 1, -1], [1, -1, 1, -1, 2, 2, -2, -2]

for dx, dy in zip(dxs, dys):
	nx, ny = x + dx, y + dy

	if in_range(nx, ny):
		cnt += 1

print(cnt)