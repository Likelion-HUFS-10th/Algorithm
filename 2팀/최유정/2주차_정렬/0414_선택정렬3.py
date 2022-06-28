T, K = map(int, input().split())
arr = list(map(int, input().split(' ')))
sorted_arr = []
run_num = 0
for i in range(T-1, 0, -1):
    right_num = arr.pop()
    max_num = max(arr[:i])
    if max_num > right_num:
        max_num_idx = arr.index(max_num)
        run_num += 1
    if run_num == K:
        print(arr[right_num], arr[max_num])
        break
if run_num < K:
    print(-1)



   
# T, K = tuple(map(int, input().split()))
# arr = list(map(int, input().split()))

# new_nums = []
# order = []

# for i in range(T-1, 0, -1):
# 	max_val = arr.pop()
# 	max_nums = max(arr[0:i])

# 	if max_nums > max_val:
# 		idx = arr.index(max_nums)
# 		order.append((max_val, max_nums))
# 		arr[idx] = max_val
# 		new_nums.append(max_nums)
	
# 	else:
# 		new_nums.append(max_val)

# new_nums.append(arr[0])

# if len(order) < K:
# 	print(-1)
# else:
# 	for i in order[K-1]:
# 		print(i, end=" ")






# def selection_sort(T, arr1, K):
#     run_num = 0
#     for i in range(T, 0, -1):
#         max_num = 0
#         for j in range(i):
#             if arr1[max_num] < arr1[j]:
#                 max_num = j
#         if max_num < i - 1:
#             arr1[max_num], arr1[i-1] = arr1[i-1], arr1[max_num]
#             run_num += 1
#         if run_num == K:
#             return arr1[max_num], arr1[i-1]
#     return -1

# T, K = map(int, input().split())
# arr = list(map(int, input().split(' ')))
# result = selection_sort(T, arr, K)
# if result == -1:
#     print(result)
# else:
#     for i in range(len(result)):
#         print(result[i], end=" ")


# 시간초과