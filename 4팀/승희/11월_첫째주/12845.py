'''
순서가 매겨진 여러장의 카드 => 레벨이 있음
인접한 카드끼리 붙일 수 있음

'''

n = int(input())
cards = list(map(int,input().split()))
cards.sort(reverse=True)

result = 0

for i in range(1,len(cards)):
    result += cards[i]+cards[i-1]
    cards[i] = cards[i-1]

print(result)
