# 병합정렬
str = input().split()
N = int(str[0])
K = int(str[-1])

str2 = input()
A = [int(w) for w in str2.split()]


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    cnt = 0
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
            cnt += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
            cnt += 1
    merged_arr += low_arr[l:]
    cnt += 1
    merged_arr += high_arr[h:]
    cnt += 1
    return merged_arr

print(merge_sort(A))
print(cnt)

# 시스템은 알겠는데 문제에 적용을 못 하겠음.