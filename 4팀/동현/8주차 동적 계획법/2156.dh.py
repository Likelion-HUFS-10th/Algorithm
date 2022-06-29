n = int(input())

wine_list =[]

for i in range(n):
    wine_list.append(int(input()))

dp = [0] * (n+1)

if n == 1:
    print(wine_list[0])
# elif n == 2:
#     print(wine_list[0] + wine_list[1])
# elif n == 3:
#     print(max(wine_list[0]+wine_list[1], wine_list[1]+wine_list[2],wine_list[0]+wine_list[2]))
else:
    dp[0] = wine_list[0]
    dp[1] = wine_list[0] + wine_list[1]
    for i in range(2,n):
        dp[i] = max(dp[i-3]+wine_list[i-1]+wine_list[i],dp[i-2]+wine_list[i],dp[i-1])
    print(dp[n-1])