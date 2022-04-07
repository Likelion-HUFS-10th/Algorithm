from collections import deque

T = int(input())

def popping(n_list, isR):
	if isR:
		n_list.pop()

	else:
		n_list.popleft()

for _ in range(T):
	p, n = input(), int(input())
	input_list = input()
	
	if n:
		nums = deque(map(int, input_list[1:-1].strip().split(',')))
	else:
		nums = deque()

	isReversed = False
	isErred = False

	for j in p:
		if j == "R":
			isReversed = not isReversed

		elif j == 'D':
			if not nums:
				isErred = True
				break

			else:
				popping(nums, isReversed)
	
	if isErred:
		print('error')
	else:
		if isReversed:
			nums.reverse()
		if nums:
			print("[", end="")
			for i in range(len(nums)-1):
				print(nums[i], end=",")
			print(f"{nums[-1]}]")
		else:
			print([])
	
