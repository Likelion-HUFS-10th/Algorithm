import sys
import copy
N, K = map(int, sys.stdin.readline().split())
A = [int(w) for w in sys.stdin.readline().split()]
AA = A[:]
cnt = 0
rule = 1

for i in range(1, N):
    for j in range(i, 0, -1):
        if A[j-1] > A[j]:
            temp = A[j]
            A[j] = A[j-1]
            cnt += 1
            print(A)
            # if cnt == K:
            #     print(A[j])
            #     print(A)
            
            A[j-1] = temp
            
            # AA에서 가장 작은 수가 가장 작은 인덱스에 위치하면,
            if A.index(min(AA)) == 0:
                AA.remove(min(AA))
                cnt += 1
                rule += 1
                print(A)
            # if cnt == K:
            #     print(A[j-1])
            #     print(A)
                 
if cnt < K:
    print("-1")