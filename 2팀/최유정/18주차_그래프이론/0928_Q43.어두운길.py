from heapq import heappop, heappush

n, m = map(int, input().split())
road = []
len = [0] * (n)
for l in range(n):
    len[l] = l
result = 0

def find_root(len, x):
    if len[x] != x:
        len[x] = find_root(len, len[x])
    return len[x]

def union_road(x, y):
    x = find_root(len, x)
    y = find_root(len, y)
    if x > y:
        len[x] = y
        return True
    elif x < y:
        len[y] = x
        return True
    else:
        return False

for _ in range(m):
    x, y, z = map(int, input().split())
    heappush(road, [z, x, y])

while road:
    s = heappop(road)
    if not union_road(s[1], s[2]):
        result += s[0]

print(result)