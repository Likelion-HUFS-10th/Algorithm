# n = int(input())
# a, b = map(int, input().split())
# m = int(input())

# graph = [[] for _ in range(m+1)]

# for _ in range(1, m+1):
#   x, y = map(int, input().split())
#   graph[x].append(y)

# print(graph)

# for i in range(len(graph)):
#   if a in graph[i]:
#     index_a = i

# print(index_a) 

import sys
sys.setrecursionlimit(300000)

def dfs(node):
  for n in graph[node]:
    if check[n] == 0:
      check[n] = check[node] + 1
      dfs(n)

n = int(input())
graph = [[] for _ in range(n+1)]
a, b = map(int, input().split()) # 촌수를 찾을 두 변수
for _ in range(int(input())):
  u, v = map(int, input().split()) # 노드 간 관계 정의
  graph[u].append(v)
  graph[v].append(u) # 관계가 있으면 서로 append

check = [0] * (n+1)
dfs(a) # 7 인자를 매개변수로 넘겨서 모든 사람과 7의 촌수를 계산한다.
print(check[b] if check[b] > 0 else -1)
