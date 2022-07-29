N = int(input())
board = [[0] * (N+1) for _ in range(N+1)]

K = int(input())
for _ in range(K):
  row, col = input().split()
  board[int(row)][int(col)] = 1

L = int(input())
timing = []
direction = []
for _ in range(L):
  d = list(input().split())
  timing.append(int(d[0]))
  direction.append(d[1])

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
timer = 0
x, y, w = 1, 1, 1
tail_x, tail_y, tail_w = 1, 1, 1
length = 1

def tail_turn():
  global tail_x, tail_y, tail_w
  while True:
    if board[tail_x][tail_y] != 2:
      tail_w -= 1
      if tail_w == -1:
        tail_w = 3
    else:
      break
  tail_x += d[tail_w][0]
  tail_y += d[tail_w][1]

def turn(C):
  global w
  if C == "L":
    w -= 1
    if w == -1:
      w = 3
  else:
    w += 1
    if w == 4:
      w = 0

while True:
  if timer in timing:
    turn(direction[0])
    direction.remove(direction[0])
    timing.remove(timing[0])
    continue
  X, Y = x + d[w][0], y + d[w][1]
  if X > N or Y > N or X < 1 or Y < 1:
    timer += 1
    break
  if board[X][Y] == 0:
    board[tail_x][tail_y] = 0
    tail_turn()
    board[X][Y] = 2
    x, y = X, Y
    timer += 1
  elif board[X][Y] == 2:
    timer += 1
    break
  else:
    length += 1
    board[x][y] = 2
    board[X][Y] = 2
    timer += 1
    x, y = X, Y
print(timer)
