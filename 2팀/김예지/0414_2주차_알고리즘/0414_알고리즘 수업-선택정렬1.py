import sys
N, K = map(int, sys.stdin.readline().split())
A = [w for w in sys.stdin.readline().split()]
cnt = 0

for i in range(N, 0, -1):
    max = 0
    for j in range(0, i):
        if (A[j] > A[max]):
            max = j
    if A[max] != A[i-1]:
        A[max], A[i-1] = A[i-1], A[max]
        cnt += 1
        if cnt == K:
            if A[max] < A[j]:
                print(A[max], A[j])
            else:
                print(A[j], A[max])
     
if cnt < K:
    print("-1")