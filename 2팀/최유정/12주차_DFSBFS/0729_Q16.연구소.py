import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy
# n이 세로 m이 가로
n, m = map(int, input().split())
lab = [
    list(map(int, input().split()))
    for _ in range(n)
]
empty = []
virus = deque()
for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            virus.append([i, j])
        if lab[i][j] == 0:
            empty.append([i, j])
walls = list(combinations(empty, 3))
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
result = []
ans = 0

def wall():
    while walls:
        wall = walls.pop()
        new_lab = copy.deepcopy(lab)
        for w in wall:
            new_lab[w[0]][w[1]] = 1
        bfs(new_lab)

def bfs(new_lab):
    global ans
    cnt = 0
    vir = copy.deepcopy(virus)
    while vir:
        x, y = vir.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if new_lab[nx][ny] == 0:
                    new_lab[nx][ny] = 2
                    vir.append([nx, ny])
    for i in new_lab:
        cnt += i.count(0)
    result.append(cnt)

wall()
print(max(result))