
import sys
n = int(sys.stdin.readline())
glass = []
dp = [0] * n

for _ in range(n):
    glass.append(int(sys.stdin.readline()))

if n == 1:
    print(glass[0])

if n == 2:
    print(glass[0]+glass[1])
else:
    dp[0] = glass[0]
    dp[1] = glass[0]+glass[1]
    dp[2] = max(glass[0]+glass[2], glass[1]+glass[2], dp[1])

    for i in range(3, n):
        dp[i] = max(dp[i-3]+glass[i-1]+glass[i], dp[i-2]+glass[i], dp[i-1] )
    print(dp[n-1])


#--------------------------------------------------------------
# [방법 찾기]
# 포도주 한잔 dp[1] = glass[0]
# 포도주 두잔 dp[2] = glass[0]+glass[1],
# 포도주 세잔 dp[3] = max(glass[0]+glass[1],glass[0]+glass[2],glass[1]+glass[2])
# 포도주 네잔 dp[4] = (dp[0]+glass[2]+glass[3],dp[1]+glass[3])
