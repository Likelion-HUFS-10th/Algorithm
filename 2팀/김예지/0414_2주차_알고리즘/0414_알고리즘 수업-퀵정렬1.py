# 퀵정렬
str = input().split()
N = int(str[0])
K = int(str[-1])

str2 = input()
A = [int(w) for w in str2.split()]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

# 퀵 정렬도 시스템은 이해가 가지만 문제에 적용을 못 시키겠음.