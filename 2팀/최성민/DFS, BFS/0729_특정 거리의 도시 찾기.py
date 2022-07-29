from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n):
	a, b = map(int, input().split())

	graph[a].append(b)

stack = []

dist = [-1] * (n + 1)
dist[x] = 0

q = deque()
while q:
	now = q.popleft()

	for i in graph[now]:
		if dist[i] == -1:
			dist[i] = dist[now] + 1
			q.append(i)

check = False
for i in range(1, n + 1):
	if dist[i] == k:
		print(i)
		check = True

if check == False:
	print(-1)