def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(n):
        if graph[i-1][j] == 1:
            union_parent(parent, i, j+1)

route = list(map(int, input().split()))

answer = "YES"
for i in range(1, m-1):
    if parent[i] != parent[i+1]:
        answer = "NO"

print(answer)