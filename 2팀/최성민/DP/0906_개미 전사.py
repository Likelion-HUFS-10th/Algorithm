n = int(input())
arr = list(map(int, input().split()))

dp = [0] * 100

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for x in range(2, n):
	dp[x] = max(dp[x-1], dp[x-2] + arr[x])

print(dp[n-1])
