import sys
input = sys.stdin.readline

n = int(input())
origin_arr = list(map(int,input().split()))
arr = [0 for _ in range(n)]

for i in range(n):
    arr[i] = [origin_arr[i], 0, i]

arr.sort()


for i in range(1,n):
    old_val = arr[i][0]
    new_val = arr[i][1]
    origin_idx = arr[i][2]

    if old_val == arr[i-1][0]:
        arr[i][1] = arr[i-1][1]
    else:
        arr[i][1] = arr[i-1][1]+1

ans = [0 for _ in range(n)]

for i in range(n):
    ans[arr[i][2]] = arr[i][1]

for i in range(n):
    print(ans[i],end=' ')