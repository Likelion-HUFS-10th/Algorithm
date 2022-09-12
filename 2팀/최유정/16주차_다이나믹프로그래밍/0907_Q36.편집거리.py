# 삽입, 삭제, 교체
a = input()
b = input()

la, lb = len(a), len(b)
dp = [[float('INF')]*(la+1) for _ in range(lb+1)]

# 첫 글자 비교
if a[0] == b[0]: dp[1][1] = 0
else: dp[1][1] = 1


for j in range(1, la+1):
    for i in range(1, lb+1):
        if dp[i][j] != float('INF'): continue
        if b[i-1] == a[j-1]:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

print(dp[lb][la])

