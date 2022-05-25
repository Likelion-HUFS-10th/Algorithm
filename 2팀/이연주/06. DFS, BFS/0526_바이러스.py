import sys
from collections import deque
input = sys.stdin.readline
linked = dict()

n = int(input())
m = int(input())

for i in range(1, n+1):
    linked[i] = []
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    linked[x].append(y)
    linked[y].append(x)
answer = 0
queue = deque([1])
visited = [0] * (n+1)
visited[1] = 1
while queue:
    x = queue.popleft()
    answer += 1
    for node in linked[x]:
        if visited[node] == 0:
            queue.append(node)
            visited[node] = 1

answer = answer -1 if answer > 0 else answer
print(answer)          