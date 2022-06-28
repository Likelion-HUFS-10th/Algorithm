def selection_sort(T, arr1, arr2):
    for i in range(T, 0, -1):
        max_num = 0
        for j in range(i):
            if arr1[max_num] < arr1[j]:
                max_num = j
        if max_num < i - 1:
            arr1[max_num], arr1[i-1] = arr1[i-1], arr1[max_num]
            if arr1 == arr2:
                return 1
    return 0



T = int(input())
arr1 = list(map(int, input().split(' ')))
arr2 = list(map(int, input().split(' ')))
print(selection_sort(T, arr1, arr2))


# 틀렸습니다