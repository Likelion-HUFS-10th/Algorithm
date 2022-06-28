import sys
N, K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))



for last in range(N-1, 0, -1):
    for i in range(last):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            K -= 1
        if K == 0:
            print(arr[i], arr[i + 1])
            sys.exit(0)
print(-1)

# 시간초과