n = int(input())
dp = [0] * (n+1)

for i in range(2 ,n+1):
    dp[i] = dp[i-1]+1

    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)


    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)

print(dp[n])



#--------------------------
# dp[1] = 0
# dp[2] = 2/2 = 1
# dp[3] = 3/3 = 1
# dp[4] = 4/2 -> 2/2 -> 1 총 2번
# dp[5] = 5-1 -> 4/2 -> 2/2 -> 1 총 3번
# dp[6] = 6/2 -> 3/3 -> 1 총 2번
#       = 6/3 -> 2/2 -> 1 총 2번
# dp[7] = 7-1 -> 6 방법 2개 총 3번

