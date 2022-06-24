n,m = map(int,input().split()) 

def bfs(n,m,ans):
    if len(ans)==m:
        print(*ans)
        return
    
    for i in range(1,n+1):
        if i not in ans:
            ans.append(i)
            bfs(n,m,ans)
            ans.pop()

bfs(n,m,[])
