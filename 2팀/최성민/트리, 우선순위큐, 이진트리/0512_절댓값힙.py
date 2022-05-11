import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []

def func(arr):
	result = heapq.heappop(arr)[1]

	return result

for i in range(n):
	order = int(input())

	if order == 0:
		if not arr:
			print(0)

		else:
			print(func(arr))
	else:
		heapq.heappush(arr, (abs(order), order))


# 