from math import factorial
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

chickens = []
houses = []

for i in range(n):
	for j in range(n):
		if grid[i][j] == 1:
			houses.append((j, i))

		if grid[i][j] == 2:
			chickens.append((j, i))

coms = list(combinations(chickens, m))

def solve(coms):
	result = 0
	
	for hx, hy in houses:
		vals = 1e9
		for cx, cy in coms:
			vals = min(abs(hx - cx) + abs(hy - cy), vals)
		result += vals
		
	return result


answer = 1e9

for com in coms:
	answer = min(solve(com), answer)

print(answer)

