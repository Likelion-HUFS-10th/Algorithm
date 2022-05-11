import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())

tree = [[] for _ in range(n+1)]
parents = [0] * (n+1)
parents[1] = 1


for _ in range(n-1):
	x, y = tuple(map(int, input().split()))
	tree[x].append(y)
	tree[y].append(x)

def dfs(curr, tree, parents):
	for node in tree[curr]:
		if parents[node] == 0:
			parents[node] = curr
		
			dfs(node, tree, parents)

dfs(1, tree, parents)

print(*parents[2:])
