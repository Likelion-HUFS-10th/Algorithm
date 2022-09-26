from collections import deque
from copy import deepcopy

n = int(input())
course = [[] for _ in range(n+1)]
time = [0] * (n+1)
entry = [0] * (n+1)
q = deque()
for i in range(n):
    list_c = list(map(int, input().split()))
    time[i+1] = list_c[0]
    for j in range(1, len(list_c)-1):
        course[list_c[j]].append(i+1)
        entry[i+1] += 1

result = deepcopy(time)

for a in range(1, n+1):
    if entry[a] == 0:
        q.append(a)

while q:
    c = q.popleft()
    for i in course[c]:
        result[i] = max(result[i], time[i] + result[c])
        entry[i] -= 1
        if entry[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(result[i])