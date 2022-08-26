n = int(input())

arr = list(map(int, input().split()))
start = 0
end = n - 1
answer = -1

while start <= end:
	mid = (start + end) // 2

	if arr[mid] == mid:
		answer = mid

	if arr[mid] > mid:
		end = mid - 1

	else:
		start = mid + 1

print(answer)
