n = int(input())

house = list(map(int, input().split()))

house.sort()

print(house[(n-1) // 2])

# answer = 1e9
# for i in house:
# 	_sum = 0

# 	for j in house:
# 		_sum += abs(i - j)

# 	if _sum < answer:
# 		answer = _sum
# 		idx = i

# print(idx)
