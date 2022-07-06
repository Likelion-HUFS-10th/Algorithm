'''
색이 연속되면 안됨
어차피 색은 세개!
'''

import sys

input = sys.stdin.readline

n = int(input())
houses = [
    list(map(int,input().split()))
    for _ in range(n)
]

for i in range(1,n):
    # 지금 상황에서 빨간색을 선택했을 때
    houses[i][0] = min(houses[i-1][1],houses[i-1][2])+houses[i][0]
    houses[i][1] = min(houses[i-1][0],houses[i-1][2])+houses[i][1]
    houses[i][2] = min(houses[i-1][1],houses[i-1][0])+houses[i][2]

print(min(houses[n-1]))
