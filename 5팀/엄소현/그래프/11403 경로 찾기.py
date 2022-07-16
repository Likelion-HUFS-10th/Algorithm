import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

output = [[0 for _ in range(n)] for _ in range(n)]

def dfs(a, b, flag, visited):
  visited[a] = False
  if not flag:
    visited[a] = True
  if a == b and flag:
    return 1
  for i in range(n):
    if visited[i] and graph[a][i] == 1:
      if dfs(i, b, True, visited):
        return 1
  return 0

for i in range(n):
  for j in range(n):
    if dfs(i, j, False, [True for _ in range(n)]):
      output[i][j] = 1

for i in range(n):
  print(*output[i])
