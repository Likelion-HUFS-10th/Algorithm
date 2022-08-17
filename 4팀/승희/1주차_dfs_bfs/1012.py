# 흰 지렁이는 배추가 인접한 곳으로는 이동 가능!

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

t = int(input()) #테스트케이스

def in_range(x,y,n,m):
    return x>=0 and x<n and y>=0 and y<m

def dfs(x, y, arr, visited, n, m):

    if not in_range(x,y,n,m) or visited[x][y]:
        return False

    visited[x][y] = True

    if arr[x][y]==1:
        dfs(x-1,y,arr,visited,n,m)
        dfs(x+1,y,arr,visited,n,m)
        dfs(x,y-1,arr,visited,n,m)
        dfs(x,y+1,arr,visited,n,m)
        return True

    return False


for _ in range(t):
    m,n,k = map(int,input().split())
    arr = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]

    for _ in range(k):
        x,y = map(int,input().split())
        arr[y][x] = 1

    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]

    cnt = 0

    for i in range(n):
        for j in range(m):
            if dfs(i,j,arr,visited,n,m):
                cnt+=1

    print(cnt)