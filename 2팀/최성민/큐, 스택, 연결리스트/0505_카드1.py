from collections import deque

n = int(input())
deck = deque([i for i in range(1, n+1)])
result = []

while len(deck) > 1:
	throw = deck.popleft()
	result.append(throw)

	deck.append(deck.popleft())

print(*result, deck[0])
