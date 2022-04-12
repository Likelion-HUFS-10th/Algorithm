import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
pcs = []

count = 0
answer = -1

for i in range(n-1, 0, -1):
	for j in range(i):
		if nums[j] > nums[j+1]:
			count += 1
			nums[j], nums[j+1] = nums[j+1], nums[j]

			if count == k:
				answer = f'{nums[j]} {nums[j+1]}'	

print(answer)

