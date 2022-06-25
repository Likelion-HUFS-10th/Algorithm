from itertools import combinations_with_replacement

n = int(input())

nums = [1, 5, 10, 50]
temp = list(combinations_with_replacement(nums, n))
result = []

for i in temp:
	result.append(sum(i))
print(len(set(result)))
