import sys
N, K = map(int, sys.stdin.readline().split())
A = [w for w in sys.stdin.readline().split()]
cnt = 0

for i in range(N - 1, 0, -1):
    for j in range(i):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            cnt += 1
            if cnt == K:
                if A[j] < A[j+1]:
                    print(A[j], A[j+1])
                else:
                    print(A[j+1], A[j])
                          
if cnt < K:
    print("-1")
