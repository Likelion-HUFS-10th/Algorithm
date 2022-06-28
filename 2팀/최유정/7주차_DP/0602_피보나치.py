import sys
input = sys.stdin.readline

def func1(n):
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for i in range(2, n+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
    return dp[n]

t = int(input())
dp = [[0 for _ in range(2)] for _ in range(100000)]

for i in range(t):
    n = int(input())
    print(' '.join(map(str, func1(n))))