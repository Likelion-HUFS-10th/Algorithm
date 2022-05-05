"""
갖고 있는 동전을 제일 큰 동전부터 금액에서 나눌 수 있는 만큼
나눠주는 방식으로 동전을 최소한 사용하는 방법 탐색
"""
N,K = map(int,input().split())
coin = []

for i in range(N):
    coin.append(int(input()))
coin.sort(reverse = True)
count = 0

for j in coin:
    if j <= K:
        if K % j == 0:
            count += K/j
            K = 0
        else:
            count += K//j
            K = K % j
    if K == 0:
        break
print(int(count))
