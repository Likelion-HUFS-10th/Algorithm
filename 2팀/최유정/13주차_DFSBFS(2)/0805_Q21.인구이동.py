#https://www.acmicpc.net/problem/16234
import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())
country = [
    list(map(int, input().split()))
    for _ in range(n)
]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def func1(a, b):
    q = deque()
    q.append([a, b])
    visited[a][b] = True
    total = country[a][b]
    union = [(a, b)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if l <= abs(country[nx][ny] - country[x][y]) <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    total += country[nx][ny]
                    union.append((nx, ny))
    for u1, u2 in union:
        country[u1][u2] = total // len(union)
    return len(union)

day = 0
while True:
    check = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]: check += (func1(i, j)-1)
    if check == 0:
        print(day)
        break
    else:
        day += 1