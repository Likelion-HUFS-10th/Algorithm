n ,m = tuple(map(int, input().split()))
miro = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [0] * m
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[0][0] = miro[0][0]
        elif i == 0:
            dp[0][j] = dp[0][j - 1] + miro[0][j]
        elif j == 0:
            dp[i][0] = dp[i - 1][0] + miro[i][0]
        else:
            dp[i][j] = max(dp[i - 1][j] + miro[i][j], dp[i][j - 1] + miro[i][j], dp[i - 1][j - 1] + miro[i][j])

print(dp[n - 1][m - 1])