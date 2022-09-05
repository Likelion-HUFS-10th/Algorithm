n, m = map(int, input().split())
dp = [float('INF')] * 10001
value = []
for _ in range(n):
    a = int(input())
    value.append(a)
    dp[a] = 1

for v in value:
    for i in range(2, m+1):
        dp[i] = min(dp[i], dp[i-v]+1)

if dp[m] == float('INF'):
    print(-1)
else:
    print(dp[m])