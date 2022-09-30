from collections import deque

n = int(input())
card = [i for i in range(1, n+1)]
card = deque(card)

while True:
    if len(card) == 1:
        break
    card.popleft()
    card.rotate(-1)


print(card[0])