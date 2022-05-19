# import sys
# sys.setrecursionlimit(10000)
# input = sys.stdin.readline

# N, M, v = map(int, input().split())

# graph = [[] for _ in range(N+1)]
# check = [0] * (N+1) 
# answer = []

# for i in range(1, M+1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# for i in range(1, N+1):
#   graph[i] = sorted(graph[i])

# def dfs(v):
#   if check[v] == 0:
#     answer.append(v)
#     check[v] += 1
#   for i in graph[v]:
#     if check[i] == 0:
#       answer.append(i)
#       check[i] += 1
#       dfs(i)
#   return answer

# def bfs(v):
#   if check[v] == 0:
#     answer.append(v)
#     check[v] += 1
#     for i in range(len(graph[v])):
#       answer.append(graph[v][i])
#       check[graph[v][i]] += 1
#   for i in graph[v]:
#     if check[graph[i]] == 0:
#       answer.append(graph[i])
#       bfs(graph[i])
#   return answer

# print(bfs(v))

n, m, v = map(int, input().split())

matrix = [[0] * (n+1) for i in range(n+1)] # 영행렬 생성
visited = [0] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  matrix[a][b] = matrix[b][a] = 1

def dfs(v):
  visited[v] = 1
  print(v, end = " ")
  for i in range(1, n+1):
    if (visited[i] == 0 and matrix[v][i] == 1):
      dfs(i)

def bfs(v):
  queue = [v]
  visited[v] = 0
  while queue:
    v = queue.pop(0)
    print(v, end = " ")
    for i in range(1, n+1):
      if(visited[i] == 1 and matrix[v][i] == 1):
        queue.append(i)
        visited[i] = 0
  
dfs(v)
print()
bfs(v)