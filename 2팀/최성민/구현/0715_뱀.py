from collections import deque 
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
apples = [([0] * n) for _ in range(n)]

for _ in range(k):
	x, y = map(int, input().split())
	apples[x-1][y-1] = 1

change = int(input())
dir_info = deque()

for _ in range(change):
	s, c = input().split()
	dir_info.append((int(s), c))

def in_range(x, y):
	return 0 <= x < n and 0 <= y < n

def change_dir(dir, c):
	if c == "D":
		dir = (dir + 1) % 4

	if c == "L":
		dir = (dir - 1) % 4

	return dir

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

sec = 0
dir = 0
x, y = 0, 0
snake = deque()
snake.append((0, 0))

t, c = dir_info.popleft()
while True:
	if sec == t:
		dir = change_dir(dir, c)

		if dir_info:
			t, c = dir_info.popleft()

	x, y = x + steps[dir][0], y + steps[dir][1]
	sec += 1

	if (x, y) in snake or not in_range(x, y):
		break

	snake.append((x, y))		

	if apples[y][x] == 1:
		apples[y][x] = 0
		continue
	else:
		snake.popleft()
	
print(sec)
