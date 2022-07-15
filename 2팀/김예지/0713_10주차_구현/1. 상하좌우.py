#14:43

N = int(input())
guide = list(map(str, input().split()))
now = [1, 1]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

alpha_dict = {"R" : 0, "L" : 1, "D" : 2, "U" : 3}

for i in guide:
  a = alpha_dict[i]
  X, Y = now[0] + dx[a], now[1] + dy[a]
  if X <= N and Y <= N and X >= 1 and Y >= 1:
    now[0], now[1] = X, Y

for j in now:
  print(j, end = " ")