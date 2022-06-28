import sys

N, K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
for i in range(1, N):
    loc = i - 1
    newitem = arr[i]

    while(0 <= loc and newitem < arr[loc]):
        if K > 0:
            K -= 1
        else:
            break
        arr[loc + 1] = arr[loc]
        loc -= 1
        
    if K == 0:
        for i in arr:
            print(i,end=' ')
        sys.exit(0)

    if (loc + 1 != i):
        arr[loc + 1] = newitem
        K -= 1
    
    
print(-1)

# 시간초과