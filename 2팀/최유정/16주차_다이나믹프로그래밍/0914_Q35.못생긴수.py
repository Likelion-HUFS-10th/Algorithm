n = int(input())
num = set([2, 3, 5])
dp = [0] * 1001
dp[1] = 1
# 1 2 3 5 4 6 10 9 15

for i in range(2, n+1):
    next = min(num)
    num.remove(next)
    dp[i] = next
    num.update([next*2, next*3, next*5])

print(dp[n])
