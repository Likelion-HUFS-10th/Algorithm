import heapq

n = int(input())

deck = []

for _ in range(n):
	heapq.heappush(deck, int(input()))

_sum = 0

if len(deck) == 1:
	_sum = 0

while len(deck) > 1:
	a = heapq.heappop(deck)
	b = heapq.heappop(deck)
	c = a + b
	_sum = _sum + c

	heapq.heappush(deck, c)

print(_sum)