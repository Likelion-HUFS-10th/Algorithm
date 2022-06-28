import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def func1(a, b):
    global cnt
    start = road[a][b]

    if a == m-1 and b == n-1:
        return 1
    if dp[a][b] != -1:
        return dp[a][b]
    dp[a][b] = 0
    for i in range(4):
        x = a + dy[i]
        y = b + dx[i]
        if 0 <= x < m and 0 <= y < n and start > road[x][y]:
            dp[a][b] += func1(x, y)
    return dp[a][b]


m, n = map(int, input().split()) 
cnt = 0
road = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]

print(func1(0, 0))

