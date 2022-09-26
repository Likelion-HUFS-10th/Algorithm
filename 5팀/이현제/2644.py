all_people = int(input())
target_a, target_b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(all_people + 1)]
visited = [False] * (all_people + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, cnt):
    visited[v] = True
    cnt += 1
    if v == target_b:
        visited[v] = cnt

    for i in graph[v]:
        if visited[i] == False:
            dfs(i, cnt)

dfs(target_a, 0)

target = visited[target_b]
if target == True or False:
    print(-1)
else:
    print(target - 1)
