n, k = map(int, input().split())

times_arr = []
dev_arr = []
ans = 1

for i in range(n-1, n-k, -1):
	times_arr.append(i)

for i in range(1, k):
	dev_arr.append(i)

t, d = 1, 1
for i in range(k-1):
	t *= times_arr[i]
	d *= dev_arr[i]

ans = t / d


print(int(ans))

