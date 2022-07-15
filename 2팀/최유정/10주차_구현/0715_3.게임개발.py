row, col = map(int, input().split())
x, y, now_dir = map(int, input().split()) 
map = [
    list(map(int, input().split()))
    for _ in range(row)
]
map[x][y] = 2

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn():
    global now_dir
    now_dir -= 1
    if now_dir == -1:
        now_dir = 3
move = 0
cnt = 1
while True:
    turn()
    nx, ny = x + dx[now_dir], y + dy[now_dir]
    if map[nx][ny] == 0:
        x, y = nx, ny
        map[x][y] = 2
        move += 1
        cnt = 0

    else:
        cnt += 1
    if cnt == 4:
        nx, ny = x - dx[now_dir], y - dy[now_dir]
        if map[nx][ny] == 0 or map[nx][ny] == 2:
            x, y = nx, ny
            move += 1
        else:
            break
        cnt = 0

print(move)