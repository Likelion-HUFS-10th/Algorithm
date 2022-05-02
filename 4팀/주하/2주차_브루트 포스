n, m = map(int, input().split())
cards = list(map(int,input().split()))
sum_cards = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            three_cards = cards[i] + cards[j] + cards[k]
            if three_cards <= m:     # 조건 m에 최대한 가까운 합을 찾기
                sum_cards = max(sum_cards,three_cards)   
            else:
                continue             # 조건에 맞지 않을 경우 continue

print(sum_cards)
