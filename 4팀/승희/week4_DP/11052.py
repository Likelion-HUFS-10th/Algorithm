n = int(input()) #카드의 개수
prices = [0]
prices.extend(list(map(int,input().split())))

dp = [0 for _ in range(n+1)]
dp[1] = prices[1]

for i in range(2,n+1):
    for j in range(1,i+1):
        dp[i] = max(prices[i], dp[i-j]+dp[j], dp[i])

print(dp[n])
