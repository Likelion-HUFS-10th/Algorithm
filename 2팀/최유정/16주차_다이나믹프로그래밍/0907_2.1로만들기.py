x = int(input())
dp = [0] * 30001

for i in range(2, x+1):
    if i % 5 == 0: dp[i] = min(dp[i-1]+1, dp[i//5]+1)
    elif i % 3 == 0: dp[i] = min(dp[i-1]+1, dp[i//3]+1)
    elif i % 2 == 0: dp[i] = min(dp[i-1]+1, dp[i//2]+1)
    else: dp[i] = dp[i-1] + 1

print(dp[x])