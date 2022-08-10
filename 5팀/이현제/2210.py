import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

graph = []
for _ in range(5):
    arr = list(map(int, input().split()))
    graph.append(arr)

result_set = set()

def dfs(i, j, result):
    result += str(graph[i][j])
    if len(result) == 6:
        result_set.add(result)
        return
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    for d in range(4):
        x = i + dx[d]
        y = j + dy[d]
        if 0 <= x <= 4 and 0 <= y <= 4:
            dfs(x, y, result)


for i in range(5):
    for j in range(5):
        dfs(i, j, '')

print(len(result_set))