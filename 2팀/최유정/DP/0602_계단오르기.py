import sys
input = sys.stdin.readline

def func1(stair):
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = stair[2] + max(stair[0], stair[1])
    for i in range(3, len(stair)):
        dp[i] = stair[i] + max(dp[i-2], dp[i-3] + stair[i-1])
    return dp[len(stair)-1]

s_num = int(input())
dp = [0] * 300

stair = []
for i in range(s_num):
    stair.append(int(input()))

if s_num == 1:
    print(stair[0])
if s_num == 2:
    print(stair[0] + stair[1])
if s_num > 2:
    print(func1(stair))