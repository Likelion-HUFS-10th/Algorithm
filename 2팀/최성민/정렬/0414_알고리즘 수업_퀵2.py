# 3% 오답

import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
count = 0
answer = -1

def quick_sort(nums, first, last):		
	if first < last:		
		pivot = partition(nums, first, last)
		
		if type(pivot) == int:
			quick_sort(nums, first, pivot-1)
			quick_sort(nums, pivot + 1, last)
	

	return nums

def partition(nums, first, last):
	global count, answer
	pivot = nums[last]
	i = first - 1
	for j in range(first, last):
		if (nums[j] <= pivot):
			i += 1
			nums[i], nums[j] = nums[j], nums[i]
			count += 1
			if count == k:
				answer = nums
				return answer
	
	if (i + 1 != last):
		nums[i+1], nums[last] = nums[last], nums[i+1]
		count += 1
		if count == k:
			answer = nums
			return answer
	
	return i+1

quick_sort(nums, 0, n-1)

if answer == -1:
	print(answer)
else:
	for i in answer:
		print(i, end=" ")
