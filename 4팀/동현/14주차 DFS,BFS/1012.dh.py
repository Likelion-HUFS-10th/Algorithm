"""
연결되어 있는 1(배추)는 하나의 벌레가 관리 가능
DFS 알고리즘 사용
"""

t = int(input())

n, m, k = map(int, input().split())

array = []
for _ in range(m):
    line = []
    for _ in range(n):
        line.append(0)
    array.append(line)

# 배추 심기
for _ in range(k):
    b, a = map(int, input().split())
    array[a][b] = 1

# DFS 알고리즘 사용
def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m: # 범위를 벗어나는 경우
        return False
        
    if array[y][x] == 1:
        array[y][x] = 0
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)