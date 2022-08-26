n, x = map(int, input().split())
num_lst = list(map(int, input().split()))
result = 0 

def binary_search(array, target, start, end):
    global result
    if start > end:
        return result
    mid = (start + end) // 2
    if array[mid] == target:
        result += 1
        binary_search(num_lst, x, start, mid - 1)
        binary_search(num_lst, x, mid + 1, end)
        return result
    elif array[mid] > target:
        binary_search(num_lst, x, start, mid - 1)
    else:
        binary_search(num_lst, x, mid + 1, end)

result = binary_search(num_lst, x, 0, n-1)

if result != None: 
    print(result)
else: 
    print(-1)
