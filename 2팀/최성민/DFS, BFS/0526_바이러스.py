import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
	a, b = map(int, input().split())

	graph[a].append(b)
	graph[b].append(a)

visited = [0 for _ in range(n+1)]
cnt = 0

def dfs(v):
	global cnt

	visited[v] = 1
	target = graph[v]

	for comp in target:
		if not visited[comp]:
			dfs(comp)
			cnt += 1

dfs(1)
print(cnt)

