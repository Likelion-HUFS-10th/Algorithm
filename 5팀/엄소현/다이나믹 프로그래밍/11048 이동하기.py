import sys
input = sys.stdin.readline

def in_range(r, c):
  return 0 <= r < n and 0 <= c < m

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
  for j in range(m):
    if i == 0 and j == 0:
      dp[i][j] = maze[i][j]
    else:
      if in_range(i-1, j):
        dp[i][j] = max(dp[i-1][j] +  maze[i][j], dp[i][j])
      if in_range(i, j-1):
        dp[i][j] = max(dp[i][j-1] +  maze[i][j], dp[i][j])
      if in_range(i-1, j-1):
        dp[i][j] = max(dp[i-1][j-1] +  maze[i][j], dp[i][j])
      
print(dp[n-1][m-1])
