n = int(input())
k = list(map(int, input().split()))
dp = [0] * 101

dp[1], dp[2] = k[0], k[1]

for i in range(3, n+1):
    dp[i] = max(k[i-1]+dp[i-2], k[i-1]+dp[i-3])

print(max(dp[n-1], dp[n]))