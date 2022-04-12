import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
count = 0
answer = -1


def merge_sort(nums, first, last):
	if first >= last:
		return

	merge_sort(nums, first, (first+last) // 2)
	merge_sort(nums, (first+last) // 2 + 1, last)

	return merge(nums, first, last)

def merge(nums, first, last):
	global count, answer
	mid = (first+last) // 2
	i, j = first, mid+1
	temp = []
	
	while i <= mid and j <= last:
		if nums[i] <= nums[j]:
			temp.append(nums[i])
			i += 1
			count += 1

		else:
			temp.append(nums[j])			
			j += 1
			count += 1
		
		if count == k:
			answer = f'{temp[-1]}'

	while i <= mid:
		temp.append(nums[i])		
		i += 1
		count += 1
		
		if count == k:
			answer = f'{temp[-1]}'

	while j <= last:
		temp.append(nums[j])
		j += 1
		count += 1
		
		if count == k:
			answer = f'{temp[-1]}'


	for i in range(first, last+1):
		nums[i] = temp[i-first]
	
	return answer
		
print(merge_sort(nums, 0, n-1))
