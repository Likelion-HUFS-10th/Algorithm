import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m = map(int, input().split())
dis = []
house = [0] * (n+1)
dis_h = []
for _ in range(m):
    a, b, c = map(int, input().split())
    heappush(dis, [c, a, b])

for h in range(1, n+1):
    house[h] = h

def find_h(house, x):
    if house[x] != x:
        house[x] = find_h(house, house[x])
    return house[x]

def union_h(x, y):
    hx = find_h(house, x)
    hy = find_h(house, y)
    if hx > hy:
        house[hx] = hy
        return True
    elif hy > hx:
        house[hy] = hx
        return True
    else:
        return False

while dis:
    s = heappop(dis)
    if union_h(s[1], s[2]):
        dis_h.append(s[0])

max_dis = max(dis_h)
print(sum(dis_h) - max_dis)