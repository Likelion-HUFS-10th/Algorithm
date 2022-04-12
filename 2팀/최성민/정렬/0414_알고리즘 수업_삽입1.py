
import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
pcs = []
count = 0
answer = -1

for i in range(1, n):
	key = nums[i]
	j = i - 1

	while nums[j] > key and j >= 0:
		nums[j+1] = nums[j]
		j -= 1
		count += 1

		if count == k:
			answer = f'{nums[j+1]}'
	
	if nums[j+1] != key:
		nums[j+1] = key
		count += 1
		
		if count == k:
			answer = f'{nums[j+1]}'

print(answer)
