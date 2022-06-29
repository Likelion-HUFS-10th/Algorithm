'''

마지막 계단은 꼭 밟아야 한다고 했으니까 
거꾸로 찾기: 마지막 계단 부터 -> 앞계단으로 

'''


n = int(input())
stair = [int(input()) for _ in range(n)]     # 각 계단 점수
dp = [0] * (n+1)                             # 계단 점수 합산

if n == 1:
    print(stair[0])
if n == 2:
    print(stair[0]+stair[1])

if n == 3:
    print(max(stair[0]+stair[2], stair[1]+stair[2]))

else :
    dp[0] = stair[0]
    dp[1] = stair[0]+stair[1]
    dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])   # 이거 안 적어서 출력값 다르게 나왔음
    for i in range(3, n):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
    print(dp[n-1])

#--------------------------------------------------------------
# [방법 찾기]
# dp[0] = stair[0]
# dp[1] = stair[0]+stair[1]
# dp[2] = (stair[0]+stair[2],stair[1]+stair[2])
# dp[3] = (dp[0]+stair[2]+stair[3],dp[1]+stair[3])
# dp[4] = (dp[1]+stair[3]+stair[4],dp[2]+stair[4])
# ...
# dp[n] = max(dp[n-3]+stair[n-1]+stair[n],dp[n-2]+stair[n]