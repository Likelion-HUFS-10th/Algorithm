import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
virus = [
    list(map(int, input().split()))
    for _ in range(n)
]
s, x, y = map(int, input().split())
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

virus_loc = {}
for i in range(n):
    for j in range(n):
        if virus[i][j] != 0:
            if virus[i][j] in virus_loc: virus_loc[virus[i][j]].append((i, j))
            else: virus_loc[virus[i][j]] = [(i, j)]

def func1():
    for kn in range(k):
        if (kn + 1) in virus_loc:
            vl = deque()
            vl.append(deque(virus_loc.pop(kn+1)))
            while vl[0]:
                v = vl[0].popleft()
                for i in range(4):
                    nx, ny = v[0] + dx[i], v[1] + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and virus[nx][ny]==0:
                        virus[nx][ny] = kn+1
                        if (kn+1) in virus_loc: virus_loc[kn+1].append((nx, ny))
                        else: virus_loc[kn+1] = [(nx, ny)]
        else:
            continue

for time in range(s):
    func1()

print(virus[x-1][y-1])