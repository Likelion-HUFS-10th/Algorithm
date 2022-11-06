# https://www.acmicpc.net/problem/16236
from collections import deque

n = int(input())
place_list = [list(map(int, input().split())) for _ in range(n)]
shark_size = 2
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 0

for x in range(n):
    for y in range(n):
        if place_list[x][y] == 9:
            shark_x = x
            shark_y = y

def findFish(shark_x, shark_y, shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    q = deque()
    q.append([shark_x, shark_y])
    visited[shark_x][shark_y] = 1
    fish_list = []

    while q:
        sx, sy = q.popleft()
        for i in range(4):
            nx, ny = sx + dx[i], sy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if place_list[nx][ny] <= shark_size:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[sx][sy] + 1
                    if place_list[nx][ny] < shark_size and place_list[nx][ny] != 0:
                        fish_list.append([nx, ny, distance[nx][ny]])

    fish_list.sort(key=lambda x: (-x[2], -x[0], -x[1]))
    return fish_list

cnt = 0
while True:
    fish = findFish(shark_x, shark_y, shark_size)

    if len(fish) == 0:
        break

    fx, fy, dis = fish.pop()
    place_list[fx][fy] = 0
    time += dis

    place_list[shark_x][shark_y] = 0
    shark_x, shark_y = fx, fy
    cnt += 1

    if cnt == shark_size:
        shark_size += 1
        cnt = 0

print(time)