n, m = map(int, input().split())
d = [10001] * (m+1)

coins = []
for _ in range(n):
    coins.append(int(input()))
    # coin = int(input())
    # coins.append(coin)
    # d[coin] = 1

# coins에 있는 모든 coin들, 그리고 coin들로 만들 수 있는 최소공배수를 구해서 카운팅을 저장하는 게 키일 것 같다
# for coin in coins:
#     for i in range(1, len(d)):
#         if i > coin and i % coin == 0:
#             d[i] = min(d[i], d[i-coin] + d[coin])
    
# print(d)

# 최소공배수를 구하는 과정이 너무 복잡해질 것이라고 판단

# 해답
d[0] = 0
for i in range(n):
    for j in range(coins[i], m+1):
        if d[j - coins[i]] != 10001:
            d[j] = min(d[j], d[j - coins[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])



