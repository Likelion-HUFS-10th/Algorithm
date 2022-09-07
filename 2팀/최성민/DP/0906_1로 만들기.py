'''
5로 나누어 떨어지면 5로 나누기
3으로 나누어 떨어지면 3으로 나누기
2로 나누어 떨어지면 2로 나누기
1 빼기
'''

x = int(input())

dp = [0] * (x + 1)

for x in range(2, x+1):
	dp[x] = dp[x-1] + 1

	if (x % 2) == 0:
		dp[x] = min(dp[x], dp[x // 2] + 1)
		
	if (x % 3) == 0:
		dp[x] = min(dp[x], dp[x // 3] + 1)

	if (x % 5) == 0:
		dp[x] = min(dp[x], dp[x // 5] + 1)

print(dp[x])