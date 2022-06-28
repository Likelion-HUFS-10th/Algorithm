import math
import sys
N, K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

def mergesort(A,p,q):
    if p == q:
        return A[p:p+1]
    mid = math.floor((p + q) / 2)
    mergesort(A, p, mid)
    mergesort(A, mid+1, q)
    merge(A, p, mid+1, q)
    

def merge(A, p, r, q):
    global K
    sorted_list = []
    left_array_num = p
    right_array_num = r
    while left_array_num < r and right_array_num <= q:
        if A[left_array_num] < A[right_array_num]:
            sorted_list.append(A[left_array_num])
            left_array_num += 1
        else:
            sorted_list.append(A[right_array_num])
            right_array_num += 1
    while left_array_num < r:
        sorted_list.append(A[left_array_num])
        left_array_num += 1
    while right_array_num <= q:
        sorted_list.append(A[right_array_num])
        right_array_num += 1

    for i in range(len(sorted_list)):
        A[p] = sorted_list[i]
        p += 1
        K -= 1
        if K == 0:
            print(sorted_list[i])
            sys.exit(0)
    

M = mergesort(arr, 0, N-1)

if M == None:
    print(-1)
else:
    print(M)