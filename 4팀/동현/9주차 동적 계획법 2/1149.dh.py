"""
1번 집과 2번 집의 색 다르게
이웃한 집 사이에 색은 다르게
dp를 각 집의 가격으로 할 경우 100 100 100과 같은 경우 처리 불가..
dp[현재]를 현재 이 집을 택할 때 이전의 집중에 현재 색깔을 제외한 dp[이전] 값중 작은 값으로 고려
"""
import sys
N = int(input())

color_list = []

for _ in range(N):
    color_list.append(list(map(int,sys.stdin.readline().split())))

# dp = [0] * (N+1)

if N == 1:
    print(min(color_list[0]))
# else:
#     dp[0] = min(color_list[0])
#     for i in range(1,N):
#         if color_list[i-1].index(dp[i-1]) == 0:
#             dp[i] = min(color_list[i][1],color_list[i][2])
#         elif color_list[i-1].index(min(color_list[i-1])) == 1:
#             dp[i] = min(color_list[i][0],color_list[i][2])
#         else:
#             dp[i] = min(color_list[i][0],color_list[i][1])
#     print(sum(dp))
else:
    for i in range(1,N):
        color_list[i][0] += min(color_list[i-1][1], color_list[i-1][2])
        color_list[i][1] += min(color_list[i-1][0], color_list[i-1][2])
        color_list[i][2] += min(color_list[i-1][0], color_list[i-1][1])
    print(min(color_list[N-1]))