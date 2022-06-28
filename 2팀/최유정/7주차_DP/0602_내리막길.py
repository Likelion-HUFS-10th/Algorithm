import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def func1(a, b):
    global cnt
    start = road[a][b]

    if a == m-1 and b == n-1:
        cnt += 1

    for i in range(4):
        x = a + dy[i]
        y = b + dx[i]

        if 0 <= x < m and 0 <= y < n and start > road[x][y]:
            func1(x, y)

    return cnt

m, n = map(int, input().split()) 
cnt = 0
road = [list(map(int, input().split())) for _ in range(m)]

print(func1(0, 0))

