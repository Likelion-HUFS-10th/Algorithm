import sys
input = sys.stdin.readline

n = int(input())
stocks = list(map(int, input().split()))
stocks.sort()

m = int(input())
buy = list(map(int, input().split()))

def searching(item, start, end):
	if start > end:
		print("no", end=" ")
		return None

	mid = (start + end) // 2

	if item == stocks[mid]:
		print("yes", end=" ")

	elif item < stocks[mid]:
		searching(item, start, mid-1)

	else:
		searching(item, mid+1, end)

for item in buy:
	searching(item, 0, n-1)

