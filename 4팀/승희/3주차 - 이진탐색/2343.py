n,m = map(int,input().split())
arr = list(map(int,input().split()))

def is_possible(mid):
    cnt = 0
    sum = 0
    for i in range(n):
        sum += arr[i]
        if sum > mid:
            # print("끊기는 지점",arr[i])
            cnt +=1
            sum = arr[i]
        elif sum == mid:
            cnt +=1
            sum = 0
        # print(arr[i], cnt)
    if sum > 0:
        cnt +=1
    return cnt

def binary_search(m, start, end):
    global ans

    mid = (start+end)//2
    # print("중간", mid)

    if start > end:
        return start

    # cnt 가 더 크다는 것은 크기를 더 늘려야 한다는 뜻
    result = is_possible(mid)
    if result <= m:
        # print(result)
        return binary_search(m, start, mid-1)
    else:
        # print(result)
        return binary_search(m, mid+1, end)

print(binary_search(m, max(arr), sum(arr)))

