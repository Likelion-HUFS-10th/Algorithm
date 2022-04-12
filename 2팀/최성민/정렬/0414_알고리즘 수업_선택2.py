import sys
from collections import deque

length, tms = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
order = deque()
idx = 1

def sorting():
	global idx

	pivot = nums.pop()
	if nums:
		max_val = max(nums)
	else:
		return

	if max_val > pivot:
		nums_idx = nums.index(max_val)
		nums[nums_idx] = pivot
		order.appendleft(max_val)
		idx += 1

	else:
		order.appendleft(pivot)

while True:
	if idx <= tms:
		if nums:
			sorting()
		else:
			break
	else:
		break

for i in nums[::-1]:
	order.appendleft(i)

if nums:
	for i in order:
		print(i, end=" ")

else:
	print(-1)
