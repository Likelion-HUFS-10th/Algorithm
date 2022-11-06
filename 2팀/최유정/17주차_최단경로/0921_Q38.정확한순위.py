n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
rank = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for i in range(1, n+1):
    for j in graph[i]:
        rank[j].append(('U', i))
        rank[i].append(('D', j))
        for r in rank[i]:
            if r[0] == 'U':
                rank[j].append(('U', r[1]))
cnt = 0
for r in rank:
    if len(r) == n-1:
        cnt += 1
    else:
        continue
print(cnt)