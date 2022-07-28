import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #n은 세로 m은 가로
mold = [list(map(int, ' '.join(input()).split())) for _ in range(n)]

cnt = 0
def dfs(x, y):
    if (x >= n) or (x < 0) or (y >= m) or (y < 0) or(mold[x][y] == 1):
        return False
    if mold[x][y] == 0:
        mold[x][y] = 1
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
    return True

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)