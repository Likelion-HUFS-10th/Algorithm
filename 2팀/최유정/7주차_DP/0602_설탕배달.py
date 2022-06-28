import sys
input = sys.stdin.readline

def func1(n):
    dp[3] = dp[5] = 1
    for i in range(6, n+1):
        if i % 3 == 0:
            dp[i] = i//3
        if i % 5 == 0:
            dp[i] = i//5
        else:
            if dp[i-3] != -1 and dp[i-5] != -1:
                dp[i] = min(dp[i-3], dp[i-5]) + 1
    return(dp[n])
    

dp = [-1] * 100000
n = int(input())
print(func1(n))