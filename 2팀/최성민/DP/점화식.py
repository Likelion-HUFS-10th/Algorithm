# t0 1
# t1 1
# t2 2
# t3 5 
# t4 14
# t5 42
# t6 132

n = int(input())
dp = [0] * (n+1)


for i in range(n+1):
	if i == 0 or i == 1:
		dp[i] = 1
	else:
		ans = 0
		for j in range(i-1, -1, -1):
			ans += dp[j] * dp[i-j-1]
		dp[i] = ans

print(dp[n])