startIdx = 0
endIdx = 0

def first(arr, target, start, end):
	global startIdx
	if start > end:
		return None

	mid = (start + end) // 2

	if (mid == 0 or target > arr[mid - 1]) and target == arr[mid]:
		startIdx = mid
		return
	
	elif arr[mid] < target:
		first(arr, target, mid + 1, end)
	
	else:
		first(arr, target, start, mid - 1)

def last(arr, target, start, end):
	global endIdx

	if start > end:
		return None

	mid = (start + end) // 2

	if (mid == n -1 or target < arr[mid + 1]) and target == arr[mid]:
		endIdx = mid
		return

	elif arr[mid] <= target:
		last(arr, target, mid + 1, end)
	
	else:
		last(arr, target, start, mid - 1)

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = n - 1

first(arr, m, start, end)
last(arr, m, start, end)

answer = endIdx - startIdx

if answer == 0:
	print(-1)
else:
	print(answer + 1)