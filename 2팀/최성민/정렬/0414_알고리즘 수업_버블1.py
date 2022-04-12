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

# ------------------------------------------------------------

# for i in range(n-1, 0, -1):
# 	strd, idx = nums[0], 0
	
# 	for j in nums[idx+1::]:
# 		if strd < j:
# 			strd, idx = j, nums.index(j)
# 			continue

# 		else:
# 			pcs.append((j, strd))
# 			nums.insert(nums.index(j)+1, strd)
# 			del nums[idx]
# 			idx = nums.index(strd)			
	
# if len(pcs) < k:
# 	print(-1)
# else:
# 	for j in pcs[k-1]:
# 		print(j, end=" ")

# ------------------------------------------------------------

# for i in range(n-1, 0, -1):
# 	strd, idx = nums[0], 0
	
# 	for j in range(1, i+1):
# 		if strd < nums[j]:
# 			strd, idx = nums[j], j
# 			continue

# 		else:
# 			pcs.append((nums[j], strd))

# 			nums.insert(j+1, strd)
# 			del nums[idx]
# 			idx = idx + 1

# if len(pcs) < k:
# 	print(-1)
# else:
# 	for j in pcs[k-1]:
# 		print(j, end=" ")

# ------------------------------------------------------------

# for i in range(n-1, 0, -1):
# 	strd = max(nums[:i+1])
# 	idx = nums.index(strd)

# 	for j in nums[idx+1::]:
# 		pcs.append(j)

# 		if len(pcs) == k:
# 			print(j, strd)

# 	del nums[idx]

# if len(pcs) < k:
# 	print(-1)

# ------------------------------------------------------------

# idx = 0

# for i in range(n-1, 0, -1):
# 	strd = nums[0]

# 	for j in range(1, i+1):
# 		if strd < nums[j]:
# 			order.append(strd)
# 			strd = nums[j]

# 		else:
# 			order.append(nums[j])
# 			idx += 1

# 		if idx == k:
# 			print(nums[j], strd)
# 			break

# 	if idx == k:
# 		break
	
# 	order.append(strd)
# 	nums = order
# 	order = []

# if idx < k:
# 	print(-1)

# ------------------------------------------------------------

# while len(pcs) < k:
# 	if nums == sorted(nums):
# 		break

# 	strd = nums[0]

# 	for i in nums[1::]:

# 		if strd < i:
# 			order.append(strd)
# 			strd = i

# 		else:
# 			pcs.append((i, strd))
# 			order.append(i)
			
# 	order.append(strd)
# 	nums = order
# 	order = []

# ------------------------------------------------------------

# for i in range(n-1, 0, -1):
# 	isChanged = False

# 	for j in range(i):
# 		if nums[j] > nums[j+1]:
# 			order.append((nums[j+1], nums[j]))
# 			nums[j], nums[j+1] = nums[j+1],nums[j]
# 			isChanged = True

# 	if not isChanged:
# 		break
	
# if len(order) < k:
# 	print(-1)
# else:
# 	for i in order[k-1]:
# 		print(i, end=" ")
