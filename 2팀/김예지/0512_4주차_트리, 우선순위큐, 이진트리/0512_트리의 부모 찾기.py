# 11725 트리의 부모 찾기

import sys
input = sys.stdin.readline

# N = int(input())
# stack = []

# for _ in range(N-1):
#     a, b = map(int, input().split())
#     if a not in [w for s in stack for w in s] and a != 1:
#         stack.append([a, b])
#     if b not in [w for s in stack for w in s] and b != 1:
#         stack.append([b, a])
    

# stack = sorted(stack)
# for i in range(N-1):
#     print(stack[i][1])
# 시간 초과

# ▼ reference
sys.setrecursionlimit(10**6) # 스택 깊이 제한 풀기(재귀 호출과 관련이 있다.)

N = int(input())
tree = [[] for _ in range(N+1)] # 왜 8개를 만들까? : 코드 깔끔하게 짜려고 처음 리스트는 버리는 건가보다.
parents = [-1]*(N+1) 

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def dfs(N):
    for i in tree[N]:
        if parents[i] == -1: # -1이라는 거 자체가 부모 노드가 아직 안 들어와 있다는 뜻.
            parents[i] = N
            dfs(i)
dfs(1)
for i in range(2, N+1):
    print(parents[i])