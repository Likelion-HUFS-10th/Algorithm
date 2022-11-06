n, m = map(int, input().split())
travels = [list(map(int, input().split())) for _ in range(n)]
travel = [0] * (n+1)
result = []
for t in range(1, n+1):
    travel[t] = t

def find_s(travel, x):
    if travel[x] != x:
        travel[x] = find_s(travel, travel[x])
    return travel[x]

def union_x(x, y):
    x = find_s(travel, x)
    y = find_s(travel, y)
    if x > y:
        travel[x] = y
    else:
        travel[y] = x

for a in range(n):
    for b in range(a+1, n):
        if travels[a][b] == 1:
            union_x(a+1, b+1)

travel_num = list(map(int, input().split()))
for t in travel_num:
    result.append(travel[t])
if len(set(result)) != 1:
    print("NO")
else:
    print("YES")