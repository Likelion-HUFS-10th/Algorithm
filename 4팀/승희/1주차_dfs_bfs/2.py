from collections import deque

n,m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input())))

# 1로만 움직일 수 있음
# 움직여야 하는 칸의 개수

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x,y):
    return x<n and y>=0 and x>=0 and y<m

def bfs(x,y):
    queue = deque() #방문한 곳들

    queue.append((x,y)) #시작 위치 우선 큐에 넣고 시작

    while queue:
        x,y = queue.popleft() #인접한 노드의 위치

        for i in range(4):
            new_x = x+dxs[i]
            new_y = y+dys[i]
            if in_range(new_x,new_y) and graph[new_x][new_y]!=0 and graph[new_x][new_y]==1:
                graph[new_x][new_y] = graph[x][y]+1
                queue.append((new_x,new_y))

bfs(0,0)
print(graph[n-1][m-1])