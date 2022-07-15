# 44:03

# N, M = map(int, input().split())
# x, y, w = map(int, input().split())
# place = [list(map(int, input().split())) for _ in range(N)]
# place[x][y] = 2
# cnt = 1

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# def now_w(w):
#   w_lst = [0, 3, 2, 1, 0]
#   for i in range(4):
#     if w == w_lst[i]:
#       return w_lst[i+1]

# w_cnt = 0
# while True:
#   X, Y = x + dx[now_w(w)], y + dy[now_w(w)]
#   if place[X][Y] != 1 and place[X][Y] != 2 :
#     w = now_w(w)
#     x, y = X, Y
#     place[x][y] += 2
#     cnt += 1
#   else:
#     if w_cnt != 4:
#       w = now_w(w)
#       w_cnt += 1
#     else:
#       break

# print(cnt)

N, M = map(int, input().split())
check = [[0] * M for i in range(N)]
a, b, d = map(int, input().split())
check[a][b] = 1

def d_control():
  global d
  d -= 1
  if d == -1:
    d == 3

map_info = []
for i in range(N):
  map_info.append(list(map(int, input().split())))

cnt = 1
control_cnt = 0

da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

while True:
  d_control()
  A, B = a + da[d], b + db[b]
  if check[A][B] == 0 and map_info[A][B] == 0:
    check[A][B] = 1
    a, b = A, B
    cnt += 1
    control_cnt = 0
    print(cnt)
    continue
  else:
    control_cnt += 1
  if control_cnt == 4:
    A, B = a - da[d], b - db[b]
    if map_info[A][B] == 0:
      a, b = A, B
  else:
    break
  control_cnt = 0

print(cnt)
