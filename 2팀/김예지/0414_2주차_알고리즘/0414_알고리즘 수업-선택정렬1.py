str = input().split()
N = int(str[0])
K = int(str[-1])

str2 = input()
A = [int(w) for w in str2.split()]

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
                break
            else:
                print(A[j], A[max])
                break
                
if cnt < K:
    print("-1")