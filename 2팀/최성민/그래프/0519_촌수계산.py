from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a, b = tuple(map(int, input().split()))

t = int(input())

family = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0
result = -1

for _ in range(t):
	parent, child = tuple(map(int, input().split()))
	family[parent].append(child)
	family[child].append(parent)

def dfs(v, cnt):
	global result
	cnt += 1
	visited[v] = True

	if v == b:
		result = cnt - 1
	
	for i in family[v]:
		if not visited[i]:
			dfs(i, cnt)
	
dfs(a, 0)
print(result)
