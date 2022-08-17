# p.149 실전문제 3 음료수 얼려 먹기

n,m = map(int,input().split())
graph = [
    list(map(int,input()))
    for _ in range(n)
]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]
cnt = 0

def in_range(x,y):
    return x<n and y<m and x>=0 and y>=0


def bfs(x, y):
    if not in_range(x,y): #범위를 넘어가면 false 반환
        return False

    if not visited[x][y] and graph[x][y]==0:
        visited[x][y] = True
        #연결된 노드 전부, 즉 상하좌우로 방문
        bfs(x-1,y)
        bfs(x,y-1)
        bfs(x,y+1)
        bfs(x+1,y)
        return True
    return False

for i in range(n):
    for j in range(m):
        if bfs(i,j)==True:
            cnt+=1

print(cnt)
