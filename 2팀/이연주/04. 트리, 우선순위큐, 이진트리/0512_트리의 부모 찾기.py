import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
parents = [0] * N
dfs = {}
for _ in range(N-1):
    (n1, n2) = tuple(map(int, input().split()))
    if n1 in dfs.keys():
        dfs[n1].append(n2)
    else:
        dfs[n1] = [n2]
    if n2 in dfs.keys():
        dfs[n2].append(n1)
    else:
        dfs[n2] = [n1]
    
stack = deque()

stack.append(1)
while stack:
    i = stack.popleft()
    for linked in dfs[i]:
        if parents[linked-1] == 0:
            parents[linked-1] = i
            stack.append((linked))
    
for j in range(1, N):
    print(parents[j])
