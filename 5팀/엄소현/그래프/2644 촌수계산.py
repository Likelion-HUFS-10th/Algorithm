from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque()
  q.append(p1)
  while(q):
    u = q.popleft()
    if u == p2:
      return visited[p2]
    for w in family[u]:
      if visited[w] == 0:
        if w == p1:
          continue
        visited[w] = visited[u] + 1
        q.append(w)
    
n = int(input())   # 사람의 수
p1, p2 = map(int, input().split())   # 촌수 계산할 서로 다른 두 사람의 번호
m = int(input())   # 부모 자식들 간의 관계의 개수
family = [[] for _ in range(n+1)]
for _ in range(m):
  v1, v2 = map(int, input().split())
  family[v1].append(v2)
  family[v2].append(v1)

visited = [0 for _ in range(n+1)]
cnt = bfs()
if cnt:
  print(cnt)
else:
  print(-1)
