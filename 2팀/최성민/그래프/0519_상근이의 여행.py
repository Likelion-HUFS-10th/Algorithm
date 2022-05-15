import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
	n, m = tuple(map(int, input().split()))
	ways = [[] for _ in range(n+1)]

	visited = [0] * (n+1)

	for _ in range(m):
		a, b = tuple(map(int, input().split()))
		ways[a].append(b)
		ways[b].append(a)

	def dfs(idx, cnt):
		visited[idx] = 1

		for i in ways[idx]:
			if not visited[i]:
				cnt = dfs(i, cnt+1)
		
		return cnt

	result = dfs(1, 0)
	print(result)

	# def dfs(v, cnt):
	# 	global result
	# 	if not v in visited:
	# 		visited.append(v)

	# 	if len(visited) == n:
	# 		print(f'v = {v} result = {result}, cnt = {cnt}')
	# 		result = min(result, cnt)
	# 		return

	# 	order.append(v)
		
	# 	while order:
	# 		next_v = order.popleft()
	# 		dfs(next_v, cnt+1)
	# 		visited.pop()
	# 		dfs(next_v, cnt)
	
	# order.append(1)
	# dfs(1, 0)
	# print(result)

