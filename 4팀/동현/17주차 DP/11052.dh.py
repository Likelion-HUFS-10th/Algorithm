"""
합을 구성하는 문제와 동일하다고 생각
4 => 2를 구성하는 방법과 숫자 2
"""
n = int(input())

money = [0] + list(map(int,input().split()))

dp = [0] * 10000

# num_list = []

# for i in range(1,n+1):
#     num_list.append(i)

# d = [0] * 1000

# for _ in range(n):
#     d[1] = 1
#     d[2] = 2
#     d[3] = 4
#     for i in range(4,n+1):
#         d[i] = d[i-3] + d[i-2] + d[i-1]

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i],dp[i-j] + money[j])

print(max(dp))