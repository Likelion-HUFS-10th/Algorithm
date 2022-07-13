'''
1km 당 1리터의 기름을 사용

'''
import sys

n = int(input()) #도시의 개수
distances = list(map(int,input().split()))
prices = list(map(int,input().split()))
ans = 0
idx = 0
min_price = sys.maxsize

for i,distance in enumerate(distances):
    if min_price > prices[i]:
        min_price = prices[i]
    ans += min_price * distance

print(ans)