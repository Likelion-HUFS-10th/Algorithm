def bubble_sort(arr1, K, T):
    run_num = 0
    for i in range(T):
        for j in range(0, T - i - 1):
            if arr1[j] > arr1[j + 1]: 
                arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j] 
                run_num += 1
            if run_num == K:
                return arr1
    return -1


T, K = map(int, input().split())
arr = list(map(int, input().split(' ')))

result = bubble_sort(arr, K, T)
if result == -1:
    print(result)
else:
    for i in range(len(result)):
        print(result[i], end=" ")

# 시간초과