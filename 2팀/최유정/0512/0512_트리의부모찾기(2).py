import sys
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
parent = [0] * (n+1)
parent_node = [1]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

while parent_node:
    root_num = parent_node.pop()
    for i in tree[root_num]:
        if parent[i] == 0:
            parent[i] = root_num
            parent_node.append(i)


for i in range(2, n+1):
    print(parent[i])