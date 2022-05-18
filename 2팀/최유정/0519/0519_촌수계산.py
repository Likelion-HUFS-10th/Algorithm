import sys
input=sys.stdin.readline
from collections import deque

def bfs(num1, num2, family):
    q = deque([num1])
    visited[num1] = True
    dof = 0
    while q:
        dof += 1
        for _ in range(len(q)):
            next_num = q.popleft()
            if next_num == num2:
                return dof - 1
            for i in family[next_num]:
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)

    return -1


n = int(input())
family = [[] for _ in range(n+1)]
num1, num2 = map(int, input().split())
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    family[a].append(b)
    family[b].append(a)

visited = [False] * (n+1)
print(bfs(num1, num2, family))