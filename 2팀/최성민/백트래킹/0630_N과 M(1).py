n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]
temp = []
ans = []

def bfs(m):
	if len(temp) == m:
		print(*temp)
		
		return

	for i in arr:
		if not i in temp:
			temp.append(i)
			bfs(m)
			temp.pop()
		

bfs(m)
