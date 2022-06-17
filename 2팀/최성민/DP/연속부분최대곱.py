import sys
input = sys.stdin.readline

n = int(input())
arr = [float(input().rstrip()) for _ in range(n)]
dp = [0] * n
dp[0] = arr[0]
ans = 0

for i in range(1, n):
	dp[i] = max(dp[i-1] * arr[i], arr[i])

print("%.3f" % max(dp))

# ----------------

# n = int(input())
# arr = [float(input().rstrip()) for _ in range(n)]

# for i in range(1, n):
# 	arr[i] = max(arr[i-1] * arr[i], arr[i])

# print("%.3f" % max(arr))