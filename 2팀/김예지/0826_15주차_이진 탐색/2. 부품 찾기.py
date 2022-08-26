N = int(input())
parts = list(map(int, input().split()))
parts = sorted(parts)
M = int(input())
requests = list(map(int, input().split()))

def binary_search(target, array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid # 왜 9는 여기서 안 걸리지...?
    elif array[mid] > target:
        binary_search(target, array, start, mid-1)
    else:
        binary_search(target, array, mid+1, end)
    
for i in requests:
    result = binary_search(i, parts, 0, N-1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")

# 언니 오빠한테 물어보기