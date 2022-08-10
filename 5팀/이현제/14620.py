from audioop import cross
from collections import deque

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
cross_sum = deque()
cross_xy = deque()
min_sum = 0

n = int(input())
site = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(1,n - 1):
    for j in range(1, n - 1):
        one_sum = site[i][j] + site[i + dy[0]][j + dx[0]] + site[i + dy[1]][j + dx[1]] + site[i + dy[2]][j + dy[2]] + site[i + dy[3]][j + dx[3]] 
        cross_sum.append(one_sum)
        cross_xy.append((j,i))

print(cross_sum, cross_xy)

def dfs()