# import sys
# input = sys.stdin.readline

# N = int(input())
# answer = [1] * (N)
# graph = []

# for i in range(N):
#   graph.append(int(input()))

# for i in range(N):
#   checked = []
#   checked.append(i+1)
#   v = graph[graph[i]-1]
#   checked.append(graph[i])
#   while True:
#     if v in checked or answer[i] == N-1:
#       answer[i] += 1
#       break
#     else:
#       answer[i] += 1
#       checked.append(graph.index(graph[v-1])+1)
#       v = graph[v-1]

# print(answer.index(max(answer))+1)
  
def dfs(node, cnt):
  check[node] = 1
  n = graph[node][0]
  if check[n] == 0:
    cnt = dfs(n, cnt+1)
  return cnt

N = int(input())
graph = [[] for _ in range(N+1)]
result = [0] * (N+1)

for i in range(1, N+1):
  graph[i].append(int(input()))

for i in range(1, N+1):
  check = [0] * (N+1)
  result[i] = dfs(i, 1)

print(result.index(max(result)))
