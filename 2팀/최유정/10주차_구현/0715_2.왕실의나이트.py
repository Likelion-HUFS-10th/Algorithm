now = input()

dirs = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
x, y = int(ord(now[0])) - int(ord('a')) + 1, int(now[1])
cnt = 0

for dir in dirs:
    nx = x + dir[0]
    ny = y + dir[1]

    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        cnt += 1

print(cnt)