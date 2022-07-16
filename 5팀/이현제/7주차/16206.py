n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort(key=lambda x: (x % 10, x))
result = 0
pointer = 0

while m != 0 and pointer < n:
    if arr[pointer] == 10:
        result += 1
        pointer += 1
    elif arr[pointer] % 10 == 0:
        if m <= (arr[pointer]//10) - 2:
            result += m
            pointer += 1
            m = 0
        else: 
            m = m - (arr[pointer]//10) + 1
            result += arr[pointer]//10
            pointer += 1
    else:
        if m <= (arr[pointer]//10) - 1:
            result += m
            pointer += 1
            m = 0
        else:
            m = m - (arr[pointer]//10)
            result += arr[pointer]//10
            pointer += 1
print(result)