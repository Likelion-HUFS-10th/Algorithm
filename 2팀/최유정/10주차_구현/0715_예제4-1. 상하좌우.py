row = int(input())
map = [
    [0, 0, 0, 0, 0]
    for _ in range(row)
]
dirs = input().split(' ')
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]  #RLUD
x, y = 0, 0
change = {'R':0, 'L':1, 'U':2, 'D':3}
num_dir = [change[n] for n in dirs]

for dir in num_dir:
    nx, ny = x + dx[dir], y + dy[dir]
    if nx >= 0 and nx <= row-1 and ny >= 0 and ny <= row-1:
        x, y = nx, ny

print(x+1, y+1)