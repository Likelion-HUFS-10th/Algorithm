# 딕셔너리 사용......
n = int(input())
arr = list(map(int, input().split()))
arr_sort = sorted(list(set(arr)))
dic_arr = {arr_sort[i]: i for i in range(len(arr_sort))}

for i in arr:
    print(dic_arr[i], end=' ')











# <시간초과>
# n = int(input())
# arr = list(map(int,input().split()))
# arr_sort = sorted(list(set(arr)))

# for i in arr:
#     print(arr_sort.index(i), end= " ")
