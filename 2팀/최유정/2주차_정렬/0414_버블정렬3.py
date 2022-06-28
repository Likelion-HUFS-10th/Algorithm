import sys
N = int(input())
arr1 = list(map(int,sys.stdin.readline().split()))
arr2 = list(map(int,sys.stdin.readline().split()))
result = 0


for last in range(N-1, 0, -1):
    for i in range(last):
        if arr1[i] > arr1[i + 1]:
            arr1[i], arr1[i + 1] = arr1[i + 1], arr1[i]
            if arr1 == arr2:
                result = 1
print(result)

# 시간초과