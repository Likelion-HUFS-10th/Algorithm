list_len, times = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

new_nums = []
order = []

for i in range(list_len-1, 0, -1):
	max_val = nums.pop()
	max_nums = max(nums[0:i])

	if max_nums > max_val:
		idx = nums.index(max_nums)
		order.append((max_val, max_nums))
		nums[idx] = max_val
		new_nums.append(max_nums)
	
	else:
		new_nums.append(max_val)

new_nums.append(nums[0])

if len(order) < times:
	print(-1)
else:
	for i in order[times-1]:
		print(i, end=" ")
