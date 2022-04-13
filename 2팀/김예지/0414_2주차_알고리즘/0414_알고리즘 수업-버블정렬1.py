str = input().split()
N = int(str[0])
K = int(str[-1])

str2 = input()
A = [int(w) for w in str2.split()]

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
