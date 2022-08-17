t = int(input())

for _ in range(t):
    n,m,k = map(int, input().split())

    cabbages = [[0] * m for _ in range (n)]
    for _ in range(k):
        x, y = map(int,input().split())
        cabbages[x][y] = 1


def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if cabbages[x][y] == 1:
        cabbages[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)

    
