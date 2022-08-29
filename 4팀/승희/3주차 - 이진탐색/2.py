import sys
input = sys.stdin.readline

n,m = map(int,input().split()) #n은 떡의 개수 / m은 요청한 길이

arr = list(map(int,input().split())) # 떡의 길이
arr.sort()

ans = 0

def binary_search(arr, m, start, end):
    global ans

    mid = (start+end)//2

    result = 0

    for i in range(n):
        if arr[i] > mid:
            result += (arr[i] - mid)

    if start > end:
        return mid

    if result >= m:
        ans = mid
        return binary_search(arr, m, mid+1, end)

    #요청한 길이보다 작으면 더 잘라야 됨
    else:
        return binary_search(arr, m, start, mid-1)

print(binary_search(arr, m, 0, max(arr)))
