import sys
input = sys.stdin.readline

n = int(input())
tri = []
dp = []
for i in range(n):
    tri.append(list(map(int, input().split())))
    dp.append([0]*(len(tri[i])+2))

dp[0][1] = tri[0][0]

for h in range(1, n):
    for w in range(1, h+2):
        dp[h][w] = max(dp[h-1][w], dp[h-1][w-1]) + tri[h][w-1]

print(max(dp[n-1]))