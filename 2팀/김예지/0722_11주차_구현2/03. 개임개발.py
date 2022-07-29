N, M = map(int, input().split())
check = [[0] * M for _ in range(N)]
a, b, w = map(int, input().split())
check[a][b] = 1
place = [list(map(int, input().split())) for _ in range(N)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 1
turn_cnt = 0

def turn():
  global w
  w -= 1
  if w == -1:
    w = 3

while True:
  turn()
  A, B = a + d[w][0], b + d[w][1]
  if place[A][B] == 0 and check[A][B] == 0:
    check[A][B] = 1
    a, b = A, B
    turn_cnt = 0
    cnt += 1
  else:
    turn_cnt += 1
  if turn_cnt == 4:
    A, B = a - d[w][0], b - d[w][1]
    if place[A][B] != 1:
      a, b = A, B
    else:
      break
    turn_cnt = 0

print(cnt)