import sys
input = sys.stdin.readline

# n, m = map(int, input().split())
# a, b, d = map(int, input().split())

# game = [list(map(int, input().split())) for _ in range(n)]

n, m = 4, 4
a, b, d = 1, 1, 0
game = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
game[b][a] = 2

dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]

def turn_left():
	global d

	d -= 1
	if d == -1:
		d = 3

cnt = 1
turn = 0
while True:
	turn_left()
	nx, ny = a + dxs[d], b + dys[d]
	
	if game[ny][nx] == 0:
		game[ny][nx] = 2
		a, b = nx, ny
		cnt += 1
		turn = 0
		continue
	
	else:
		turn += 1

	if turn == 4:
		nx, ny = a - dxs[d], b - dys[d]

		if game[ny][nx] == 0 or game[ny][nx] == 2:
			a, b = nx, ny
		
		else:
			break

		turn = 0
	

print(cnt)

