'''
집이 몇개인지
각각의 집을 빨, 초, 파로 칠하는 비용이 주어졌을 때
1. 1번집의 색 != 2번집의 색 => 3번 조건이랑 어차피 겹침
2. n번집의 색 != n-1번집의 색 => 3번 조건이랑 어차피 겹침
3. i번 집의 색은 i-1, i+1와 같지 않아야
즉, 연속해서 같은 색 x
'''
import sys

input = sys.stdin.readline

n = int(input())
houses = []
sorted_houses = []

for _ in range(n):
    house = list(map(int,input().split()))
    houses.append(house)
    sorted_houses.append(sorted(house))

dp = [0]*n #각 집의 색칠 비용

dp[0] = min(houses[0]) #가장 비용이 작은 색으로 선택
if houses[1].index(sorted_houses[1][0]) == houses[0].index(dp[0]):
        first_choice = sorted_houses[1][1] + sorted_houses[0][0]
        second_choice = sorted_houses[1][0] + sorted_houses[0][1]
        if first_choice < second_choice:
            dp[1] = sorted_houses[0][1]
        else:
            dp[0] = sorted_houses[0][1]
            dp[1] = sorted_houses[1][0]
else:
    dp[1] = sorted_houses[1][0]

for i in range(2,n):
    min_color = min(houses[i])

    # 지금 보고 있는 인덱스에서 가장 비용이 적게 드는 색과 이전 인덱스에서 가장 비용이 적게 드는 색이 겹치면
    if houses[i].index(min_color) == houses[i-1].index(dp[i-1]):
        first_choice = sorted_houses[i][1] + sorted_houses[i-1][0]
        second_choice = sorted_houses[i][0] + sorted_houses[i-1][1]
        if first_choice < second_choice:
            dp[i] = sorted_houses[i][1]
        else:
            dp[i-1] = sorted_houses[i-1][1]
            dp[i] = sorted_houses[i][0]
    else:
        dp[i] = min_color
        print(dp[i])

print(dp)
print(sum(dp))
