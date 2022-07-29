from itertools import combinations

n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

home = []
chicken = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      home.append((i, j))
    elif graph[i][j] == 2:
      chicken.append((i, j))
    else:
      continue
# --------
candidates = list(combinations(chicken, m))

def get_sum(candidate):
  result = 0
  for hx, hy in home:
    temp = 1e9
    for cx, cy in candidate:
      temp = min(temp, abs(hx-cx) + abs(hy-cy))
    result += temp
  return result

result = 1e9
for candidate in candidates:
  result = min(result, get_sum(candidate))

# d = [0] * len(chicken)
# cnt = [0] * len(chicken)
# for i in range(len(home)):
#   for j in range(len(chicken)):
#     d.append(abs(home[i][0] - chicken[j][0]) + abs(home[i][1] - chicken[j][1]))

print(result)