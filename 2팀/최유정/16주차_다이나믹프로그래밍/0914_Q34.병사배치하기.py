import sys
input = sys.stdin.readline

n = int(input())
sol = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if sol[i] < sol[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
