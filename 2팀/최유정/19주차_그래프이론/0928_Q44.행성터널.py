from heapq import heappop, heappush
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
solar = []
for i in range(n):
    x, y, z = map(int, input().split())
    solar.append([x, y, z, i])
q = []
result = [0] * n
for r in range(n): result[r] = r
min_value = 0

for i in combinations(solar, 2):
    min_num = min(abs(a - b) for a, b in zip(i[0][:3], i[1][:3]))
    heappush(q, [min_num, i[0][3], i[1][3]])

def find_root(result, x):
    if result[x] != x: result[x] = find_root(result, result[x])
    return result[x]

def union(x, y):
    x = find_root(result, x)
    y = find_root(result, y)
    if x > y:
        result[x] = y
        return True
    elif x < y:
        result[y] = x
        return True
    else: return False

while q:
    length = heappop(q)
    if not union(length[1], length[2]): continue
    else: min_value += length[0]
    if len(set(result)) == 1: break

print(min_value)