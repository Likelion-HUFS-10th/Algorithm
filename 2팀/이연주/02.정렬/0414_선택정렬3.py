# 알고리즘 수업 - 선택 정렬 3

n, k = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))
sorted_arr = sorted(arr)
dic = dict()

for i in range(1, n+1):
    dic[arr[i]] = i
cnt = 0

if k > n-1:
    print(-1)
else:
    for i in range(n, 1, -1):
        if arr[i] == sorted_arr[i]:
            continue
        cnt += 1
        swap_num = arr[i]   # swap 대상 (dic[swap_num] == i 인 수)
        arr[i], arr[dic[arr[i]]] = sorted_arr[i], swap_num
        dic[swap_num], dic[arr[i]] = dic[arr[i]], i

        if cnt == k:
            print(swap_num, sorted_arr[i])
            break

    if cnt < k:
        print(-1)