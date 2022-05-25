import queue
import sys
from collections import deque
input = sys.stdin.readline
m, n, k = tuple(map(int, input().split()))
array = [[0 for _ in range(n)] for _ in range(m) ]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = []
for _ in range(k):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    for i in range(x1, x2):
        for j in range(y1, y2):
            array[j][i] = 1

for i in range(m):
    for j in range(n):
        if array[i][j] == 0:
            queue = deque([(i, j)])
            array[i][j] = 1
            cnt = 0
            while queue:
                (x, y) = queue.popleft()
                cnt += 1
                for l in range(4):
                    if 0 <= x+dx[l] < m and 0 <= y+dy[l] < n and array[x+dx[l]][y+dy[l]] == 0:
                        queue.append((x+dx[l], y+dy[l]))    
                        array[x+dx[l]][y+dy[l]] = 1
            answer.append(cnt)

answer.sort()
print(len(answer))
print(*answer)