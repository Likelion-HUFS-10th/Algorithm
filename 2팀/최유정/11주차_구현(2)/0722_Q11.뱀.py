import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
dirs = [list(input().split()) for _ in range(l)]
for dir in dirs:
    dir[0] = int(dir[0])
dirs.append([100000, 'X'])
map = [[0]*n for _ in range(n)]
for apple in apples:
    map[apple[0]-1][apple[1]-1] = 1
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def check(dir, x):
    if dir == 'D':
        x = (x + 1) % 4
    if dir == 'L':
        x = (x - 1) % 4
    return x


def func1():
    now_time = 0
    snake = deque()
    snake.append([0, 0])
    now_dir, dir_x = 'D', -1
    for dir in dirs:
        if dir[0] == 0:
            now_dir = dir[1]
            continue
        dir_x = check(now_dir, dir_x)
        for _ in range(now_time, dir[0]):
            now_time += 1
            head = [snake[0][0]+ dx[dir_x], snake[0][1]+dy[dir_x]]
            snake.appendleft(head)
            if head[1] < 0 or head[1] > (n-1) or head[0] < 0 or head[0] > (n-1):
                return now_time
            if map[head[0]][head[1]] == 1:
                map[head[0]][head[1]] = 0
            elif snake[0] == snake[-1]:
                return now_time
            else:
                snake.pop()
        now_dir = dir[1]
    return now_time

print(func1())