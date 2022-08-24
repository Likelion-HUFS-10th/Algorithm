from collections import deque
import sys

input = sys.stdin.readline
n,m,k,x = map(int,input().split()) #도시의 개수 / 도로의 개수 / 거리 / 출발 도시
x -=1 # 0부터 시작하기 때문에
# 거리 => dfs

arr = [
    []
    for _ in range(n)
]

for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    arr[a].append(b)

visited = [False for _ in range(n)]
distance = [0 for _ in range(n)]
answer = []


def bfs(x, k):
    global answer

    q = deque()
    q.append((x))
    visited[x] = True
    distance[x] = 0

    while q:
        now = q.popleft() #지금 있는 위치
        for i in arr[now]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[now]+1
                q.append(i)
            if distance[i]==k and i not in answer:
                answer.append(i)

    if len(answer)==0:
        print(-1)
    else:
        answer.sort()
        for i in range(len(answer)):
            print(answer[i]+1)

bfs(x,k)

# def bfs(x,y):
#     q = deque()
#     q.append((x,y))

#     while q:
#         now_x,now_y = q.popleft()
#         now_cnt = arr[now_x][now_y]
#         for i in range(n):
#             if arr[now_y][i]!=0:
#                 arr[now_y][i]=now_cnt+1
#                 q.append((now_y,i))

# for i in range(n):
#     bfs(x,i)

# for i in range(n):
#     print(arr[i])
# flag = False
# for i in range(n):
#     min_num = sys.maxsize
#     for j in range(n):
#        if arr[j][i]<min_num and arr[j][i]!=0:
#            min_num = arr[j][i]
#     if min_num == k:
#         flag = True
#         print(i+1)

# if not flag:
#     print(-1)
