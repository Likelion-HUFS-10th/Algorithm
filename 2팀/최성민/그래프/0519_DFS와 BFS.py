import sys
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m, v = tuple(map(int, input().split()))
tree = [[] for _ in range(n+1)]
dfs_visit = []
order = deque()
bfs_visit = []


for i in range(m):
	a, b = tuple(map(int, input().split()))

	tree[a].append(b)
	tree[b].append(a)

def dfs(start):
	dfs_visit.append(start)

	for i in sorted(tree[start]):
		if not i in dfs_visit:
			dfs(i)

def bfs(start):
	bfs_visit.append(start)
	order.append(start)
	tree[start].sort()

	while order:
		start = order.popleft()
		for i in sorted(tree[start]):
			if i not in bfs_visit:
				bfs_visit.append(i)
				order.append(i)

dfs(v)
bfs(v)

print(*dfs_visit)
print(*bfs_visit)
