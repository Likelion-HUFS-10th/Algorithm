num = int(input())
cards = []

for i in range(num, 0, -1):
    cards.append(i) #num 부터 1까지 역순으로 추가

while len(cards) > 1:
    cards.pop()
    cards.insert(0, cards[-1])
    cards.pop()
    

print(cards[0])