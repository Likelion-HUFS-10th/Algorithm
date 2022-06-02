n = int(input())
nums = list(map(int, input().split()))
arr = [1] * n

for i in range(n):
	for j in range(i):
		if nums[j] < nums[i]:
			arr[i] = max(arr[i], arr[j] + 1)

print(max(arr))
