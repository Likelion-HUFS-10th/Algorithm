import sys
from collections import deque
input=sys.stdin.readline

def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                next = list(set(graph[n]) - set(visited))
                next.sort()
                queue += next
    return visited

def dfs(graph, root):
    visited = []
    stack = [root]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                next = list(set(graph[n]) - set(visited))
                next.sort(reverse=True)
                stack += next
    return visited



n, m, v = map(int, input().split())
graph = {}
for i in range(m):
    num1, num2 = map(int, input().split())
    if num1 not in graph:
        graph[num1] = [num2]
    elif num2 not in graph[num1]:
        graph[num1].append(num2)

    if num2 not in graph:
        graph[num2] = [num1]
    elif num1 not in graph[num2]:
        graph[num2].append(num1)


print(" ".join(str(i) for i in dfs(graph, v)))
print(" ".join(str(i) for i in bfs(graph, v)))
