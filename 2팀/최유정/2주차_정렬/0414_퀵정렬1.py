import sys
N, K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

def quick_sort(arr, p, q):
    if p < q:
        pivot = partition(arr, p, q)
        quick_sort(arr, p, pivot - 1)
        quick_sort(arr, pivot + 1, q)

def partition(arr, p, q):
    global K
    i = p - 1
    pivot = arr[q]

    for j in range(p, q):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            K -= 1
            if K == 0:
                print(arr[i], arr[j])
                sys.exit(0)
    if i + 1 != q:
        arr[i + 1], arr[q] = arr[q], arr[i + 1]
        K -= 1
        if K == 0:
            print(arr[i+1], arr[q])
            sys.exit(0)
    return i + 1


Q = quick_sort(arr, 0, N-1)

if Q == None:
    print(-1)
else:
    print(Q)