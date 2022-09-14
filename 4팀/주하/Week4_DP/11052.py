n = int(input())
cost = list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], cost[j-1]+dp[i-j])

print(max(dp))


# 1 5 6 7
# 0 1 2 3 i
# for i in range(n):
#     for j in range(1,i+1):
#         cal = n - i
#         re = cal + i
#         if n == re:
#             dp[i] = dp[i] + cost[i] + cost[n-i]
#         elif n % i == 0:
#             result = n // i
#             dp[i] = cost[i-1] * result
# print(max(dp))
