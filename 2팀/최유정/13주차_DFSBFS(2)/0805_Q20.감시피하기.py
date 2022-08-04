from itertools import combinations
from collections import deque

n = int(input())
hall = [
    list(input().split())
    for _ in range(n)
]
t_list, x_list = [], []
for i in range(n):
    for j in range(n):
        if hall[i][j] == 'T': t_list.append((i, j))
        elif hall[i][j] == 'X': x_list.append((i, j))
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def check():
    teacher = deque(t_list)
    while teacher:
        a, b = teacher.popleft()
        for i in range(4):
            na, nb = a, b
            while True:
                nx, ny = na + dx[i], nb + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if hall[nx][ny] == 'S': return False
                    elif hall[nx][ny] == 'O': break
                    na, nb = nx, ny
                else: break
    return True
            

result = False
for p in list(combinations(x_list, 3)):
    for x, y in p:
        hall[x][y] = 'O'
    if check():
        result = True
        break
    for x, y in p:
        hall[x][y] = 'X'

if result:
    print("YES")
else:
    print("NO")