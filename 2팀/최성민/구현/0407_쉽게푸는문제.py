start, end = tuple(map(int, input().split()))

nums = []
sum = 0

for i in range(1, 1000+1):
	for j in range(i):
		nums.append(i)

for i in range(start-1, end):
	sum += nums[i]

print(sum)
