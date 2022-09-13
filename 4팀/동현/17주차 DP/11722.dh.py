"""
dp[i]와 dp[j]+1을 비교해주는 부분 참고
"""
n = int(input())

A = list(map(int,input().split()))

dp = [0]* 1000

for i in range(n):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp)+1)