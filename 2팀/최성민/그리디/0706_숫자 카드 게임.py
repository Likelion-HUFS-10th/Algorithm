import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]
temp = []

for card in cards:
	temp.append(min(card))

print(max(temp))

"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = 0

for i in range(n):
	card = list(map(int, input().split()))
	min_value = min(card)
	result = max(min_value, result)

print(result)
"""