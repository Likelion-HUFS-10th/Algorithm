from collections import deque
n = int(input())
i = 0
cards = deque([i for i in range(1, n+1)])
trash = []
while len(cards) > 1 :
    if i % 2 == 0:
        x = cards.popleft()
        trash.append(x)
    else:
        x = cards.popleft()
        cards.append(x)
    i += 1
print(*trash, cards[0])