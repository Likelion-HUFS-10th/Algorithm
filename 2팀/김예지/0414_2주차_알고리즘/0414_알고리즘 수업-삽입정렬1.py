str = input().split()
N = int(str[0])
K = int(str[-1])

str2 = input()
A = [int(w) for w in str2.split()]

cnt = 0
for i in range(1, N):
    for j in range(i, 0, -1):
        if A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            cnt += 1
            if cnt == K:
                print(A[k])
                          
if cnt < K:
    print("-1")