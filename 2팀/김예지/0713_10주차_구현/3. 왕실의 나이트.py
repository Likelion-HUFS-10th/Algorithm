# 10:57
now = list(input())
now[0] = int(ord(now[0])) - int(ord('a')-1)
now[1] = int(now[1])

moves = [(2, -1), (2, 1), (-2, 1), (-2, -1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
cnt = 0

for i in range(8):
  X, Y = now[0] + moves[i][0], now[1] + moves[i][1]
  if X <= 8 and Y <= 8 and X >= 1 and Y >= 1:
    cnt += 1

print(cnt)


