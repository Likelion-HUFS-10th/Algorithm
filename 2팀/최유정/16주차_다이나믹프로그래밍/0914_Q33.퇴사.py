# https://www.acmicpc.net/problem/14501

n = int(input())
works = []
for i in range(n):
    works.append(list(map(int, input().split())))

for j in range(n):
    if j + works[j][0] > n:
        works[j] = [0, 0]

dp = [0] * (n+1)
dp[n-1] = works[n-1][1]

for i in range(n-2, -1, -1):
    dp[i] = max(dp[works[i][0]+i:]) + works[i][1]
print(max(dp))
