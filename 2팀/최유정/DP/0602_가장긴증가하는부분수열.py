import sys
input = sys.stdin.readline

def func1(pgs):
    for i in range(len(pgs)):
        for j in range(i):
            if pgs[j] < pgs[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

a = int(input())
pgs = list(map(int, input().split()))
dp = [1] * 10000
print(func1(pgs))