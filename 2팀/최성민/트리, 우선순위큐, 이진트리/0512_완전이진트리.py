from collections import deque

n = int(input())
buildings = list(map(int, input().split()))
visit = []

def tree(arr, level):
	idx = len(arr) // 2

	visit.append((arr[idx], level))

	if idx >= 1:
		tree(arr[:idx], level+1)
		tree(arr[idx+1:], level+1)

tree(buildings, 1)

visit.sort(key = lambda x: x[1])
visit = deque(visit)

for i in range(n):
	for j in range(2 ** i):
		print(visit.popleft()[0], end=" ")
	print()
	