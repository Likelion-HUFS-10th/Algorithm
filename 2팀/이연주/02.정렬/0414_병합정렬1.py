import math
N, K = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
answer = -1

def merge(left, mid, right):
    global arr, answer, K
    i, j = left, mid+1
    tmp = []
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j]) 
            j += 1
        K -= 1
        if K == 0:
            answer = tmp[-1]
            

    while i <= mid: # 왼쪽 배열이 남은 경우
        tmp.append(arr[i])
        i += 1
        K -= 1
        if K == 0:
            answer = tmp[-1]
        

    while j <= right: # 오른쪽 배열이 남은 경우
        tmp.append(arr[j])
        j += 1
        K -= 1
        if K == 0:
            answer = tmp[-1]
        
    
    i, t = left, 0
    while i <= right:
        arr[i] = tmp[t]
        t += 1
        i += 1

    return answer


def merge_sort (left, right):
    if left < right: 
        mid = math.floor((left + right) / 2)
        merge_sort(left, mid)
        merge_sort(mid+1, right)
        return merge(left, mid, right)

left, right = 0, N-1
print(merge_sort(left, right))