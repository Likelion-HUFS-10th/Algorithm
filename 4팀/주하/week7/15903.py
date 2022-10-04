# 카드 합체 놀이
n, m = map(int,input().split())

cards = list(map(int,input().split()))

for _ in range(m):
    cards.sort()                     # 정렬
    min_card = cards[0] + cards[1]   # 가장 작은 수 2개 합
    cards[0] = min_card
    cards[1] = min_card

print(sum(cards))
