"""
두 카드는 인접한 카드여야 함
업그레이드된 카드의 레벨은 변하지 않음
"""
n = int(input())
card_list = list(map(int, input().split()))
card_list.sort(reverse=True)

result = 0

for i in range(len(card_list)):
    if i <= 1:
        result += card_list[i]
    else:
        result += card_list[0] + card_list[i]

print(result)