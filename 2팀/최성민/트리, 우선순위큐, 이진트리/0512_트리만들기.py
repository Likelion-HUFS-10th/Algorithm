n, m = tuple(map(int,input().split()))

if m == 2:
	for i in range(n-1):
		print(i, i+1)

if m > 2:
	print("0 1")
	for i in range(1, m):
		print("1", i+1)
	for j in range(m, n-1):
		print(j, j+1)